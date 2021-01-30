import employee
import json
import operator
import requests
from requests.exceptions import HTTPError, RequestException, Timeout
from xml.etree.ElementTree import fromstring

if __name__ == "__main__":
    # Resposta 4 (v. linha 76)
    resposta_4 = []
    try:
        response = requests.get("https://storage.googleapis.com/psel-2021/soleng&backoffice/Psel2021.xml")
        response.raise_for_status()
    except (HTTPError, RequestException, Timeout):
        print("O download do XML falhou, por favor verifique sua conexão à internet e tente executar o programa novamente!")
    except Exception as e:
        print("Um erro não previsto ocorreu:", e)
    else:
        xmldoc = fromstring(response.content)
        employees = []
        for item in xmldoc.iterfind("employee"):
            name = item.findtext("name")
            cpf = item.findtext("CPF")
            salary = item.findtext("salary")
            position = item.findtext("position")
            marital_status = item.findtext("marital_status")
            new_employee = employee.Employee(name, cpf, salary, position, marital_status)

            # Resposta 4 (v. linha 76)
            if position != "COORDENADOR" and marital_status != "CASADO":
                resposta_4.append({
                    "valid_cpf": new_employee.is_cpf_valid(),
                    "name": name,
                    "CPF": cpf,
                    "possibles_origin": new_employee.possible_states()
                })

            employees.append(new_employee)

    # 1. Funcionários ordenados por salário (decrescente)
    resposta_1_instances = sorted(employees, key=operator.attrgetter("salary"), reverse=True)
    resposta_1 = []
    for e in resposta_1_instances:
        resposta_1.append({
            "name": e.name,
            "CPF": e.cpf_str,
            "salary": int(e.salary),
            "position": e.position,
            "marital_status": e.marital_status,
        })

    # 2. Quantidade de funcionários em cada cargo (ordem alfabética)
    resposta_2 = {
        "analista": sum(e.position == "ANALISTA" for e in employees),
        "coordenador": sum(e.position == "COORDENADOR" for e in employees),
        "diretor": sum(e.position == "DIRETOR" for e in employees),
        "gerente": sum(e.position == "GERENTE" for e in employees)
    }

    # 3. Cinco Coordenadores casados com menor salário (crescente)
    resposta_3 = []
    counter = 5
    for e in reversed(resposta_1_instances):
        if counter == 0: break
        if e.position == "COORDENADOR" and e.marital_status == "CASADO":
            resposta_3.append({
                "name": e.name,
                "CPF": e.cpf_str,
                "salary": int(e.salary),
                "position": e.position,
                "marital_status": e.marital_status,
            })
            counter -= 1

    # 4. Validação de CPF e possíveis estados de origem de cada funcionário
    # Observação: a variável resposta_4 foi preenchida durante a iteração do XML

    # 5. Custo total para a empresa dos funcionários que estão no cargo de Analista
    resposta_5 = 0.0
    for e in employees:
        if e.position == "ANALISTA":
            resposta_5 += 1.95 * float(e.salary)
    resposta_5 = round(resposta_5, 2)

    # Compilar respostas
    resposta_dict = {
        "api_key": "",
        "full_name": "Pedro Henrique Siqueira de Oliveira",
        "email": "pedro.oliveira@raccoon.ag",
        "code_link": "https://gitlab.com/pedro-oli/BackOffice_SolEng",
        "response_1": resposta_1,
        "response_2": resposta_2,
        "response_3": resposta_3,
        "response_4": resposta_4,
        "response_5": resposta_5,
    }

    #resposta_json = json.dumps(resposta_dict, indent=2) # talvez seja esse o certo, e o debaixo é só pra imprimir no console # !!APAGAR ISSO DEPOIS!!
    resposta_json = json.dumps(resposta_dict, indent=2, ensure_ascii=False).encode('utf8')
    print(resposta_json.decode())