class Person:

    def __init__(self,first_name):
        self._first_name = first_name

    # Getter Function
    @property
    def first_name(self):
        return self._first_name

    # Setter Function
    @first_name.setter
    def first_name(self,value):
        if not isinstance(value,str):
            raise ValueError(f'Expected a string,{value} given.')
        else:
            self._first_name = value

    # Deleter Function(optional)
    @first_name.deleter
    def first_name(self):
        raise AttributeError("Can't delete Attribute.")


    # Creating Instance
p1 = Person('John')

print(p1.first_name)


