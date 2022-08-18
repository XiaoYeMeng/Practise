import tkinter as tk
import requests

window = tk.Tk()
window.title('QRCode')
window.geometry('1000x600')


def menu_update(i):
    if i == 'yuan_qi_beef_%2B1':
        requests.post('http://127.0.0.1:8888/?i=yuan_qi_beef_%2B1')

    if i == 'yuan_qi_beef_-1':
        requests.post('http://127.0.0.1:8888/?i=yuan_qi_beef_-1')

    if i == 'yuan_qi_pork_%2B1':
        requests.post('http://127.0.0.1:8888/?i=yuan_qi_pork_%2B1')

    if i == 'yuan_qi_pork_-1':
        requests.post('http://127.0.0.1:8888/?i=yuan_qi_pork_-1')

    if i == 'yuan_qi_lamb_%2B1':
        requests.post('http://127.0.0.1:8888/?i=yuan_qi_lamb_%2B1')

    if i == 'yuan_qi_lamb_-1':
        requests.post('http://127.0.0.1:8888/?i=yuan_qi_lamb_-1')


bt = tk.Button(window, text='牛肉庫存數量 + 1', width=18, command=lambda: menu_update('yuan_qi_beef_%2B1'), font=('Time new roman', 18))
bt.pack()
bt = tk.Button(window, text='牛肉庫存數量 - 1', width=18, command=lambda: menu_update('yuan_qi_beef_-1'), font=('Time new roman', 18))
bt.pack()
bt = tk.Button(window, text='豬肉庫存數量 + 1', width=18, command=lambda: menu_update('yuan_qi_pork_%2B1'), font=('Time new roman', 18))
bt.pack()
bt = tk.Button(window, text='豬肉庫存數量 - 1', width=18, command=lambda: menu_update('yuan_qi_pork_-1'), font=('Time new roman', 18))
bt.pack()
bt = tk.Button(window, text='羊肉庫存數量 + 1', width=18, command=lambda: menu_update('yuan_qi_lamb_%2B1'), font=('Time new roman', 18))
bt.pack()
bt = tk.Button(window, text='羊肉庫存數量 - 1', width=18, command=lambda: menu_update('yuan_qi_lamb_-1'), font=('Time new roman', 18))
bt.pack()

window.mainloop()
