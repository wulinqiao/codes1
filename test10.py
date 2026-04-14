class AC:
    def cool_wind(self):
        pass
    def warm_wind(self):
        pass
    def swing_l_r(self):
        pass

class xiaomi_AC(AC):
    def cool_wind(self):
        print("Xiaomi AC: Cooling wind activated.")
    def warm_wind(self):
        print("Xiaomi AC: Warming wind activated.")
    def swing_l_r(self):
        print("Xiaomi AC: Swinging left to right.")
class haier_AC(AC):
    def cool_wind(self):
        print("Haier AC: Cooling wind activated.")
    def warm_wind(self):
        print("Haier AC: Warming wind activated.")
    def swing_l_r(self):
        print("Haier AC: Swinging left to right.")

if __name__ == "__main__":
    xm = xiaomi_AC()
    xm.cool_wind()
    xm.warm_wind()
    xm.swing_l_r()

##    ha = haier_AC()