from datetime import datetime
from dateutil.relativedelta import relativedelta

from utils.constants import *
from utils.tables import lookup_table


def evaluate(data: list, test_date: str):
    """
    Evaluate all person data
    :param data: list of persons
    :param test_date: date of the test
    :return: list of evaluated persons
    """
    evaluated_list = []
    for person in data:
        age = calculate_age(person[BIRTH_DATE], test_date)
        gender = parse_gender(person[GENDER])
        table = find_table(age, gender)
        print(f'\n{person[NAME]} Age: {age}, Gender: {gender}')

        # Calculate the score of each category for the person

        best_agility = find_best_and_convert(True, person, AGILITY)
        score_agility = calculate_agility(best_agility, table)
        print(f'- Agility: {person[AGILITY]} -> {score_agility}')

        best_throw = find_best_and_convert(True, person, THROWING1, THROWING2, THROWING3)
        score_throw = calculate_throwing(best_throw, table)
        print(f'- Throwing: {best_throw} -> {score_throw}')

        best_jump = find_best_and_convert(True, person, JUMPING1, JUMPING2)
        score_jump = calculate_jumping(best_jump, table)
        print(f'- Jumping: {best_jump} -> {score_jump}')

        best_sprint = find_best_and_convert(False, person, SPRINTING1, SPRINTING2)
        score_sprint = calculate_sprinting(best_sprint, table)
        print(f'- Sprinting: {best_sprint} -> {score_sprint}')

        best_coordination = find_best_and_convert(False, person, COORDINATION)
        score_coordination = calculate_coordination(best_coordination, table)
        print(f'- Coordination: {best_coordination} -> {score_coordination}')

        best_endurance = find_best_and_convert(True, person, ENDURANCE)
        score_endurance = calculate_endurance(best_endurance, table)
        print(f'- Endurance: {best_endurance} -> {score_endurance}')

        # Convert all values to the correct format, because Excel can't handle the german format
        best_agility_str = str(best_agility).replace('.', ',')
        best_throw_str = str(best_throw).replace('.', ',')
        best_jump_str = str(best_jump).replace('.', ',')
        best_sprint_str = str(best_sprint).replace('.', ',')
        best_coordination_str = str(best_coordination).replace('.', ',')
        best_endurance_str = str(best_endurance).replace('.', ',')
        sum_str = (str(score_agility + score_throw + score_jump + score_sprint + score_coordination + score_endurance)
                   .replace('.', ','))
        age_str = str(age).replace('.', ',')

        # Build a new dict for the evaluated person and append to the list
        evaluated_list.append({
            OUT_NAME: person[NAME],
            OUT_SCHOOL: person[SCHOOL],
            OUT_GENDER: gender,
            OUT_AGE: age_str,
            OUT_HEIGHT: person[HEIGHT],
            OUT_AGILITY: best_agility_str,
            OUT_AGILITY_POINTS: score_agility,
            OUT_THROWING: best_throw_str,
            OUT_THROWING_POINTS: score_throw,
            OUT_JUMPING: best_jump_str,
            OUT_JUMPING_POINTS: score_jump,
            OUT_SPRINTING: best_sprint_str,
            OUT_SPRINTING_POINTS: score_sprint,
            OUT_COORDINATION: best_coordination_str,
            OUT_COORDINATION_POINTS: score_coordination,
            OUT_ENDURANCE: best_endurance_str,
            OUT_ENDURANCE_POINTS: score_endurance,
            OUT_SUM: sum_str
        })

    return evaluated_list


def find_best_and_convert(high_is_best: bool, person: dict, *values: str) -> float:
    """
    Find the best value from the given values and convert it to float
    :param high_is_best: flag if high values are better
    :param person: person dictionary
    :param values: values to compare
    :return: best value as float
    """
    value_list = [float(person[value].replace(',', '.')) for value in values]
    best_value = max(value_list) if high_is_best else min(value_list)

    return best_value


def calculate_agility(value: float, table: dict) -> int:
    """
    Calculate the score for the agility test
    :param value: value of the test
    :param table: table for the test
    :return: score for the test
    """
    lookup_list = table["Agility"]
    score = 0
    for i in range(30):
        if value > lookup_list[i]:
            score += 1

    return score


def calculate_throwing(value: float, table: dict) -> int:
    """
    Calculate the score for the throw test
    :param value: value of the test
    :param table: table for the test
    :return: score for the test
    """
    lookup_list = table["Throwing"]
    score = 0
    for i in range(30):
        if value > lookup_list[i]:
            score += 1

    return score


def calculate_jumping(value: float, table: dict) -> int:
    """
    Calculate the score for the jump test
    :param value: value of the test
    :param table: table for the test
    :return: score for the test
    """
    lookup_list = table["Jumping"]
    score = 0
    for i in range(30):
        if value > lookup_list[i]:
            score += 1

    return score


def calculate_sprinting(value: float, table: dict) -> int:
    """
    Calculate the score for the sprint test
    :param value: value of the test
    :param table: table for the test
    :return: score for the test
    """
    lookup_list = table["Sprinting"]
    score = 0
    for i in range(30):
        if value < lookup_list[i]:
            score += 1

    return score


def calculate_coordination(value: float, table: dict) -> int:
    """
    Calculate the score for the coordination test
    :param value: value of the test
    :param table: table for the test
    :return: score for the test
    """
    lookup_list = table["Coordination"]
    score = 0
    for i in range(30):
        if value < lookup_list[i]:
            score += 1

    return score


def calculate_endurance(value: float, table: dict) -> int:
    """
    Calculate the score for the endurance test
    :param value: value of the test
    :param table: table for the test
    :return: score for the test
    """
    lookup_list = table["Endurance"]
    score = 0
    for i in range(30):
        if value > lookup_list[i]:
            score += 1

    return score


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
        return MALE
    if gender_str in GENDER_FEMALE_LIST:
        return FEMALE


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
