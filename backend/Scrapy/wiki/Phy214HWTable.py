import requests
from lxml.etree import HTML

URL = "https://courses.physics.illinois.edu/phys214/sp2015/syllabus.asp"
TABLE_PATH = ".//table[@summary='Syllabus table for PHYS 214']/tbody"

def get_clean_text(rows):
	return "\n".join(row.strip() for row in rows.itertext()).strip()

homeworks = []

req = requests.get(URL)
page = HTML(req.text)
table = page.find(TABLE_PATH)
for i in table:
	if "Homework" in get_clean_text(i):
		date = get_clean_text(i[0])
		name = ""
		if "Homework" in get_clean_text(i[4]):
			name = get_clean_text(i[4])
		if "Homework" in get_clean_text(i[3]):
			name = get_clean_text(i[3])
		if len(i) > 6:
			date = get_clean_text(i[1])
			name = get_clean_text(i[6])
		if "Homework " not in name:
			continue
		#date = date.replace("\n", "")
		#name = name.replace("\n", "")
		homework = { 'date': date, 'name': name }
		homeworks.append(homework)

print homeworks
