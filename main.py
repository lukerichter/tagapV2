import csv

from utils.evaluation import evaluate
from utils.tables import convert_date_folder

test_date = '3/5/2025'
file_path = 'data/test.csv'
out_file = 'data/evaluated.csv'


def read_file(file: str) -> list:
    """
    Read csv file and return dictionary of data
    :param file: file path
    :return: dictionary of data
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
    with open(out_file, 'w', encoding='utf-8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=content[0].keys())
        writer.writeheader()
        writer.writerows(content)


if __name__ == '__main__':
    data = read_file(file_path)
    evaluated_list = evaluate(data, test_date)
    write_file(out_file, evaluated_list)
