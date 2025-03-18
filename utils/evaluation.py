from datetime import datetime
from dateutil.relativedelta import relativedelta

from utils.constants import *
from utils.tables import find_table


def evaluate(data: list, test_date: datetime) -> list:
    """
    Evaluate all person data. This method does only work if the data is correct.
    Use the method ``test_and_prepare_table()`` to prepare the data first.
    :param data: list of persons
    :param test_date: date of the test
    :return: list of evaluated persons
    """
    evaluated_list = []

    for person in data:
        age = calc_age(person[BIRTH_DATE], test_date)
        table = find_table(age, person[GENDER])

        # Calculate the score of each category for the person
        best_agility = find_best_and_convert(True, person, AGILITY)
        score_agility = calc_category_score(best_agility, table["Agility"], ">")

        best_throw = find_best_and_convert(True, person, THROWING)
        score_throw = calc_category_score(best_throw, table["Throwing"], ">")

        best_jump = find_best_and_convert(True, person, JUMPING)
        score_jump = calc_category_score(best_jump, table["Jumping"], ">")

        best_sprint = find_best_and_convert(False, person, SPRINTING)
        score_sprint = calc_category_score(best_sprint, table["Sprinting"], "<")

        best_coordination = find_best_and_convert(False, person, COORDINATION)
        score_coordination = calc_category_score(best_coordination, table["Coordination"], "<")

        best_endurance = find_best_and_convert(True, person, ENDURANCE)
        score_endurance = calc_category_score(best_endurance, table["Endurance"], ">")

        # Print the results for the person (for debugging)
        print(f'{person[NAME]} {' ' * (20 - len(person[NAME]))}'
              f'-> Agility: {score_agility}, Throwing: {score_throw}, Jumping: {score_jump}, '
              f'Sprinting: {score_sprint}, Coordination: {score_coordination}, Endurance: {score_endurance}, '
              f'Total: {score_agility + score_throw + score_jump + score_sprint + score_coordination + score_endurance}')

        # Build a new dict for the evaluated person and append to the list
        # Convert all values to the correct format, because Excel can't handle the german format
        total = score_agility + score_throw + score_jump + score_sprint + score_coordination + score_endurance
        evaluated_list.append({
            OUT_NAME: person[NAME],
            OUT_SCHOOL: person[SCHOOL],
            OUT_GENDER: person[GENDER],
            OUT_AGE: convert_format(age),
            OUT_HEIGHT: person[HEIGHT],
            OUT_AGILITY: convert_format(best_agility),
            OUT_AGILITY_POINTS: score_agility,
            OUT_THROWING: convert_format(best_throw),
            OUT_THROWING_POINTS: score_throw,
            OUT_JUMPING: convert_format(best_jump),
            OUT_JUMPING_POINTS: score_jump,
            OUT_SPRINTING: convert_format(best_sprint),
            OUT_SPRINTING_POINTS: score_sprint,
            OUT_COORDINATION: convert_format(best_coordination),
            OUT_COORDINATION_POINTS: score_coordination,
            OUT_ENDURANCE: convert_format(best_endurance),
            OUT_ENDURANCE_POINTS: score_endurance,
            OUT_SUM: convert_format(total)
        })

    return evaluated_list


def calc_category_score(val: float, lookup_list: list, op: str) -> int:
    """
    Calculate the score for a category based on the lookup list and an operator (either '<' or '>')
    :param val: value to compare
    :param lookup_list: point list for the category
    :param op: operator to compare the values ('<' or '>')
    :return: score for the category
    """
    return sum(1 for x in lookup_list if (op == "<" and val < x) or (op == ">" and val > x))


def convert_format(value: float) -> str:
    """
    Convert the format of the value from english to german
    :param value: value to convert
    :return: converted value
    """
    if value == float('-inf') or value == float('inf'):
        return INVALID

    return str(value).replace('.', ',')


def find_best_and_convert(high_is_best: bool, person: dict, keys: list) -> float:
    """
    Find the best value from the given values and convert it to float
    :param high_is_best: flag if high values are better
    :param person: person dictionary
    :param keys: keys of values in the person dictionary to compare to
    :return: best value
    """
    value_list = []
    for key in keys:
        if person[key] == INVALID:
            value_list.append(float('-inf') if high_is_best else float('inf'))
        else:
            value_list.append(person[key])

    return max(value_list) if high_is_best else min(value_list)


def calc_age(birthdate_str: str, test_date: datetime) -> int:
    """
    Calculate age of the person based on the birthdate and the test date in
    the format 'mm/dd/yyyy' or 'dd.mm.yyyy'
    :param birthdate_str: birthdate of the person
    :param test_date: date of the test
    :return: age of the person rounded to the nearest half year
    """
    time_format = '%m/%d/%Y' if '/' in birthdate_str else '%d.%m.%Y'
    birthdate = datetime.strptime(birthdate_str, time_format)

    # Calculate age in years with decimal places for months and days
    delta = relativedelta(test_date, birthdate)
    age_in_years = delta.years + delta.months / 12 + delta.days / 365.25

    # Round age to the nearest half year
    rounded_age = int(age_in_years)
    rounded_age += 0.5 if age_in_years - rounded_age >= 0.5 else 0

    return rounded_age
