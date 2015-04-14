from lxml.etree import HTML
import requests
import re

SITE_URL = "http://www.math.uiuc.edu/~schenck/M241S15_files/M241S15.html"
SITE_PATH = ".//b"
EXAM_RE = re.compile(r'(?P<Name>\w* \w* \d+): \w+, (?P<Date>\w+ \d+)')

def extract_data(text):
	return [{
		"name": matched.group("Name"),
		"date": matched.group("Date")
		} for matched in EXAM_RE.finditer(text)]

def get_exam_date():
	res = requests.get(SITE_URL)
	page = HTML(res.text)
	exam = " ".join(map(lambda e: " ".join(e.itertext()), page.findall(SITE_PATH)))
	print extract_data(exam)

get_exam_date()
