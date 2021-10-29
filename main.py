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
from department import Departament


class Organization:
    def __init__(self):
        self.employee_db = list()
        self.departament_db = list()

    def insert_new_employee(self):
        emp_tmp = Employee()
        try:
            emp_tmp.input_full_data()
            self.employee_db.append(emp_tmp)
        except:
            print('Данные были введены некорректно, процедура ввода прервана!')

    def remove_employee(self, name: str):
        if not self.employee_db:
            search = self.search_employee(name)
            if search.count() == 1:
                self.employee_db.remove(search[0])
            else:
                print('Нет сотрудников удовлетворяющих критериям! Имя: {}'.format(name))
        else:
            print('Список сотрудников пуст!')

    def search_employee(self, name: str):
        clar_list = list()
        for i in self.employee_db:
            is_find = False
            for personality in name.split():
                if personality in i.get_devided_full_name():
                    is_find = True
                    continue
                else:
                    is_find = False
                    break
            if is_find:
                clar_list.append(i)
        if clar_list.count() > 1:
            return self._clarification(clar_list)
        else:
            return clar_list

    def _clarification(self, clar_list):
        print('Поиск выдал следующие совпадения:\n\tФИО | Адрес | Отделы | Дата рождения | Должность')
        for n, i in enumerate(clar_list):
            print('{}. {}'.format(n, i.print_full_data()))
        try:
            return [clar_list.pop(int(input('Выберите нужный номер строки в списке: ')))]
        except:
            print('Введенное значение не корректно! Отмена поиска!')
            return []

    def insert_new_departament(self):
        pass

    def remove_employee(self):
        pass

    def search_departament(self):
        pass


def main():
    pass


if __name__ == '__main__':
    main()
