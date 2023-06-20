import re
from exceptions import InvalidCPFException


CPF_REGEX_PATTERN = "(\d{3}).(\d{3}).(\d{3})-(\d{2})"
REJECTED_CPF_REGIONS = ["6", "7", "8"]

class CheckCpfService():
  def validate(self, cpf):
    if self.__is_invalid_format(cpf): self.__raise_invalid_by_format()

    self.__cpf = cpf
    self.__first_digit = cpf[-2]
    self.__second_digit = cpf[-1]
    self.__cpf_numbers = self.__get_cpf_numbers()
    self.__region_code = cpf[-4]

    if not self.__is_valid_cpf(): self.__raise_invalid_cpf()
    if self.__is_rejected_region(): self.__raise_invalid_by_rejected_region()
    return True

  def __is_invalid_format(self, cpf):
    match = re.match(CPF_REGEX_PATTERN, cpf)

    if match == None: return True

    return match.group() != cpf

  def __is_valid_cpf(self):
    if self.__is_all_numbers_equal(): return False

    first_digit_ok = self.__check_first_digit()
    second_digit_ok = self.__check_second_digit()

    return first_digit_ok and second_digit_ok

  def __is_rejected_region(self):
    return REJECTED_CPF_REGIONS.count(self.__region_code) > 0

  def __is_all_numbers_equal(self):
    uniq_values = set(self.__cpf_numbers)
    return len(uniq_values) == 1

  def __check_first_digit(self):
    first_nine_digits = self.__cpf_numbers[0:9]

    amount = 0
    for index, range_index in enumerate(range(10, 1, -1)):
      amount += range_index * int(first_nine_digits[index])

    result = (amount * 10) % 11
    if result == 10: result = 0

    return str(result) == self.__first_digit

  def __check_second_digit(self):
    first_nine_digits = self.__cpf_numbers[0:9] + self.__first_digit

    amount = 0
    for index, range_index in enumerate(range(11, 1, -1)):
      amount += range_index * int(first_nine_digits[index])

    result = (amount * 10) % 11
    if result == 10: result = 0

    return str(result) == self.__second_digit

  def __get_cpf_numbers(self):
    numbers = ""
    for char in self.__cpf:
      try:
        numbers += str(int(char))
      except ValueError:
        continue
    return numbers

  def __raise_invalid_by_format(self):
    raise InvalidCPFException("Formato do CPF invalido.")

  def __raise_invalid_cpf(self):
    raise InvalidCPFException("CPF invalido.")

  def __raise_invalid_by_rejected_region(self):
    raise InvalidCPFException("Região de CPF não aceita.")
