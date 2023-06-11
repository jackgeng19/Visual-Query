import ijson
import json
import sys


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

def main() -> int:
	parse('out.json', 'v2/annotations/all_narrations_redacted.json')
	return 0

if __name__ == '__main__':
    sys.exit(main())