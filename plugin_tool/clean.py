from utils import load_plugins, save_plugins, get_existing_plugins_by_type


def cleanup_plugins(force=False, dry_run=False):
    plugins = load_plugins()
    existing_names = {p["name"] for p in get_existing_plugins_by_type()}

    to_remove = [
        plugin for plugin in plugins
        if plugin["name"] not in existing_names
    ]
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

    cleaned_plugins = [
        plugin for plugin in plugins
        if plugin["name"] in existing_names
    ]
    save_plugins(cleaned_plugins)
    print(f"Removed {removed_count} orphaned plugins(s) from plugins.json.")
