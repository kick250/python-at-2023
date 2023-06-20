from exceptions import PeopleNotFoundException

class AllPeoples():
  __peoples = []

  @classmethod
  def build(cls):
    return AllPeoples()

  def get_all(self):
    return self.__peoples.copy()

  def get_by_id(self, id):
    for people in self.get_all():
      if people.id == id: return people

    raise PeopleNotFoundException()

  def get_by_cpf(self, cpf):
    for people in self.get_all():
      if people.cpf == cpf: return people

  def create(self, people):
    if people.id == None:
      people.id = self.__new_id()

    self.__add_people(people)

  def update(self, people):
    pass

  def delete_by_id(self, id):
    if not self.is_exiting_id(id):
      raise PeopleNotFoundException()

    self.__delete_by_id(id)

  def delete_all(self):
    self.__peoples.clear()

  def is_exiting_id(self, id):
    for people in self.get_all():
      if people.id == id: return True

    return False

  def count(self):
    return len(self.get_all())

  def last(self):
    return self.get_all()[self.count() - 1]

  def __new_id(self):
    return self.count() + 1

  def __add_people(self, people):
    position = self.__get_position_by_id(people.id)

    if position == None:
      position = self.count()

    self.__peoples.insert(position, people)
    self.__organize_peoples()

  def __delete_by_id(self, id):
    position = self.__get_position_by_id(id)

    self.__peoples.pop(position)
    self.__organize_peoples()

  def __organize_peoples(self):
    for i, people in enumerate(self.get_all()):
      people.id = i + 1

  def __get_position_by_id(self, id):
    people_position = None
    for people in self.get_all():
      if people.id != id: continue

      position = people.id - 1 # -1 pq o id 1 ocupa a posicao 0
      people_position = position
      break
    return people_position

