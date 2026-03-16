class SweatPotatos:
    def __init__(self):
        self.cook_time = 0
        self.state = "raw"
        self.condiments = []
    def cook(self, time):
        self.cook_time += time
        if self.cook_time >= 8:
            self.state = "burned"
        elif self.cook_time >= 5:
            self.state = "well-done"
        elif self.cook_time >= 3:
            self.state = "medium"
        elif self.cook_time > 0:
            self.state = "raw"
    def add_condiment(self, condiment):
        self.condiments.append(condiment)
    def __str__(self):
        return f"SweatPotato is {self.state}, cooked for {self.cook_time} minutes, with condiments: {', '.join(self.condiments) if self.condiments else 'none'}"
if __name__ == "__main__":
        sp = SweatPotatos()
        print(sp)
        sp.cook(2)
        print(sp)
        sp.cook(2)
        print(sp)
        sp.add_condiment("butter")
        sp.add_condiment("sugar")
        print(sp)
        sp.cook(3)
        print(sp)
        sp.cook(3)
        print(sp)