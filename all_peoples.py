from operator import attrgetter
from people import People
from datetime import datetime as Datetime

class AllPeoples():
  __peoples = []

  @classmethod
  def build(cls):
    return AllPeoples();

  @classmethod
  def delete_all(cls):
    cls.__peoples = []

  def create(self, people):
    if people.id == None:
      people.id = self.__new_id()

    self.__add_people(people)

  def create_collection(self, peoples):
    for people in peoples:
      self.create(people)

  def get_all(self):
    return self.__peoples

  def get_by_id(self, id):
    for people in self.get_all():
      if people.id == id: return people

  def get_by_cpf(self, cpf):
    for people in self.get_all():
      if people.cpf == cpf: return people

  def count(self):
    return len(self.get_all())

  def last(self):
    return self.get_all()[self.count() - 1]

  def __new_id(self):
    return self.count() + 1

  def __add_people(self, people):
    self.__peoples.append(people)
    self.__organize_peoples()

  def __organize_peoples(self):
    self.__peoples.reverse() # manter o id do mais recente
    self.__peoples.sort(key = attrgetter('id'))

    ids = []
    for people in self.get_all():
      if people.id in ids:
        people.id += 1
      ids.append(people.id)