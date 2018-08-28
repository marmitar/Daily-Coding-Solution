class __Query_Part__:

    def __init__(self):
        self.__parts__ = dict()
        self.__end__ = False

    def insert(self, item):
        if not item:
            self.__end__ = True
            return

        qpart = self.__parts__.get(item[0])
        if not qpart:
            qpart = __Query_Part__()
            self.__parts__[item[0]] = qpart

        qpart.insert(item[1:])

    def get(self, item=None):

        if not item:
            ans = list()

            for letter, qpart in self.__parts__.items():
                for partial_str in qpart.get():
                    ans.append(letter + partial_str)

            if self.__end__:
                ans.append("")

            return ans

        else:
            qpart = self.__parts__.get(item[0])

            if qpart:
                return qpart.get(item[1:])
            else:
                return list()


class Query:

    def __init__(self):
        self.__partial__ = __Query_Part__()

    def insert(self, item):
        if type(item) is str:
            self.__partial__.insert(item)

        elif type(item) is list:
            for obj in item:
                if type(obj) is not str:
                    raise TypeError("List constains non-string items")

                self.__partial__.insert(obj)

        else:
            raise TypeError("Item is not string nor list")

    def __getitem__(self, string: str):
        return [string + partial for partial in self.__partial__.get(string)]
