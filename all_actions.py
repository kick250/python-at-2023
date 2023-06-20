from ex_1 import index_flow
from ex_2 import insert_flow
from ex_3 import delete_flow
from ex_4 import update_cpf_flow
from ex_5 import switch_last_name_flow


def program_exit():
  print("Obrigado por usar nosso sistema.")
  print("Tchau!!")
  exit()

class AllActions():
  def get_all_options(self):
    return self.__all_options()

  def get_action_by_id(self, id):
    for action in self.__all_actions():
      if action['id'] == id: return action

  def __all_options(self):
    return [
      { 'id': 1, 'action_name': 'Inserir novo cadastro' },
      { 'id': 2, 'action_name': 'Alterar CPF' },
      { 'id': 3, 'action_name': 'Trocar sobrenomes' },
      { 'id': 4, 'action_name': 'Remover cadastro' },
      { 'id': 5, 'action_name': 'Listar todos os cadastros' },
      { 'id': 6, 'action_name': 'Encerrar' }
    ]

  def __all_actions(self):
    return [
      { 'id': 1, 'action': insert_flow },
      { 'id': 2, 'action': update_cpf_flow },
      { 'id': 3, 'action': switch_last_name_flow },
      { 'id': 4, 'action': delete_flow },
      { 'id': 5, 'action': index_flow },
      { 'id': 6, 'action': program_exit }
    ]