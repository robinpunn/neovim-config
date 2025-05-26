-- line number
vim.opt.number = true

-- tokyonight colorscheme
require("tokyonight").setup({
  style = "night",
  transparent = false	
})
vim.cmd[[colorscheme tokyonight]]

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

-- folding
vim.api.nvim_create_autocmd("FileType", {
  pattern = "*",
  callback = function()
    vim.wo.foldmethod = "expr"
    vim.wo.foldexpr = "v:lua.vim.treesitter.foldexpr()"
    vim.wo.foldlevel = 99  -- (optional) open all folds by default
  end,
})


---LSP
local lspconfig = require('lspconfig')
--python
lspconfig.pylsp.setup({})
--javscript
lspconfig.ts_ls.setup({})

--dx messages
vim.keymap.set('n', '<leader>e', vim.diagnostic.open_float)
--jump to dx
vim.keymap.set('n', "]g", function() vim.diagnostic.jump({count = 1}) end)
vim.keymap.set('n', "[g", function() vim.diagnostic.jump({count = -1}) end)
--dx message on jump
vim.diagnostic.config({
    jump = {float = true}
})
-- location list
vim.keymap.set('n', '<leader>q', function()
	vim.diagnostic.setloclist()
	vim.cmd("lopen")
end)


-- example from nvim-treesitter github
--[[
require'nvim-treesitter.configs'.setup {
  -- A list of parser names, or "all" (the listed parsers MUST always be installed)
  ensure_installed = { "c", "lua", "vim", "vimdoc", "query", "markdown", "markdown_inline" },

  -- Install parsers synchronously (only applied to `ensure_installed`)
  sync_install = false,

  -- Automatically install missing parsers when entering buffer
  -- Recommendation: set to false if you don't have `tree-sitter` CLI installed locally
  auto_install = true,

  -- List of parsers to ignore installing (or "all")
  ignore_install = { "javascript" },

  ---- If you need to change the installation directory of the parsers (see -> Advanced Setup)
  -- parser_install_dir = "/some/path/to/store/parsers", -- Remember to run vim.opt.runtimepath:append("/some/path/to/store/parsers")!

  highlight = {
    enable = true,

    -- NOTE: these are the names of the parsers and not the filetype. (for example if you want to
    -- disable highlighting for the `tex` filetype, you need to include `latex` in this list as this is
    -- the name of the parser)
    -- list of language that will be disabled
    disable = { "c", "rust" },
    -- Or use a function for more flexibility, e.g. to disable slow treesitter highlight for large files
    disable = function(lang, buf)
        local max_filesize = 100 * 1024 -- 100 KB
        local ok, stats = pcall(vim.loop.fs_stat, vim.api.nvim_buf_get_name(buf))
        if ok and stats and stats.size > max_filesize then
            return true
        end
    end,

    -- Setting this to true will run `:h syntax` and tree-sitter at the same time.
    -- Set this to `true` if you depend on 'syntax' being enabled (like for indentation).
    -- Using this option may slow down your editor, and you may see some duplicate highlights.
    -- Instead of true it can also be a list of languages
    additional_vim_regex_highlighting = false,
  },
}
]]













-- old config i didn't want to delete
--[[
vim.opt.foldmethod = "indent"
]]
