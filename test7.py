class Prentice:
    def __init__(self):
        self.kongfu = '[黑马煎饼果子配方]'
        self.__money = 1000000
    def make_cake(self):
        print(f'使用{self.kongfu}制作煎饼果子') 
    def money(self):
        return self.__money
    def set_money(self, value):
        self.__money = value
class TuSun(Prentice):
    pass
if __name__ == '__main__':
    ts = TuSun()
    ts.make_cake()
    print(ts.money())
    ts.set_money(2000000)
    print(ts.money())