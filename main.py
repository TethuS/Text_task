import random

def get_deletingt_lines(path, num_str):

    with open(path, "r") as file:
        str_count = get_count_of_lines(path)
        del_list = get_rand_lines_for_del(num_str, str_count)
        with open(path[:-4] + "_res.txt", "w") as new_file:
            for str_num, line in enumerate(file):
                if str_num + 1 not in del_list:
                    new_file.write(line)


# подсчитываем строки в файле
def get_count_of_lines(path):
    with open(path, "r") as file:
        count = 0
        for line in file:
            count += 1
    return count


# создаем список рандомных строк, которые позже будем удалять из файла
def get_rand_lines_for_del(num_str, str_count):
    lines_to_del = []
    for i in range(num_str):
        num = random.randint(0, str_count - 1)
        lines_to_del.append(num)
    return lines_to_del

def main():
    path = input("Введите путь к файлу и его имя. \nПример: C:\path\\name.txt \n >>")
    #Не получается подставить функцию значение 14 по умолчанию
    # выдает ошибку ValueError: invalid literal for int() with base 10: ''
    # работает лишь через костыль в инпуте
    num_str = int(input("Введите число удаляемых строк (по умолчанию 14): \n >>") or 14)
    get_deletingt_lines(path, num_str)

main()
