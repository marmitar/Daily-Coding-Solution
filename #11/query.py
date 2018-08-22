from re import match


class Query:

    def __init__(self):
        self.__options__ = list()

    def insert(self, item):
        if type(item) is str:
            self.__options__.append(item)

        elif type(item) is list:
            for obj in item:
                if type(obj) is str:
                    self.__options__.append(obj)
                else:
                    raise TypeError("List constains non-string items")

        else:
            raise TypeError("Item is not string nor list")

    def __getitem__(self, string: str):
        return [
            option
            for option in self.__options__
            if match(string, option)
        ]
