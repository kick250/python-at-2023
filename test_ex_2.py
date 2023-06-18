from people import People
from all_peoples import AllPeoples
from datetime import datetime as Datetime
import ex_2


def test_create_people():
  all_peoples = AllPeoples.build()
  all_peoples.delete_all()
  people = People(1, "Ana Julia", "32811263080", Datetime(2004, 6, 20))

  ex_2.create_people(people)

  created_people = all_peoples.get_by_id(people.id)
  assert people.id == created_people.id
  assert people.name == created_people.name
  assert people.cpf == created_people.cpf
  assert people.birthdate == created_people.birthdate



def test_create_people_with_existing_id():
  all_peoples = AllPeoples.build()
  all_peoples.delete_all()

  people1 = People(1, "Ana Julia", "32811263080", Datetime(2004, 6, 20))
  people2 = People(1, "Paulo Silva", "55641086045", Datetime(2001, 10, 22))

  ex_2.create_people(people1)
  ex_2.create_people(people2)
  new_id = 2

  created_people = all_peoples.get_by_id(people2.id)
  assert people2.id == created_people.id
  assert people2.name == created_people.name
  assert people2.cpf == created_people.cpf
  assert people2.birthdate == created_people.birthdate

  last_people = all_peoples.last()
  assert new_id == last_people.id
  assert people1.name == last_people.name
  assert people1.cpf == last_people.cpf
  assert people1.birthdate == last_people.birthdate

def test_create_people_with_id_none():
  all_peoples = AllPeoples.build()
  all_peoples.delete_all()
  people = People(None, "Ana Julia", "32811263080", Datetime(2004, 6, 20))

  ex_2.create_people(people)

  created_people = all_peoples.get_by_id(people.id)
  assert 1 == created_people.id
  assert people.name == created_people.name
  assert people.cpf == created_people.cpf
  assert people.birthdate == created_people.birthdate