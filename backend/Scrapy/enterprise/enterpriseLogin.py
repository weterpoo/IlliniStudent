import requests
from lxml.etree import HTML

URL = 'https://webprod.admin.uillinois.edu/ssa/servlet/SelfServiceLogin?appName=edu.uillinois.aits.SelfServiceLogin&dad=BANPROD1'
LOGIN_URL = 'https://eas.admin.uillinois.edu/eas/servlet/%s'

NETID = ""
PASSWORD = ""

s = requests.Session()
requests.packages.urllib3.disable_warnings()
credentials = {
        "inputEnterpriseId": NETID,
        "password": PASSWORD, 
        "queryString": "null",
        "BTN_LOGIN": "Login",
        "pwc": "",
        "RESET_SQ_P": "Reset Your Password",
        "usq": "",
        "principalInput": "",
        "ContinueButton": 'Continue'
}
headers = {'User-Agent': 'Safari'}
attempt = s.get(URL)
login_id = HTML(attempt.text).find('.//form[@name="easForm"]').attrib['action']
res = s.post(LOGIN_URL% login_id, data=credentials, headers=headers)
with open('x.html', 'w') as dump:
        dump.write(res.text)
#relay = HTML(s.post(LOGIN_URL, data=credentials).text)


