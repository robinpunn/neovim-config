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
  end,
}

