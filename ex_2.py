from people import People
from all_peoples import AllPeoples
from helpers import input_number, input_date, input_cpf, input_name, peoples_summary_view


def get_people_from_form(): # formulario paga capturar dados da pessoa
  print("Formulario de pessoa")
  id = input_number(message = "Digite o ID: ", allow_none = True) # pegando id
  name = input_name(message = "Digite o nome: ") # pegando nome
  cpf = input_cpf(message = "Digite o CPF(somente numeros): ") # pegando cpf
  birthdate = input_date(message = "Digite a data de nascimento(ex: 12/12/2012): ") # pegando data

  return People(id, name, cpf, birthdate) # criando pessoa

def create_people(people):
  all_people = AllPeoples.build()
  all_people.create(people)

def show_all_peoples():
  peoples = get_all_peoples()
  print(peoples_summary_view(peoples))

def get_all_peoples():
  all_people = AllPeoples.build()
  return all_people.get_all()

def main():
  people = get_people_from_form() # montando pessoa com dados do form
  create_people(people) # criando ela no repositorio
  show_all_peoples()

if __name__ == "__main__":
  main()