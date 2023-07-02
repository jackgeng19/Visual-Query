import ijson
import json
import sys
import os


def parse(out_path: str, input_path: str) -> None:
	output_json = {}
	item_json = {}
	keys = []
	number_of_keys = int(input("Enter the number of entries you need: "))

	with open(input_path, "rb") as f:
		i = 0
		for prefix, name, value in ijson.parse(f):
			if name == 'start_map' and len(prefix) == 43:
				keys.append(prefix)
				i = i+1
			if i>=number_of_keys:
				break
	f.close()

	for key in keys:
		with open(input_path, "rb") as start_f:
			item_json['narrations'] = list(ijson.items(start_f, '%s.narrations.item' % key, use_float=True))
		with open(input_path, "rb") as summary_f:
			item_json['summaries'] = list(ijson.items(summary_f, '%s.summaries.item' % key, use_float=True))
		output_json['%s'%key] = item_json
		start_f.close()
		summary_f.close()

	with open(out_path, 'w') as outfile:
		json.dump(output_json, outfile)


def batch_parse(folder):
    "Parse all json files in a folder."
    for file in os.listdir(folder):
        if not file.endswith(".json"):
            continue
        parse(f'mod_{file}', f'{file}')

# def main() -> int:
# 	parse('out.json', 'v2/annotations/all_narrations_redacted.json')
# 	return 0

if __name__ == "__main__":
    """ If the input is a single file, the script calls the parse(). Calls the batch_parse() otherwise."""
    if len(sys.argv) == 1:
        raise Exception("Function Requires a minimum of 1 argument: Fully Qualified Path to Video or Folder")
        exit()
    if ".json" in sys.argv[1]:
        try:
            parse(sys.argv[2],sys.argv[1])
        except:
            parse(f'mod_{sys.argv[1]}', sys.argv[1])
    else:
        if len(sys.argv) == 3:
            # Two folders
            batch_parse(sys.argv[1])
            batch_parse(sys.argv[2])
        elif len(sys.argv) == 2:
            batch_parse(sys.argv[1])
        else:
            raise Exception("Function Requires a minimum of 1 argument: Fully Qualified Path to Video or Folder")
    # sys.exit(main())