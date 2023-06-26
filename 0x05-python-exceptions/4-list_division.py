#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    div = []
    for i in range(list_length):
            result = 0
            try:
                division = my_list_1[i] / my_list_2[i]
                result = division
            except ZeroDivisionError:
                result = 0
                print("division by 0")
            except TypeError:
                result = 0
                print("wrong type")
            except ValueError:
                pass
            except IndexError:
                print("out of range")
            finally:
                 div.append(result)
    return div


my_l_1 = [10, 8, 4]
my_l_2 = [2, 4, 4]
result = list_division(my_l_1, my_l_2, max(len(my_l_1), len(my_l_2)))
print(result)

print("--")

my_l_1 = [10, 8, 4, 4]
my_l_2 = [2, 0, "H", 2, 7]
result = list_division(my_l_1, my_l_2, max(len(my_l_1), len(my_l_2)))
print(result)