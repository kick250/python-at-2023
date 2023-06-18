from datetime import datetime as Datetime
from all_peoples import AllPeoples
from people import People
import helpers


def get_peoples(): # funcao para pegar pessoas
  all_peoples = AllPeoples.build() # montando repositorio de pessoas
  return all_peoples.get_all() # pegando as pessoas do repositorio

def peoples_summary_view(peoples): # criando visualizacao de pessoas cadastradas
  return helpers.peoples_summary_view(peoples)

def index_flow():
  peoples = get_peoples() # pegando pesssoas
  print(peoples_summary_view(peoples)) # exibindo pessoas

def main():
  index_flow()

if __name__ == "__main__":
  main()