from flask import Flask, jsonify
import pandas as pd


def read_csv():
	data = []
	df = pd.read_csv('history.csv', encoding='utf-8')
	data = df.to_dict(orient='records')
	return data

def get_data():
     data = read_csv()
     return jsonify(data)

csv = read_csv()
# data = get_data()
print(csv)
# print(data)