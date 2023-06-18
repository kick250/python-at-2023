from datetime import datetime as Datetime
import ex_1
from people import People

def test_get_peoples():
  peoples = ex_1.get_peoples()

  for people in peoples:
    assert people.__class__ == People

def test_peoples_summary_view():
  people1 = People(1, "Ana Julia", "32811263080", Datetime(2004, 6, 20))
  people2 = People(2, "Paulo Silva", "55641086045", Datetime(2001, 10, 22))
  peoples = [people1, people2]

  expected_view = "\n".join([
    35 * '-',
    'Id: 1', 'Nome: Ana Julia',
    'Cpf: 328.112.630-80',
    'Data de nascimento: 20/06/2004',
    35 * '-',
    'Id: 2', 'Nome: Paulo Silva',
    'Cpf: 556.410.860-45',
    'Data de nascimento: 22/10/2001',
    35 * '-'
  ])

  view = ex_1.peoples_summary_view(peoples)
  assert view == expected_view

def test_peoples_summary_view_when_empty():
  peoples = []

  expected_view = "\n".join([
    35 * '-',
    'Não existem pessoas cadastradas.',
    35 * '-']
  )

  view = ex_1.peoples_summary_view(peoples)
  assert view == expected_view


def test_main():
  try:
    ex_1.main()
    assert True
  except:
    assert False