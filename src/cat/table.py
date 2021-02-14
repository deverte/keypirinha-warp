"""Markdown-style table.

Markdown-style table.
You can specify number of rows `m`, number of columns `n` and width of the
columns `w` (technically, width will be more by two). By default, width equals
to `10` and you can specify only `m` and `n`. Values must be separated by commas
(without spaces).

    Typical usage

    Warp:
    `\\table` → `2,3,8`
    Output:
    ```
    |          |          |          |
    | -------- | -------- | -------- |
    |          |          |          |
    |          |          |          |
    ```
"""

import keypirinha as kp

KEYWORD_TABLE = "\\table" # Markdown-style

def assign_cat(plugin):
    """Assigns `table` module keywords to the `Warp` plugin."""

    item = plugin.create_item(
        category=plugin.CATEGORY_TABLE,
        label=KEYWORD_TABLE,
        short_desc="Table",
        target=KEYWORD_TABLE,
        args_hint=kp.ItemArgsHint.REQUIRED,
        hit_hint=kp.ItemHitHint.IGNORE)
    return item

def _construct_output(user_input):
    """Converts `user_input` string to output string and returns some meta."""

    output = ""
    short_desc = ""
    error_indicator = False

    attrs = user_input.split(',')

    if not len(attrs) in [2, 3]:
        error_indicator = True
        output = (
            f"Number of attributes must be 2 or 3. "
            f"Wrong value: {user_input}")
    if not error_indicator and False in [a.isdigit() for a in attrs]:
        error_indicator = True
        output = (
            f"All attributes must be a positive integer. "
            f"Wrong value: {user_input}")
    if not error_indicator and True in [int(a) < 1 for a in attrs]:
        error_indicator = True
        output = (
            f"All attributes must be ≥ 1. "
            f"Wrong value: {user_input}")

    if not error_indicator:
        nrows = 1
        ncols = 3
        width = 10

        if len(attrs) == 2:
            nrows = int(attrs[0])
            ncols = int(attrs[1])
        elif len(attrs) == 3:
            nrows = int(attrs[0])
            ncols = int(attrs[1])
            width = int(attrs[2])
        output = ((
            "| " + " " * width + " ") * ncols + "|\n" + (
            "| " + "-" * width + " ") * ncols + "|\n" + ((
            "| " + " " * width + " ") * ncols + "|\n") * nrows)
        short_desc = f"table [rows: {nrows}, cols: {ncols}, width: {width}]"
    
    return output, short_desc, error_indicator

def get_suggestions(plugin, user_input):
    """Returns the result of this plugin."""
    
    item = None
    if len(user_input) > 0:
        output, short_desc, error_indicator = _construct_output(user_input)
        if error_indicator:
            item = plugin.create_error_item(
                label=output,
                short_desc="Error")
        else:
            item = plugin.create_item(
                category=plugin.CATEGORY_SYMBOLS,
                label=user_input,
                short_desc=short_desc,
                target=output,
                args_hint=kp.ItemArgsHint.FORBIDDEN,
                hit_hint=kp.ItemHitHint.IGNORE)
    return item