class AllPeoples():
  __peoples = []

  @classmethod
  def build(cls):
    return AllPeoples();

  def create(self, people):
    self.__peoples.append(people)

  def create_collection(self, peoples):
    for people in peoples:
      self.create(people)

  def get_all(self):
    return self.__peoples