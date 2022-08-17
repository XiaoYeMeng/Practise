import tkinter as tk
import openpyxl
import pandas as pd

window = tk.Tk()
window.title('QRCode')
window.geometry('1000x600')

# 讀取excel sheet
xlsx = openpyxl.load_workbook('./menu.xlsx')
sheet = xlsx['menu']
# 第一題
beef = sheet.cell(column=1, row=2).value
pork = sheet.cell(column=2, row=2).value
lamb = sheet.cell(column=3, row=2).value

# menu dict
menu = {
    'beef': beef,
    'pork': pork,
    'lamb': lamb
}


# 更新菜單
def menu_update(i):
    global beef, pork, lamb

    if i == 'yuan_qi_beef_+1':
        beef += 1
        sheet['A2'] = beef
        xlsx.save('./menu.xlsx')
        print(beef)

    elif i == 'yuan_qi_beef_-1':
        beef -= 1
        sheet['A2'] = beef
        xlsx.save('./menu.xlsx')
        print(beef)

    elif i == 'yuan_qi_pork_+1':
        pork += 1
        sheet['B2'] = pork
        xlsx.save('./menu.xlsx')
        print(pork)

    elif i == 'yuan_qi_pork_-1':
        pork -= 1
        sheet['B2'] = pork
        xlsx.save('./menu.xlsx')
        print(pork)

    elif i == 'yuan_qi_lamb_+1':
        lamb += 1
        sheet['C2'] = lamb
        xlsx.save('./menu.xlsx')
        print(lamb)

    elif i == 'yuan_qi_lamb_-1':
        lamb -= 1
        sheet['C2'] = lamb
        xlsx.save('./menu.xlsx')
        print(lamb)

    else:
        print('False')
    custom = pd.read_excel('menu.xlsx', sheet_name=['menu'])
    print(custom)


def test():
    print(et.get())


et = tk.Entry(window, font=('Time new roman', 18))
et.pack()
bt = tk.Button(window, text='click', command=lambda: menu_update(et.get()), font=('Time new roman', 18))
bt.pack()

window.mainloop()
