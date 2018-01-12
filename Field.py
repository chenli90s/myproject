

class Field:

    def __init__(self, *args, **kwargs):

        self.args = args
        self.kwargs = kwargs

    def __getattr__(self, item):
        return self.kwargs[item]


# class TextField(Field):
#
#     pass
#
# class EnumField(Field):
#
#     pass