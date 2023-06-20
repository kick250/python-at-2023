from all_actions import AllActions
from helpers import input_number
from exceptions import InvalidInputException


def get_options():
  all_actions = AllActions()
  return all_actions.get_all_options()

def get_action_by_id(id):
  all_actions = AllActions()
  return all_actions.get_action_by_id(id)

def ask_for_option(options):
  print("Escolha uma das ações abaixo:")
  for option in options:
    print(f"{option['id']}. {option['action_name']}")
  return input_number(
    message = "Opção: ",
    min = options[0]['id'],
    max = options[-1]['id']
  )

def main():
  while True:
    try:
      options = get_options() # buscando opcoes disponiveis
      action_id = ask_for_option(options) # pergundao opcao para usuario
      action = get_action_by_id(action_id) # pegando acao para executar
      action['action']() # executando acao pedida pelo usuario
    except InvalidInputException as exception: # tratando erro de input invalido
      print(str(exception))

if __name__ == "__main__":
  main()