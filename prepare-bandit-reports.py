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

	for entry in data:
		if entry["github_url"] != "":
			file_path = (script_directory + "/htmloutput/" +  entry["project_name"] + ".html")
			if os.path.exists(file_path) and os.path.isfile(file_path):
				print("html file already exists")
				print()
				continue
			else:
				print(entry["github_url"])
				print()
				command = ['rm', '-rf', script_directory + "/clonearea/test/"]
				subprocess.run(command, check=True)

				target_directory = script_directory + "/clonearea/test/"
				subprocess.run(['git', 'clone', '--depth', '1', entry["github_url"], target_directory], check=True)

				subprocess.run(['bandit', '-r', (script_directory + "/clonearea/test/."), '--format', 'html', '--output', (script_directory + "/htmloutput/" + entry["project_name"] + ".html")], check=False)
				#break
				"""

				# semgrep --config=p/security-audit /Users/arpitjain/Downloads/security-advisory/clonearea/test/. --json > semgrep_results.json

				subprocess.run(
					[f"semgrep --config=p/security-audit " + (script_directory + "/clonearea/test/.") + " --json > semgrep_results.json"],
					 # Capture the output instead of printing it to the console
					check=False,  # Raise an exception if the command fails
					text=True,  # Convert the output to a string instead of bytes
				)

				#print(result.stdout)
				#subprocess.run(['bandit', '-r', (script_directory + "/clonearea/test/."), '--format', 'html', '--output', (script_directory + "/htmloutput/" + entry["project_name"] + ".html")], check=False)

				with open("semgrep_results.json") as json_file:
					semgrep_results = json.load(json_file)
				semgrep_results = json.loads(result.stdout)
				print(semgrep_results)
				print("aaa]\n")
				for finding in semgrep_results["results"]:
					print(finding)
					
				# Extract the findings
				findings = [
					{
						"rule_id": finding["check_id"],
						"severity": finding["extra"]["severity"],
						"file": finding["path"],
						"line": finding["start"]["line"],
						"message": finding["extra"]["message"],
					}
					for finding in semgrep_results["results"]
				]

				# Read the HTML template
				with open("semgrep_template.html") as template_file:
					template_content = template_file.read()

				# Render the HTML report
				template = Template(template_content)
				html_report = template.render(findings=findings)

				# Save the HTML report
				with open((script_directory + "/semgrephtmloutput/" + entry["project_name"] + ".html"), "w") as html_file:
					html_file.write(html_report)
				"""