import helpers

def test_convert_date_from_string():
  date_string = "15/12/2023"
  date = helpers.convert_date_from_string(date_string)
  assert date.day == 15
  assert date.month == 12
  assert date.year == 2023

def test_convert_date_from_string_when_invalid():
  date_string = "29/02/2023"

  try:
    helpers.convert_date_from_string(date_string)
    assert False
  except ValueError:
    assert True
  except:
    assert False
