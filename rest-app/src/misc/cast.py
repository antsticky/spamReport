import json


def safe_json_loads(json_str: str, default={}):
    """
    Safely load JSON string into a dictionary, with an optional default value.

    Args:
        json_str (str): The JSON string to be loaded.
        default (dict, optional): The default value to return if JSON parsing fails. Defaults to an empty dictionary.

    Returns:
        dict: The parsed JSON content as a dictionary, or the default value if parsing fails.
    """

    try:
        return json.loads(json_str)
    except:
        return default
