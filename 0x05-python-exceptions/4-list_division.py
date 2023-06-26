#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    div = []
    for i in range(list_length):
            try:
                division = my_list_1[i] / my_list_2[i]
                div.append(division)
            except ZeroDivisionError:
                print("division by 0")
                div.append(0)
            except TypeError:
                div.append(0)
                print("wrong type")
            except ValueError:
                pass
            except IndexError:
                print("out of range")
    return div
