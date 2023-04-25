import csv
import json
import subprocess
import os
#from jinja2 import Template

csv_file_path = 'snyk_output.csv'

# Read the CSV data
with open(csv_file_path, 'r') as csv_file:
	csv_reader = csv.DictReader(csv_file)
	data = [row for row in csv_reader]
	script_directory = os.path.dirname(os.path.abspath(__file__))
	print("Script directory:", script_directory)
	result = subprocess.run(["pwd"], capture_output=True, text=True)
	# Print the output
	print(result.stdout.strip())
	result = subprocess.run(["ls"], capture_output=True, text=True)

	# Print the output
	print(result.stdout.strip())
	for entry in data:
		if entry["github_url"] != "":
			print(entry["github_url"])
			print()
			command = ['rm', '-rf', script_directory + "/clonearea/test/"]
			subprocess.run(command, check=True)

			target_directory = script_directory + "/clonearea/test/"
			subprocess.run(['git', 'clone', '--depth', '1', entry["github_url"], target_directory], check=True)

			subprocess.run(['bandit', '-r', (script_directory + "/clonearea/test/."), '--format', 'html', '--output', (script_directory + "/htmloutput/" + entry["project_name"] + ".html")], check=False)
			#break