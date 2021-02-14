"""Arabic-Roman numbers converter.

Converts arabic numbers to roman numbers with BibTeX-style syntax.

    Typical usage

    Warp:
    `\\RN` → `2021`
    Output:
    `ⅯⅯⅩⅩⅠ`
"""

import keypirinha as kp

KEYWORD_ROMAN_CAPITAL = "\\RN"
KEYWORD_ROMAN_SMALL = "\\Rn"

MAPPING_ROMAN_CAPITAL = [
    ["1", "Ⅰ"],
    ["2", "Ⅱ"],
    ["3", "Ⅲ"],
    ["4", "Ⅳ"],
    ["5", "Ⅴ"],
    ["6", "Ⅵ"],
    ["7", "Ⅶ"],
    ["8", "Ⅷ"],
    ["9", "Ⅸ"],
    ["10", "Ⅹ"],
    ["11", "Ⅺ"],
    ["12", "Ⅻ"],
    ["50", "Ⅼ"],
    ["100", "Ⅽ"],
    ["500", "Ⅾ"],
    ["1000", "Ⅿ"]]

MAPPING_ROMAN_SMALL = [
    ["1", "ⅰ"],
    ["2", "ⅱ"],
    ["3", "ⅲ"],
    ["4", "ⅳ"],
    ["5", "ⅴ"],
    ["6", "ⅵ"],
    ["7", "ⅶ"],
    ["8", "ⅷ"],
    ["9", "ⅸ"],
    ["10", "ⅹ"],
    ["11", "ⅺ"],
    ["12", "ⅻ"],
    ["50", "ⅼ"],
    ["100", "ⅽ"],
    ["500", "ⅾ"],
    ["1000", "ⅿ"]]

def assign_cat(plugin):
    """Assigns `roman` module keywords to the `Warp` plugin."""

    meta = [
        [KEYWORD_ROMAN_CAPITAL, "Roman Capital Number: ⅯⅮⅭⅬⅩⅤⅠ"],
        [KEYWORD_ROMAN_SMALL, "Roman Small Number: ⅿⅾⅽⅼⅹⅴⅰ"]]
    items = [plugin.create_item(
        category=plugin.CATEGORY_ROMAN,
        label=el[0],
        short_desc=el[1],
        target=el[0],
        args_hint=kp.ItemArgsHint.REQUIRED,
        hit_hint=kp.ItemHitHint.IGNORE) for el in meta]
    return items

def _construct_output(user_input, prev_target):
    """Converts `user_input` string to output string."""

    output = ""
    error_indicator = False

    if not user_input.isdigit():
        error_indicator = True
        output = (
            f"Converts only arabic numres into roman numbers. "
            f"Wrong input: {user_input}")
    if not error_indicator and int(user_input) < 1:
        error_indicator = True
        output = (
            f"Arabic number must be a positive integer. "
            f"Wrong input: {user_input}")

    if not error_indicator and prev_target == KEYWORD_ROMAN_CAPITAL:
        output = _arabic_to_roman(user_input, MAPPING_ROMAN_CAPITAL)
    elif not error_indicator and prev_target == KEYWORD_ROMAN_SMALL:
        output = _arabic_to_roman(user_input, MAPPING_ROMAN_SMALL)

    return output, error_indicator

def _arabic_to_roman(user_input, mapping):
    """Converts arabic number to a roman number."""

    output = ""
    residual = int(user_input)
    for roman_base in [1000, 100, 10, 1]:
        residual, roman_occurences = _conversion_step(
            mapping, residual, roman_base)
        output += roman_occurences
    return output

def _conversion_step(mapping, residual, roman_base):
    """Conversion step for roman number base."""

    keys = [el[0] for el in mapping]
    values = [el[1] for el in mapping]

    roman_number = ""
    number_of_occurrences = residual // roman_base
    residual -= roman_base * number_of_occurrences
    roman_idx = keys.index(str(roman_base))
    roman_single = values[roman_idx]
    if number_of_occurrences == 4:
        current_base = values[keys.index(str(roman_base * 5))]
        lesser_base = values[keys.index(str(roman_base))]
        roman_occurences = lesser_base + current_base
    elif number_of_occurrences >= 5 and number_of_occurrences < 9:
        current_base = values[keys.index(str(roman_base * 5))]
        lesser_base = values[keys.index(str(roman_base))]
        roman_occurences = (
            current_base + lesser_base * (number_of_occurrences - 5))
    elif number_of_occurrences == 9:
        current_base = values[keys.index(str(roman_base * 10))]
        lesser_base = values[keys.index(str(roman_base))]
        roman_occurences = lesser_base + current_base
    else:
        roman_occurences = roman_single * number_of_occurrences
    return residual, roman_occurences

def get_suggestions(plugin, user_input, prev_target):
    """Returns the result of this plugin."""
    
    item = None
    if len(user_input) > 0:
        output, error_indicator = _construct_output(user_input, prev_target)
        if error_indicator:
            item = plugin.create_error_item(
                label=output,
                short_desc="Error")
        else:
            item = plugin.create_item(
                category=plugin.CATEGORY_SYMBOLS,
                label=user_input,
                short_desc=output,
                target=output,
                args_hint=kp.ItemArgsHint.FORBIDDEN,
                hit_hint=kp.ItemHitHint.IGNORE)
    return item