import random
import tkinter as tk
from tkinter import messagebox
import dict as dt
import time

window = tk.Tk()
window.title('mora')
window.geometry('800x600')


# 判斷答案a的狀況
def a():
    # 答案a若正確
    if bt_a['text'] == dt.topic_1_a or bt_a['text'] == dt.topic_5_a or bt_a['text'] == dt.topic_9_a:
        messagebox.showinfo('ture', 'point + 10')
        lb_point['text'] += 10

    # 答案a若不正確
    else:
        messagebox.showerror('false', 'point + 0')

    # 若題數 = 10 , 秀出總分數以及鎖定答案選項
    if lb_number['text'] == 10:
        messagebox.showinfo('end', '總分 = ' + str(lb_point['text']))
        bt_a['state'] = tk.DISABLED
        bt_b['state'] = tk.DISABLED
        bt_c['state'] = tk.DISABLED
        bt_d['state'] = tk.DISABLED
        bt_reset['state'] = tk.NORMAL
        # 做題時間結束
        lb_sec['text'] = 'end'

    # 若題數 < 10 , 題數與題目更換為下一題
    if lb_number['text'] < 10:
        dt.topic_random.pop(0)
        lb_q['text'] = dt.topic_random[0][0]
        bt_a['text'] = dt.topic_random[0][1]
        bt_b['text'] = dt.topic_random[0][2]
        bt_c['text'] = dt.topic_random[0][3]
        bt_d['text'] = dt.topic_random[0][4]
        lb_number['text'] += 1
        # 重新倒數做題時間
        lb_sec['text'] = int(10)


# 判斷答案b的狀況
def b():
    # 答案b若正確
    if bt_b['text'] == dt.topic_2_b or bt_b['text'] == dt.topic_6_b or bt_b['text'] == dt.topic_10_b:
        messagebox.showinfo('ture', 'point + 10')
        lb_point['text'] += 10

    # 答案b若不正確
    else:
        messagebox.showerror('false', 'point + 0')

    # 若題數 = 10 , 秀出總分數以及鎖定答案選項
    if lb_number['text'] == 10:
        messagebox.showinfo('end', '總分 = ' + str(lb_point['text']))
        bt_a['state'] = tk.DISABLED
        bt_b['state'] = tk.DISABLED
        bt_c['state'] = tk.DISABLED
        bt_d['state'] = tk.DISABLED
        bt_reset['state'] = tk.NORMAL
        # 做題時間結束
        lb_sec['text'] = 'end'

    # 若題數 < 10 , 題數與題目更換為下一題
    if lb_number['text'] < 10:
        dt.topic_random.pop(0)
        lb_q['text'] = dt.topic_random[0][0]
        bt_a['text'] = dt.topic_random[0][1]
        bt_b['text'] = dt.topic_random[0][2]
        bt_c['text'] = dt.topic_random[0][3]
        bt_d['text'] = dt.topic_random[0][4]
        lb_number['text'] += 1
        # 重新倒數做題時間
        lb_sec['text'] = int(10)


# 判斷答案c的狀況
def c():
    # 答案c若正確
    if bt_c['text'] == dt.topic_3_c or bt_c['text'] == dt.topic_7_c:
        messagebox.showinfo('ture', 'point + 10')
        lb_point['text'] += 10

    # 答案c若不正確
    else:
        messagebox.showerror('false', 'point + 0')

    # 若題數 = 10 , 秀出總分數以及鎖定答案選項
    if lb_number['text'] == 10:
        messagebox.showinfo('end', '總分 = ' + str(lb_point['text']))
        bt_a['state'] = tk.DISABLED
        bt_b['state'] = tk.DISABLED
        bt_c['state'] = tk.DISABLED
        bt_d['state'] = tk.DISABLED
        bt_reset['state'] = tk.NORMAL
        # 做題時間結束
        lb_sec['text'] = 'end'

    # 若題數 < 10 , 題數與題目更換為下一題
    if lb_number['text'] < 10:
        dt.topic_random.pop(0)
        lb_q['text'] = dt.topic_random[0][0]
        bt_a['text'] = dt.topic_random[0][1]
        bt_b['text'] = dt.topic_random[0][2]
        bt_c['text'] = dt.topic_random[0][3]
        bt_d['text'] = dt.topic_random[0][4]
        lb_number['text'] += 1
        # 重新倒數做題時間
        lb_sec['text'] = int(10)


# 判斷答案d的狀況
def d():
    # 答案d若正確
    if bt_d['text'] == dt.topic_4_d or bt_d['text'] == dt.topic_8_d:
        messagebox.showinfo('ture', 'point + 10')
        lb_point['text'] += 10

    # 答案d若不正確
    else:
        messagebox.showerror('false', 'point + 0')

    # 若題數 = 10 , 秀出總分數以及鎖定答案選項
    if lb_number['text'] == 10:
        messagebox.showinfo('end', '總分 = ' + str(lb_point['text']))
        bt_a['state'] = tk.DISABLED
        bt_b['state'] = tk.DISABLED
        bt_c['state'] = tk.DISABLED
        bt_d['state'] = tk.DISABLED
        bt_reset['state'] = tk.NORMAL
        # 做題時間結束
        lb_sec['text'] = 'end'

    # 若題數 < 10 , 題數與題目更換為下一題
    if lb_number['text'] < 10:
        dt.topic_random.pop(0)
        lb_q['text'] = dt.topic_random[0][0]
        bt_a['text'] = dt.topic_random[0][1]
        bt_b['text'] = dt.topic_random[0][2]
        bt_c['text'] = dt.topic_random[0][3]
        bt_d['text'] = dt.topic_random[0][4]
        lb_number['text'] += 1
        # 重新倒數做題時間
        lb_sec['text'] = int(10)


# 開始做題 , 鎖定開始bt , 解除鎖定答案選項
def start():
    bt_start['state'] = tk.DISABLED
    bt_a['state'] = tk.NORMAL
    bt_b['state'] = tk.NORMAL
    bt_c['state'] = tk.NORMAL
    bt_d['state'] = tk.NORMAL
    lb_q['text'] = dt.topic_random[0][0]
    bt_a['text'] = dt.topic_random[0][1]
    bt_b['text'] = dt.topic_random[0][2]
    bt_c['text'] = dt.topic_random[0][3]
    bt_d['text'] = dt.topic_random[0][4]
    window.after(0, sec_countdown)


# 重置
def reset():
    # 解除鎖定開始bt以及答案選項
    time.sleep(1)
    bt_start['state'] = tk.NORMAL
    bt_reset['state'] = tk.DISABLED
    bt_a['state'] = tk.DISABLED
    bt_b['state'] = tk.DISABLED
    bt_c['state'] = tk.DISABLED
    bt_d['state'] = tk.DISABLED
    # 重置題目LB
    lb_q['text'] = '題目'
    # 重置題數為1
    lb_number['text'] = int(1)
    # 重置分數為0
    lb_point['text'] = int(0)
    # 重置秒數為10
    lb_sec['text'] = int(10)
    bt_a['text'] = 'A'
    bt_b['text'] = 'B'
    bt_c['text'] = 'C'
    bt_d['text'] = 'D'
    # dict list 加回題目

    dt.topic = []
    dt.topic.append([dt.topic_1_q, dt.topic_1_a, dt.topic_1_b, dt.topic_1_c, dt.topic_1_d])
    dt.topic.append([dt.topic_2_q, dt.topic_2_a, dt.topic_2_b, dt.topic_2_c, dt.topic_2_d])
    dt.topic.append([dt.topic_3_q, dt.topic_3_a, dt.topic_3_b, dt.topic_3_c, dt.topic_3_d])
    dt.topic.append([dt.topic_4_q, dt.topic_4_a, dt.topic_4_b, dt.topic_4_c, dt.topic_4_d])
    dt.topic.append([dt.topic_5_q, dt.topic_5_a, dt.topic_5_b, dt.topic_5_c, dt.topic_5_d])
    dt.topic.append([dt.topic_6_q, dt.topic_6_a, dt.topic_6_b, dt.topic_6_c, dt.topic_6_d])
    dt.topic.append([dt.topic_7_q, dt.topic_7_a, dt.topic_7_b, dt.topic_7_c, dt.topic_7_d])
    dt.topic.append([dt.topic_8_q, dt.topic_8_a, dt.topic_8_b, dt.topic_8_c, dt.topic_8_d])
    dt.topic.append([dt.topic_9_q, dt.topic_9_a, dt.topic_9_b, dt.topic_9_c, dt.topic_9_d])
    dt.topic.append([dt.topic_10_q, dt.topic_10_a, dt.topic_10_b, dt.topic_10_c, dt.topic_10_d])

    dt.topic_random = random.sample(dt.topic, len(dt.topic))


# 做題時間倒數
def sec_countdown():
    if lb_sec['text'] > 0:
        lb_sec['text'] -= 1
        window.after(1000, sec_countdown)


    elif lb_sec['text'] == 0:
        messagebox.showerror('time up', 'point + 0')
        dt.topic_random.pop(0)
        lb_q['text'] = dt.topic_random[0][0]
        bt_a['text'] = dt.topic_random[0][1]
        bt_b['text'] = dt.topic_random[0][2]
        bt_c['text'] = dt.topic_random[0][3]
        bt_d['text'] = dt.topic_random[0][4]
        lb_number['text'] += 1
        lb_sec['text'] = int(10)
        window.after(1000, sec_countdown)


# 當下題數
lb_number = tk.Label(window, text=int(1), width=9, font=('Time new roman', 18))
lb_number.pack()
# 當下題目
lb_q = tk.Label(window, text='題目', width=18, font=('Time new roman', 18))
lb_q.pack()
# 當下分數
lb_point = tk.Label(window, text=int(0), width=9, font=('Time new roman', 18))
lb_point.pack()
# 倒數秒數
lb_sec = tk.Label(window, text=int(10), width=9, font=('Time new roman', 18))
lb_sec.pack()

# 開始做題
bt_start = tk.Button(window, text='start', width=9, command=start, font=('Time new roman', 18))
bt_start.pack()
# 重新開始
bt_reset = tk.Button(window, text='reset', width=9, command=reset, font=('Time new roman', 18))
bt_reset.pack()
# 答案ABCD
bt_a = tk.Button(window, text='A', width=9, command=a, font=('Time new roman', 18))
bt_a.pack()
bt_b = tk.Button(window, text='B', width=9, command=b, font=('Time new roman', 18))
bt_b.pack()
bt_c = tk.Button(window, text='C', width=9, command=c, font=('Time new roman', 18))
bt_c.pack()
bt_d = tk.Button(window, text='D', width=9, command=d, font=('Time new roman', 18))
bt_d.pack()

bt_a['state'] = tk.DISABLED
bt_b['state'] = tk.DISABLED
bt_c['state'] = tk.DISABLED
bt_d['state'] = tk.DISABLED
bt_reset['state'] = tk.DISABLED

window.mainloop()