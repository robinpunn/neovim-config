import argparse
from sync import sync_plugins
from edit import edit_plugin
from clean import cleanup_plugins
from add import add_plugin


def main():
    parser = argparse.ArgumentParser(description="Neovim Plugin Manager")
    subparsers = parser.add_subparsers(dest="command")

    add_parser = subparsers.add_parser("add", help="Add an entry to 'plugins.json' to be installed")
    add_parser.add_argument("repo", help="Plugin in the format 'author/name'")
    add_parser.add_argument("--tag", help="Optional tag")
    add_parser.add_argument("--branch", help="Optional branch")
    add_parser.add_argument("--plugin-type", choices=["start","opt"], default="start")

    sync_parser = subparsers.add_parser("sync", help="Sync plugins from disk to plugins.json")
    sync_parser.add_argument("--force", action="store_true")

    edit_parser = subparsers.add_parser("edit", help="Edit a plugin in plugins.json")
    edit_parser.add_argument("name", help="Name of the plugin to edit")
    edit_parser.add_argument("--repo", help="New repu URL")
    edit_parser.add_argument("--tag", help="Tag to use")
    edit_parser.add_argument("--branch", help="Branch to use")
    edit_parser.add_argument("--plugin-type", choices=["start", "opt"], help="Lazy load?")
    edit_parser.add_argument("--clear-tag", action="store_true", help="Remove the tag field")
    edit_parser.add_argument("--clear-branch", action="store_true", help="Remove the branch field")

    cleanup_parser = subparsers.add_parser("clean", help="Remove plugins not found on disk")
    cleanup_parser.add_argument("--force", action="store_true", help="Skip confirmation prompt")
    cleanup_parser.add_argument("--dry-run", action="store_true", help="Preview changes without saving")

    args = parser.parse_args()

    if args.command == "add":
        add_plugin(identifier=args.repo,
                   tag=args.tag,
                   branch=args.branch,
                   plugin_type=args.plugin_type
                   )
    elif args.command == "sync":
        sync_plugins(force_repo_update=args.force)
    elif args.command == "edit":
        edit_plugin(name=args.name,
                    repo=args.repo,
                    tag=args.tag,
                    branch=args.branch,
                    plugin_type=args.plugin_type,
                    clear_tag=args.clear_tag,
                    clear_branch=args.clear_branch
                    )
    elif args.command == "clean":
        cleanup_plugins(force=args.force, dry_run=args.dry_run)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
