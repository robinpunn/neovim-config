return {
  'nvim-telescope/telescope.nvim',
  branch = '0.1.x',  
  dependencies = {
    'nvim-lua/plenary.nvim',
    {
      'nvim-telescope/telescope-fzf-native.nvim',
      build = 'make',
      cond = function() return vim.fn.executable 'make' == 1 end,
    },
  },
  config = function()
    require('telescope').setup{
      extensions = {
        fzf = {
          fuzzy = true,
          override_generic_sorter = true,
          override_file_sorter = true,
          case_mode = "smart_case",
        }
      }
    }
    -- Load FZF 
    pcall(function() require('telescope').load_extension('fzf') end)
    
    vim.keymap.set('n', '<leader>ff', require('telescope.builtin').find_files, { desc = 'Telescope find files' })
    vim.keymap.set('n', '<leader>fg', require('telescope.builtin').live_grep, { desc = 'Telescope live grep' })
    vim.keymap.set('n', '<leader>fb', require('telescope.builtin').buffers, { desc = 'Telescope buffers' })
    vim.keymap.set('n', '<leader>fh', require('telescope.builtin').help_tags, { desc = 'Telescope help tags' })
  end,
}

