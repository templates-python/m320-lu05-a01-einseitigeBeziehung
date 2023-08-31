class House:
    '''
    Die Klasse gibt einzig den Typ eines Hauses zurück.
    '''

    def __init__(self, name):
        '''
        Legt den Typ des Hauses fest
        '''
        self._type = name

    @property
    def type(self):
        '''
        Liefert den Typ des Hauses
        :return: Typ des Hauses
        '''
        return self._type


class HomeOwner:
    '''
    Ein Hausbesitzer. Er wird durch seinen Namen benannt und kann den Typ seines Hauses bekannt geben
    '''

    def __init__(self, name, house):
        '''
        Erzeugt ein HomeOwnerObjekt mit einem Namen und der Referenz auf sein Haus
        :param name: Name des Hausbesitzer
        :param house: Referenz zum Haus
        '''
        self._name = name
        self._my_house = house  # Der owner erhält die Referenz im Konstruktor geliefert und weist diese zu.

    @property
    def name(self):
        return self._name

    def print(self):
        '''
        gibt die Infos zum Hausbesitzer und seinem Haus aus.
        '''
        print(f'{self._name} besitzt ein {self._my_house.type}')  # Der owner kan die Referenz nutzen.


if __name__ == '__main__':
    house = House('Landhaus')
    owner = HomeOwner('Ron', house)  # Dem owner wird die Referenz zum Haus mitgegeben.
    owner.print()
