import json
import sys

def groupby(out_path: str, input_path: str) -> None:
    grouped_data = {}

    with open(input_path, 'r') as file:
        data = json.load(file)

    # project_ids = set()

    # for video_id, video_data in data.items():
    #     narrations = video_data.get('narrations', [])
    #     for narration in narrations:
    #         project_id = narration.get('_project_id')
    #         if project_id:
    #             project_ids.add(project_id)

    # print(list(project_ids))

    for key, value in data.items():
        i = 1
        for item in value['narrations']:
            project_id = item['_project_id']
            # print(item)
            if project_id not in grouped_data:
                grouped_data[project_id] = {}
                grouped_data[project_id][key] = value
                grouped_data[project_id][key]['narrations'] = []



            grouped_data[project_id][key]['narrations'].append(item)

            print(f"{i}, {grouped_data[project_id][key]['narrations']}")

            i += 1
 

    with open(out_path, 'w') as file:
        json.dump(grouped_data, file)


def main() -> int:
    groupby('groupby.json', 'QA_automation/testing.json')
    return 0


if __name__ == '__main__':
    sys.exit(main())