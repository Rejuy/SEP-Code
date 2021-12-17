from services.mysql_service import db
import pandas as pd
import numpy as np
import json


if __name__ == "__main__":
    # load json
    f = open("../department.txt", "r", encoding="utf-8")
    department_list = json.load(f)['list']
    for i in range(len(department_list)):
        department_list[i]['text'] = department_list[i]['text'][4:]
    # load csv
    file_name = "../course.csv"
    raw_data = pd.read_csv(open(file_name,encoding='utf-8',errors="ignore"),keep_default_na=False)
    headers = np.array(raw_data.columns.tolist())
    whole_data = np.array(raw_data)
    key_list = ['name', 'teacher', 'department', 'type', 'credit']
    val_location = [3, 5, 0, 9, 4]
    course_list = []
    for i in range(1, len(whole_data)):
        course = {}
        flag = False
        for j in range(len(key_list)):
            if key_list[j] != "type" and whole_data[i][val_location[j]] == "":
                flag = True
                break
            course[key_list[j]] = whole_data[i][val_location[j]]
        if flag:
            continue
        # 适配department
        change = False
        for d in department_list:
            if course['department'] == d['text']:
                course['department'] = d['value']
                change = True
        if not change:
            course['department'] = 49
        # 适配type
        if "年级" in course['name']:
            course['type'] = 5
        elif course['name'] == "中国近现代史刚要" or "中国特色社会主义" in course['name']:
            course['type'] = 6
        else:
            if course['department'] == 28 or course['department'] == 37:
                course['type'] = 2
            else:
                if "实验课" in course['type']:
                    course['type'] = 4
                elif "文化素质核心课" in course['type']:
                    course['type'] = 7
                elif "文化素质课" in course['type']:
                    course['type'] = 8
                elif "实践课" in course['type']:
                    course['type'] = 9
                else:
                    course['type'] = 1

        # print(course)
        if course not in course_list:
            course_list.append(course)
            db.addItem("course_list", course)
    print(course_list)
