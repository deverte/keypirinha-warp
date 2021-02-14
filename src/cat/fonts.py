"""Math fonts LaTeX-like commands.

Math fonts with LaTeX-like and some extra commands.
> :warning: May be some bugs with conversion.

    Typical usage

    Warp:
    `\\mathfrak` → `Lorem ipsum dolor sit amet`
    Output:
    `𝔏𝔬𝔯𝔢𝔪 𝔦𝔭𝔰𝔲𝔪 𝔡𝔬𝔩𝔬𝔯 𝔰𝔦𝔱 𝔞𝔪𝔢𝔱`
"""

import keypirinha as kp

KEYWORD_MATHCAL = "\\mathcal" # LaTeX math environment
KEYWORD_MATHBB = "\\mathbb" # LaTeX math environment
KEYWORD_MATHFRAK = "\\mathfrak" # LaTeX math environment
KEYWORD_MATHSF = "\\mathsf" # LaTeX math environment
KEYWORD_TEXTSF = "\\textsf" # pure LaTeX
KEYWORD_MATHBF = "\\mathbf" # LaTeX math environment
KEYWORD_TEXTBF = "\\textbf" # pure LaTeX
KEYWORD_MATHBI = "\\mathbi" # LaTeX math environment
KEYWORD_TEXTIT = "\\textit" # pure LaTeX
KEYWORD_TEXTTT = "\\texttt" # pure LaTeX

MAPPING_MATHCAL_MAIN = [
    ["A", "𝒜"],
    ["C", "𝒞"],
    ["D", "𝒟"],
    ["G", "𝒢"],
    ["J", "𝒥"],
    ["K", "𝒦"],
    ["N", "𝒩"],
    ["O", "𝒪"],
    ["P", "𝒫"],
    ["Q", "𝒬"],
    ["S", "𝒮"],
    ["T", "𝒯"],
    ["U", "𝒰"],
    ["V", "𝒱"],
    ["W", "𝒲"],
    ["X", "𝒳"],
    ["Y", "𝒴"],
    ["Z", "𝒵"],
    ["a", "𝒶"],
    ["b", "𝒷"],
    ["c", "𝒸"],
    ["d", "𝒹"],
    ["f", "𝒻"],
    ["h", "𝒽"],
    ["i", "𝒾"],
    ["j", "𝒿"],
    ["k", "𝓀"],
    ["l", "𝓁"],
    ["m", "𝓂"],
    ["n", "𝓃"],
    ["p", "𝓅"],
    ["q", "𝓆"],
    ["r", "𝓇"],
    ["s", "𝓈"],
    ["t", "𝓉"],
    ["u", "𝓊"],
    ["v", "𝓋"],
    ["w", "𝓌"],
    ["x", "𝓍"],
    ["y", "𝓎"],
    ["z", "𝓏"]]

MAPPING_MATHCAL_EXTRA = [
    ["B", "ℬ"],
    ["E", "ℰ"],
    ["F", "ℱ"],
    ["H", "ℋ"],
    ["I", "ℐ"],
    ["L", "ℒ"],
    ["M", "ℳ"],
    ["R", "ℛ"],
    ["e", "ℯ"],
    ["g", "ℊ"],
    ["o", "ℴ"]]

MAPPING_MATHBB_MAIN = [
    ["A", "𝔸"],
    ["B", "𝔹"],
    ["D", "𝔻"],
    ["E", "𝔼"],
    ["F", "𝔽"],
    ["G", "𝔾"],
    ["I", "𝕀"],
    ["J", "𝕁"],
    ["K", "𝕂"],
    ["L", "𝕃"],
    ["M", "𝕄"],
    ["O", "𝕆"],
    ["S", "𝕊"],
    ["T", "𝕋"],
    ["U", "𝕌"],
    ["V", "𝕍"],
    ["W", "𝕎"],
    ["X", "𝕏"],
    ["Y", "𝕐"],
    ["a", "𝕒"],
    ["b", "𝕓"],
    ["c", "𝕔"],
    ["d", "𝕕"],
    ["e", "𝕖"],
    ["f", "𝕗"],
    ["g", "𝕘"],
    ["h", "𝕙"],
    ["i", "𝕚"],
    ["j", "𝕛"],
    ["k", "𝕜"],
    ["l", "𝕝"],
    ["m", "𝕞"],
    ["n", "𝕟"],
    ["o", "𝕠"],
    ["p", "𝕡"],
    ["q", "𝕢"],
    ["r", "𝕣"],
    ["s", "𝕤"],
    ["t", "𝕥"],
    ["u", "𝕦"],
    ["v", "𝕧"],
    ["w", "𝕨"],
    ["x", "𝕩"],
    ["y", "𝕪"],
    ["z", "𝕫"],
    ["0", "𝟘"],
    ["1", "𝟙"],
    ["2", "𝟚"],
    ["3", "𝟛"],
    ["4", "𝟜"],
    ["5", "𝟝"],
    ["6", "𝟞"],
    ["7", "𝟟"],
    ["8", "𝟠"],
    ["9", "𝟡"]]

MAPPING_MATHBB_EXTRA = [
    ["C", "ℂ"],
    ["H", "ℍ"],
    ["N", "ℕ"],
    ["P", "ℙ"],
    ["Q", "ℚ"],
    ["R", "ℝ"],
    ["Z", "ℤ"]]

MAPPING_MATHFRAK_MAIN = [
    ["A", "𝔄"],
    ["B", "𝔅"],
    ["D", "𝔇"],
    ["E", "𝔈"],
    ["F", "𝔉"],
    ["G", "𝔊"],
    ["J", "𝔍"],
    ["K", "𝔎"],
    ["L", "𝔏"],
    ["M", "𝔐"],
    ["N", "𝔑"],
    ["O", "𝔒"],
    ["P", "𝔓"],
    ["Q", "𝔔"],
    ["S", "𝔖"],
    ["T", "𝔗"],
    ["U", "𝔘"],
    ["V", "𝔙"],
    ["W", "𝔚"],
    ["X", "𝔛"],
    ["Y", "𝔜"],
    ["a", "𝔞"],
    ["b", "𝔟"],
    ["c", "𝔠"],
    ["d", "𝔡"],
    ["e", "𝔢"],
    ["f", "𝔣"],
    ["g", "𝔤"],
    ["h", "𝔥"],
    ["i", "𝔦"],
    ["j", "𝔧"],
    ["k", "𝔨"],
    ["l", "𝔩"],
    ["m", "𝔪"],
    ["n", "𝔫"],
    ["o", "𝔬"],
    ["p", "𝔭"],
    ["q", "𝔮"],
    ["r", "𝔯"],
    ["s", "𝔰"],
    ["t", "𝔱"],
    ["u", "𝔲"],
    ["v", "𝔳"],
    ["w", "𝔴"],
    ["x", "𝔵"],
    ["y", "𝔶"],
    ["z", "𝔷"]]

MAPPING_MATHFRAK_EXTRA = [
    ["C", "ℭ"],
    ["H", "ℌ"],
    ["I", "ℑ"],
    ["R", "ℜ"],
    ["Z", "ℨ"]]

MAPPING_MATHSF = [
    ["A", "𝖠"],
    ["B", "𝖡"],
    ["C", "𝖢"],
    ["D", "𝖣"],
    ["E", "𝖤"],
    ["F", "𝖥"],
    ["G", "𝖦"],
    ["H", "𝖧"],
    ["I", "𝖨"],
    ["J", "𝖩"],
    ["K", "𝖪"],
    ["L", "𝖫"],
    ["M", "𝖬"],
    ["N", "𝖭"],
    ["O", "𝖮"],
    ["P", "𝖯"],
    ["Q", "𝖰"],
    ["R", "𝖱"],
    ["S", "𝖲"],
    ["T", "𝖳"],
    ["U", "𝖴"],
    ["V", "𝖵"],
    ["W", "𝖶"],
    ["X", "𝖷"],
    ["Y", "𝖸"],
    ["Z", "𝖹"],
    ["a", "𝖺"],
    ["b", "𝖻"],
    ["c", "𝖼"],
    ["d", "𝖽"],
    ["e", "𝖾"],
    ["f", "𝖿"],
    ["g", "𝗀"],
    ["h", "𝗁"],
    ["i", "𝗂"],
    ["j", "𝗃"],
    ["k", "𝗄"],
    ["l", "𝗅"],
    ["m", "𝗆"],
    ["n", "𝗇"],
    ["o", "𝗈"],
    ["p", "𝗉"],
    ["q", "𝗊"],
    ["r", "𝗋"],
    ["s", "𝗌"],
    ["t", "𝗍"],
    ["u", "𝗎"],
    ["v", "𝗏"],
    ["w", "𝗐"],
    ["x", "𝗑"],
    ["y", "𝗒"],
    ["z", "𝗓"],
    ["0", "𝟢"],
    ["1", "𝟣"],
    ["2", "𝟤"],
    ["3", "𝟥"],
    ["4", "𝟦"],
    ["5", "𝟧"],
    ["6", "𝟨"],
    ["7", "𝟩"],
    ["8", "𝟪"],
    ["9", "𝟫"]]

MAPPING_MATHBF = [
    ["A", "𝐀"],
    ["B", "𝐁"],
    ["C", "𝐂"],
    ["D", "𝐃"],
    ["E", "𝐄"],
    ["F", "𝐅"],
    ["G", "𝐆"],
    ["H", "𝐇"],
    ["I", "𝐈"],
    ["J", "𝐉"],
    ["K", "𝐊"],
    ["L", "𝐋"],
    ["M", "𝐌"],
    ["N", "𝐍"],
    ["O", "𝐎"],
    ["P", "𝐏"],
    ["Q", "𝐐"],
    ["R", "𝐑"],
    ["S", "𝐒"],
    ["T", "𝐓"],
    ["U", "𝐔"],
    ["V", "𝐕"],
    ["W", "𝐖"],
    ["X", "𝐗"],
    ["Y", "𝐘"],
    ["Z", "𝐙"],
    ["a", "𝐚"],
    ["b", "𝐛"],
    ["c", "𝐜"],
    ["d", "𝐝"],
    ["e", "𝐞"],
    ["f", "𝐟"],
    ["g", "𝐠"],
    ["h", "𝐡"],
    ["i", "𝐢"],
    ["j", "𝐣"],
    ["k", "𝐤"],
    ["l", "𝐥"],
    ["m", "𝐦"],
    ["n", "𝐧"],
    ["o", "𝐨"],
    ["p", "𝐩"],
    ["q", "𝐪"],
    ["r", "𝐫"],
    ["s", "𝐬"],
    ["t", "𝐭"],
    ["u", "𝐮"],
    ["v", "𝐯"],
    ["w", "𝐰"],
    ["x", "𝐱"],
    ["y", "𝐲"],
    ["z", "𝐳"],
    ["0", "𝟎"],
    ["1", "𝟏"],
    ["2", "𝟐"],
    ["3", "𝟑"],
    ["4", "𝟒"],
    ["5", "𝟓"],
    ["6", "𝟔"],
    ["7", "𝟕"],
    ["8", "𝟖"],
    ["9", "𝟗"]]

MAPPING_MATHBI = [
    ["A", "𝑨"],
    ["B", "𝑩"],
    ["C", "𝑪"],
    ["D", "𝑫"],
    ["E", "𝑬"],
    ["F", "𝑭"],
    ["G", "𝑮"],
    ["H", "𝑯"],
    ["I", "𝑰"],
    ["J", "𝑱"],
    ["K", "𝑲"],
    ["L", "𝑳"],
    ["M", "𝑴"],
    ["N", "𝑵"],
    ["O", "𝑶"],
    ["P", "𝑷"],
    ["Q", "𝑸"],
    ["R", "𝑹"],
    ["S", "𝑺"],
    ["T", "𝑻"],
    ["U", "𝑼"],
    ["V", "𝑽"],
    ["W", "𝑾"],
    ["X", "𝑿"],
    ["Y", "𝒀"],
    ["Z", "𝒁"],
    ["a", "𝒂"],
    ["b", "𝒃"],
    ["c", "𝒄"],
    ["d", "𝒅"],
    ["e", "𝒆"],
    ["f", "𝒇"],
    ["g", "𝒈"],
    ["h", "𝒉"],
    ["i", "𝒊"],
    ["j", "𝒋"],
    ["k", "𝒌"],
    ["l", "𝒍"],
    ["m", "𝒎"],
    ["n", "𝒏"],
    ["o", "𝒐"],
    ["p", "𝒑"],
    ["q", "𝒒"],
    ["r", "𝒓"],
    ["s", "𝒔"],
    ["t", "𝒕"],
    ["u", "𝒖"],
    ["v", "𝒗"],
    ["w", "𝒘"],
    ["x", "𝒙"],
    ["y", "𝒚"],
    ["z", "𝒛"],
    ["0", "𝟎"],
    ["1", "𝟏"],
    ["2", "𝟐"],
    ["3", "𝟑"],
    ["4", "𝟒"],
    ["5", "𝟓"],
    ["6", "𝟔"],
    ["7", "𝟕"],
    ["8", "𝟖"],
    ["9", "𝟗"]]

MAPPING_TEXTIT_MAIN = [
    ["A", "𝐴"],
    ["B", "𝐵"],
    ["C", "𝐶"],
    ["D", "𝐷"],
    ["E", "𝐸"],
    ["F", "𝐹"],
    ["G", "𝐺"],
    ["H", "𝐻"],
    ["I", "𝐼"],
    ["J", "𝐽"],
    ["K", "𝐾"],
    ["L", "𝐿"],
    ["M", "𝑀"],
    ["N", "𝑁"],
    ["O", "𝑂"],
    ["P", "𝑃"],
    ["Q", "𝑄"],
    ["R", "𝑅"],
    ["S", "𝑆"],
    ["T", "𝑇"],
    ["U", "𝑈"],
    ["V", "𝑉"],
    ["W", "𝑊"],
    ["X", "𝑋"],
    ["Y", "𝑌"],
    ["Z", "𝑍"],
    ["a", "𝑎"],
    ["b", "𝑏"],
    ["c", "𝑐"],
    ["d", "𝑑"],
    ["e", "𝑒"],
    ["f", "𝑓"],
    ["g", "𝑔"],
    ["i", "𝑖"],
    ["j", "𝑗"],
    ["k", "𝑘"],
    ["l", "𝑙"],
    ["m", "𝑚"],
    ["n", "𝑛"],
    ["o", "𝑜"],
    ["p", "𝑝"],
    ["q", "𝑞"],
    ["r", "𝑟"],
    ["s", "𝑠"],
    ["t", "𝑡"],
    ["u", "𝑢"],
    ["v", "𝑣"],
    ["w", "𝑤"],
    ["x", "𝑥"],
    ["y", "𝑦"],
    ["z", "𝑧"],
    ["0", "0"],
    ["1", "1"],
    ["2", "2"],
    ["3", "3"],
    ["4", "4"],
    ["5", "5"],
    ["6", "6"],
    ["7", "7"],
    ["8", "8"],
    ["9", "9"]]

MAPPING_TEXTIT_EXTRA = [
    ["h", "ℎ"]]

MAPPING_TEXTTT = [
    ["A", "𝙰"],
    ["B", "𝙱"],
    ["C", "𝙲"],
    ["D", "𝙳"],
    ["E", "𝙴"],
    ["F", "𝙵"],
    ["G", "𝙶"],
    ["H", "𝙷"],
    ["I", "𝙸"],
    ["J", "𝙹"],
    ["K", "𝙺"],
    ["L", "𝙻"],
    ["M", "𝙼"],
    ["N", "𝙽"],
    ["O", "𝙾"],
    ["P", "𝙿"],
    ["Q", "𝚀"],
    ["R", "𝚁"],
    ["S", "𝚂"],
    ["T", "𝚃"],
    ["U", "𝚄"],
    ["V", "𝚅"],
    ["W", "𝚆"],
    ["X", "𝚇"],
    ["Y", "𝚈"],
    ["Z", "𝚉"],
    ["a", "𝚊"],
    ["b", "𝚋"],
    ["c", "𝚌"],
    ["d", "𝚍"],
    ["e", "𝚎"],
    ["f", "𝚏"],
    ["g", "𝚐"],
    ["h", "𝚑"],
    ["i", "𝚒"],
    ["j", "𝚓"],
    ["k", "𝚔"],
    ["l", "𝚕"],
    ["m", "𝚖"],
    ["n", "𝚗"],
    ["o", "𝚘"],
    ["p", "𝚙"],
    ["q", "𝚚"],
    ["r", "𝚛"],
    ["s", "𝚜"],
    ["t", "𝚝"],
    ["u", "𝚞"],
    ["v", "𝚟"],
    ["w", "𝚠"],
    ["x", "𝚡"],
    ["y", "𝚢"],
    ["z", "𝚣"],
    ["0", "𝟶"],
    ["1", "𝟷"],
    ["2", "𝟸"],
    ["3", "𝟹"],
    ["4", "𝟺"],
    ["5", "𝟻"],
    ["6", "𝟼"],
    ["7", "𝟽"],
    ["8", "𝟾"],
    ["9", "𝟿"]]

def assign_cat(plugin):
    """Assigns `fonts` module keywords to the `Warp` plugin."""

    meta = [
        [KEYWORD_MATHCAL, "Script (or calligraphy): 𝒜ℬ𝒞𝒶𝒷𝒸𝒜𝒞𝒶𝒷𝒸"],
        [KEYWORD_MATHBB, "Double-struck: 𝔸𝔹ℂ𝕒𝕓𝕔𝟙𝟚𝟛𝔸𝔹𝕒𝕓𝕔𝟙𝟚𝟛"],
        [KEYWORD_MATHFRAK, "Fraktur: 𝔄𝔅ℭ𝔞𝔟𝔠𝔄𝔅𝔞𝔟𝔠"],
        [KEYWORD_MATHSF, "Sans-serif: 𝖠𝖡𝖢𝖺𝖻𝖼𝟣𝟤𝟥𝖠𝖡𝖢𝖺𝖻𝖼𝟣𝟤𝟥"],
        [KEYWORD_TEXTSF, "Sans-serif: 𝖠𝖡𝖢𝖺𝖻𝖼𝟣𝟤𝟥𝖠𝖡𝖢𝖺𝖻𝖼𝟣𝟤𝟥"],
        [KEYWORD_MATHBF, "Serif Bold: 𝐀𝐁𝐂𝐚𝐛𝐜𝟏𝟐𝟑𝐀𝐁𝐂𝐚𝐛𝐜𝟏𝟐𝟑"],
        [KEYWORD_TEXTBF, "Serif Bold: 𝐀𝐁𝐂𝐚𝐛𝐜𝟏𝟐𝟑𝐀𝐁𝐂𝐚𝐛𝐜𝟏𝟐𝟑"],
        [KEYWORD_MATHBI, "Serif Bold italic: 𝑨𝑩𝑪𝒂𝒃𝒄𝟏𝟐𝟑𝑨𝑩𝑪𝒂𝒃𝒄𝟏𝟐𝟑"],
        [KEYWORD_TEXTIT, "Serif Italic: 𝐴𝐵𝐶𝑎𝑏𝑐123𝐴𝐵𝐶𝑎𝑏𝑐"],
        [KEYWORD_TEXTTT, "Mono-space: 𝙰𝙱𝙲𝚊𝚋𝚌𝟷𝟸𝟹𝙰𝙱𝙲𝚊𝚋𝚌𝟷𝟸𝟹"]]
    items = [plugin.create_item(
        category=plugin.CATEGORY_FONTS,
        label=el[0],
        short_desc=el[1],
        target=el[0],
        args_hint=kp.ItemArgsHint.REQUIRED,
        hit_hint=kp.ItemHitHint.IGNORE) for el in meta]
    return items

def _construct_output(user_input, prev_target):
    """Converts `user_input` string to output string and it's description.
    
    There are some bug with symbols with code greater than `U+FFFF`.
    For this reason, exceptions list must be specified for symbols from
    `U+0000` to `U+FFFF`. See more at `_process` function.
    """

    target = ""
    short_desc = ""
    if prev_target == KEYWORD_MATHCAL:
        target, short_desc = _process(
            user_input, MAPPING_MATHCAL_MAIN, extra=MAPPING_MATHCAL_EXTRA)
    elif prev_target == KEYWORD_MATHBB:
        target, short_desc = _process(
            user_input, MAPPING_MATHBB_MAIN, extra=MAPPING_MATHBB_EXTRA)
    elif prev_target == KEYWORD_MATHFRAK:
        target, short_desc = _process(
            user_input, MAPPING_MATHFRAK_MAIN, extra=MAPPING_MATHFRAK_EXTRA)
    elif prev_target == KEYWORD_MATHSF:
        target, short_desc = _process(user_input, MAPPING_MATHSF)
    elif prev_target == KEYWORD_MATHBF:
        target, short_desc = _process(user_input, MAPPING_MATHBF)
    elif prev_target == KEYWORD_MATHBI:
        target, short_desc = _process(user_input, MAPPING_MATHBI)
    elif prev_target == KEYWORD_TEXTIT:
        target, short_desc = _process(
            user_input, MAPPING_TEXTIT_MAIN, extra=MAPPING_TEXTIT_EXTRA)
    elif prev_target == KEYWORD_TEXTTT:
        target, short_desc = _process(user_input, MAPPING_TEXTTT)
    return target, short_desc

def _process(user_input, mapping, extra=[]):
    """Processes `user_input` string."""

    target = user_input
    for symbol in mapping:
        target = target.replace(symbol[0], symbol[1])
    for symbol in extra:
        target = target.replace(symbol[0], symbol[1])

    # short_desc = target

    # Some magic...
    # Problems with `item.target()` in `self.on_execute()` and `short_desc`
    # (`target_desc`).
    # Presumably, this connected with Keypirinha backend (on interpreter this
    # works fine).
    # `item.target()` and `self.create_item()` splits some output unicode chars
    # into two (e.g. U+1D49C).
    # Tested with different encodings (utf-8, utf-16-le, utf-16-be, utf-32-le,
    # utf-32-be) - no results.
    mirror = ""
    for char in target:
        if char in [symbol[1] for symbol in mapping]:
            mirror += char
    short_desc = target + mirror
    target = target + mirror * 3

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