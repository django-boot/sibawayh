import logging


logger = logging.getLogger(__name__)


SIBA_SETTINGS = {
    "error_on_unknown_key": False,
    "key_split_delimiter": ".",
    "locales_path": None,
    "cache_locales": True,
    "prefixes": ["application"],
    "default_prefix": "application",
    "default_locale": "en",
    "locales": ["en"],
    "pluralization": {
        "some_enabled": True,
        "some_limit": 4
    }
}


def set_setting(key: str, value: str):
    if key not in SIBA_SETTINGS:
        logger.warning(f"Siba settings don't seem to expect the key")

    SIBA_SETTINGS[key] = value


def get_setting(key: str):
    return SIBA_SETTINGS.get(key)


