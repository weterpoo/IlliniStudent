from lxml.etree import HTML
import requests
import re
import json

ANN_PATH = ".//dl[@class='week']/dd"
ANN_URL = "http://www.math.uiuc.edu/~schenck/M241S15_files/schedule2.html#current"
HW_RE = re.compile(r'(?P<NAME>HW \d+\w*) \([Dd]ue (?P<DUE_DATE>\d+/\d+)\)')
DUMP_NAME = "tom.json" 

def extract_data(text):
    return [{
            "date": matched.group("DUE_DATE"),
            "name": matched.group("NAME")
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
    
    
    
    
    
    

