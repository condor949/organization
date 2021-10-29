# Атрибуты сотрудника которые должны храниться:
#  - ФИО
#  - Адрес проживания
#  - Принадлежность к отделам
#  - Дата рождения
#  - Должность

class Employee:
    def __init__(self):
        self._full_name = ''
        self._address = ''
        self._departments = list()
        self._birthday = ''
        self._position = ''

    def get_full_name(self):
        return self._full_name

    def get_divided_full_name(self):
        return self._full_name.split()

    def get_departments(self):
        return self._departments

    def input_full_data(self):
        try:
            self._full_name = str(input('Введите полное имя сотрудника,\n в формате Фамилия Имя Отчество,'
                                        ' через пробел и нажмите Enter'))
            self._address = str(input('Введите адрес сотрудника и нажмите Enter'))
            self._departments = str(input('Введите названия отделов где числится сотрудник,\n'
                                          ' через пробел и нажмите Enter')).split()
            self._birthday = str(input('Введите дату рождения сотрудника,\n'
                                       ' в формате ДД.ММ.ГГГГ и нажмите Enter'))
            self._position = str(input('Введите должность сотрудника и нажмите Enter'))
        except:
            raise Exception()

    def print_full_data(self):
        print('{} | {} | {} | {} | {}'.format(self._full_name,
                                              self._address,
                                              self._departments,
                                              self._birthday,
                                              self._position))
