import tkinter as tk


def hour_up():
    lb_hour['text'] += 1


def hour_down():
    if lb_hour['text'] > 0:
        lb_hour['text'] -= 1


def min_up():
    if lb_min['text'] < 59:
        lb_min['text'] += 1
    else:
        lb_min['text'] -= 59


def min_down():
    if lb_min['text'] > 0:
        lb_min['text'] -= 1
    else:
        lb_min['text'] += 59


def sec_up():
    if lb_sec['text'] < 59:
        lb_sec['text'] += 1
    else:
        lb_sec['text'] -= 59


def sec_down():
    if lb_sec['text'] > 0:
        lb_sec['text'] -= 1
    else:
        lb_sec['text'] += 59


def start():
    if lb_sec['text'] > 0:
        lb_sec['text'] -= 1
        window.after(1000, start)
        print('sec')
    elif lb_sec['text'] == 0 and lb_min['text'] > 0:
        lb_min['text'] -= 1
        lb_sec['text'] += 59
        window.after(1000, start)
        print('min')
    elif lb_sec['text'] == 0 and lb_min['text'] == 0 and lb_hour['text'] > 0:
        lb_hour['text'] -= 1
        lb_min['text'] += 59
        lb_sec['text'] += 59
        window.after(1000, start)
        print('hour')
    else:
        lb_end['text'] = 'Time is up.'


# todo pause and lock
# def pause():


def reset():
    lb_hour['text'] = 0
    lb_min['text'] = 0
    lb_sec['text'] = 0
    lb_end['text'] = ''


'''
GUI
'''
window = tk.Tk()
window.title('Countdown Timer')
window.geometry('800x400')

'''
Label
'''
lb_title = tk.Label(window, text='Countdown Timer', font=('Time new roman', 54))
lb_title.pack()
lb_hour = tk.Label(window, text=int(0), font=('Time new roman', 36))
lb_hour.place(x=200, y=100)
lb_hour_colon = tk.Label(window, text=':', font=('Time new roman', 36))
lb_hour_colon.place(x=300, y=95)
lb_min = tk.Label(window, text=int(0), font=('Time new roman', 36))
lb_min.place(x=350, y=100)
lb_min_colon = tk.Label(window, text=':', font=('Time new roman', 36))
lb_min_colon.place(x=450, y=95)
lb_sec = tk.Label(window, text=int(0), font=('Time new roman', 36))
lb_sec.place(x=500, y=100)
lb_end = tk.Label(window, text='', font=('Time new roman', 36))
lb_end.place(x=265, y=300)

'''
Button
'''
bt_hour_up = tk.Button(window, text='↑', font=('Time new roman', 9), command=hour_up)
bt_hour_up.place(x=250, y=105)
bt_hour_down = tk.Button(window, text='↓', font=('Time new roman', 9), command=hour_down)
bt_hour_down.place(x=250, y=125)
bt_min_up = tk.Button(window, text='↑', font=('Time new roman', 9), command=min_up)
bt_min_up.place(x=400, y=105)
bt_min_down = tk.Button(window, text='↓', font=('Time new roman', 9), command=min_down)
bt_min_down.place(x=400, y=125)
bt_sec_up = tk.Button(window, text='↑', font=('Time new roman', 9), command=sec_up)
bt_sec_up.place(x=550, y=105)
bt_sec_down = tk.Button(window, text='↓', font=('Time new roman', 9), command=sec_down)
bt_sec_down.place(x=550, y=125)
bt_start = tk.Button(window, width=5, text='start', font=('Time new roman', 36), command=start)
bt_start.place(x=100, y=200)
bt_pause = tk.Button(window, width=5, text='pause', font=('Time new roman', 36))
bt_pause.place(x=300, y=200)
bt_reset = tk.Button(window, width=5, text='reset', font=('Time new roman', 36), command=reset)
bt_reset.place(x=500, y=200)


window.mainloop()
