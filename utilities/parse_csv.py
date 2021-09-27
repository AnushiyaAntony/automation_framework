import os
from pandas import read_csv


file_path = os.path.join(os.getcwd(), "testdata", "booking_data.csv")


def get_test_data():
    df = read_csv(file_path)
    test_data = []
    for index, row in df.iterrows():
        test_data.append(tuple(row))
    return test_data
