from utils import load_plugins, save_plugins, get_orphaned_plugins


def cleanup_plugins(force=False, dry_run=False):
    all_plugins = load_plugins()
    to_remove, existing_names = get_orphaned_plugins(all_plugins)
    removed_count = len(to_remove)

    if removed_count == 0:
        print("Nothing to remove")
        return

    print(f"{removed_count} orphaned plugin(s) found.")
    for plugin in to_remove:
        print(f" - {plugin['name']}")

    if dry_run:
        print("\nDry run mode: No changes made.")
        return

    if not force:
        confirm = input("Remove them from plugins.json? (y/n): ").strip().lower()
        if confirm != "y":
            print("Cleanup aborted")
            return

    cleaned_plugins = [p for p in all_plugins if p["name"] in existing_names]

    save_plugins(cleaned_plugins)
    print(f"Removed {removed_count} orphaned plugins(s) from plugins.json.")
