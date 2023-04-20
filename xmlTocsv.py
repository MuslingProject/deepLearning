# xml(sjml)를 csv 파일로 변환
import os
import xml.etree.ElementTree as ET
from bs4 import BeautifulSoup as bf

# 기본 작업
target_dir = r"C:\DATA"
file_list = os.listdir(target_dir)
xml_list = []

for file in file_list:
  if ".sjml" in file:
    xml_list.append(file)


# 모든 xml 파일 불러오기
for xml_file in xml_list:
  target_path = target_dir + "\\" + xml_file
  target_xml = open(target_path, "rt", encoding="utf-8")
  
  # 데이터 파싱 (중요 내용만 저장)
  tree = bf(target_xml, features="xml")

  # 데이터 저장
  datas = tree.find_all('p')

#!/bin/env/ python
#-*- coding:utf-8 -*-
  for d in datas:
    # null일 경우 저장하지 않게
      new_file = open("test.csv", 'at', encoding="utf-8")
      new_file.write(d.text)
      new_file.write('\n')
      new_file.close()
  

print("Parsing Sucessed")
