from people import People
from all_peoples import AllPeoples
from helpers import input_number, input_date, input_cpf, input_name, ask_confirmation


def get_people_from_form(): # formulario paga capturar dados da pessoa
  print("Formulario de pessoa")
  id = input_number(message = "Digite o ID: ", allow_none = True, min = 1) # pegando id
  name = input_name(message = "Digite o nome: ") # pegando nome
  cpf = input_cpf(message = "Digite o CPF(somente numeros): ") # pegando cpf
  birthdate = input_date(message = "Digite a data de nascimento(ex: 12/12/2012): ", allow_future = False) # pegando data

  return People(id, name, cpf, birthdate) # criando pessoa

def create_people(people):
  all_people = AllPeoples.build()
  all_people.create(people)

def insert_flow():
  people = get_people_from_form() # montando pessoa com dados do form
  if ask_confirmation(): # pedindo confirmacao
    create_people(people) # criando ela no repositorio
    print("Pessoa criada com sucesso.")

def main():
  insert_flow()

if __name__ == "__main__":
  main()