def flatten_dict(d, parent_key='', sep='.'):

    items = {}
    if isinstance(d, dict):
        for k, v in d.items():
            new_key = f"{parent_key}{sep}{k}" if parent_key else k
            if isinstance(v, dict):
                items.update(flatten_dict(v, new_key, sep=sep))
            elif isinstance(v, list):
                for idx, item in enumerate(v):
                    list_key = f"{new_key}[{idx}]"
                    items.update(flatten_dict(item, list_key, sep=sep))
            else:
                items[new_key] = v
    elif isinstance(d, list):
        for idx, item in enumerate(d):
            list_key = f"{parent_key}[{idx}]"
            items.update(flatten_dict(item, list_key, sep=sep))
    else:
        items[parent_key] = d
    return items

# --- TESTS ---

def test_flatten_dict():
    # Simple nested dict
    inp = {'user': {'id': 1, 'name': 'Ana'}, 'meta': {'lang': 'en'}}
    out = {'user.id': 1, 'user.name': 'Ana', 'meta.lang': 'en'}
    assert flatten_dict(inp) == out

    
    inp = {'users': [{'id': 1}, {'id': 2}], 'meta': {'lang': 'en'}}
    out = {'users[0].id': 1, 'users[1].id': 2, 'meta.lang': 'en'}
    assert flatten_dict(inp) == out

    # Nested dicts and lists
    inp = {
        'a': {
            'b': [
                {'c': 1},
                {'d': 2}
            ]
        },
        'e': [3, 4]
    }
    out = {
        'a.b[0].c': 1,
        'a.b[1].d': 2,
        'e[0]': 3,
        'e[1]': 4
    }
    assert flatten_dict(inp) == out

    # List at root
    inp = [{'x': 1}, {'y': 2}]
    out = {'[0].x': 1, '[1].y': 2}
    assert flatten_dict(inp) == out

    # Mixed types
    inp = {'a': [1, {'b': 2}], 'c': 3}
    out = {'a[0]': 1, 'a[1].b': 2, 'c': 3}
    assert flatten_dict(inp) == out

   

if __name__ == "__main__":
    test_flatten_dict()
    # INSERT_YOUR_CODE
    sample_input = {'user': {'id': 1, 'name': 'Ana'}, 'meta': {'lang': 'en'}}
    sample_output = flatten_dict(sample_input)
    print(sample_output)
    
