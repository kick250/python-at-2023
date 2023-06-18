from datetime import datetime


def input_name(message = "Digite o nome: "):
  name = None
  while name == None or len(name) <= 0:
    name = input(message).strip()

    if len(name) <= 0:
      print("Nome nao pode ser vazio")

  return name

def input_number(message = "Digite um numero: ", allow_none = False):
  value_parsed = None
  while value_parsed == None:
    try:
      value = input(message).strip()

      if allow_none and len(value) == 0:
        return None

      value_parsed = int(value)
    except ValueError:
      print("valor invalido digitado.")
      next
  return value_parsed

def input_date(message = "Digite a data: ", date_format = "%d/%m/%Y"):
  date = None
  while date == None:
    try:
      value = input(message).strip()
      date = datetime.strptime(value, date_format)
    except ValueError:
      print("valor invalido digitado.")
      next
  return date

def input_cpf(message = "Digite a data: "):
  cpf = None
  while cpf == None:
    try:
      value = input(message).strip()

      if len(value) != 11:
        print("tamanho do cpf invalido.")
        continue

      cpf = int(value)
    except ValueError:
      print("valor invalido digitado.")
      next
  return str(cpf)

def people_summary_view(people):
  SEPARATOR = "\n"
  result = []

  result.append(f"Id: {people.id}")
  result.append(f"Nome: {people.name}")
  result.append(f"Cpf: {people.get_formatted_cpf()}")
  result.append(f"Data de nascimento: {people.get_formatted_birthdate()}")

  return SEPARATOR.join(result)

def peoples_summary_view(peoples): # criando visualizacao de pessoas cadastradas
  SEPARATOR = "\n"
  result = []

  if len(peoples) == 0: # verificando se a lista ta vazia
    result.append(35 * "-")
    result.append("Não existem pessoas cadastradas.")
  else:
    for people in peoples:
      result.append(35 * "-")
      result.append(people_summary_view(people))
  result.append(35 * "-")
  return SEPARATOR.join(result)
