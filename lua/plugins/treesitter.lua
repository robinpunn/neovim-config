-- Treesitter highlight/indent
require'nvim-treesitter.configs'.setup {
  ensure_installed = {
	"python",
	"html",
	"javascript",
	"typescript",
	"tsx"
	},
  highlight = { enable = true },
  indent = { enable = true }, 
}
