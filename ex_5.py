from all_peoples import AllPeoples
from exceptions import PeopleNotFoundException
from helpers import input_number, ask_confirmation


def ask_people_id(message):
  return input_number(message = message)

def get_people_by_id(id):
  all_peoples = AllPeoples.build()
  return all_peoples.get_by_id(id)

def switch_last_names(people1, people2):
  all_peoples = AllPeoples.build()

  people1_last_name = people1.last_name
  people2_last_name = people2.last_name
  people1.update_last_name(people2_last_name)
  people2.update_last_name(people1_last_name)

  all_peoples.update(people1)
  all_peoples.update(people2)


def switch_last_name_flow():
  print("Fazendo troca de nomes: ")
  people1_id = ask_people_id("Digite o id da pessoa 1: ") # capturando id da pessoa 1
  people2_id = ask_people_id("Digite o id da pessoa 2: ") # capturando id da pessoa 2

  try:
    people1 = get_people_by_id(people1_id) # encontrando pessoa 1
    people2 = get_people_by_id(people2_id) # encontrando pessoa 2

    if ask_confirmation():
      switch_last_names(people1, people2) # trocando sobrenomes
      print("Sobrenomes trocados com sucesso.")
  except PeopleNotFoundException as e: # tratando exception de nao encontrado
    print(str(e))

def main():
  switch_last_name_flow()


if __name__ == "__main__":
  main()