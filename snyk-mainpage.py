import requests
from bs4 import BeautifulSoup
from snykindividualscrape import *
import csv
import argparse

def scrape_basicsr_data(url):
	response = requests.get(url)
	
	if response.status_code != 200:
		print(f"Failed to get data from the website. Status code: {response.status_code}")
		return
	
	soup = BeautifulSoup(response.content, "html.parser")
	elements = soup.find_all(text=text_filter)
	#print(len(elements))
	for element in elements:
		aa = (element.parent.parent)
		new_soup = BeautifulSoup(str(aa), "html.parser")
		a_tags = new_soup.find_all('a')
		output = []
		for i in a_tags:
			if "/advisor/python" in i.get('href') and "/advisor/packages/python" not in i.get('href'):
				output.append("https://snyk.io" + i.get('href'))
		return output
	# Find table rows
	#rows = soup.find_all("ul")
	#print(len(rows))
	#print(rows[5].text)
	#elements_by_custom_attr = soup.find_all(attrs={"data-v-a476bd7c data-v-091084b9": ""})
	#print(len(elements_by_custom_attr))

def text_filter(text):
    return "Python Packages Index" in text


#url = "https://snyk.io/advisor/packages/python/popularity/influential-project"
"""
	{
	"type": "key-ecosystem-project",
	"url": "https://snyk.io/advisor/packages/python/popularity/key-ecosystem-project?page=",
	"start": 1,
	"len": 2
	},
	{
	"type": "influential-project",
	"url": "https://snyk.io/advisor/packages/python/popularity/influential-project?page=",
	"start": 5,
	"len": 6
	},
	{
	"type": "recognized",
	"start": 32,
	"url": "https://snyk.io/advisor/packages/python/popularity/recognized?page=",
	"len": 32
	},
"""
_list = [
	{
	"type": "limited",
	"start": 324,
	"url": "https://snyk.io/advisor/packages/python/popularity/limited?page=",
	"len": 1381
	}
	]
"""
_list = [
	{
	"type": "recognized",
	"start": 1,
	"url": "https://snyk.io/advisor/packages/python/popularity/influential-project?page=",
	"len": 1
	}
	]
"""

def main():
	with open("snyk_output.csv", "a+", newline='') as csvfile:
		count = 0
		for _type in _list:
			for it in range(_type["start"], _type["len"] + 1):
				url = _type["url"] + str(it)
				basicsr_data = scrape_basicsr_data(url)
				for iterator, url in enumerate(basicsr_data):
					aa = scrape_project_info(url)
					print(aa)
					print("aaafa")
					if aa != None:
						aa['type'] = _type["type"]
						if count == 0:
							header = aa.keys()
							writer = csv.DictWriter(csvfile, fieldnames=header)
							writer.writeheader() 
							count = count + 1
						else:
							print(aa)
							print(_type["type"] + " " + str(it) + " iterator: " + str(iterator))
							print()
							writer.writerow(aa)
							csvfile.flush()

if __name__ == '__main__':
	main()
