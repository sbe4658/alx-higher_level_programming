#!/usr/bin/python3
def safe_print_division(a, b):
    res = 0.0
    try:
        res = a / b
        return res
    except (TypeError, ZeroDivisionError):
        res = None
        return None
    finally:
        if res:
            print("Inside result: {:.1f}".format(res))
        else:
            print("Inside result: None")
