from flask import Flask, render_template, request, send_file, jsonify
from flask_cors import CORS, cross_origin
import json
import os
import csv
from datetime import date
from datetime import datetime
import pytz
import pandas as pd


id_lst = ['btn_1', 'btn_2', 'btn_3', 'btn_4', 'btn_5', 'btn_6', 'btn_7', 'btn_8', 'btn_9',
          'btn_10', 'btn_11', 'btn_12', 'btn_13', 'btn_14', 'btn_15', 'btn_16', 'btn_17', 'btn_18']
staffs_lst_2 = [
    ['btn_1', 'LÊ PHƯƠNG', '070032', 'TEST REQUEST', 'RD'],
    ['btn_2', 'TRƯƠNG TƯ XUÂN', '080262', 'TEST REQUEST', 'RD'],
    ['btn_3', 'TRƯƠNG THÀNH TAM', '080427', 'B/T', 'RD'],
    ['btn_4', 'LÊ THANH TUẤN', '101339', 'TEST REQUEST', 'RD'],
    ['btn_5', 'PHẠM THỊ PHƯƠNG', '172684', 'TEST REQUEST', 'RD'],
    ['btn_6', 'NGUYỄN HOÀNG VIỆT', '172759', 'TEST REQUEST', 'RD'],
    ['btn_7', 'NGUYỄN THỊ HỒNG YẾN', '172824', 'TEST REQUEST', 'RD'],
    ['btn_8', 'BÙI ĐÌNH HỒNG PHÚC', '193273', 'TEST REQUEST', 'RD'],
    ['btn_9', 'TRƯƠNG VĂN MINH', '203591', 'TEST REQUEST', 'RD'],
    ['btn_10', 'NGUYỄN QUANG QUÍ', '203638', 'TEST REQUEST', 'RD'],
    ['btn_11', 'NGUYỄN THỊ DIỄM MY', '213714', 'TEST REQUEST', 'RD'],
    ['btn_12', 'LÊ MINH THẮNG', '223906', 'TEST REQUEST', 'RD'],
    ['btn_13', 'LÊ QUỐC TRUNG', '224016', 'B/T', 'RD'],
    ['btn_14', 'NGUYỄN TUẤN ANH', '224057', 'TEST REQUEST', 'RD'],
    ['btn_15', 'TRẦN VĂN LƯU', '234102', 'TEST REQUEST', 'RD'],
    ['btn_16', 'LÊ HUỲNH ANH KHOA', '234168', 'B/T', 'RD'],
    ['btn_17', 'NGUYỄN MAI PHƯƠNG', '234170', 'TEST REQUEST', 'RD'],
    ['btn_18', 'PHẠM NG NGỌC TUYẾT', '234172', 'TEST REQUEST', 'RD'],
]


def get_date():
    curr_date = date.today()
    print(curr_date)
    return curr_date


def get_time():
    # Specify the desired time zone
    # Replace with your desired time zone
    desired_timezone = pytz.timezone("Asia/Ho_Chi_Minh")

    # Get the current time in the desired time zone
    curr_time = datetime.now(desired_timezone).strftime("%H:%M")
    print(curr_time)

    return curr_time


def get_name_of_weekday():
    import datetime
    current_date = datetime.datetime.now()
    week_day = current_date.weekday()
    # week_day = 6
    # week_day_name = datetime.datetime.strftime(current_date, '%A')
    return week_day


def read_csv():
    data = []
    # with open('history.csv', 'r', encoding='utf-8') as file:
    #     reader = csv.reader('history.csv')
    #     reader_lst = list(reader)
    #     last_20_lines = reader_lst[-20:]
    # reverse_data = sorted(last_20_lines, reverse=True)

    df = pd.read_csv('history.csv', encoding='utf-8')
    reversed_df = df.iloc[::-1]
    lines_head = reversed_df.head(350)
    data = lines_head.to_dict(orient='records')
    # print(data)
    return data


app = Flask(__name__,static_url_path='/static', static_folder='templates')
CORS(app)


@app.route("/")
def index():
    return render_template("index.html")
    # return "Hello, World!"


@app.route("/viet")
def viet():
    return render_template("viet.html")

@app.route("/thi-phuong")
def viet():
    return render_template("thi-phuong.html")







@app.route("/api/data", methods=['GET'])
# @cross_origin(allow_origin="http://127.0.0.1:5000")
def get_data():
    data = read_csv()
    return jsonify(data)


@app.route("/finished-page")
def finish_page():
    return "Successful check-in(out)!"


@app.route("/download-history")
def download_history():
    filename = "log.xlsx"
    return send_file(filename, as_attachment=True)


@app.route("/download-history-csv")
def download_history_csv():
    filename = "history.csv"
    return send_file(filename, as_attachment=True)


@app.route("/button-click", methods=["POST"])
def button_click():
    return "Chấm tăng ca rồi nha."


@app.route("/button", methods=["POST"])
def handle_button():
    button_id = request.json['buttonId']
    person_name = request.json['content']
    person_date = get_date()
    person_time = get_time()

    def write_staff_data_to_csv():
        index = None
        start_time = None
        for i, staff in enumerate(staffs_lst_2):
            if staff[0] == button_id:
                index = i
                break

        weekday = get_name_of_weekday()
        if weekday == 6:
            start_time = '7:30'
        else:
            start_time = '16:30'

        with open("history.csv", 'a', encoding="utf-8", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([staffs_lst_2[index][1], staffs_lst_2[index][2], start_time,
                            person_time, staffs_lst_2[index][3], staffs_lst_2[index][4], person_date])

        filename = "history.csv"
        df = pd.read_csv(filename, dtype={1: str})
        # print(df)
        # print(type(df))
        df.to_excel("log.xlsx", index=False)

    write_staff_data_to_csv()
    return 'Data written.'


if __name__ == "__main__":
    # app.run(port=5500)
    app.run()
