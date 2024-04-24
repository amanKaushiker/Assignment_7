class Myclass:
    def __init__(self, value):
        self._value = value

    def show(self):
        print(f"Value is {self._value}")

    @property
    def ten_value(self):
        return 10 * self._value

    @ten_value.setter
    def ten_value(self, new_value):
        self._Value = new_value / 10


obj1 = Myclass(10)
obj1.show()
obj1.ten_value = 98
print(obj1.ten_value)
