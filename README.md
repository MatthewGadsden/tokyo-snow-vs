# Tokyo Snow

![A snowy Tokyo alley at night, lit by vending machines](tokyo-snow-banner.jpg)

Tokyo Snow is a warm, dark color scheme for Visual Studio Code, sampled from a single photo: a snowy Tokyo alley at night, lit only by a row of vending machines. The **lit machines and signs** give it its reds, oranges and golds, the **snow under green-tinted light** gives it sage, moss and pine, and the **shadowed walls and pavement** become the backgrounds. Every colour in the theme is one of the 13 below; nothing is invented outside the photo.

It is the VS Code port of the `tokyo-snow` palette that themes the rest of my desktop (Hyprland, waybar, rofi, hyprlock, Neovim and the shell prompt), so the editor finally matches everything around it.

## Palette

### Accents

| | Name | Hex | In the photo | In the editor |
| --- | --- | --- | --- | --- |
| <img src="images/palette/brick.png" width="48" height="24" alt="brick"> | brick | `#96402e` | Deep red in the machines' shadows | Reserved; not used in the editor |
| <img src="images/palette/neon.png" width="48" height="24" alt="neon"> | neon | `#d5583d` | The red KIRIN sign | Keywords, tags, `this`/`self`, errors |
| <img src="images/palette/ember.png" width="48" height="24" alt="ember"> | ember | `#db814c` | Burnt-orange machine glow | Numbers, constants, escapes, decorators |
| <img src="images/palette/amber.png" width="48" height="24" alt="amber"> | amber | `#e1b568` | Lit drink shelves | Types and classes, cursor, accent, warnings |
| <img src="images/palette/gold.png" width="48" height="24" alt="gold"> | gold | `#ecd08f` | The BOSS sign and lit panels | Body text, variables, operators |
| <img src="images/palette/sage.png" width="48" height="24" alt="sage"> | sage | `#c4c88e` | Snow under the green-tinted light | Properties and keys, regular expressions |
| <img src="images/palette/moss.png" width="48" height="24" alt="moss"> | moss | `#a6d46c` | Mid green tint | Strings, added lines |
| <img src="images/palette/pine.png" width="48" height="24" alt="pine"> | pine | `#6fc28a` | Cold green-teal cast on the snow | Functions and methods, links, info |

### Text & backgrounds

| | Name | Hex | In the photo | In the editor |
| --- | --- | --- | --- | --- |
| <img src="images/palette/night.png" width="48" height="24" alt="night"> | night | `#1c1c1a` | Deepest shadow | Sidebar, panels, title and status bars |
| <img src="images/palette/shadow.png" width="48" height="24" alt="shadow"> | shadow | `#2a2a28` | The alley's dark walls | Editor background |
| <img src="images/palette/slate.png" width="48" height="24" alt="slate"> | slate | `#3a3933` | Lit edges of the shadows | Borders, current line, list selection |
| <img src="images/palette/dim.png" width="48" height="24" alt="dim"> | dim | `#7d7860` | Shadowed pavement | Comments, line numbers, muted text |
| <img src="images/palette/snow.png" width="48" height="24" alt="snow"> | snow | `#f1e4b5` | The brightest snow | Emphasised text, active tabs |

## Installation

Tokyo Snow isn't on the Visual Studio Marketplace yet, so install it from this repository.

1. Clone the repository:
   ```sh
   git clone https://github.com/MatthewGadsden/tokyo-snow-vs
   ```
2. Link it into your extensions folder (edits show up after a window reload):
   ```sh
   ln -s "$PWD/tokyo-snow-vs" ~/.vscode/extensions/tokyo-snow-vs
   ```
   Use `~/.vscode-oss/extensions` for Code - OSS or VSCodium.
3. Or, instead of linking, package it as a `.vsix` and install that:
   ```sh
   cd tokyo-snow-vs
   npx @vscode/vsce package
   code --install-extension tokyo-snow-vs-1.0.2.vsix
   ```
4. Restart Visual Studio Code, or run "Developer: Reload Window"
5. Press `Ctrl+Shift+P` (or `Cmd+Shift+P` on Mac) to open the command palette
6. Type "Color Theme" and select "Preferences: Color Theme"
7. Select "Tokyo Snow" from the list

## Usage

Once installed, switch to the "Tokyo Snow" theme by:

1. Opening the Command Palette (`Ctrl+Shift+P` or `Cmd+Shift+P`)
2. Typing "Color Theme"
3. Selecting "Preferences: Color Theme"
4. Choosing "Tokyo Snow" from the themes

Open [`tokyo-snow-demo.js`](tokyo-snow-demo.js) to see most of the syntax colours in one place; its comments say which colour each piece of syntax should be.

## Contributing

Contributions are welcome. Submit issues or pull requests on [GitHub](https://github.com/MatthewGadsden/tokyo-snow-vs/issues). If you change a colour, keep it inside the 13-colour palette above.

## License

MIT License
