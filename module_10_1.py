"""Необходимо создать функцию write_words(word_count, file_name),
где word_count - количество записываемых слов, file_name - название файла, куда будут записываться слова.
Функция должна вести запись слов "Какое-то слово № <номер слова по порядку>" в соответствующий файл
 с прерыванием после записи каждого на 0.1 секунду.
Сделать паузу можно при помощи функции sleep из модуля time, предварительно импортировав её: from time import sleep.
В конце работы функции вывести строку "Завершилась запись в файл <название файла>".

После создания файла вызовите 4 раза функцию write_words, передав в неё следующие значения:

    10, example1.txt
    30, example2.txt
    200, example3.txt
    100, example4.txt

После вызовов функций создайте 4 потока для вызова этой функции со следующими аргументами для функции:

    10, example5.txt
    30, example6.txt
    200, example7.txt
    100, example8.txt

Запустите эти потоки методом start не забыв, сделать остановку основного потока при помощи join.
Также измерьте время затраченное на выполнение функций и потоков. Как это сделать рассказано в лекции к домашнему заданию.
"""
import threading
from time import time, sleep


def write_words(word_count: int, file_name):
    with open(file_name, 'w', encoding='UTF8') as file:
        for i in range(1, word_count + 1):
            file.write(f'Какое-то слово № {i}\n')
            sleep(0.1)
    return print(f"Завершилась запись в файл {file_name}")


start_time = time()


write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')

end_time = time()
print(f'Работа потоков{end_time - start_time}')

start_time = time()
thread = threading.Thread(target=write_words(10, 'example5.txt'))
thread.start()
thread.join()
thread_1 = threading.Thread(target=write_words(30, 'example6.txt'))
thread_1.start()
thread_2 = threading.Thread(target=write_words(200, 'example7.txt'))
thread_2.start()
thread_3 = threading.Thread(target=write_words(100, 'example8.txt'))
thread_3.start()
end_time = time()

print(f'Работа потоков{end_time - start_time}')
