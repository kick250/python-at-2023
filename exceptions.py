class PeopleNotFoundException(Exception):
  def __init__(self, message = "Pessoa não encontrada."):
    super().__init__(message)