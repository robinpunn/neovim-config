import argparse
from sync import sync_plugins
from edit import edit_plugin


def main():
    parser = argparse.ArgumentParser(description="Neovim Plugin Manager")
    subparsers = parser.add_subparsers(dest="command")

    subparsers.add_parser("sync", help="Sync plugins from disk to plugins.json")

    edit_parser = subparsers.add_parser("edit", help="Edit a plugin in plugins.json")
    edit_parser.add_argument("name", help="Name of the plugin to edit")
    edit_parser.add_argument("--repo", help="New repu URL")
    edit_parser.add_argument("--tag", help="Tag to use")
    edit_parser.add_argument("--branch", help="Branch to use")
    edit_parser.add_argument("--plugin-type", choices=["start", "opt"], help="Lazy load?")
    edit_parser.add_argument("--clear-tag", action="store_true", help="Remove the tag field")
    edit_parser.add_argument("--clear-branch", action="store_true", help="Remove the branch field")

    args = parser.parse_args()

    if args.command == "sync":
        sync_plugins()
    elif args.command == "edit":
        edit_plugin(args.name,
                    args.repo,
                    args.tag,
                    args.branch,
                    args.plugin_type,
                    args.clear_tag,
                    args.clear_branch
                    )
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
