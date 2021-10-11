import sys
import json

nb = sys.stdin.read()

json_in = json.loads(nb)

def strip_output_from_cell(cell):
    if "outputs" in cell:
        cell["outputs"] = []
    if "execution_count" in cell:
        cell["execution_count"] = None

for cell in json_in["cells"]:
    strip_output_from_cell(cell)

json.dump(json_in, sys.stdout, sort_keys=True, indent=1, separators=(",",": "))
