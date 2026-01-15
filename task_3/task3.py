import sys
# python3 task3 values.json tests.json report.json
import json

"""
оформил в духе ООП, это больше для себя
"""


class ReadJSON:
    def __init__(self):
        self.values_file = sys.argv[1]
        self.tests_file = sys.argv[2]
        self.report_file = sys.argv[3]


    def json_to_py(self, data):
        with open(data, 'r', encoding="utf-8") as file:
            return json.load(file)
        
    def fill_values(self, structure, values):
        for itm in structure:
            itm_id = itm["id"]
            if itm_id is not None and itm_id in values:
                itm["value"] = values[itm_id]

            if "values" in itm and isinstance(itm["values"], list):
                self.fill_values(itm["values"], values)

    def run(self):
        values_data = self.json_to_py(self.values_file)
        values = {}
        for itm in values_data["values"]:
            if "id" in itm and "value" in itm:
                values[itm["id"]] = itm["value"]
        
        structure = self.json_to_py(self.tests_file)
        self.fill_values(structure["tests"], values)

        with open(self.report_file, "w", encoding="utf-8") as report:
            json.dump(structure, report, ensure_ascii=False, indent=2)

if __name__ == "__main__":
    read = ReadJSON()
    read.run()



    