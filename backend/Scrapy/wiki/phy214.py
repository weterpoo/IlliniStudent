from lxml.etree import HTML
import requests
import re
import json

URL = "https://courses.physics.illinois.edu/phys214/sp2015/syllabus.asp"
PATH = ".//table[@summary='Syllabus table for PHYS 214']/tbody"
FILE_NAME = "Phys214Table.json"

def get_clean_text(rows):
	return "\n".join(row.strip() for row in rows.itertext()).strip()

def extract(text):
	return [{
		"date": matched.group(1),
		"name": matched.group(2)
		} for matched in re.compile(r'(\d/\d*/\d*).*(Homework \d)').finditer(text)]

def get_homework_date():
	doc = HTML(requests.get(URL).text)
	table = doc.find(PATH)
	homeworks = []
	for row in table:
		text = get_clean_text(row).replace("\n", "")
		ec = text.encode('utf-8')
		row = extract(ec)
		try:
			if hasattr(row[0], "get"):
				homeworks.append(row)
		except IndexError:
			None
	return json.dumps(homeworks)

if __name__ == "__main__":
	with open(FILE_NAME, 'w') as out:
		table = get_homework_date()
		out.write(table)