"""LaTeX commands for diacritical symbols.

Adds diacritical modifier characters.

    Typical usage

    Warp:
    `\\overline` → `awesome`
    Output:
    `a̅w̅e̅s̅o̅m̅e̅`
"""

import keypirinha as kp

from Warp.cat import symbols

MAPPING_DIACRITICAL = [
    ["\\overline", "\u0305"],
    # ["\\underline", "\u0332"],
    # ["\\widehat", "\u0302"],
    # ["\\widetilde", "\u0303"],
    # ["\\overrightarrow", "\u20D7"],
    ["\\overleftarrow", "\u20D6"],
    ["\\acute", "\u0301"],
    # ["\\\'", "\u0301"],
    ["\\breve", "\u0306"],
    # ["\\u", "\u0306"],
    ["\\ddot", "\u0308"],
    # ["\\\"", "\u0308"],
    ["\\grave", "\u0300"],
    ["\\tilde", "\u0303"],
    ["\\bar", "\u0304"],
    ["\\check", "\u030C"],
    ["\\dot", "\u0307"],
    # ["\\.", "\u0307"],
    ["\\hat", "\u0302"],
    ["\\vec", "\u20D7"],
    # ["\\b", "\u0332"],
    ["\\r", "\u030A"],
    ["\\t", "\u0311"],
    # ["\\^", "\u0302"],
    ["\\H", "\u030B"],
    # ["\\v", "\u030C"],
    # ["\\\`", "\u0300"],
    # ["\\t", "\u0361"],
    # ["\\~", "\u0303"],
    ["\\c", "\u0327"],
    # ["\\=", "\u0305"],
    ["\\d", "\u0323"],
    ["\\uline", "\u0332"], # ulem package
    ["\\uuline", "\u0333"], # ulem package
    ["\\uwave", "\u0330"], # ulem package
    ["\\sout", "\u0336"], # ulem package
    ["\\xout", "\u0338"], # ulem package
    ["\\dashuline", "\u0331"], # ulem package
    ["\\dotuline", "\u0324"]] # ulem package

def assign_cat(plugin):
    """Assigns `diacritical` module mapping words to the `Warp` plugin."""

    items = []
    for item in MAPPING_DIACRITICAL:
        items.append(
            plugin.create_item(
                category=plugin.CATEGORY_DIACRITICAL,
                label=item[0],
                short_desc=f"Diactirical symbol: o{item[1]}",
                target=item[1],
                args_hint=kp.ItemArgsHint.REQUIRED,
                hit_hint=kp.ItemHitHint.IGNORE))
    return items

def _construct_output(user_input, prev_target):
    """Converts `user_input` string to output string.
    
    `prev_target` is a diacritical symbol (target of `MAPPING_DIACRITICAL`).
    """

    if user_input in [s[0] for s in symbols.MAPPING_SYMBOLS]:
        # Exact match (one symbol)
        idx = [s[0] for s in symbols.MAPPING_SYMBOLS].index(user_input)
        output = [s[1] for s in symbols.MAPPING_SYMBOLS][idx] + prev_target
    else:
        # All symbols
        output = "".join([s + prev_target for s in user_input])
    return output

def get_suggestions(plugin, user_input, prev_target):
    """Returns the result of this plugin."""
    
    item = None
    if len(user_input) > 0:
        output = _construct_output(user_input, prev_target)
        if len(output) > 0:
            item = plugin.create_item(
                category=plugin.CATEGORY_SYMBOLS,
                label=user_input,
                short_desc=output,
                target=output,
                args_hint=kp.ItemArgsHint.FORBIDDEN,
                hit_hint=kp.ItemHitHint.IGNORE)
    return item