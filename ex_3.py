from exceptions import PeopleNotFoundException
from all_peoples import AllPeoples
from helpers import input_number, ask_confirmation


def ask_people_id():
  return input_number(message = "Digite o id da pessoa que deseja apagar: ")

def delete_people_by_id(id):
  all_peoples = AllPeoples.build()
  all_peoples.delete_by_id(id)

def check_existing_people(id):
  all_peoples = AllPeoples.build()
  exist = all_peoples.is_exiting_id(id)

  if not exist: raise PeopleNotFoundException()
  return True

def delete_flow():
  people_id = ask_people_id() # capturando id da pessoa
  try:
    check_existing_people(people_id) # verificando se a pessoa existe
    if ask_confirmation():
      delete_people_by_id(people_id) # deletando ela do repositorio
      print(f"Pessoa de id {people_id} apagada.")
  except PeopleNotFoundException as exception: # tratando erro de pessoa nao encontrada
    print(str(exception))

def main():
  delete_flow()

if __name__ == "__main__":
  main()