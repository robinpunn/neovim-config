# neovim-config

## Features

- **Colorscheme:** 
    - tokyonight
- **Line numbers**
- **Treesitter:** 
    - syntax highlighting
    - code folding
    - indentation
- **LSP (Language Server Protocol):** 
    - go to definition  
    - python (pylsp)
    - javaScript/typeScript (ts_ls)
- **Fugitive**
    - lazy load on `<leader>gs` or `<cmd>G`
- **Telescope**
    - fzf
- **Keymaps:**  
    - diagnostics navigation
    - quick access to location list

## Structure
`~/.config/nvim/`
```
├── init.lua
└── lua/
  ├── config/
  │ └── lazy.lua
  ├── core/
  │ ├── options.lua 
  │ ├── keymaps.lua 
  │ └── autocmds.lua 
  └── plugins/
    ├── treesitter.lua
    ├── lspconfig.lua
    ├── fugitive.lua
    ├── telescope.lua
    └── tokyonight.lua
```
