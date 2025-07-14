return {
  "neovim/nvim-lspconfig",
  config = function()
    local lspconfig = require("lspconfig")

    local on_attach = function(client, bufnr)
      local buf_map = function(mode, lhs, rhs, desc)
        vim.keymap.set(mode, lhs, rhs, { buffer = bufnr, desc = desc })
      end

      buf_map("n", "<leader>gd", vim.lsp.buf.definition, "Go to definition")
      buf_map("n", "K", vim.lsp.buf.hover, "Show hover")
    end

    -- Python LSP
    lspconfig.pylsp.setup({
      on_attach = on_attach,
    })

    -- TypeScript / JavaScript LSP (typescript-language-server)
    lspconfig.ts_ls.setup({
      on_attach = on_attach,
    })

    -- HTML LSP
    lspconfig.html.setup({
      on_attach = on_attach,
    })
  end,
}

