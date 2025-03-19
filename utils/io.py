import csv

from utils.constants import KEYS


def read_file(file: str) -> list:
    """
    Read csv file and return dictionary of data
    :param file: file path
    :return: list of dictionaries with the data
    """
    with open(file, 'r', encoding='utf-8', newline='') as f:
        dict_data = csv.DictReader(f)
        list_of_dict = list(dict_data)
    return list_of_dict


def write_file(file: str, content: list):
    """
    Write evaluated data to a new csv file
    :param file: Location of the new file
    :param content: List of evaluated data
    """
    keys = content[0].keys()
    with open(file, 'w', encoding='utf-8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=keys)
        writer.writeheader()
        writer.writerows(content)


def create_pattern_table(file: str):
    """
    Create a pattern table for the user to download
    :return:
    """
    with open(file, 'w', encoding='utf-8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=KEYS)
        writer.writeheader()
