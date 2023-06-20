from datetime import date as Date
from exceptions import InvalidInputException, InvalidCPFException
from check_cpf_service import CheckCpfService


def input_name(message = "Digite o nome: "):
  name = None
  while name == None or len(name) <= 0 or len(name.split(" ")) != 2:
    name = input(message).strip()

    if len(name) <= 0:
      __raise_invalid_input("Nome nao pode ser vazio")

    if len(name.split(" ")) != 2:
      __raise_invalid_input("Voce deve preencher o nome e um sobrenome.")

  return str(name).title()

def input_number(message = "Digite um numero: ", allow_none = False, min = None, max = None):
  value_parsed = None
  while value_parsed == None:
    try:
      value = input(message).strip()

      if allow_none and len(value) == 0:
        return None

      if min != None and int(value) < min:
        __raise_invalid_input("O valor deve ser maior que zero.")
        continue

      if max != None and int(value) > max:
        __raise_invalid_input(f"O valor deve ser menor ou igual a {max}.")
        continue

      value_parsed = int(value)
    except ValueError:
      __raise_invalid_input("valor invalido digitado.\nO valor deve ser um numero.")
      continue
  return value_parsed

def input_date(message = "Digite a data: ", allow_future = True):
  date = None
  while date == None:
    try:
      value = input(message).strip()
      date_value = convert_date_from_string(value)

      if not allow_future and date_value > Date.today():
        __raise_invalid_input("Essa data não pode ser do futuro.")

      date = date_value
    except ValueError:
      __raise_invalid_input("valor invalido digitado.")
      continue
  return date

def input_cpf(message = "Digite a data: "):
  cpf = None
  while cpf == None:
    try:
      value = input(message).strip()
      validate_cpf(value)
      cpf = value
    except ValueError:
      __raise_invalid_input("valor invalido digitado.")
      continue
  return str(cpf)

def convert_date_from_string(date_string):
  day, month, year = date_string.split('/') # ex: 12/12/2000
  return Date(int(year), int(month), int(day))

def validate_cpf(cpf):
  try:
    service = CheckCpfService()
    service.validate(cpf)
    return True
  except InvalidCPFException as exception:
    __raise_invalid_input(str(exception))

def __raise_invalid_input(message):
  raise InvalidInputException(message)

def ask_confirmation():
  while True:
    response = input("Tem certeza que deseja realizar esta ação?(sim/não) ").strip().lower()
    if response == "sim": return True
    elif response == "não": return False
    else: print("Reposta inválida.")

