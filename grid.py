from custom_array import Array


class Grid():

    def __init__(self, rows, columns, fill_value=None) -> None:
        self.data = Array(rows)
        for row in range(rows):
            self.data[row] = Array(columns, fill_value)

    def get_height(self) -> int:
        return len(self.data)

    def get_width(self) -> int:
        return len(self.data[0])

    def __getitem__(self, index) -> Array:
        return self.data[index]

    def __str__(self) -> str:
        result = ''
        for row in range(self.get_height()):
            for col in range(self.get_width()):
                result += f'{str(self.data[row][col])} '
            result += '\n'
        return result
