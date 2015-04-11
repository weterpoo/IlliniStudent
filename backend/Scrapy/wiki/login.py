import requests
from lxml.etree import HTML

LOGIN_URL = "https://wiki.cites.illinois.edu/Shibboleth.sso/Login"
LOGIN_POST_URL = "https://shibboleth.illinois.edu/idp/Authn/UserPassword"

def login_wiki(init_url, netid, password):
    '''
    automate logging in WIKI 
    :param init_url: password-protected url you want to go to
    :param netid: netid
    :param password: password
    '''
    credentials = {"j_username": netid, "j_password": password}
    s = requests.Session()
    requests.packages.urllib3.disable_warnings()
    s.get(init_url, verify=False)
    s.get(LOGIN_URL)
    relay = HTML(s.post(LOGIN_POST_URL, data=credentials).text)
    form = relay.find(".//form[@method='post']")
    final_url = form.attrib['action']
    relay_state = form.find(".//input[@name='RelayState']").attrib['value']
    saml_response = form.find(".//input[@name='SAMLResponse']").attrib['value']
    s.post(final_url, data={'RelayState': relay_state,
                    'SAMLResponse': saml_response})
    return s


# example usage
URL = "https://wiki.cites.illinois.edu/wiki/pages/viewpage.action?title=Home&spaceKey=cs125" 
NETID = "" # put your netid here
PASSWORD = "" # put your password here
session = login_wiki(URL, NETID, PASSWORD)
print session.get(URL).text



