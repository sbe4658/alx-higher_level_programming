#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    res = []
    for idx in range(list_length):
        try:
            res.append(my_list_1[idx] / my_list_2[idx])
        except (ValueError, TypeError):
            print("wrong type")
            res.append(0)
            continue
        except IndexError:
            print("out of range")
            res.append(0)
            continue
        except ZeroDivisionError:
            res.append(0)
            print("division by 0")
            continue
        finally:
            pass
    return res
