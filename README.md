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
  - python (pylsp)
  - javaScript/typeScript (tsserver)
- **Keymaps:**  
  - diagnostics navigation
  - quick access to location list

## Structure
- ~/.config/nvim/
├── init.lua
└── lua/
  ├── core/
  │ ├── options.lua 
  │ ├── keymaps.lua 
  │ └── autocmds.lua 
  └── plugins/
    ├── treesitter.lua
    ├── lspconfig.lua
    └── colorscheme.lua
