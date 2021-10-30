# Разработать приложение которое будет хранить в оперативной памяти список сотрудников
# отделов организации. Приложение должно поддерживать
# - добавление удаление и поиск записи об отделе
# - добавление удаление и поиск записи о сотруднике
# Атрибуты сотрудника которые должны храниться:
#  - ФИО
#  - Адрес проживания
#  - Принадлежность к отделам
#  - Дата рождения
#  - Должность
# Атрибуты отдела которые должны храниться:
#  - Название
#  - Количество сотрудников
#  - Список комнат в которых размещается
from employee import Employee
from department import Department


class Organization:
    def __init__(self):
        self.employee_db = list()
        self.department_db = list()

    def insert_new_employee(self):
        emp_tmp = Employee()
        try:
            emp_tmp.input_full_data()
            self.employee_db.append(emp_tmp)
            print("Количество сотрудников: {}".format(len(self.employee_db)))
        except:
            print('\nДанные были введены некорректно, процедура ввода прервана!')

    def remove_employee(self, name: str):
        if len(self.employee_db) > 0:
            search = self.search_employee(name)
            if len(search) == 1:
                self.employee_db.remove(search[0])
            else:
                print('\nНет сотрудников удовлетворяющих критериям! Имя: {}'.format(name))
        else:
            print('\nСписок сотрудников пуст!')

    def search_employee(self, name: str):
        clar_list = list()
        if not self.employee_db:
            print('\nСписок сотрудников пуст!')
            return
        for i in self.employee_db:
            is_find = False
            for personality in name.split():
                # print("personality = {}".format(personality))
                # tmp = i.get_full_name()
                # print('full name = {}'.format(tmp.split()))
                if personality in i.get_divided_full_name():
                    is_find = True
                    continue
                else:
                    is_find = False
                    break
            if is_find:
                # print('appent to clar-list')
                clar_list.append(i)
        if len(clar_list) > 1:
            return self._clarification(clar_list)
        else:
            return clar_list

    def _clarification(self, clar_list):
        print('\nПоиск выдал следующие совпадения:\n\tФИО | Адрес | Отделы | Дата рождения | Должность')
        for n, i in enumerate(clar_list):
            print('{}. {}'.format(n + 1, i.get_full_data()))
        try:
            return [clar_list.pop(int(input('\nВыберите нужный номер строки в списке: ')))]
        except:
            print('\nВведенное значение не корректно! Отмена поиска!')
            return []

    def insert_new_department(self):
        dpt_tmp = Department()
        try:
            dpt_tmp.input_full_data()
            self.department_db.append(dpt_tmp)
            print("Количество отделов: {}".format(len(self.department_db)))
        except:
            print('\nДанные были введены некорректно, процедура ввода прервана!')

    def remove_department(self, name: str):
        if len(self.department_db) > 0:
            search = self.search_department(name)
            print('rem dep search: '.format(search))
            if search != '':
                self.department_db.remove(search)
            else:
                print('\nНет отдела с таким названием! Отдел: {}'.format(name))
        else:
            print('\nСписок отделов пуст!')

    def search_department(self, name: str):
        if not self.department_db:
            print('\nСписок отделов пуст!')
            return
        for i in self.department_db:
            tmp = i.get_name()
            if name == tmp:
                print("i found it!")
                return i
        return ''


def main():
    menu = "Команды: \n" \
           "* search - Совершить поиск по базе данных\n" \
           "* insert - Внести запись в базу данных\n" \
           "* delete - Удалить запись из базы данных\n" \
           "* exit - Выход из программы\n" \
           "Аргументы команд: \n" \
           "E - сотрудник\n" \
           "D - отдел\n" \
           "пример: search E Вася\n" \
           "Введите команду...\n"
    org = Organization()
    while True:
        script = input('\nДобро пожаловать в БД организации\n' + menu).split()
        if len(script) == 3:
            if script[0] == 'search':
                if script[1] == 'E':
                    aa = org.search_employee(script[2])
                    if aa != None and len(aa) > 0:
                        print(aa[0].get_full_data())
                elif script[1] == 'D':
                    aa = org.search_department(script[2])
                    if aa != None:
                        print(aa.get_full_data())
                else:
                    print("Ошибка! Я не знаю такой команды!")
            elif script[0] == 'delete':
                if script[1] == 'E':
                    org.remove_employee(script[2])
                elif script[1] == 'D':
                    org.remove_department(script[2])
                else:
                    print("Ошибка! Я не знаю такой команды!")
        elif len(script) == 2:
            #     insert
            if script[1] == 'E':
                org.insert_new_employee()
            elif script[1] == 'D':
                org.insert_new_department()
            else:
                print("Ошибка! Я не знаю такой команды!")
        elif len(script) == 1:
            if script[0] == 'exit':
                quit(0)
            else:
                print("Ошибка! Я не знаю такой команды!")
        else:
            print("Ошибка! Я не знаю такой команды!")


if __name__ == '__main__':
    main()
