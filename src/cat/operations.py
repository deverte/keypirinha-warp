"""LaTeX math operations with complex commands.

Math commands with required fields (fractions, roots).

    Typical usage

    Warp:
    `\\frac` → `{42}{101}`
    Output:
    `⁴²⁄₁₀₁`
"""

import keypirinha as kp

import re

from Warp.cat import base

KEYWORD_FRAC = "\\frac"
KEYWORD_FFRAC = "\\Frac" # Additional: full (3-lines) expressions
KEYWORD_ROOT = "\\sqrt"

MAPPING_FRAC = [
    ["{1}{2}", "½"],
    ["{1}{4}", "¼"],
    ["{3}{4}", "¾"],
    ["{1}{7}", "⅐"],
    ["{1}{9}", "⅑"],
    ["{1}{10}", "⅒"],
    ["{1}{3}", "⅓"],
    ["{2}{3}", "⅔"],
    ["{1}{5}", "⅕"],
    ["{2}{5}", "⅖"],
    ["{3}{5}", "⅗"],
    ["{4}{5}", "⅘"],
    ["{1}{6}", "⅙"],
    ["{5}{6}", "⅚"],
    ["{1}{8}", "⅛"],
    ["{3}{8}", "⅜"],
    ["{5}{8}", "⅝"],
    ["{7}{8}", "⅞"],
    ["{1}", "⅟"],
    ["{0}{3}", "↉"],
    ["{a}{c}", "℀"],
    ["{a}{s}", "℁"],
    ["{c}{u}", "℆"],
    ["{c}{o}", "℅"],
    ["{A}{S}", "⅍"]]

MAPPING_ROOT = [
    ["[2]", "√"],
    ["[3]", "∛"],
    ["[4]", "∜"]]

def assign_cat(plugin):
    """Assigns `operations` module keywords to the `Warp` plugin."""

    meta = [
        [KEYWORD_FRAC, "Fraction: ½"],
        [KEYWORD_FFRAC, "Fraction: ÷"],
        [KEYWORD_ROOT, "Root: √"]]
    items = [plugin.create_item(
        category=plugin.CATEGORY_OPERATIONS,
        label=el[0],
        short_desc=el[1],
        target=el[0],
        args_hint=kp.ItemArgsHint.REQUIRED,
        hit_hint=kp.ItemHitHint.IGNORE) for el in meta]
    return items

def _construct_frac(user_input):
    """Constructs a fraction consisted of superscript and subscript symbols.
    
    `user_input` must be in form of `{x}{y}` where `x` and `y` are arbitary
    values.
    """

    target = ""

    pattern = r"{(.*)}{(.*)}"
    match = re.match(pattern, user_input)
    if match and user_input.count("{") == 2 and user_input.count("}") == 2:
        numerator = match.group(1)
        denominator = match.group(2)

        original_superscript = [s[0] for s in base.MAPPING_SUPERSCRIPT]
        superscript = [s[1] for s in base.MAPPING_SUPERSCRIPT]

        original_subscript = [s[0] for s in base.MAPPING_SUBSCRIPT]
        subscript = [s[1] for s in base.MAPPING_SUBSCRIPT]

        for char in numerator:
            if char in original_superscript:
                idx = original_superscript.index(char)
                target += superscript[idx]
        target += "⁄"
        for char in denominator:
            if char in original_subscript:
                idx = original_subscript.index(char)
                target += subscript[idx]
    
    return target

def _construct_ffrac(user_input):
    """Constructs a fraction consisted of three lines (numerator, line and denominator).
    
    `user_input` must be a string with a positive integer - length of the
    fraction's line (without two boundary signs).
    """

    target = ""
    error_indicator = False

    if not user_input.isdigit():
        error_indicator = True
        target = (
            f"Length of the fraction must be a positive integer. "
            f"Wrong value: {user_input}")
    if not error_indicator and int(user_input) < 1:
        error_indicator = True
        target = (
            f"Length of the fraction must be ≥ 1. "
            f"Wrong value: {user_input}")
    if not error_indicator:
        length = int(user_input)
        target = (
            " " + " " * length + " \n" +
            "―" + "―" * length + "―\n" +
            " " + " " * length + " \n")

    return target, error_indicator

def get_suggestions(plugin, user_input, prev_target):
    """Returns the result of this plugin."""
    
    items = []
    if prev_target == KEYWORD_FRAC:
        if len(user_input) > 0:
            target = _construct_frac(user_input)
            if len(target) > 0:
                items.append(
                    plugin.create_item(
                        category=plugin.CATEGORY_SYMBOLS,
                        label=user_input,
                        short_desc=target,
                        target=target,
                        args_hint=kp.ItemArgsHint.FORBIDDEN,
                        hit_hint=kp.ItemHitHint.IGNORE))
        for item in MAPPING_FRAC:
            items.append(
                plugin.create_item(
                    category=plugin.CATEGORY_SYMBOLS,
                    label=item[0],
                    short_desc=item[1],
                    target=item[1],
                    args_hint=kp.ItemArgsHint.FORBIDDEN,
                    hit_hint=kp.ItemHitHint.IGNORE))
    elif prev_target == KEYWORD_FFRAC:
        if len(user_input) > 0:
            target, error_indicator = _construct_ffrac(user_input)
            if error_indicator:
                items.append(
                    plugin.create_error_item(
                        label=target,
                        short_desc="Error"))
            else:
                items.append(
                    plugin.create_item(
                        category=plugin.CATEGORY_SYMBOLS,
                        label=user_input,
                        short_desc=target,
                        target=target,
                        args_hint=kp.ItemArgsHint.FORBIDDEN,
                        hit_hint=kp.ItemHitHint.IGNORE))
    elif prev_target == KEYWORD_ROOT:
        for item in MAPPING_ROOT:
            items.append(
                plugin.create_item(
                    category=plugin.CATEGORY_SYMBOLS,
                    label=item[0],
                    short_desc=item[1],
                    target=item[1],
                    args_hint=kp.ItemArgsHint.FORBIDDEN,
                    hit_hint=kp.ItemHitHint.IGNORE))
    return items