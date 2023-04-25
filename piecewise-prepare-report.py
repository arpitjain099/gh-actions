import csv
import json
import subprocess
import os
import argparse
#from jinja2 import Template

def main(start, end):
	print(f'Argument 1: {start}')
	start = int(start)

	csv_file_path = 'clean_csv.csv'

	# Read the CSV data
	with open(csv_file_path, 'r') as csv_file:
		csv_reader = csv.DictReader(csv_file)
		data = [row for row in csv_reader]
		script_directory = os.path.dirname(os.path.abspath(__file__))
		print("Script directory:", script_directory)
		for iterator, entry in enumerate(data):
			if entry["github_url"] != "" and iterator >= start and iterator <= start + 99:
				file_path = (script_directory + "/htmloutput/" +  entry["project_name"] + ".html")
				print(entry["github_url"])
				print("Iterator: " + str(iterator))
				print()
				command = ['rm', '-rf', script_directory + "/clonearea/test/"]
				subprocess.run(command, check=True)

				target_directory = script_directory + "/clonearea/test/"
				subprocess.run(['git', 'clone', '--depth', '1', entry["github_url"], target_directory], check=True)

				subprocess.run(['bandit', '-r', (script_directory + "/clonearea/test/."), '--format', 'html', '--output', (script_directory + "/htmloutput/" + entry["project_name"] + ".html")], check=False)
				#break

if __name__ == '__main__':
	parser = argparse.ArgumentParser(description='Give start arguments')
	parser.add_argument('--start', type=str, required=True, help='start')
	args = parser.parse_args()
	main(args.arg1, args.arg2)