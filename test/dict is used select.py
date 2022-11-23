
import pytest
class Fruit:
    def __init__(self, name):
        self.name = name
        self.cubed = False

    def cube(self):
        self.cubed = True


class FruitSalad:
    def __init__(self, *fruit_bowl):
        self.fruit = fruit_bowl
        self._cube_fruit()

    def _cube_fruit(self):
        for fruit in self.fruit:
            fruit.cube()


# Arrange
@pytest.fixture
def fruit_bowl():
    return "import pytest"


def test_fruit_salad(self,fruit_bowl):
    # Act
    # 这里接收到fixture函数fruit_bowl的返回值，
    # 也就是[Fruit("apple"), Fruit("banana")]，并使用
    fruit_salad = FruitSalad(*fruit_bowl)

    # Assert
    # python内置函数all()，用于判断给定的可迭代参数 iterable 中的所有元素是否都为 TRUE，
    # 如果是返回 True，否则返回 False
    print([fruit.cubed for fruit in fruit_salad.fruit])
    
    
def test_temp(fruit_bowl):
    return fruit_bowl

def main():
    def test_temp(fruit_bowl):
        return fruit_bowl
main()