from operator import attrgetter
from people import People
from datetime import datetime as Datetime

class AllPeoples():
  __peoples = [
    People(1, "Ana Julia", "32811263080", Datetime(2004, 6, 20)), # criando pessoa
    People(2, "Paulo Silva", "55641086045", Datetime(2001, 10, 22)), # criando pessoa
    People(3, "Juliana Paulino", "44617331069", Datetime(2000, 1, 23)) # criando pessoa
  ]

  @classmethod
  def build(cls):
    return AllPeoples();

  @classmethod
  def delete_all(cls):
    cls.__peoples = []

  def create(self, people):
    existing_people = None
    if people.id == None:
      people.id = self.__new_id()
    elif self.existing_id(people.id):
      existing_people = self.get_by_id(people.id)
      existing_people.id = self.__new_id()

    self.__peoples.append(people)
    self.__order_peoples()

  def create_collection(self, peoples):
    for people in peoples:
      self.create(people)

  def get_all(self):
    return self.__peoples

  def get_by_id(self, id):
    for people in self.get_all():
      if people.id == id: return people

  def count(self):
    return len(self.get_all())

  def last(self):
    return self.get_all()[self.count() - 1]

  def existing_id(self, id):
    for people in self.get_all():
      if people.id == id: return True

    return False

  def __new_id(self):
    return self.count() + 1

  def __order_peoples(self):
    self.__peoples.sort(key = attrgetter('id'))
