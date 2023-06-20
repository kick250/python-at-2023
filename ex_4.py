from exceptions import PeopleNotFoundException
from all_peoples import AllPeoples
from helpers import input_number, input_cpf, ask_confirmation


def ask_people_id():
  return input_number(message = "Digite o id da pessoa que deseja atualizar o CPF: ")

def get_people_by_id(id):
  all_peoples = AllPeoples.build()
  return all_peoples.get_by_id(id)

def ask_for_new_cpf(people):
  print(f"O cpf do {people.name} atual é: {people.get_formatted_cpf()}")
  return input_cpf(message = "Qual sera o novo cpf(somente numeros): ")

def update_cpf(people, new_cpf):
  all_peoples = AllPeoples.build()

  people.cpf = new_cpf
  all_peoples.update(people)

def update_cpf_flow():
  people_id = ask_people_id() # capturando id

  try:
    people = get_people_by_id(people_id) # encontrando pessoa
    cpf = ask_for_new_cpf(people) # capturando novo cpf

    if ask_confirmation():
      update_cpf(people, cpf) # atualizando cpf
      print("Pessoa atualizada com sucesso.")
  except PeopleNotFoundException as e: # tratando exception de nao encontrado
    print(str(e))

def main():
  update_cpf_flow()

if __name__ == "__main__":
  main()