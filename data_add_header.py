# 공백 제거
# 감정 분류 헤더 추가
# 내용 헤더 추가 

import csv

input_file = "test_successed.csv"
output_file = "test_add_header.csv"

# 감정, 내용 헤더 추가
with open(input_file, 'r', encoding='utf-8', newline='') as csv_in_file:
    with open(output_file, 'w', encoding='utf-8', newline='') as csv_out_file:
        freader = csv.reader(csv_in_file)
        fwriter = csv.writer(csv_out_file)
        header_list = ['내용', '감정']
        fwriter.writerow(header_list)

        print(header_list)

        for row in freader:
            fwriter.writerow (row)
            print(row)
