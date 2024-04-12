# from flask import Flask, jsonify
import pandas as pd


# def read_csv():
# 	data = []
# 	df = pd.read_csv('history.csv', encoding='utf-8')
# 	df_list = list(df)
# 	sorted_data = sorted(df_list, reverse=True)
# 	data = df.to_dict(orient='records')
# 	return sorted_data

# def get_data():
#      data = read_csv()
#      return jsonify(data)

# csv = read_csv()
# # data = get_data()
# print(csv)
# # print(data)

import pandas as pd

# Create a sample DataFrame
data = {'Name': ['Alice', 'Bob', 'Charlie', 'David'],
        'Age': [25, 30, 35, 40],
        'City': ['New York', 'London', 'Paris', 'Tokyo']}
df = pd.DataFrame(data)

# Reverse the DataFrame
reversed_df = df.iloc[::-1]

# Print the reversed DataFrame
print(reversed_df)