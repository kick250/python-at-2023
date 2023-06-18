import re


class People():
  def __init__(self, id, name, cpf, birthdate):
    self.__id = id
    self.__name = name
    self.__cpf = cpf
    self.__birthdate = birthdate

  @property
  def id(self):
    return self.__id

  @property
  def name(self):
    return self.__name

  def get_formatted_cpf(self):
    if self.__cpf == None:
      return "";

    return re.sub("(\d{3})(\d{3})(\d{3})(\d{2})", r'\1.\2.\3-\4', self.__cpf)

  def get_formatted_birthdate(self):
    return self.__birthdate.strftime("%d/%m/%Y")
