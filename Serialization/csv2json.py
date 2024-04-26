import csv
import json
from pathlib import Path


def csv2json(from_file: Path, to_file: Path) -> None:
    json_list = []
    with open(from_file, 'r', newline='', encoding='utf-8') as f:
        csv_write = csv.reader(f, dialect='excel-tab')
        for i, line in enumerate(csv_write):
            json_dict = {}
            if i == 0:
                continue
            else:
                level, id, name = line
                json_dict['level'] = int(level)
                json_dict['id'] = f"{int(id):010}"
                json_dict['name'] = name.title()
                json_dict['hash'] = hash(f"{json_dict['name']}{json_dict['id']}")
                json_list.append(json_dict)

    with open(to_file, 'w', encoding='utf-8') as f:
        json.dump(json_list, f, indent=2)



