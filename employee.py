import re

# Otherwise valid CPF exceptions
def _exceptions(cpf):
        if len(cpf)!=11:
            return True
        else:
            s="".join(str(x) for x in cpf)
            if (
                s=="00000000000"
                or s=="11111111111"
                or s=="22222222222"
                or s=="33333333333"
                or s=="44444444444"
                or s=="55555555555"
                or s=="66666666666"
                or s=="77777777777"
                or s=="88888888888"
                or s=="99999999999"):
                return True
        return False

class Employee(object):
    # Translates 123.456.789-10 to 12345678910
    @staticmethod
    def _translate(cpf):
        return "".join(re.findall("\\d", cpf))

    # Generates CPF's last digit
    @staticmethod
    def _gen(cpf):
        res = []
        for i, a in enumerate(cpf):
            b = len(cpf) + 1 - i
            res.append(b * a)

        res = sum(res) % 11

        if res > 1:
            return 11 - res
        else:
            return 0

    def __init__(self, name, cpf, salary, position, marital_status):
        self.name = name
        self.salary = float(salary)
        self.position = position
        self.marital_status = marital_status
        # Saves unparsed CPF
        self.cpf_str = cpf

        # Parses CPF
        if isinstance(cpf, str):
            if not cpf.isdigit():
               cpf = self._translate(cpf)
        self.cpf = [int(x) for x in cpf]

    def is_cpf_valid(self):
        if _exceptions(self.cpf):
            return False

        s = self.cpf[:9]
        s.append(self._gen(s))
        s.append(self._gen(s))
        return s == self.cpf[:]

    def possible_states(self):
        if self.is_cpf_valid():
            eighth_digit = self.cpf[8]
            state_dict = {
                0: ["RS"],
                1: ["DF", "GO", "MT", "MS", "TO"],
                2: ["AC", "AM", "AP", "PA", "RO", "RR"],
                3: ["CE", "MA", "PI"],
                4: ["AL", "PB", "PE", "RN"],
                5: ["BA", "SE"],
                6: ["MG"],
                7: ["ES", "RJ"],
                8: ["SP"],
                9: ["PR", "SC"]
            }
            return state_dict.get(eighth_digit)
        # Invalid CPF
        return []
