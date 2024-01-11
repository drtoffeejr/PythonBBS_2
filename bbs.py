from datetime import datetime
import csv
import os

file_path = "./bbs.csv"

#---------------

def read_comment():
    
    if not os.path.exists(file_path):
        return

    with open(file_path, "r", encoding="UTF-8") as csv_file:
        csv_reader = csv.reader(csv_file)
        lines = list(csv_reader)
    
    for line in (lines):
        name, comment, time = line
        print(f"{name}: {comment} - {time} -")


#---------------

NAME_MAX = 20
COMMENT_MAX = 100

def new_comment():
    while True:
        errors = []
        
        text_NAME = input("名前: ")
    
        if(text_NAME == ""):
            errors.append("お名前は入力して下さい。")
        elif(NAME_MAX < len(text_NAME)):
            errors.append("お名前は20文字以内で入力して下さい。")
        
        if len(errors) > 0:
            for error in errors:
                print(error)
        else:
            break
    
    while True:
        errors = []

        text_COMM = input("コメント: ")
    
        if(text_COMM == ""):
            errors.append("コメントは入力して下さい。")
        elif(COMMENT_MAX < len(text_COMM)):
            errors.append("コメントは100文字以内で入力して下さい。")
            
        if len(errors) > 0:
            for error in errors:
                print(error)
        else:
            break

    comment_time = datetime.now()
    write_time = comment_time.strftime("%Y年%m月%d日 %H時%M分%S秒")
    
    if not os.path.exists(file_path):
        with open(file_path, "w", newline='', encoding="UTF-8") as csv_file:
            csv_writer = csv.writer(csv_file)
    
    with open(file_path, "a", newline='', encoding="UTF-8") as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow([text_NAME, text_COMM, write_time])
    
    with open(file_path, "r", encoding="UTF-8") as csv_file:
        csv_reader = csv.reader(csv_file)
        lines = list(csv_reader)
    
    for line in lines:
        name, comment, time = line
        print(f"{name}: {comment} - {time} -")
        

#---------------

def cont_ques():
    
    cont_ans = input("0) 終了する 1)書き込む :")
    
    if cont_ans in ["0"]:
        print("終了します")
    
    elif cont_ans in ["1"]:
        new_comment()
        cont_ques()
    
    else:
        print("エラー：0か１で入力してください")
        cont_ques()
