import csv
import json
from typing import List, Dict, Any


def interests_to_dict(interests) -> Dict[str, Any]:
    mapped_interests = {}
    for interest in interests:
        inmap = mapped_interests
        keys = interest.key.split('.')
        for key in keys[:-1]:
            if key not in inmap:
                inmap[key] = {}
            inmap = inmap[key]
        inmap[keys[-1]] = interest.value
    return mapped_interests


def export_file(interests, filename):
    if filename.endswith('.json'):
        data = interests_to_dict(interests)
        export_json(data, filename)
    elif filename.endswith('.yaml') or filename.endswith('.yml'):
        data = interests_to_dict(interests)
        export_yaml(data, filename)
    elif filename.endswith('.csv'):
        export_csv(interests, filename)


def export_json(data, filename):
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)


def export_csv(interests, filename):
    with open(filename, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['Key', 'Label', 'Value'])
        for interest in interests:
            writer.writerow([interest.key, interest.label, interest.value])


def export_yaml(data, filename):
    try:
        import yaml
        with open(filename, 'w') as f:
            yaml.dump(data, f, default_flow_style=False)
    except ImportError:
        import logging
        logging.error("PyYAML is not installed. Cannot export to YAML.")
