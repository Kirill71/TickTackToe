from enum import Enum, auto


class State(Enum):
    X_WIN = auto()
    O_WIN = auto()
    DRAW = auto()
    IMPOSSIBLE = auto()
    NOT_FINISHED = auto()

    def __str__(self):
        return {
            self.X_WIN: "X wins",
            self.O_WIN: "O wins",
            self.DRAW: "Draw",
            self.NOT_FINISHED: "Game not finished",
            self.IMPOSSIBLE: "Impossible"
        }[self]


class StateChecker:
    empty_cell_sigh = "_"

    def __init__(self, table):
        self.__table = table
        self.__state = State.NOT_FINISHED

    def process_state(self):

        if self.__is_win("X"):
            if self.__is_win("O"):
                self.__state = State.IMPOSSIBLE
            else:
                self.__state = State.X_WIN
        elif self.__is_win("O"):
            self.__state = State.O_WIN
        elif self.__is_draw():
            self.__state = State.DRAW
        elif self.__is_not_finished():
            self.__state = State.NOT_FINISHED
        else:
            self.__state = State.IMPOSSIBLE

        return self.__state

    def __is_win(self, side):
        table = self.__table
        length = table.get_size()
        win = [side] * length

        for row in table:
            if row == win:
                return True

        for i in range(length):
            column = []
            for j in range(length):
                column.append(table[j][i])
            if column == win:
                return True

        diag = []
        for i in range(length):
            diag.append(table[i][i])
        if diag == win:
            return True

        diag.clear()
        for i in range(length):
            diag.append(table[i][length - i - 1])

        return diag == win

    def __has_empty_cells(self):
        table = self.__table.get_content()
        empty_sigh = StateChecker.empty_cell_sigh
        for row in table:
            if empty_sigh in row:
                return True

        return False

    def __is_no_side_win(self):
        return \
            not self.__is_win("X") \
            and not self.__is_win("O")

    def __is_draw(self):
        return self.__is_no_side_win() and not self.__has_empty_cells()

    def __is_not_finished(self):
        return self.__is_no_side_win() and self.__has_empty_cells() and not self.__is_impossible()

    def __is_impossible(self):
        table = self.__table.get_content()
        countX = 0
        countO = 0
        for row in table:
            countX += row.count("X")
            countO += row.count("O")
        return abs(countX - countO) > 1
