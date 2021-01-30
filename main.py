import employee
from urllib.request import urlopen
from xml.etree.ElementTree import parse

var_url = urlopen("https://storage.googleapis.com/psel-2021/soleng&backoffice/Psel2021.xml")
xmldoc = parse(var_url)

for item in xmldoc.iterfind("employee"):
    name = item.findtext("name")
    cpf = item.findtext("CPF")
    salary = item.findtext("salary")
    position = item.findtext("position")
    marital_status = item.findtext("marital_status")

    new_employee = employee.Employee(name, cpf, salary, position, marital_status)
    print("CPF:", cpf, "| Possíveis estados:", new_employee.possible_states())