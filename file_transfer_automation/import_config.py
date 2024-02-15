from typing import Any
import tomli


def import_config() -> dict[str, Any]:
    with open('config.toml', 'rb') as f:
        config = tomli.load(f)
    return config
