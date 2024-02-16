import json


def safe_json_loads(json_str: str, default={}):
    try:
        return json.loads(json_str)
    except:
        return default
