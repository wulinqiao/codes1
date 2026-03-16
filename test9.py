class HeroFighter:
    def power(self):
        return 60
class AdvHeroFighter(HeroFighter):
    def power(self):
        return 80
class EnemyFighter:
    def power(self):
        return 70
def battle(fighter1, fighter2):
    if fighter1.power() > fighter2.power():
        print("Fighter 1 wins!")
    elif fighter1.power() < fighter2.power():
        print("Fighter 2 wins!")
    else:
        print("It's a tie!")
    
if __name__ == "__main__":
    h1 = HeroFighter()
    e1 = EnemyFighter()
    h2 = AdvHeroFighter()
    battle(h1, e1)  # Fighter 2 wins!
    battle(h2, e1)  # Fighter 1 wins!