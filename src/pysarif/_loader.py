import json

from ._sarif_log import SarifLog

def delete_none(_dict):
    """Delete None values recursively from all of the dictionaries, tuples, lists, sets"""
    if isinstance(_dict, dict):
        for key, value in list(_dict.items()):
            if isinstance(value, (list, dict, tuple, set)):
                _dict[key] = delete_none(value)
            elif value is None or key is None:
                del _dict[key]

    elif isinstance(_dict, (list, set, tuple)):
        _dict = type(_dict)(delete_none(item) for item in _dict if item is not None)

    return _dict

def load_from_dict(dict: dict) -> SarifLog:
    return SarifLog.from_dict(dict)

def load_from_json(json: str) -> SarifLog:
    return SarifLog.from_json(json)

def load_from_file(filepath: str) -> SarifLog:
    with open(filepath, 'r', encoding="utf-8") as f:
        contents = f.read()
    return load_from_json(contents)

def save_to_dict(sarif: SarifLog) -> dict:
    out = sarif.to_dict()
    out = delete_none(out)
    return out

def save_to_json(sarif: SarifLog) -> str:
    return json.dumps(save_to_dict(sarif))

def save_to_file(sarif: SarifLog, filepath: str):
    with open(filepath, 'w', encoding="utf-8") as f:
        contents = save_to_json(sarif)
        f.write(contents)