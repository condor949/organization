# Атрибуты отдела которые должны храниться:
#  - Название
#  - Количество сотрудников
#  - Список комнат в которых размещается
class Department:
    def __init__(self):
        self._name = ''
        self._employeers_count = ''
        self._rooms = list()

    def input_full_data(self):
        try:
            self._name = input('Введите полное название отдела и нажмите Enter: ')
            print("department name {}".format(self._name))
            self._employeers_count = input('Введите количество сотрудников и нажмите Enter: ')
            print("_employeers_count {}".format(self._employeers_count))
            self._rooms = input('Введите список комнат нажмите Enter: ').split()
            print("_rooms {}".format(self._rooms))
        except:
            print("EXCEPTION")
            raise Exception()

    def get_name(self):
        return self._name

    def get_full_data(self):
        return [self._name, self._employeers_count, self._rooms]