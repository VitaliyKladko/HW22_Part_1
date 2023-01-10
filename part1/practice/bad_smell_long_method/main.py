# В задании представлена одна большая функция... 
# Делает она всего ничего:
# - читает из строки (файла)         `_read`
# - сортирует прочитанные значения   `_sort`
# - фильтрует итоговый результат     `_filter`

# Конечно, вы можете попробовать разобраться как она 
# это делает, но мы бы советовали разнести функционал 
# по более узким функциям и написать их с нуля


csv = """Вася;39\nПетя;26\nВасилий Петрович;9"""


def get_users_list(text: str) -> list:
    read_data: list = _read(text)
    sorted_data: list = _sort(read_data)
    return _filter(sorted_data)


def _read(text: str) -> list:
    """
    Функция отдает список списков с именем и возрастом
    """
    return [word.split(';') for word in text.split('\n')]


def _sort(read_data: list) -> list:
    """
    Функция отдает сортированный по возр. список списков с именем и возрастом
    """
    return sorted(read_data, key=lambda lst: int(lst[1]))


def _filter(sort_data: list) -> list:
    """
    Отдает списки людей, возраст которых > 10 лет
    """
    return [lst for lst in sort_data if int(lst[1]) > 10]


if __name__ == '__main__':
    print(get_users_list(csv))
