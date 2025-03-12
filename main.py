import csv

from utils.evaluation import evaluate
from utils.file_io import read_file, write_file

test_date = '3/5/2025'
file_path = 'data/test.csv'
out_file = 'data/evaluated.csv'


if __name__ == '__main__':
    data = read_file(file_path)
    evaluated_list = evaluate(data, test_date)
    write_file(out_file, evaluated_list)
