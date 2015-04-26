import requests
from lxml.etree import HTML
import json

SITE_URL = "https://courses.physics.illinois.edu/phys212/syllabus.asp"
TABLE_PATH = './/table[@summary="Syllabus table for PHYS 212"]/tbody'
DATE_INDEX = 0
HW_INDEX = 5
FILE_NAME = "Phys212Table.json"

def get_clean_text(rows):
	return "\n".join(row.strip() for row in rows.itertext()).strip()

def get_homework_date():
	req = requests.get(SITE_URL)
	page = HTML(req.text)
	table = page.find(TABLE_PATH)
	homeworks = []
	for row in table:
		if len(row) < 5:
			continue
		date = get_clean_text(row[DATE_INDEX])
		name = get_clean_text(row[HW_INDEX])
		if "due" not in name:
			continue
		if "Tuesday" in date:
			date = date.replace("Tuesday", "").lstrip()
		homework = { 'date': date,'name': name }
		homeworks.append(homework)
	return json.dumps(homeworks)

if __name__ == "__main__":
	with open(FILE_NAME, 'w') as out:
		table = get_homework_date()
		out.write(table)
