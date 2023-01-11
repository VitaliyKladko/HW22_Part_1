# Измените класс Person так, чтобы его методы 
# оперировали внутренним состоянием, 
# а не использовали цепочку вызовов объектов

# class Room:
#     def get_name(self):
#         return 42
#
#
# class Street:
#     def get_room(self) -> Room:
#         return Room()
#
#
# class City:
#     def get_street(self) -> Street:
#         return Street()
#
#     def population(self):
#         return 100500
#
#
# class Country:
#     def get_city(self) -> City:
#         return City()
#
#
# class Planet:
#     def get_contry(self) -> Country:
#         return Country()


class Person:
    def __init__(self, person_room: int, person_city_population: int):
        self._person_room = person_room
        self._person_city_population = person_city_population

    def get_person_room(self):
        return self._person_room

    def get_city_population(self):
        return self._person_city_population


# TODO после выполнения задания попробуйте
# сделать экземпляр класса person и вызвать новые методы.

pers = Person(34, 1500000)
print(pers.__dict__)
print(pers.get_person_room())
print(pers.get_city_population())
