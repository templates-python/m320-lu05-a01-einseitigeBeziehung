import pytest
from house_and_owner import House, HomeOwner

class TestHouseOwner:

    @pytest.fixture
    def house(self):
        return House('Landhaus')

    @pytest.fixture
    def owner(self, house):
        return HomeOwner('Ron', house)


    def test_house(self, house):
        assert house.type == 'Landhaus'


    def test_owner(self, owner):
        assert owner.name == 'Ron'


    def test_print(self, owner,  capsys):
       owner.print()
       captured = capsys.readouterr()
       assert captured.out == 'Ron besitzt ein Landhaus\n'

