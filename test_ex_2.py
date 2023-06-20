from people import People
from all_peoples import AllPeoples
from datetime import date as Date
import ex_2


def test_create_people():
  all_peoples = AllPeoples.build()
  all_peoples.delete_all()
  people = People(1, "Ana Julia", "32811263080", Date(2004, 6, 20))

  ex_2.create_people(people)

  created_people = all_peoples.get_by_id(people.id)
  assert people.id == created_people.id
  assert people.name == created_people.name
  assert people.cpf == created_people.cpf
  assert people.birthdate == created_people.birthdate



def test_create_people_with_existing_id():
  all_peoples = AllPeoples.build()
  all_peoples.delete_all()

  people1 = People(1, "Ana Julia", "32811263080", Date(2004, 6, 20))
  people2 = People(2, "Gustavo Silva", "55641086045", Date(2001, 10, 22))
  people_with_existing_id = People(1, "Paulo Silva", "99330737021", Date(2001, 10, 22))

  ex_2.create_people(people1)
  ex_2.create_people(people2)
  ex_2.create_people(people_with_existing_id)

  created_people = all_peoples.get_by_cpf(people_with_existing_id.cpf)
  assert 1 == created_people.id
  assert people_with_existing_id.name == created_people.name
  assert people_with_existing_id.cpf == created_people.cpf
  assert people_with_existing_id.birthdate == created_people.birthdate

  saved_people_1 = all_peoples.get_by_cpf(people1.cpf)
  assert 2 == saved_people_1.id
  assert people1.name == saved_people_1.name
  assert people1.cpf == saved_people_1.cpf
  assert people1.birthdate == saved_people_1.birthdate

  saved_people_2 = all_peoples.get_by_cpf(people2.cpf)
  assert 3 == saved_people_2.id
  assert people2.name == saved_people_2.name
  assert people2.cpf == saved_people_2.cpf
  assert people2.birthdate == saved_people_2.birthdate

def test_create_people_with_id_none():
  all_peoples = AllPeoples.build()
  all_peoples.delete_all()
  people = People(None, "Ana Julia", "32811263080", Date(2004, 6, 20))

  ex_2.create_people(people)

  created_people = all_peoples.get_by_id(people.id)
  assert 1 == created_people.id
  assert people.name == created_people.name
  assert people.cpf == created_people.cpf
  assert people.birthdate == created_people.birthdate