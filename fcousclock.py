import tkinter as tk
from tkinter import messagebox
import time

# 设置工作和休息时间
WORK_TIME = 25 * 60
BREAK_TIME = 5 * 60

# 初始化计时器
timer = None

# 创建主窗口
root = tk.Tk()
root.title("Focus Clock")

# 创建显示标签
time_label = tk.Label(root, font=("Helvetica", 36))
time_label.pack()

# 更新显示标签
def update_label():
    # 获取剩余时间
    remaining_time = WORK_TIME - int(time.time() - start_time)
    
    # 如果剩余时间小于等于0，弹出提示框并重置计时器
    if remaining_time <= 0:
        messagebox.showinfo("Time's up!", "Take a break!")
        reset_timer()
        return
    
    # 将剩余时间转换为分钟和秒钟
    minutes, seconds = divmod(remaining_time, 60)
    
    # 更新显示标签
    time_label.config(text=f"{minutes:02}:{seconds:02}")
    
    # 继续计时
    timer = root.after(1000, update_label)

# 开始计时器
def start_timer():
    global start_time, timer
    
    # 如果计时器已经在运行，则不执行任何操作
    if timer is not None:
        return
    
    # 记录开始时间并开始计时
    start_time = time.time()
    timer = root.after(1000, update_label)

# 重置计时器
def reset_timer():
    global timer
    
    # 取消计时器并重置显示标签
    if timer is not None:
        root.after_cancel(timer)
        timer = None
    
    time_label.config(text="25:00")

# 创建开始和重置按钮
start_button = tk.Button(root, text="Start", command=start_timer)
start_button.pack()

reset_button = tk.Button(root, text="Reset", command=reset_timer)
reset_button.pack()

# 初始化显示标签并启动主循环
reset_timer()
root.mainloop()
