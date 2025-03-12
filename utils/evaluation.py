from datetime import datetime
from dateutil.relativedelta import relativedelta

from utils.constants import *
from utils.tables import lookup_table


def evaluate(data: list, test_date: str):
    """
    Evaluate all person data
    :param data: list of persons
    :param test_date: date of the test
    """
    for person in data:
        age = calculate_age(person[BIRTH_DATE], test_date)
        gender = parse_gender(person[GENDER])
        table = find_table(age, gender)
        print(f'{person[NAME]} ({age}): {table}')


def calculate_age(birthdate_str: str, test_date_str: str) -> int:
    """
    Calculate age of the person based on the birthdate and the test date in
    the format 'mm/dd/yyyy' or 'dd.mm.yyyy'
    :param birthdate_str: birthdate of the person
    :param test_date_str: date of the test
    :return: age of the person rounded to the nearest half year
    """
    time_format = '%m/%d/%Y' if '/' in birthdate_str else '%d.%m.%Y'
    birthdate = datetime.strptime(birthdate_str, time_format)
    test_date = datetime.strptime(test_date_str, time_format)

    # Calculate age in years with decimal places for months and days
    delta = relativedelta(test_date, birthdate)
    age_in_years = delta.years + delta.months / 12 + delta.days / 365.25

    # Round age to the nearest half year
    rounded_age = int(age_in_years)
    rounded_age += 0.5 if age_in_years - rounded_age >= 0.5 else 0

    return rounded_age


def parse_gender(gender_str: str) -> str:
    """
    Parse the gender from the string to a standardized format
    :param gender_str: gender string
    :return: standardized gender string
    """
    gender_str = gender_str.strip().lower()
    if gender_str in GENDER_MALE_LIST:
        return 'm'
    if gender_str in GENDER_FEMALE_LIST:
        return 'w'


def find_table(age: int, gender: str):
    """
    Find the table based on
    :param age: age of the person
    :param gender: gender of the person
    :return: table name
    """
    # Parse age to the nearest available table
    parsed_age = 7 if age < 7 else (10 if age > 10 else age)
    table = lookup_table[gender][parsed_age]

    return table
