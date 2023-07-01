import json
import sys

def groupby(out_path: str, input_path: str) -> None:
    grouped_data = {}

    with open(input_path, 'r') as file:
        data = json.load(file)

    for key, value in data.items():
        project_id = value['narrations'][0]['_project_id']
        if project_id not in grouped_data:
            grouped_data[project_id] = {}
        grouped_data[project_id][key] = value

    with open(out_path, 'w') as outfile:
        json.dump(grouped_data, outfile)


def main() -> int:
    groupby('groupby.json', 'QA_automation/out.json')
    print("Grouped by project_id")
    return 0


if __name__ == '__main__':
    sys.exit(main())