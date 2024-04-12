import csv
import pandas as pd

def read_csv():
    data = []
    # with open('history.csv', 'r', encoding='utf-8') as file:
    #     reader = csv.reader('history.csv')
    #     reader_lst = list(reader)
    #     last_20_lines = reader_lst[-20:]
    # reverse_data = sorted(last_20_lines, reverse=True)

    df = pd.read_csv('history.csv', encoding='utf-8')
    reversed_df = df.iloc[::-1]
    data = reversed_df.to_dict(orient='records')
    print(data)
    return data

data = read_csv()
print(type(data))
print(len(data))
