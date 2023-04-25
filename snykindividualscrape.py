import requests
from bs4 import BeautifulSoup

url = "https://snyk.io/advisor/python/opencensus-ext-azure"

def scrape_project_info(url):
	response = requests.get(url)
	if response.status_code != 200:
		print(f"Failed to get data from the website. Status code: {response.status_code}")
		return
	
	soup = BeautifulSoup(response.content, "html.parser")
	t_aa = soup.find(class_="intro")
	new_soup = BeautifulSoup(str(t_aa), "html.parser")
	h1 = new_soup.find("h1").text


	version_container = new_soup.find("div", {"class": "name"})
	version = version_container.find("span").text
	container = new_soup.find("div", {"class": "container"})

	for aaa in new_soup.findAll("span"):
		if "License" in aaa.text	:
			_license = aaa.text


	links = container.findAll("a")
	github_url = ""
	pypi_url = ""
	
	for link in links:
		if "pypi.org" in link["href"]:
			pypi_url = link["href"]
		if "github.com" in link["href"]:
			github_url = link["href"]

	project_info = {
		"project_name": h1,
		"version": version,
		"license": _license,
		"pypi_url": pypi_url,
		"github_url": github_url,
		"snyk_url": url
	}
	
	return project_info

"""
if __name__ == "__main__":
	project_info = scrape_project_info(url)
	if project_info:
		print(project_info)
"""