from all_peoples import AllPeoples
from datetime import datetime as Datetime
from people import People
from exceptions import PeopleNotFoundException
import ex_4

def test_search_by_id():
  all_peoples = AllPeoples.build()
  people1 = People(1, "Ana Julia", "32811263080", Datetime(2004, 6, 20))
  all_peoples.create(people1)

  found_people = ex_4.get_people_by_id(people1.id)

  assert found_people.__class__ == People
  assert people1.id == found_people.id
  assert people1.name == found_people.name
  assert people1.cpf == found_people.cpf
  assert people1.birthdate == found_people.birthdate


def test_search_by_id_when_not_found():
  all_peoples = AllPeoples.build()
  all_peoples.delete_all()

  try:
    ex_4.get_people_by_id(1010)
    assert False
  except PeopleNotFoundException as e:
    assert True
    assert str(e) == "Pessoa não encontrada."


def test_update_cpf():
  all_peoples = AllPeoples.build()
  people1 = People(1, "Ana Julia", "32811263080", Datetime(2004, 6, 20))
  all_peoples.create(people1)

  new_cpf = '39429017063'
  ex_4.update_cpf(people1, new_cpf)

  saved_people = all_peoples.get_by_id(people1.id)
  assert saved_people.id == people1.id
  assert saved_people.cpf == new_cpf
  assert saved_people.name == people1.name
  assert saved_people.birthdate == people1.birthdate