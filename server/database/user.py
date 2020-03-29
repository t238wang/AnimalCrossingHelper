from mongoengine import StringField


class User:
    class Hemisphere:
        NORTH = 1
        SOUTH = 2
        def get_values(self):
            return [1, 2]
    sw_id = StringField(required=True)
    hemishpere = IntField(rerquired=True, choices=Hemisphere.get_values())
    name = StringField(required=True)
    island_name = StringField(required=True)
