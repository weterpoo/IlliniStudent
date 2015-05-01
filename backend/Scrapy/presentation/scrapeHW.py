import sys
import requests
import json
import re
from lxml.etree import HTML

M_PATH = ".//dl[@class='week']/dd"
M_URL = "http://www.math.uiuc.edu/~schenck/M241S15_files/schedule2.html#current"
M_RE = re.compile(r'(?P<NAME>HW \d+\w*) \([Dd]ue (?P<DUE_DATE>\d+/\d+)\)')
PHYS212_PATH = ".//table[@summary='Syllabus table for PHYS 212']/tbody"
PHYS212_URL = "https://courses.physics.illinois.edu/phys212/syllabus.asp"       
PHYS214_PATH = ".//table[@summary='Syllabus table for PHYS 214']/tbody"
PHYS214_URL = "https://courses.physics.illinois.edu/phys214/sp2015/syllabus.asp"

def get_clean_text(texts):
    return "\n".join(text.strip() for text in texts.itertext()).strip()

def extract_table(texts):
    return [{
            "date": matched.group("DUE_DATE"),
            "name": matched.group("NAME")
            } for matched in M_RE.finditer(texts)]

def get_math_table():
    req = requests.get(URL)
    page = HTML(req.text)
    homeworks = " ".join(map(lambda e: " ".join(e.itertext()), page.findall(M_PATH)))
    table = extract_table(homeworks)
    return json.dumps(table)

def get_physics_212_table():
    req = requests.get(URL)
    page = HTML(req.text)
    table = page.find(PHYS212_PATH)
    homeworks = []
    for row in table:
            if len(row) < 5:
                    continue
            date = get_clean_text(row[0])
            name = get_clean_text(row[5])
            if "due" not in name:
                    continue
            if "Tuesday" in date:
                    date = date.replace("Tuesday", "").lstrip()
            homework = {"date": date, "name": name}
            homeworks.append(homework)
    return json.dumps(homeworks)

def get_physics_214_table():
    req = requests.get(URL)
    page = HTML(req.text)
    table = page.find(PHYS214_PATH)
    homeworks = []
    for row in table:
            text = get_clean_text(row).replace("\n", "")
            encoded = text.encode('utf-8')
            homework = extract_table(encoded)
            try:
                if hasattr(row[0], "get"):
                        homeworks.append(homework)
            except IndexError:
                None
    return json.dumps(homeworks)

if __name__ == "__main__":
       if len(sys.argv) != 3:
               sys.exit(1)
       NAME = sys.argv[1]
       URL = sys.argv[2]
       with open(NAME, 'w') as out:
           if URL == M_URL:
               table = get_math_table()
           elif URL == PHYS212_URL:
               table = get_physics_212_table()
           elif URL == PHYS214_URL:
               table = get_physics_214_table()
           out.write(table)
