
class Dragon:   # TODO Написать 3 класса с документацией и аннотацией типов
    def __init__(self, name: str, age: int):

        if not isinstance(name, str):
            raise TypeError("name должен быть объектом типа str")
        self.name = name

        if not isinstance(age, int):
            raise TypeError("age должен быть типом int")
        if age < 0:
            raise ValueError("age не может быть отрицательным")
        self.age = age
    def method_1(self) -> None:
        ...
    def method_11(self) -> None:
        ...



class Planet:
    def __init__(self, name: str, distance: int):

        if not isinstance(name, str):
            raise TypeError("name должен быть объектом типа str")
        self.name = name

        if not isinstance(distance, int):
            raise TypeError("distance должен быть объектом типа int")
        if distance < 0:
            raise ValueError("distance не может быть отрицательным")
        self.distance = distance
    def method_2(self) -> None:
        ...
    def method_22(self) -> None:
        ...

class Art:
    def __init__(self, name: str, square: int):

        if not isinstance(name, str):
            raise TypeError("name должен быть объектом типа str")
        self.name = name

        if not isinstance(square, int):
            raise TypeError("square должен быть объектом типа int")
        if square < 0:
            raise ValueError("square не может быть отрицательным")
        self.square = square
    def method_3(self) -> None:
        ...
    def method_33(self) -> None:
        ...

if __name__ == "__main__":
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    import doctest
    doctest.testmod()
