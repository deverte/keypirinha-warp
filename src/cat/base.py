"""Base LaTeX syntax commands.

LaTeX superscript and subscript commands.
Supports some greek letters (but not all).
For exapmle, you can write `\\beta` in superscript environment (`^`) and result
will be `ᵝ`. The match must be exact.
All extra symbols will be ignored. For example, if you write `a%h` in subscript
environment, result will be `ₐₕ` (without `%`).

    Typical usage

    Warp:
    `^` → `(96+48)`
    Output:
    `⁽⁹⁶⁺⁴⁸⁾`
"""

import keypirinha as kp

KEYWORD_SUPERSCRIPT = "^"
KEYWORD_SUBSCRIPT = "_"

MAPPING_SUPERSCRIPT = [
    # Punctuation
    ["!", "ᵎ"],
    [".", "ᐧ"],
    [",", ","],
    # Numbers
    ["0", "⁰"],
    ["1", "¹"],
    ["2", "²"],
    ["3", "³"],
    ["4", "⁴"],
    ["5", "⁵"],
    ["6", "⁶"],
    ["7", "⁷"],
    ["8", "⁸"],
    ["9", "⁹"],
    # Math Symbols
    ["+", "⁺"],
    ["-", "⁻"],
    ["=", "⁼"],
    ["(", "⁽"],
    [")", "⁾"],
    ["\dot", "ᐧ"],
    ["\\times", "ᕁ"],
    ["\\neq", "ᙾ"],
    # Latin Small Letters
    ["a", "ᵃ"],
    ["b", "ᵇ"],
    ["с", "ᶜ"],
    ["d", "ᵈ"],
    ["e", "ᵉ"],
    ["f", "ᶠ"],
    ["g", "ᵍ"],
    ["h", "ʰ"],
    ["i", "ⁱ"],
    ["j", "ʲ"],
    ["k", "ᵏ"],
    ["l", "ˡ"],
    ["m", "ᵐ"],
    ["n", "ⁿ"],
    ["o", "ᵒ"],
    ["p", "ᵖ"],
    ["q", "ᑫ"], # displacement
    ["r", "ʳ"],
    ["s", "ˢ"],
    ["t", "ᵗ"],
    ["u", "ᵘ"],
    ["v", "ᵛ"],
    ["w", "ʷ"],
    ["x", "ˣ"],
    ["y", "ʸ"],
    ["z", "ᶻ"],
    # Latin Capital Letters
    ["A", "ᴬ"],
    ["B", "ᴮ"],
    ["C", "ᶜ"], # displacement from small letters
    ["D", "ᴰ"],
    ["E", "ᴱ"],
    ["F", "ᶠ"], # displacement from small letters
    ["G", "ᴳ"],
    ["H", "ᴴ"],
    ["I", "ᴵ"],
    ["J", "ᴶ"],
    ["K", "ᴷ"],
    ["L", "ᴸ"],
    ["M", "ᴹ"],
    ["N", "ᴺ"],
    ["O", "ᴼ"],
    ["P", "ᴾ"],
    ["Q", "Q"], # displacement
    ["R", "ᴿ"],
    ["s", "ˢ"], # displacement from small letters
    ["T", "ᵀ"],
    ["U", "ᵁ"],
    ["V", "ⱽ"],
    ["W", "ᵂ"],
    ["x", "ˣ"], # displacement from small letters
    ["y", "ʸ"], # displacement from small letters
    ["z", "ᶻ"], # displacement from small letters
    # Greek Letters
    ["\\beta", "ᵝ"],
    ["\\gamma", "ᵞ"],
    ["\\delta", "ᵟ"],
    ["\\Delta", "ᐞ"],
    ["\\theta", "ᶿ"],
    ["\\phi", "ᶲ"],
    ["\\psi", "ᵠ"],
    ["\\upsilon", "ᶹ"],
    ["\\zeta", "ᶼ"],
    ["\\Omega", "ᶷ"],
    ["\\chi", "ᵡ"]]

MAPPING_SUBSCRIPT = [
    # Numbers
    ["0", "₀"],
    ["1", "₁"],
    ["2", "₂"],
    ["3", "₃"],
    ["4", "₄"],
    ["5", "₅"],
    ["6", "₆"],
    ["7", "₇"],
    ["8", "₈"],
    ["9", "₉"],
    # Math Symbols
    ["+", "₊"],
    ["-", "₋"],
    ["=", "₌"],
    ["(", "₍"],
    [")", "₎"],
    # Latin Letters
    ["a", "ₐ"],
    ["b", "₆"], # displacement
    ["c", "꜀"], # displacement
    ["d", "ₔ"], # displacement
    ["e", "ₑ"],
    ["f", "բ"], # displacement
    ["g", "₉"], # displacement
    ["h", "ₕ"],
    ["i", "ᵢ"],
    ["j", "ⱼ"],
    ["k", "ₖ"],
    ["l", "ₗ"],
    ["m", "ₘ"],
    ["n", "ₙ"],
    ["o", "ₒ"],
    ["p", "ₚ"],
    ["q", "q"],
    ["r", "ᵣ"],
    ["s", "ₛ"],
    ["t", "ₜ"],
    ["u", "ᵤ"],
    ["v", "ᵥ"],
    ["w", "ᵥᵥ"],
    ["x", "ₓ"],
    ["y", "ᵧ"], # displacement
    ["z", "₂"], # displacement
    # Greek Letters
    ["\\beta", "ᵦ"],
    ["\\gamma", "ᵧ"],
    ["\\rho", "ᵨ"],
    ["\\psi", "ᵩ"],
    ["\\chi", "ᵪ"]]

def assign_cat(plugin):
    """Assigns `base` module keywords to the `Warp` plugin."""

    meta = [
        [KEYWORD_SUPERSCRIPT, "Superscript: ¹²³"],
        [KEYWORD_SUBSCRIPT, "Subscript: ₁₂₃"]]
    items = [plugin.create_item(
        category=plugin.CATEGORY_BASE,
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
    if prev_target == KEYWORD_SUPERSCRIPT:
        target, short_desc = _process(
            user_input, MAPPING_SUPERSCRIPT, passing_extra=False)
    elif prev_target == KEYWORD_SUBSCRIPT:
        target, short_desc = _process(
            user_input, MAPPING_SUBSCRIPT, passing_extra=False)
    return target, short_desc

def _process(user_input, mapping, passing_extra=True):
    """Maps `user_input` symbols to it's LaTeX counterparts.
    
    If `passing_extra` is set to `True`, then characters that are not in the
    mappings, will be represented in the output unchanged.
    If `passing_extra` is set to `False`, the extra characters will be ignored.
    """

    target = user_input
    if user_input in [s[0] for s in mapping]:
        # Exact match (one symbol)
        idx = [s[0] for s in mapping].index(user_input)
        target = [s[1] for s in mapping][idx]
    else:
        # All symbols
        for symbol in mapping:
            target = target.replace(symbol[0], symbol[1])

        if not passing_extra:
            new_target = ""
            for idx, symbol in enumerate(target):
                if target[idx] == user_input[idx]:
                    pass
                else:
                    new_target += symbol
            target = new_target

    short_desc = target

    return target, short_desc

def get_suggestions(plugin, user_input, prev_target):
    """Returns the result of this plugin."""

    item = None
    if len(user_input) > 0:
        target, short_desc = _construct_output(user_input, prev_target)
        if len(target) > 0:
            item = plugin.create_item(
                category=plugin.CATEGORY_SYMBOLS,
                label=user_input,
                short_desc=short_desc,
                target=target,
                args_hint=kp.ItemArgsHint.FORBIDDEN,
                hit_hint=kp.ItemHitHint.IGNORE)
    return item