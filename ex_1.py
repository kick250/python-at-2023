from datetime import datetime as Datetime
from all_peoples import AllPeoples
from people import People
import helpers


def get_peoples(): # funcao para pegar pessoas
  all_peoples = AllPeoples.build() # montando repositorio de pessoas

  # adicionando exemplo de pessoas no repositorio
  all_peoples.create_collection([
    People(1, "Ana Julia", "32811263080", Datetime(2004, 6, 20)), # criando pessoa
    People(2, "Paulo Silva", "55641086045", Datetime(2001, 10, 22)), # criando pessoa
    People(3, "Juliana Paulino", "44617331069", Datetime(2000, 1, 23)) # criando pessoa
  ])

  return all_peoples.get_all() # pegando as pessoas do repositorio

def peoples_summary_view(peoples): # criando visualizacao de pessoas cadastradas
  return helpers.peoples_summary_view(peoples)

def main():
  peoples = get_peoples() # pegando pesssoas
  print(peoples_summary_view(peoples)) # exibindo pessoas

if __name__ == "__main__":
  main()