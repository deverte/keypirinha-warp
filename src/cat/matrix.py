"""Matrices and cases in LaTeX style.

Converts specified dimensions to the matrices (or cases).
If number of dimensions is `2`, then you can specify one value (e.g. `n`) and it
will be interpreted as square matrix `n × n`. Or you can specify two values
(rows `m` and columns `n`) separated by comma (without spaces): `m,n`, and it
will be interpreted as matrix `m × n`.

    Typical usage

    Warp:
    `\\Bmatrix` → `3,4`
    Output:
    ```
    ⎧ x  x  x  x ⎫
    ⎪            ⎪
    ⎨ x  x  x  x ⎬
    ⎪            ⎪
    ⎩ x  x  x  x ⎭
    ```
"""

import keypirinha as kp

KEYWORD_CASES = "\\cases" # amsmath-style
KEYWORD_SQCASES = "\\sqcases" # additional
KEYWORD_MATRIX = "\\matrix" # amsmath-style
KEYWORD_PMATRIX = "\\pmatrix" # amsmath-style
KEYWORD_BMATRIX = "\\bmatrix" # amsmath-style
KEYWORD_BBMATRIX = "\\Bmatrix" # amsmath-style
KEYWORD_VMATRIX = "\\vmatrix" # amsmath-style
KEYWORD_VVMATRIX = "\\Vmatrix" # amsmath-style

def assign_cat(plugin):
    """Assigns `matrix` module keywords to the `Warp` plugin."""

    meta = [
        [KEYWORD_MATRIX, "Plain Matrix:  X "],
        [KEYWORD_PMATRIX, "Parentheses; Round Brackets Matrix: (X)"],
        [KEYWORD_BMATRIX, "Brackets; Square Brackets Matrix: [X]"],
        [KEYWORD_BBMATRIX, "Braces; Curly Brackets Matrix: {X}"],
        [KEYWORD_VMATRIX, "Pipes Matrix: |X|"],
        [KEYWORD_VVMATRIX, "Double Pipes Matrix: ║X║"],
        [KEYWORD_CASES, "Cases: {X"],
        [KEYWORD_SQCASES, "Square Cases: [X"]]
    items = [plugin.create_item(
        category=plugin.CATEGORY_MATRIX,
        label=el[0],
        short_desc=el[1],
        target=el[0],
        args_hint=kp.ItemArgsHint.REQUIRED,
        hit_hint=kp.ItemHitHint.IGNORE) for el in meta]
    return items

def _construct_output(user_input, prev_target):
    """Converts `user_input` string to output string and it's description."""

    target = ""
    short_desc = ""
    error_indicator = False

    dims = user_input.split(',')

    if prev_target == KEYWORD_CASES:
        error_indicator, target, short_desc = _d1_target(
            dims, "cases", user_input, _cases)
    elif prev_target == KEYWORD_SQCASES:
        error_indicator, target, short_desc = _d1_target(
            dims, "sqcases", user_input, _sqcases)
    elif prev_target == KEYWORD_MATRIX:
        error_indicator, target, short_desc = _d2_target(
            dims, "matrix", user_input, _matrix)
    elif prev_target == KEYWORD_PMATRIX:
        error_indicator, target, short_desc = _d2_target(
            dims, "pmatrix", user_input, _pmatrix)
    elif prev_target == KEYWORD_BMATRIX:
        error_indicator, target, short_desc = _d2_target(
            dims, "bmatrix", user_input, _bmatrix)
    elif prev_target == KEYWORD_BBMATRIX:
        error_indicator, target, short_desc = _d2_target(
            dims, "Bmatrix", user_input, _bbmatrix)
    elif prev_target == KEYWORD_VMATRIX:
        error_indicator, target, short_desc = _d2_target(
            dims, "vmatrix", user_input, _vmatrix)
    elif prev_target == KEYWORD_VVMATRIX:
        error_indicator, target, short_desc = _d2_target(
            dims, "Vmatrix", user_input, _vvmatrix)

    return target, short_desc, error_indicator

def _d1_target(dims, name, user_input, representation):
    """Creates a one-dimensional object (e.g. cases)."""

    isndims = lambda dims, n: (len(dims) == n)
    isalldigits = lambda dims: not False in [d.isdigit() for d in dims]
    isallgt0 = lambda dims: not False in [int(d) > 0 for d in dims]

    error_indicator = False
    target = ""
    short_desc = ""

    if not error_indicator and not isndims(dims, 1):
        error_indicator = True
        target = (
            f'`{name}` number of dimensions must be 1. '
            f'Wrong input: `{user_input}`.')
    if not error_indicator and not isalldigits(dims):
        error_indicator = True
        target = (
            f'`{name}` dimension must be a positive integer number. '
            f'Wrong input: `{user_input}`.')
    if not error_indicator and not isallgt0(dims):
        error_indicator = True
        target = (
            f'`{name}` dimension must be more than 0. '
            f'Wrong input: `{user_input}`.')
    if not error_indicator:
        nrows = int(dims[0])
        target = representation(nrows)
        short_desc = f"{name} [{nrows}]"
    return error_indicator, target, short_desc

def _d2_target(dims, name, user_input, representation):
    """Creates a two-dimensional object (e.g. matrix)."""

    isndims = lambda dims, n: (len(dims) == n)
    isalldigits = lambda dims: not False in [d.isdigit() for d in dims]
    isallgt0 = lambda dims: not False in [int(d) > 0 for d in dims]

    error_indicator = False
    target = ""
    short_desc = ""

    if not error_indicator and not (isndims(dims, 1) or isndims(dims, 2)):
        error_indicator = True
        target = (
            f'`{name}` number of dimensions must be 1 or 2. '
            f'Wrong input: `{user_input}`.')
    if not error_indicator and not isalldigits(dims):
        error_indicator = True
        target = (
            f'`{name}` dimensions must be a positive integer numbers. '
            f'Wrong input: `{user_input}`.')
    if not error_indicator and not isallgt0(dims):
        error_indicator = True
        target = (
            f'`{name}` dimensions must be more than 0. '
            f'Wrong input: `{user_input}`.')
    if not error_indicator:
        nrows = int(dims[0])
        ncols = int(dims[0]) if isndims(dims, 1) else int(dims[1])
        target = representation(nrows, ncols)
        short_desc = f"{name} [{nrows} x {ncols}]"
    return error_indicator, target, short_desc

def _cases(nrows):
    """Creates a curly cases."""

    cases = ""
    if nrows == 1:
        cases = "{ x"
    elif nrows % 2 == 0:
        cases = (
            "⎧ x\n" + (
            "⎪\n" +
            "⎪ x\n") * (nrows // 2 - 1) +
            "⎨\n" + (
            "⎪ x\n" +
            "⎪\n") * (nrows // 2 - 1) +
            "⎩ x")
    else:
        cases = (
            "⎧ x\n" +
            "⎪\n" + (
            "⎪ x\n" +
            "⎪\n") * (nrows // 2 - 1) +
            "⎨ x\n" + (
            "⎪\n" +
            "⎪ x\n") * (nrows // 2 - 1) +
            "⎪\n" +
            "⎩ x")
    return cases

def _sqcases(nrows):
    """Creates a square cases."""

    sqcases = ""
    if nrows == 1:
        sqcases = "[ x"
    else:
        sqcases = (
            "⎡ x\n" + (
            "⎢\n" +
            "⎢ x\n") * (nrows - 2) +
            "⎢\n" +
            "⎣ x")
    return sqcases

def _matrix(nrows, ncols):
    """Creates a matrix with no borders."""

    matrix = (
        "  x" + "  x" * (ncols - 1) + "  \n" + (
        "   " + "   " * (ncols - 1) + "  \n" +
        "  x" + "  x" * (ncols - 1) + "  \n") * (nrows - 1))
    return matrix

def _pmatrix(nrows, ncols):
    """Creates a matrix with a round brackets borders."""

    pmatrix = ""
    if nrows == 1:
        pmatrix = "( x" + "  x" * (ncols - 1) + " )"
    else:
        pmatrix = (
            "⎛ x" + "  x" * (ncols - 1) + " ⎞\n" + (
            "⎜  " + "   " * (ncols - 1) + " ⎟\n" +
            "⎜ x" + "  x" * (ncols - 1) + " ⎟\n") * (nrows - 2) +
            "⎜  " + "   " * (ncols - 1) + " ⎟\n" +
            "⎝ x" + "  x" * (ncols - 1) + " ⎠")
    return pmatrix

def _bmatrix(nrows, ncols):
    """Creates a matrix with a square brackets borders."""

    bmatrix = ""
    if nrows == 1:
        bmatrix = "[ x" + "  x" * (ncols - 1) + " ]"
    else:
        bmatrix = (
            "⎡ x" + "  x" * (ncols - 1) + " ⎤\n" + (
            "⎢  " + "   " * (ncols - 1) + " ⎥\n" +
            "⎢ x" + "  x" * (ncols - 1) + " ⎥\n") * (nrows - 2) +
            "⎢  " + "   " * (ncols - 1) + " ⎥\n" +
            "⎣ x" + "  x" * (ncols - 1) + " ⎦")
    return bmatrix

def _bbmatrix(nrows, ncols):
    """Creates a matrix with a curly brackets borders."""

    bbmatrix = ""
    if nrows == 1:
        bbmatrix = "{ x" + "  x" * (ncols - 1) + " }"
    elif nrows % 2 == 0:
        bbmatrix = (
            "⎧ x" + "  x" * (ncols - 1) + " ⎫\n" + (
            "⎪  " + "   " * (ncols - 1) + " ⎪\n" +
            "⎪ x" + "  x" * (ncols - 1) + " ⎪\n") * (nrows // 2 - 1) +
            "⎨  " + "   " * (ncols - 1) + " ⎬\n" + (
            "⎪ x" + "  x" * (ncols - 1) + " ⎪\n" +
            "⎪  " + "   " * (ncols - 1) + " ⎪\n") * (nrows // 2 - 1) +
            "⎩ x" + "  x" * (ncols - 1) + " ⎭")
    else:
        bbmatrix = (
            "⎧ x" + "  x" * (ncols - 1) + " ⎫\n" +
            "⎪  " + "   " * (ncols - 1) + " ⎪\n" + (
            "⎪ x" + "  x" * (ncols - 1) + " ⎪\n" +
            "⎪  " + "   " * (ncols - 1) + " ⎪\n") * (nrows // 2 - 1) +
            "⎨ x" + "  x" * (ncols - 1) + " ⎬\n" + (
            "⎪  " + "   " * (ncols - 1) + " ⎪\n" +
            "⎪ x" + "  x" * (ncols - 1) + " ⎪\n") * (nrows // 2 - 1) +
            "⎪  " + "   " * (ncols - 1) + " ⎪\n" +
            "⎩ x" + "  x" * (ncols - 1) + " ⎭")
    return bbmatrix

def _vmatrix(nrows, ncols):
    """Creates a matrix with a pipes brackets borders."""

    vmatrix = (
        "⎢ x" + "  x" * (ncols - 1) + " ⎥\n" + (
        "⎢  " + "   " * (ncols - 1) + " ⎥\n" +
        "⎢ x" + "  x" * (ncols - 1) + " ⎥\n") * (nrows - 1))
    return vmatrix

def _vvmatrix(nrows, ncols):
    """Creates a matrix with a double pipes brackets borders."""

    vvmatrix = (
        "║ x" + "  x" * (ncols - 1) + " ║\n" + (
        "║  " + "   " * (ncols - 1) + " ║\n" +
        "║ x" + "  x" * (ncols - 1) + " ║\n") * (nrows - 1))
    return vvmatrix

def get_suggestions(plugin, user_input, prev_target):
    """Returns the result of this plugin."""
    
    item = None
    if len(user_input) > 0:
        target, short_desc, error_indicator = _construct_output(
            user_input, prev_target)
        if error_indicator:
            item = plugin.create_error_item(
                label=target,
                short_desc="Error")
        else:
            item = plugin.create_item(
                category=plugin.CATEGORY_SYMBOLS,
                label=user_input,
                short_desc=short_desc,
                target=target,
                args_hint=kp.ItemArgsHint.FORBIDDEN,
                hit_hint=kp.ItemHitHint.IGNORE)
    return item