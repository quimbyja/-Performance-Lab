import json
import sys
# python3 test.py values.json tests.json, report.json
"""
Проводил проверку и разработку логики в целом
"""
def load(file):
    with open(file, "r", encoding="utf-8") as js:
        return json.load(js)
    
test_sctructure = load(sys.argv[2])
values_data = load(sys.argv[1])
report = sys.argv[3]

values = {}
for itm in values_data["values"]:
    if "id" in itm and "value" in itm:
        values[itm["id"]] = itm["value"]

# print(values)


def fill(test_structure, values):
    for itm in test_structure:
        id = itm["id"]
        if id is not None and id in values:
            itm["value"] = values[id]

        if "values" in itm and isinstance(itm["values"], list):
            fill(itm["values"], values)


fill(test_sctructure["tests"],values)

with open(report, "w", encoding="utf-8") as f:
    json.dump(test_sctructure, f, ensure_ascii=False, indent=2)