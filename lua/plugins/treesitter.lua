return {
  "nvim-treesitter/nvim-treesitter",
  build = ":TSUpdate",
  config = function()
    require('nvim-treesitter.configs').setup {
      ensure_installed = {
        "python",
        "html",
        "javascript",
        "typescript",
        "tsx",
	"go",
	"solidity",
	"rust",
	"c",
	"asm",
      },
      highlight = { enable = true },
      indent = { enable = true },
    }
  end,
}

