from utils import load_plugins, save_plugins


def edit_plugin(name,
                repo=None,
                tag=None,
                branch=None,
                plugin_type=None,
                clear_tag=None,
                clear_branch=None
                ):
    plugins = load_plugins()
    found = False

    for plugin in plugins:
        if plugin["name"] == name:
            found = True
            if repo:
                plugin["repo"] = repo
                print(f"Updated repo for {name} to {repo}")
            if tag:
                plugin["tag"] = tag
                plugin.pop("branch", None)
                print(f"Set tag for {name} to {tag}")
            if branch:
                plugin["branch"] = branch
                plugin.pop("tag", None)
                print(f"Set branch for {name} to {branch}")
            if plugin_type in {"start", "opt"}:
                plugin["type"] = plugin_type
                print(f"Set type for {name} to {plugin_type}")
            if clear_tag:
                plugin.pop("tag", None)
                print(f"Removed tag from {name}")
            if clear_branch:
                plugin.pop("branch", None)
                print(f"Removed branch from {name}")
            break

    if not found:
        print(f"Plugin '{name}' not found.")
        return

    save_plugins(plugins)
    print(f"Updated '{name}' in plugins.json")
