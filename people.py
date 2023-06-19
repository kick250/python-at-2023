import re


class People():
  def __init__(self, id, name, cpf, birthdate):
    self.id = id
    self.name = name
    self.cpf = cpf
    self.birthdate = birthdate

  def get_formatted_cpf(self):
    if self.cpf == None:
      return ""

    return re.sub("(\d{3})(\d{3})(\d{3})(\d{2})", r'\1.\2.\3-\4', self.cpf)

  def get_formatted_birthdate(self):
    return self.birthdate.strftime("%d/%m/%Y")