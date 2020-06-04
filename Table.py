class Table:
    def __init__(self):
        self.__content = self.__generate_default_table()

    def __iter__(self):
        return self.__content.__iter__()

    def __getitem__(self, item):
        return self.__content[item]

    def __setitem__(self, key, value):
        self.__content[key] = value

    @staticmethod
    def __generate_default_table():
        default_row_size = 3
        return [["_" for _ in range(default_row_size)] for _ in range(default_row_size)]

    def get_content(self):
        return self.__content

    def get_size(self):
        return len(self.__content)

    def insert(self, i, j, sign):
        n = self.get_size()

        if self[n - j][i - 1] == "_":
            self[n - j][i - 1] = sign
            return True

        return False


class TablePrinter:
    border_char = '-'
    border_width = 9

    def __init__(self, table):
        self.__table = table

    def print(self):
        char = TablePrinter.border_char
        width = TablePrinter.border_width

        print(char * width)
        for row in self.__table.get_content():
            formatted_row = ''
            for item in row:
                formatted_row += f"{item} "

            print("| " + formatted_row[: -1] + " |")

        print(char * width)
