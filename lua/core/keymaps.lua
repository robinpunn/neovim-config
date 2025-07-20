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
--vim.keymap.set('n', '<leader>q', function()
--	vim.diagnostic.setloclist()
--	vim.cmd("lopen")
--end)

-- Oil
vim.keymap.set("n", "<leader>o", "<cmd>Oil<cr>", { desc = "Open Oil file explorer" })
vim.keymap.set("n", "<leader>O", function() require("oil").open_float(".") end, { desc = "Open Oil (float)" })

-- netrw
local netrw_win = nil
local function toggle_netrw()
  -- Check if the tracked window still contains netrw
  if netrw_win and vim.api.nvim_win_is_valid(netrw_win) then
    local buf = vim.api.nvim_win_get_buf(netrw_win)
    if vim.api.nvim_buf_get_option(buf, 'filetype') == 'netrw' then
      -- It's still netrw, close it
      vim.api.nvim_win_close(netrw_win, false)
      netrw_win = nil
    else
      -- Window exists but no longer netrw, open new netrw
      vim.cmd('Vex | vertical resize 30')
      netrw_win = vim.api.nvim_get_current_win()
    end
  else
    -- No valid netrw window, open new one
    vim.cmd('Vex | vertical resize 30')
    netrw_win = vim.api.nvim_get_current_win()
  end
end

vim.keymap.set('n', '<C-b>', toggle_netrw, { noremap = true, silent = true, desc = "Toggle netrw" })
