# Keypirinha Plugin: Warp

This is Warp, a plugin for the
[Keypirinha](http://keypirinha.com) launcher.

Converts LaTeX-like syntax (symbols and exressions) to Unicode.

`\xi` → `ξ`

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
1. Open Keypirinha and enter Warp's environment (type `$`).
2. Write a LaTeX-style command.
3. Press `Enter` (result will be copied into clipboard).
4. Paste result into a text editor or into some text field.


## Download

Latest version:
[Warp/Releases](https://github.com/deverte/keypirinha-warp/releases).


## Install

Once the `Warp.keypirinha-package` file is installed,
move it to the `InstalledPackage` folder located at:

* `Keypirinha\portable\Profile\InstalledPackages` in **Portable mode**
* **Or** `%APPDATA%\Keypirinha\InstalledPackages` in **Installed mode** (the
  final path would look like
  `C:\Users\%USERNAME%\AppData\Roaming\Keypirinha\InstalledPackages`)


## Usage

Example:  
1. Enter the Warp environment (type `$` and press *Enter*). Now you will see
some suggestions of this plugin.
2. Enter the **mathfrak** environment. Start typing `mathfrak` or `\mathfrak`
and you will see suggestion `\mathfrak`. Press *Enter*.
3. Type `Hello World!` and press *Enter*.
4. Now in your system cipboard will be `ℌ𝔢𝔩𝔩𝔬, 𝔚𝔬𝔯𝔩𝔡!`. You can paste it into an
arbitary text editor or some text field (:note: some text fields don't support
Unicode, or your text editor can use another encoding at this moment - in this
case you will see rectangles instead of `ℌ𝔢𝔩𝔩𝔬, 𝔚𝔬𝔯𝔩𝔡!`).

For more commands and environments, see
[Warp/Wiki](https://github.com/deverte/keypirinha-warp/wiki).


## Change Log

See change log and roadmap at
[Warp/Projects](https://github.com/deverte/keypirinha-warp/projects).


## License

This package is distributed under the terms of the [MIT license](./LICENSE).


## Contribute

1. Check for open issues or open a fresh issue to start a discussion around a
   feature idea or a bug (see
   [Warp/Issues](https://github.com/deverte/keypirinha-warp/issues)).
2. Fork this repository on GitHub to start making your changes to the **dev**
   branch.
3. Send a pull request.
4. Add yourself to the *Contributors* section below (or create it if needed)!

### Build Instructions
For developing, you need to use the
[Keypirinha/SDK](https://github.com/Keypirinha/SDK).

Let's assume that the SDK is located at `%KEYPIRINHA_SDK%` directory,
project is located at `%PROJECT%` directory and Keypirinha is located at
`%KEYPIRINHA_HOME%`.
1. First, you need to enter the SDK's environment:
`%KEYPIRINHA_SDK%\cmd\kpenv.cmd`.
2. Then run `%PROJECT%\make.cmd build`.
3. And copy `%PROJECT%\build\Warp.keypirinha-package` into
`%KEYPIRINHA_HOME%\config\Profile\InstalledPackages\Warp.keypirinha-package`.

Alternatively, you can create and modify this file
(replace `enter\your\sdk\path`, `enter\your\project\path` and
`enter\your\keypirinha\path` with your actual values):
```cmd
set KEYPIRINHA_SDK=enter\your\sdk\path
set PROJECT=enter\your\project\path
set KEYPIRINHA_HOME=enter\your\keypirinha\path

%KEYPIRINHA_SDK%\cmd\kpenv.cmd
cd %PROJECT%
make.cmd build
copy %PROJECT%\build\Warp.keypirinha-package %KEYPIRINHA_HOME%\config\Profile\InstalledPackages\Warp.keypirinha-package
```