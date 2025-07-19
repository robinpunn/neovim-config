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

-- Oil
vim.keymap.set("n", "<leader>o", "<cmd>Oil<cr>", { desc = "Open Oil file explorer" })
vim.keymap.set("n", "<leader>O", function() require("oil").open_float(".") end, { desc = "Open Oil (float)" })
