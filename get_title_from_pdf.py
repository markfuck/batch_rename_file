"""
@author: majb
@date: 2019/1/18
@file: get_title_from_pdf.py
"""
from PyPDF2 import PdfFileReader
import os, datetime


def format_str(old_str):
    old_str = old_str.replace("\\", "_")
    old_str = old_str.replace("/", "_")
    old_str = old_str.replace(":", "_")
    old_str = old_str.replace("：", "_")
    old_str = old_str.replace("*", "_")
    old_str = old_str.replace("?", "_")
    old_str = old_str.replace("\"", "_")
    old_str = old_str.replace("<", "_")
    old_str = old_str.replace("<", "_")
    old_str = old_str.replace("|", "_")
    return old_str


def get_format_num(position):
    num = str(position + 1)
    if len(num) == 1:
        num = "00" + num
    elif len(num) == 2:
        num = "0" + num
    return num


def get_title(path):
    for root, dirs, files in os.walk(path):
        print(files)
        files = sorted(files, key=lambda x: os.path.getmtime(os.path.join(path, x)), reverse=False)
        title = str()
        for position in range(0, len(files)):
            file_path = path + "\\" + files[position]
            time_stamp = os.path.getmtime(file_path)
            date = datetime.datetime.fromtimestamp(time_stamp)
            print("修改时间: {}".format(date.strftime("%Y-%m-%d %H:%M:%S")), end=" ")
            with open(file_path, "rb") as f:
                pdf_reader = PdfFileReader(f)
                title = pdf_reader.getDocumentInfo().title
                print(title)

            title = format_str(title)
            sorted_num = get_format_num(position)
            os.rename(file_path, path + "\\" + sorted_num + "_" + title + ".pdf")


if __name__ == '__main__':
    get_title("D:\\PycharmProjects\\batch_rename_file\\file")
