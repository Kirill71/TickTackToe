from StateChecker import StateChecker, State
from Table import TablePrinter


class Game:

    def __init__(self, table):
        self.__table = table

    def play(self):
        table = self.__table
        printer = TablePrinter(table)
        checker = StateChecker(table)
        end_game = {State.DRAW, State.O_WIN, State.X_WIN}
        count = 1
        printer.print()
        while checker.process_state() not in end_game:
            while True:
                i, j = input("Enter the coordinates:>").split()
                status, message = self.__is_valid(i, j)
                if not status:
                    print(message)
                    continue

                if table.insert(int(i), int(j), "X" if count % 2 == 1 else "O"):
                    break
                else:
                    print("This cell is occupied! Choose another one!")
            printer.print()
            count += 1

        printer.print()
        print(checker.process_state())

    def __is_valid(self, i, j):
        table = self.__table

        if not i.isdigit() or not j.isdigit():
            return False, "You should enter numbers!"

        if int(i) > table.get_size() or int(j) > table.get_size():
            return False, f"Coordinates should be from 1 to {table.get_size()}!"

        return True, ""
