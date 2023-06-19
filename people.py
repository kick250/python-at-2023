import re
from datetime import datetime as Datetime


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

  def update_last_name(self, new_last_name):
    self.name = " ".join([self.first_name, new_last_name])

  def get_days_since_of_birthdate(self):
    delta = Datetime.today() - self.birthdate
    return delta.days

  @property
  def first_name(self):
    if self.name == None: return ""

    return self.name.split(" ")[0]

  @property
  def last_name(self):
    if self.name == None: return ""

    return self.name.split(" ")[-1]
