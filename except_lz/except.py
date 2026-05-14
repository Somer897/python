import pandas as pd
from pandas.errors import EmptyDataError

#Чтение файла
#цикл идет, пока не ввести правильную ссылку
class bank:


    def __init__(self, name):
        self.name = name

        try:
            file = pd.read_csv(self.name, encoding='UTF-8-sig')

        except FileNotFoundError:   

            print(f"Файл '{self.name}' не найден, попробуйте ещё раз")    
                
        except PermissionError:

            print('Нет доступа в файл')

        except EmptyDataError:
            print('Файл пустой')

        self.file = file

    def column(self):
        while True:
            try:
                column = str(input('Введите название изучаемого столбца: '))
                self.file[column]

            except KeyError:
                print('Столбец не найден')

            else:
                print('Столбец существует')

            finally:
                choose = str(input('Хотите продолжить(да)'))
                if choose != 'да' :
                    break

    def cell(self, self1: 'bank'):
        column_names = self.file.columns.tolist()
        list1 = []
        for i in column_names:
            try:
                val = str(self.file.at[1, i])
                new_val = float(val)
                list1.append(type(new_val))
            except ValueError:
                list1.append(type(val))

        column_names1 = self1.file.columns.tolist()
        list2 = []
        for i in column_names1:
            try:
                val1 = str(self1.file.at[1, i])
                new_val1 = float(val)
                list2.append(type(new_val1))
            except ValueError:
                list2.append(type(val1))

        if list1 == list2:
            print('Столбцы такие же, как и ожидалось')
        else:
            print(f'Столбцы не совпадают, ожидалось: {list1}, а в файле: {list2}')
        
        


a = bank('var5.csv')
b = bank('csv.csv')
a.cell(b)