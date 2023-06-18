from all_peoples import AllPeoples
from datetime import datetime as Datetime
from people import People
from exceptions import PeopleNotFoundException
import ex_3


def test_delete_people():
  all_peoples = AllPeoples.build()
  people1 = People(1, "Ana Julia", "32811263080", Datetime(2004, 6, 20))
  people2 = People(2, "Paulo Silva", "55641086045", Datetime(2001, 10, 22))
  people3 = People(3, "Juliana Paulino", "44617331069", Datetime(2000, 1, 23))
  all_peoples.create(people1)
  all_peoples.create(people2)
  all_peoples.create(people3)

  ex_3.delete_people_by_id(people2.id)

  saved_people1 = all_peoples.get_by_cpf(people1.cpf)
  assert saved_people1.id == 1

  saved_people3 = all_peoples.get_by_cpf(people3.cpf)
  assert saved_people3.id == 2



def test_delete_not_existing_people():
  all_peoples = AllPeoples.build()
  all_peoples.delete_all()

  try:
    ex_3.delete_people_by_id(1010)
    assert False
  except PeopleNotFoundException as e:
    assert True
    assert str(e) == "Pessoa não encontrada."