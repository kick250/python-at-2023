from check_cpf_service import CheckCpfService
from exceptions import InvalidCPFException


def test_when_cpf_is_valid():
  service = CheckCpfService()
  valid_cpfs = [
    '246.310.030-30',
    '818.474.830-20',
    '087.965.780-41',
    '733.796.530-39',
    '318.973.430-51',
    '946.395.900-91',
    '211.383.610-62',
    '383.802.740-08',
    '407.949.420-32',
    '861.694.250-59',
  ]

  for cpf in valid_cpfs:
    result = service.validate(cpf)
    assert result == True

def test_when_cpf_is_invalid():
  service = CheckCpfService()
  invalid_cpfs = [
    '123.456.789-10',
    '456.789.123-54',
    '789.456.123-65',
    '424.675.789-99',
    '654.789.123-43',
    '143.842.789-22',
    '654.456.984-55',
    '221.673.789-43',
  ]

  for cpf in invalid_cpfs:
    try:
      service.validate(cpf)
      assert False
    except InvalidCPFException as e:
      assert True
      assert str(e) == "CPF invalido."
    except:
      assert False



def test_when_cpf_has_same_numbers():
  service = CheckCpfService()
  invalid_cpfs = [
    '111.111.111-11',
    '222.222.222-22',
    '333.333.333-33',
    '444.444.444-44',
    '555.555.555-55',
    '666.666.666-66',
    '777.777.777-77',
    '888.888.888-88',
    '999.999.999-99',
  ]

  for cpf in invalid_cpfs:
    try:
      service.validate(cpf)
      assert False
    except InvalidCPFException as e:
      assert True
      assert str(e) == "CPF invalido."
    except:
      assert False

def test_when_cpf_format_invalid():
  service = CheckCpfService()
  invalid_cpfs = [
    '2222222',
    '11111111111',
    '333333333',
    '44444444444',
    '55555555555',
    '666.666.6',
    '7-7777777',
    '88888888888',
    '99999999999',
  ]

  for cpf in invalid_cpfs:
    try:
      service.validate(cpf)
      assert False
    except InvalidCPFException as e:
      assert True
      assert str(e) == "Formato do CPF invalido."
    except:
      assert False

def test_when_cpf_is_from_rejected_region():
  service = CheckCpfService()
  invalid_cpfs = [
    '097.275.817-81',
    '972.300.637-52',
    '638.022.857-86',
    '635.777.307-73',
    '996.536.028-61',
    '509.022.588-50',
    '580.419.016-46',
    '074.622.066-92',
    '507.406.267-52',
    '121.089.397-50',
  ]

  for cpf in invalid_cpfs:
    try:
      service.validate(cpf)
      assert False
    except InvalidCPFException as e:
      assert True
      assert str(e) == "Região de CPF não aceita."
    except:
      assert False
