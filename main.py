import employee
import requests
# from urllib.request import urlopen
from requests.exceptions import HTTPError, RequestException, Timeout
from xml.etree.ElementTree import fromstring
#from xml.etree.ElementTree import parse

#var_url = urlopen("https://storage.googleapis.com/psel-2021/soleng&backoffice/Psel2021.xml")
#xmldoc = parse(var_url)
try:
    response = requests.get("https://storage.googleapis.com/psel-2021/soleng&backoffice/Psel2021.xml")
    response.raise_for_status()
except (HTTPError, RequestException, Timeout):
    print("O download do XML falhou, por favor verifique sua conexão à internet e tente executar o programa novamente!")
except Exception as e:
    print("Um erro não previsto ocorreu:", e)
else:
    xmldoc = fromstring(response.content)
    for item in xmldoc.iterfind("employee"):
        name = item.findtext("name")
        cpf = item.findtext("CPF")
        salary = item.findtext("salary")
        position = item.findtext("position")
        marital_status = item.findtext("marital_status")

        new_employee = employee.Employee(name, cpf, salary, position, marital_status)
        print("CPF:", cpf, "| Possíveis estados:", new_employee.possible_states())