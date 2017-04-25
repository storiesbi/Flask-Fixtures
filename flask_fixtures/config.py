JSON_PARSE_DATETIME = 'loaders.json.parse_datetime'

_default_settings = {
    JSON_PARSE_DATETIME: True
}

settings = _default_settings.copy()


def reset():
    global settings
    settings = _default_settings.copy()