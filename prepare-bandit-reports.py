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
	subprocess.run("pwd")
	subprocess.run("ls")
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