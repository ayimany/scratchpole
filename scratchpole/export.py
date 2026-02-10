import json


def export_file(interests, filename):
    if filename.endswith('.json'):
        export_json(interests, filename)

# TODO: This seems inefficient
def export_json(interests, filename):
    mapped_interests = {}
    for interest in interests:
        inmap = mapped_interests
        keys = interest.key.split('.')
        for key in keys[:-1]:
            if key not in inmap:
                inmap[key] = {}
            inmap = inmap[key]
        inmap[keys[-1]] = interest.value

    json.dump(mapped_interests, open(filename, 'w'))
