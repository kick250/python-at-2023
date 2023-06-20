from all_peoples import AllPeoples


def people_summary_view(people): # criando visualizacao uma pessoa
  SEPARATOR = "\n"
  result = []

  result.append(f"Id: {people.id}")
  result.append(f"Nome: {people.name}")
  result.append(f"Cpf: {people.get_formatted_cpf()}")
  result.append(f"Data de nascimento: {people.get_formatted_birthdate()}")
  result.append(f"Dias desde o nascimento: {people.get_days_since_of_birthdate()}")

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

def get_peoples(): # funcao para pegar pessoas
  all_peoples = AllPeoples.build() # montando repositorio de pessoas
  return all_peoples.get_all() # pegando as pessoas do repositorio

def index_flow():
  peoples = get_peoples() # pegando pesssoas
  print(peoples_summary_view(peoples)) # exibindo pessoas

def main():
  index_flow()

if __name__ == "__main__":
  main()