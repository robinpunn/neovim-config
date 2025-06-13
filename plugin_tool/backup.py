import os
import shutil
from datetime import datetime
from utils import (
    INIT_LUA_FILE,
    LUA_PLUGINS_DIR,
    LUA_PLUGINS_CORE_DIR,
    JSON_FILE,
    BACKUP_DIR
)


def create_backup():
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_path = os.path.join(BACKUP_DIR, f"backup-{timestamp}")
    os.makedirs(backup_path, exist_ok=True)

    if os.path.exists(INIT_LUA_FILE):
        shutil.copy(INIT_LUA_FILE, os.path.join(backup_path, "init.lua"))
        print("Backed up init.lua")

    if os.path.exists(JSON_FILE):
        shutil.copy(JSON_FILE, os.path.join(backup_path, "plugins.json"))
        print("Backed up plugins.json")

    lua_dir_backup = os.path.join(backup_path, "lua")
    os.makedirs(lua_dir_backup, exist_ok=True)

    for config_dir in [LUA_PLUGINS_DIR, LUA_PLUGINS_CORE_DIR]:
        if os.path.exists(config_dir):
            name = os.path.basename(config_dir)
            target = os.path.join(lua_dir_backup, name)

            if not os.path.exists(target):
                shutil.copytree(config_dir, target)
                print(f"Backed up plugin configs from lua/{name}")
            else:
                print(f"Skipped lua/{name}: already exists in backup.")

    print(f"\n✅ Backup complete: {backup_path}")
