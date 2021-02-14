# Keypirinha launcher (keypirinha.com)

import keypirinha as kp
import keypirinha_util as kpu
import keypirinha_net as kpnet

from Warp.cat import base
from Warp.cat import symbols
from Warp.cat import operations
from Warp.cat import diacritical
from Warp.cat import fonts
from Warp.cat import roman
from Warp.cat import matrix
from Warp.cat import table
from Warp.cat import dirtree

class Warp(kp.Plugin):
    """
    Converts LaTeX-like syntax (symbols and exressions) to Unicode.

    This plugin is mainly designed for scientists (mathematicians, physicists,
    chemists, biologists, ...) and IT professionals (data scientists, ...).
    The main purpose is to give an ability to write lighter text and is to
    offload markup (Markdown, AsciiDoc, reStructuredText, LaTeX) from excessive
    commands or long syntax. Writing `α` instead of `\\alpha` makes text much
    more readable, doesn't it? Moreover, thanks to Keypirinha's independency,
    you can use LaTeX-like syntax almost everywhere. It can be plain text
    editors (Vim, Emacs, Atom, Visual Studio Code, ...) and even WYSWYG editors
    (Libre Office Writer, Microsoft Word and etc).

    Typical usage of this plugin:
    0. Open Keypirinha and enter Warp's environment (type `$`).
    1. Write a LaTeX-style command.
    2. Press `Enter` (result will be copied into clipboard).
    3. Paste result into a text editor or into some text field.
    """

    KEYWORD_PLUGIN = "$"

    CATEGORY_BASE = kp.ItemCategory.USER_BASE + 1
    CATEGORY_SYMBOLS = kp.ItemCategory.USER_BASE + 2
    CATEGORY_OPERATIONS = kp.ItemCategory.USER_BASE + 3
    CATEGORY_DIACRITICAL = kp.ItemCategory.USER_BASE + 4
    CATEGORY_FONTS = kp.ItemCategory.USER_BASE + 5
    CATEGORY_ROMAN = kp.ItemCategory.USER_BASE + 6
    CATEGORY_MATRIX = kp.ItemCategory.USER_BASE + 7
    CATEGORY_TABLE = kp.ItemCategory.USER_BASE + 8
    CATEGORY_DIRTREE = kp.ItemCategory.USER_BASE + 9

    def __init__(self):
        super().__init__()

    def on_start(self):
        pass

    def on_catalog(self):
        self.set_catalog([
            self.create_item(
                category=kp.ItemCategory.KEYWORD,
                label=self.KEYWORD_PLUGIN,
                short_desc="Convert LaTeX symbol to Unicode symbol",
                target=self.KEYWORD_PLUGIN,
                args_hint=kp.ItemArgsHint.REQUIRED,
                hit_hint=kp.ItemHitHint.NOARGS)])

    def on_suggest(self, user_input, items_chain):
        is_keyword = True
        if len(items_chain) > 0:
            is_keyword = (items_chain[0].category() != kp.ItemCategory.KEYWORD)
        if is_keyword:
            return
            
        suggestions = []

        category = items_chain[-1].category()
        target = items_chain[-1].target()

        # Add suggestions
        if category == self.CATEGORY_BASE:
            suggestions.append(base.get_suggestions(self, user_input, target))
        elif category == self.CATEGORY_OPERATIONS:
            suggestions.extend(
                operations.get_suggestions(self, user_input, target))
        elif category == self.CATEGORY_DIACRITICAL:
            suggestions.append(
                diacritical.get_suggestions(self, user_input, target))
        elif category == self.CATEGORY_FONTS:
            suggestions.append(fonts.get_suggestions(self, user_input, target))
        elif category == self.CATEGORY_ROMAN:
            suggestions.append(roman.get_suggestions(self, user_input, target))
        elif category == self.CATEGORY_MATRIX:
            suggestions.append(matrix.get_suggestions(self, user_input, target))
        elif category == self.CATEGORY_TABLE:
            suggestions.append(table.get_suggestions(self, user_input))
        elif category == self.CATEGORY_DIRTREE:
            suggestions.append(dirtree.get_suggestions(self, user_input))
        else:
            # Assign categories (main plugin entries)
            suggestions.extend(base.assign_cat(self))
            suggestions.extend(symbols.assign_cat(self))
            suggestions.extend(operations.assign_cat(self))
            suggestions.extend(diacritical.assign_cat(self))
            suggestions.extend(fonts.assign_cat(self))
            suggestions.extend(roman.assign_cat(self))
            suggestions.extend(matrix.assign_cat(self))
            suggestions.append(table.assign_cat(self))
            suggestions.append(dirtree.assign_cat(self))

        self.set_suggestions(suggestions, kp.Match.DEFAULT, kp.Sort.SCORE_DESC)

    def on_execute(self, item, action):
        if item:
            kpu.set_clipboard(item.target())

    def on_activated(self):
        pass

    def on_deactivated(self):
        pass

    def on_events(self, flags):
        pass
