from all_peoples import AllPeoples
from datetime import date as Date
from people import People
from exceptions import PeopleNotFoundException
import ex_5

def test_search_by_id():
  all_peoples = AllPeoples.build()
  people1 = People(1, "Ana Julia", "32811263080", Date(2004, 6, 20))
  all_peoples.create(people1)

  found_people = ex_5.get_people_by_id(people1.id)

  assert found_people.__class__ == People
  assert people1.id == found_people.id
  assert people1.name == found_people.name
  assert people1.cpf == found_people.cpf
  assert people1.birthdate == found_people.birthdate


def test_search_by_id_when_not_found():
  all_peoples = AllPeoples.build()
  all_peoples.delete_all()

  try:
    ex_5.get_people_by_id(1010)
    assert False
  except PeopleNotFoundException as e:
    assert True
    assert str(e) == "Pessoa não encontrada."


def test_switch_last_names():
  all_peoples = AllPeoples.build()

  people1 = People(1, "Paulo Silva", "55641086045", Date(2001, 10, 22))
  all_peoples.create(people1)
  people2 = People(2, "Juliana Paulino", "44617331069", Date(2000, 1, 23))
  all_peoples.create(people2)

  ex_5.switch_last_names(people1, people2)

  saved_people1 = all_peoples.get_by_id(people1.id)
  saved_people2 = all_peoples.get_by_id(people2.id)

  assert saved_people1.name == "Paulo Paulino"
  assert saved_people2.name == "Juliana Silva"