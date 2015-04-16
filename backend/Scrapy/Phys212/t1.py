import requests
from lxml.etree import HTML

doc = HTML(requests.get('https://courses.physics.illinois.edu/phys212/syllabus.asp').text)

def get_text(el):
    return "\n".join(t.strip() for t in el.itertext()).strip()

table = doc.find('.//table[@summary="Syllabus table for PHYS 212"]/tbody')

date_index = 0
homework_index = 5

homeworks = []
for row in table:
    if len(row) < 5:
        continue
    date = get_text(row[date_index])
    name = get_text(row[homework_index])
    if name == '':
        continue
    hwk = {
        'date': date,
        'name': name 
    }
    homeworks.append(hwk)


for h in homeworks:
    print "DATE!!!!!!!!!", h['date']
    print "\t\t\t", h['name']
        

