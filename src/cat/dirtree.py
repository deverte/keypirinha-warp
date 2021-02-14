"""Directory tree visualization command.

Visualization of the directory tree by specifying files' or directories' levels.
Result quite similar to the LaTeX's dirtree plugin.

Builds a directory tree by specifying the file or directory levels separated
by commas (without spaces).
First directory level must be equal to `1`.
The next level of the directory or file must be less than the current level
or equal to the current level or exceed the current level by `1`.

    Typical usage

    Warp:
    `\\dirtree` → `1,2,3,4,3,3,4,2,3,2`
    Output:
    ```
    <!-- command: 1,2,3,4,3,3,4,2,3,2 -->
    x
    ├─ x
    │  ├─ x
    │  │  └─ x
    │  ├─ x
    │  └─ x
    │     └─ x
    ├─ x
    │  └─ x
    └─ x
    ```
"""

import keypirinha as kp

KEYWORD_DIRTREE = "\\dirtree" # dirtree style

def assign_cat(plugin):
    """Assigns `dirtree` module keyword to the `Warp` plugin."""

    item = plugin.create_item(
        category=plugin.CATEGORY_DIRTREE,
        label=KEYWORD_DIRTREE,
        short_desc="Directory Tree",
        target=KEYWORD_DIRTREE,
        args_hint=kp.ItemArgsHint.REQUIRED,
        hit_hint=kp.ItemHitHint.IGNORE)
    return item

def _construct_output(user_input):
    """Builds a directory tree.

    Builds a directory tree by specifying the file or directory levels separated
    by commas (without spaces).
    First directory level must be equal to `1`.
    The next level of the directory or file must be less than the current level
    or equal to the current level or exceed the current level by `1`.
    """

    output = ""
    error_indicator = False

    levels = user_input.split(',')
    # Check if first value equals to `1`
    if levels[0] != '1':
        error_indicator = True
        output = f'First level must be `1`. Wrong input: `{user_input}`.'
    # Check if all levels are integers
    if not error_indicator:
        for level in levels:
            if not level.isdigit():
                error_indicator = True
                output = f'All levels must be a positive integer numbers. Wrong input: `{user_input}`.'
                break
    # Check if all levels are less, equal or exceeds previous level on 1
    if not error_indicator:
        for idx, level in enumerate(levels):
            if len(levels) > 1 and int(level) > int(levels[idx-1]) + 1:
                error_indicator = True
                output = f'Level `{level}` must be ≤ `{int(levels[idx-1]) + 1}`. Wrong input: `{user_input}`.'
                break
    
    if not error_indicator:
        levels_int = [int(level) for level in levels]
        tree_list = _construct_tree(levels_int)
        output = f"<!-- command: {user_input} -->\n" + "\n".join(tree_list)

    return output, error_indicator

def _construct_tree(levels):
    """Main algorithm for constructing a directory tree."""
    tree_list = _create_skeleton(levels)
    max_len = _max_len(tree_list)
    embedded = _embed(tree_list, max_len)
    transposed = _transpose(embedded, max_len)
    mirrored = _mirror(transposed)
    joined = _join(mirrored)
    unmirrored = _mirror(joined)
    direct = _transpose(unmirrored, len(levels)+1)
    unembedded = _unembed(direct)
    return unembedded

def _create_skeleton(levels):
    """Creates so-called 'skeleton' consisted only of margins and 'joints'"""
    tree_list = []
    for level in levels:
        if level == 1:
            tree_list.append("x")
        else:
            tree_list.append("   " * (level - 2) + "└─ x")
    return tree_list

def _max_len(tree_list):
    """Calculates max length of tree's strings"""
    max_len = 0
    for row in tree_list:
        if len(row) > max_len:
            max_len = len(row)
    return max_len

def _embed(tree_list, max_len):
    """Embeds a tree list with margins at the end of the strings"""
    # Alignment to a single length (embedding with spaces)
    new_tree_list = tree_list
    for idx, row in enumerate(tree_list):
        new_tree_list[idx] = row + " " * (max_len - len(row))
    return new_tree_list

def _transpose(tree_list, width):
    """Transposes a tree list"""
    transposed = ["" for _ in range(width)]
    for row in tree_list:
        for idx, symbol in enumerate(row):
            transposed[idx] += symbol
    return transposed

def _mirror(tree_list):
    """Mirrors a tree list from left ro right"""
    # Reverse (left to right)
    mirrored = []
    for row in tree_list:
        mirrored.append(row[::-1])
    return mirrored

def _join(tm_tree_list):
    """Joins a 'joints' with a couplings."""
    joined = []
    for row in tm_tree_list:
        new_row = ""
        is_start = 0
        for symbol in row:
            if symbol == "└":
                if is_start == 0:
                    is_start = 1
                    new_row += symbol
                else:
                    new_row += "├"
            elif symbol == " " and is_start:
                new_row += "│"
            elif symbol == "x":
                if is_start:
                    is_start = 0
                new_row += symbol
            else:
                new_row += symbol
        joined.append(new_row)
    return joined

def _unembed(tree_list):
    """Unembeds (or deletes) extra spaces at the end of the strings."""
    unembedded = []
    for line in tree_list:
        unembedded.append(line.rstrip())
    return unembedded

def get_suggestions(plugin, user_input):
    """Returns the result of this plugin."""
    
    item = None
    if len(user_input) > 0:
        output, error_indicator = _construct_output(user_input)
        if error_indicator:
            item = plugin.create_error_item(
                label=output,
                short_desc="Error")
        else:
            item = plugin.create_item(
                category=plugin.CATEGORY_SYMBOLS,
                label=user_input,
                short_desc=f"dirtree",
                target=output,
                args_hint=kp.ItemArgsHint.FORBIDDEN,
                hit_hint=kp.ItemHitHint.IGNORE)
    return item