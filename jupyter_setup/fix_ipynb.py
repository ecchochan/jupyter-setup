from pathlib import Path
import json

for path in Path('').rglob('*.ipynb'):
    print(path)
    with open(path) as f:
        text = f.read()

    j = json.loads(text)
    for e in j['cells']:
        e['source'] = [e.encode('utf-8', 'surrogateescape').decode('utf-8') for e in e['source']]
    with open(path, 'w') as f:
        f.write(json.dumps(j, ensure_ascii=False, indent=2))
