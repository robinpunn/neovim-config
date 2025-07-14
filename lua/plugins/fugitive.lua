return {
  "tpope/vim-fugitive",
  cmd = { "Git" },  -- lazy-load on :Git command
  keys = {
    { "<leader>gs", "<cmd>Git<cr>", desc = "Git status" },
  },
}

