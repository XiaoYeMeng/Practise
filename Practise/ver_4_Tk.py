import tkinter as tk
import requests

window = tk.Tk()
window.title('QRCode')
window.geometry('500x300')

url = 'http://127.0.0.1:8888/?i=yuan_qi_'


# 菜單更新
def menu_update(i):
    # 牛肉庫存 + 1
    if i == 'yuan_qi_beef_%2B1':
        requests.post(url + 'beef_%2B1')

    # 牛肉庫存 - 1
    if i == 'yuan_qi_beef_-1':
        requests.post(url + 'beef_-1')

    if i == 'yuan_qi_pork_%2B1':
        requests.post(url + 'pork_%2B1')

    if i == 'yuan_qi_pork_-1':
        requests.post(url + 'pork_-1')

    if i == 'yuan_qi_lamb_%2B1':
        requests.post(url + 'lamb_%2B1')

    if i == 'yuan_qi_lamb_-1':
        requests.post(url + 'lamb_-1')


'''
GUI
'''
bt = tk.Button(window, text='牛肉庫存數量 + 1', width=18, command=lambda: menu_update('yuan_qi_beef_%2B1'),
               font=('Time new roman', 18))
bt.pack()
bt = tk.Button(window, text='牛肉庫存數量 - 1', width=18, command=lambda: menu_update('yuan_qi_beef_-1'),
               font=('Time new roman', 18))
bt.pack()
bt = tk.Button(window, text='豬肉庫存數量 + 1', width=18, command=lambda: menu_update('yuan_qi_pork_%2B1'),
               font=('Time new roman', 18))
bt.pack()
bt = tk.Button(window, text='豬肉庫存數量 - 1', width=18, command=lambda: menu_update('yuan_qi_pork_-1'),
               font=('Time new roman', 18))
bt.pack()
bt = tk.Button(window, text='羊肉庫存數量 + 1', width=18, command=lambda: menu_update('yuan_qi_lamb_%2B1'),
               font=('Time new roman', 18))
bt.pack()
bt = tk.Button(window, text='羊肉庫存數量 - 1', width=18, command=lambda: menu_update('yuan_qi_lamb_-1'),
               font=('Time new roman', 18))
bt.pack()

window.mainloop()
