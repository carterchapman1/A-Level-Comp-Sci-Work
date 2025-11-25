class Wagon:
    def __init__(self,name):
        self._name = name

    def __str__(self):
        return f'<Wagon : {self._name}>'

class Closed_wagon(Wagon):
    def __init__(self, name):
        super().__init__(name)

class Open_wagon(Wagon):
    def __init__(self, name):
        super().__init__(name)


class Siding:
    def __init__(self):
        self._top_of_wagon = -1
        self._wagon_array = [None] * 30
    
    def push_wagon(self,wagon):
        self._top_of_wagon += 1
        self._wagon_array[self._top_of_wagon] = wagon
    
    def pop_wagon(self):
        if self._top_of_wagon > -1:
            wagon_data = self._wagon_array[self._top_of_wagon]
            self._top_of_wagon -=1
            return wagon_data
        else:
            return 'No Wagons left'
    
    def get_siding_info(self):
        return self._wagon_array[self._top_of_wagon]

class Yard:
    def __init__(self,size:int):
        self.size = [None] * size
    


def testing():
    yard = Yard(5)

    siding = Siding

    wagon1 = Open_wagon('Bob')
    wagon2 = Closed_wagon('Fred')
    wagon3 = Wagon('Thomas')

    

    siding.push_wagon(wagon1)
    siding.push_wagon(wagon2)
    siding.push_wagon(wagon3)
    
    siding.push_wagon(siding.pop_wagon())
    siding.get_siding_info()



print(testing())