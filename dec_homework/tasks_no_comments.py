import datetime
import sys


def task1():
    original_write = sys.stdout.write

    def my_write(string_text):
        if string_text != '\n':
            current_time = datetime.datetime.now()
            str_date_time = current_time.strftime("%d-%m-%Y, %H:%M:%S")
            original_write('['+str_date_time+']: '+string_text+'\n')

    sys.stdout.write = my_write
    print("1, 2, 3")
    sys.stdout.write = original_write


def task2():

    def timed_output(function):
        def wrapper(*args, **kwargs):
            current_time = datetime.datetime.now()
            str_date_time = current_time.strftime("%d-%m-%Y, %H:%M:%S")
            sys.stdout.write('[' + str_date_time + ']: ')
            function(*args, **kwargs)

        return wrapper

    @timed_output
    def print_greeting(name):
        print(f'Hello, {name}!')

    print_greeting("Nikita")


def task3():

    def redirect_output(filepath):
        def outer_wrapper(function):
            def inner_wrapper(*args, **kwargs):
                original_write = sys.stdout.write

                def file_write(string_text):
                    with open(filepath, 'a') as file:
                        file.write(string_text)

                with open(filepath, 'w') as file:
                    file.write('')
                sys.stdout.write = file_write
                function(*args, **kwargs)

            return inner_wrapper

        return outer_wrapper

    @redirect_output('./function_output.txt')
    def calculate():
        for power in range(1, 5):
            for num in range(1, 20):
                print(num ** power, end=' ')
            print()

    calculate()


if __name__ == '__main__':
    task1()
    task2()
    task3()
