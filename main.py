import csv

from utils.evaluation import evaluate

test_date = '1/3/2025'
file_path = 'data/test.csv'


def read_file(file: str) -> list:
    """
    Read csv file and return list of data
    :param file: file path
    :return: list of data
    """
    with open(file, 'r', encoding='utf-8') as f:
        list_data = list(csv.reader(f))
    return list_data


def read_to_dict(file: str) -> list:
    """
    Read csv file and return dictionary of data
    :param file: file path
    :return: dictionary of data
    """
    with open(file, 'r', encoding='utf-8') as f:
        dict_data = csv.DictReader(f)
        list_of_dict = list(dict_data)
    return list_of_dict


if __name__ == '__main__':
    data = read_to_dict(file_path)
    evaluate(data, test_date)
