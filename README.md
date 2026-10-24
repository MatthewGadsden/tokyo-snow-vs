# Tokyo Snow

![Tokyo Snow Theme](icon.png)

Tokyo Snow is a warm, dark color scheme for Visual Studio Code, sampled from a photo of a snowy Tokyo alley at night. The lit vending machines give it reds, oranges and golds, the green-tinted glow on the snow gives it sage and pine, and the shadowed pavement and walls become the backgrounds. It is the VS Code port of the `tokyo-snow` palette used across my Hyprland setup (waybar, rofi, hyprlock, Neovim and the shell prompt).

## Palette

| Name   | Hex       | Used for                                       |
| ------ | --------- | ---------------------------------------------- |
| night  | `#1c1c1a` | Sidebar, panels, title and status bars         |
| shadow | `#2a2a28` | Editor background                              |
| slate  | `#3a3933` | Borders, current line, list selection          |
| dim    | `#7d7860` | Comments, line numbers, muted text             |
| snow   | `#f1e4b5` | Emphasised text, active tabs                   |
| gold   | `#ecd08f` | Body text, variables, operators                |
| neon   | `#d5583d` | Keywords, tags, errors                         |
| ember  | `#db814c` | Numbers, constants, escapes, decorators        |
| amber  | `#e1b568` | Types and classes, cursor, accent, warnings    |
| sage   | `#c4c88e` | Properties and keys, regular expressions       |
| moss   | `#a6d46c` | Strings, added lines                           |
| pine   | `#6fc28a` | Functions and methods, links, info             |
| brick  | `#96402e` | (part of the palette; not used in the editor)  |

## Installation

Tokyo Snow is not on the Marketplace yet, so install it from this repo.

**Link the folder** (picks up edits after a window reload):

```sh
git clone https://github.com/MatthewGadsden/tokyo-snow-vs
ln -s "$PWD/tokyo-snow-vs" ~/.vscode/extensions/tokyo-snow-vs
```

Use `~/.vscode-oss/extensions` for Code - OSS or VSCodium.

**Or package it** as a `.vsix`:

```sh
npx @vscode/vsce package
code --install-extension tokyo-snow-vs-1.0.0.vsix
```

## Usage

Once installed, switch to the "Tokyo Snow" theme by:

1. Opening the Command Palette (`Ctrl+Shift+P` or `Cmd+Shift+P`)
2. Typing "Color Theme"
3. Selecting "Preferences: Color Theme"
4. Choosing "Tokyo Snow" from the themes

Open `tokyo-snow-demo.js` to see most of the syntax colours in one place.

## Contributing

Issues and pull requests are welcome on [GitHub](https://github.com/MatthewGadsden/tokyo-snow-vs/issues).

## License

MIT License
