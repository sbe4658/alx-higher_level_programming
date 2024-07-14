#!/usr/bin/python3
""" Inhertits from list object/class. """


class MyList(list):
    """ list attributes+ catchs for int types ;). """
    def print_sorted(self):
        """Sorts a list of ``int``s. """
        print(sorted(self))
