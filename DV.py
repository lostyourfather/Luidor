import pandas as pd
import tkinter as tk


class Program:
    def __init__(self):
        self.main_window = tk.Tk()
        self.date1 = tk.StringVar()
        self.date2 = tk.StringVar()
        self.name_obj = tk.StringVar()
        self.first_input_field = tk.Entry(textvariable=self.date1)
        self.second_input_field = tk.Entry(textvariable=self.date2)
        self.third_input_field = tk.Entry(textvariable=self.name_obj)
        self.btn = tk.Button(command=self.click)
        self.answer_field = tk.Label(bg='Green')
        self.date1_label = tk.Label(text='От: ')
        self.date2_label = tk.Label(text='До: ')
        self.name_obj_label = tk.Label(text='Название объекта: ')
        self.file = self.clear_file()
        self.data = pd.read_csv(self.file, index_col='date/time', parse_dates=True, sep=';', dtype='unicode')
        self.data = self.data.sort_index()

    def visual_design(self):
        self.main_window.title('Обработчик данных')
        self.main_window.geometry('300x300')
        self.first_input_field.grid(row=0, column=1)
        self.second_input_field.grid(row=1, column=1)
        self.third_input_field.grid(row=2, column=1)
        self.btn['text'] = 'Посчитать'
        self.btn.grid(row=3, column=1)
        self.answer_field.grid(row=4, column=1)
        self.date1_label.grid(row=0, column=0)
        self.date2_label.grid(row=1, column=0)
        self.name_obj_label.grid(row=2, column=0)
        self.main_window.mainloop()

    def click(self):
        a = self.data.loc[self.date1.get():self.date2.get(), 'dosing package name']
        b = self.data.loc[self.date1.get():self.date2.get(), 'actual dosing time']
        c = self.data.loc[self.date1.get():self.date2.get(), 'actual flow rate K1']
        name = self.name_obj.get()
        cnt = 0
        dict_obj_weight = dict()
        for i, j in enumerate(a):
            b[i] = b[i].replace(',', '.')
            c[i] = c[i].replace(',', '.')
            dict_obj_weight[j] = dict_obj_weight.get(j, 0) + (float(b[i]) * float(c[i]))
            if j == name:
                cnt += 1

        self.answer_field['text'] = 'Название: ' + str(name) + '\n' + "Количество: " + str(cnt) + '\n' + 'Вес: ' + str(
            dict_obj_weight[name])

    def clear_file(self):
        file = open('shotdata.csv', 'r')
        first_required = 'SEP=;'
        second_required = '[-];[DD:MM:YYYY hh:mm:ss];[-];[-];[-];[s];[s];[g];[g];[°C];[°C];[g/s];[g/s];[-];[-];[bar];[bar];[bar];[°C];[°C];[°C];[°C];[g/s];[g/s];[-];[-];[bar];[bar];[bar];[°C];[°C]'
        data_file = ''
        for row in file.readlines():
            if first_required in row or second_required in row:
                continue
            else:
                data_file = data_file + str(row)
        file.close()
        file = open('shotdata.csv', 'w')
        file.write(data_file)
        file.close()
        return 'shotdata.csv'


Program().visual_design()
