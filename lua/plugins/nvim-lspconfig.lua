---LSP
local lspconfig = require('lspconfig')

-- keymaps
local on_attach = function(client, bufnr)
    local buf_map = function(mode, lhs, rhs, desc)
	vim.keymap.set(mode, lhs, rhs, { buffer = bufnr, desc = desc})
    end

    buf_map('n', '<leader>gd', vim.lsp.buf.definition, "Go to definition")
    buf_map('n', 'K', vim.lsp.buf.hover, "Show hover")
end


--python
lspconfig.pylsp.setup({
    on_attach = on_attach,
})
--javscript
lspconfig.ts_ls.setup({
    on_attach = on_attach,
})
