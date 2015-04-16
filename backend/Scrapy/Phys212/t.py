from lxml.etree import HTML
import requests
import re
import json

ANN_PATH = ".//*[@id=content]/table/tbody/tr"
ANN_URL = "https://courses.physics.illinois.edu/phys212/syllabus.asp"
HW_RE = re.compile(r'(?P<NAME>Tuesday Homework \d due)')
DUMP_NAME = "phys212.json" 

def extract_data(text):
    return [{
            "date": matched.group("NAME")#,
#            "name": matched.group("NAME")
            } for matched in HW_RE.finditer(text)]

def get_formated_announcement():
    res = requests.get(ANN_URL) 
    page = HTML(res.text)
    homeworks = " ".join(map(lambda e: " ".join(e.itertext()), page.findall(ANN_PATH)))
    table = extract_data(homeworks)
    return json.dumps(table) 

if __name__ == "__main__":
    with open(DUMP_NAME, 'w') as out:
        table = get_formated_announcement()
        out.write(table)
    
    
    
    
    
    

