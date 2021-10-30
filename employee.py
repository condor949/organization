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
        divided = self._full_name.split()
        return divided

    def get_departments(self):
        return self._departments

    def input_full_data(self):
        try:
            self._full_name = input('Введите полное имя сотрудника, в формате Фамилия Имя Отчество,'\
                                        ' через пробел и нажмите Enter: ')
            # print("full name {}".format(self._full_name))
            self._address = input('Введите адрес сотрудника и нажмите Enter: ')
            # print("address {}".format(self._address))
            self._departments = input('Введите названия отделов где числится сотрудник,'\
                                          ' через пробел и нажмите Enter: ').split()
            # print("departments {}".format(self._departments))
            self._birthday = input('Введите дату рождения сотрудника,'\
                                       ' в формате ДД.ММ.ГГГГ и нажмите Enter: ')
            # print("birthday {}".format(self._birthday))
            self._position = input('Введите должность сотрудника и нажмите Enter: ')
            # print("position {}".format(self._position))
        except:
            # print("EXCEPTION")
            raise Exception()

    def get_full_data(self):
        return [self._full_name, self._address, self._departments, self._birthday, self._position]

    def print_full_data(self):
        print('{} | {} | {} | {} | {}'.format(self._full_name,
                                              self._address,
                                              self._departments,
                                              self._birthday,
                                              self._position))
