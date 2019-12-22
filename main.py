"""
@author: https://github.com/markfuck
@date: 2019/12/20
"""

import tkinter as tk
from tkinter.messagebox import showerror
from tkinter.messagebox import showinfo
import os


def modify_file_name():
    file_path = entry_file_path.get()
    if len(file_path) == 0:
        showerror("错误", "输入文件路径")

    files = os.listdir(file_path)
    if len(files) == 0:
        showerror("错误", "文件夹下没有文件")
    else:
        try:
            for f_name in files:
                print(f_name)
                # f = f_name.split("-")[4]
                # index = f.index("_combined")
                # start = f[0:index]
                # end = f[index + 9:f.index(".")]
                # new_name = file_path + "\\MARS-" + start + end + ".fastq.gz"
                new_name = file_path + "\\" + f_name.replace("MARS", "MRSA")
                os.rename(file_path + "\\" + f_name, new_name)
            showinfo("成功", "共{}个文件，全部修改成功".format(len(files)))
        except Exception as e:
            print(e)
            showerror("错误", "出现异常~")


root = tk.Tk()
width, height = 400, 300
size = "%dx%d+%d+%d" % (
    width, height, (root.winfo_screenwidth() - width) / 2, (root.winfo_screenheight() - height) / 2)
root.geometry(size)
root.title("没事学学写代码吧~")

frame_acc = tk.Frame(root)
frame_acc.pack()
tk.Label(frame_acc, text="文件路径：", pady=50, fg="blue", font=("宋体", 16)).grid(row=0, column=0)
entry_file_path = tk.Entry(frame_acc)
entry_file_path.grid(row=0, column=1)
btn = tk.Button(root, text="修改", font=("宋体", 16), command=modify_file_name)
btn.pack()
root.mainloop()
