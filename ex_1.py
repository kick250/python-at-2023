from people import People
from datetime import datetime as Datetime

def get_peoples(): # funcao para pegar pessoas
  people1 = People(1, "Ana Julia", "32811263080", Datetime(2004, 6, 20)) # criando pessoa
  people2 = People(2, "Paulo Silva", "55641086045", Datetime(2001, 10, 22)) # criando pessoa
  people3 = People(3, "Juliana Paulino", "44617331069", Datetime(2000, 1, 23)) # criando pessoa
  return [people1, people2, people3]

def peoples_summary_view(peoples): # criando visualizacao de pessoas cadastradas
  SEPARATOR = "\n"
  result = []

  if len(peoples) == 0:
    result.append(35 * "-")
    result.append("Não existem pessoas cadastradas.")
  else:
    for people in peoples:
      result.append(35 * "-")
      result.append(f"Id: {people.id}")
      result.append(f"Nome: {people.name}")
      result.append(f"Cpf: {people.get_formatted_cpf()}")
      result.append(f"Data de nascimento: {people.get_formatted_birthdate()}")
  result.append(35 * "-")

  return SEPARATOR.join(result)

def main():
  peoples = get_peoples()
  print(peoples_summary_view(peoples))

if __name__ == "__main__":
  main()