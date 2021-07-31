# 基礎類別（介面）
class Transportation():

    def __init__(self, color, max_tank):
        self.color = color
        self.max_tank = max_tank
        self.tank = 0
    
    def show_color(self):
        print(f"你的車是{self.color}的")

    def change_color(self, color):
        self.color = color
        print(f"車的顏色已經漆成{color}囉")

    def drive(self):
        if self.tank == 0:
            print("油不夠，先去加油吧")
        else:
            self.tank -= 1
            print("駕駛了一段路程")

    def refuel(self):
        self.tank = self.max_tank
        print("把油加滿囉") 
        
# 汽車子類別
class Car(Transportation):
    
    def __init__(self, color="白色", max_tank=20):
        super().__init__(color, max_tank)  # 繼承運輸工具的屬性
        self.door_close = True
        print(f"獲得一台{self.color}的汽車")
    
    def open_door(self):
        self.door_close = False
        print("開車門")
        
    def close_door(self):
        self.door_close = True
        print("關車門")

    def drive(self): # 物件導向的多型運用，當子類別函式與父類別函式名稱相同時，繼承子類別的物件會使用子類別的函式。
        if self.tank == 0:
            print("油不夠了，先去加油吧")
        else:
            if self.door_close:
                self.tank =- 1
                print("駕駛了一段路程")
            else:
                print("門還沒關，不可以危險駕駛！")

# 機車子類別
class Moto(Transportation):

    def __init__(self, color="黑色", max_tank=5):
        super().__init__(color, max_tank) # 繼承運輸工具的屬性
        print(f"獲得一台{self.color}的機車")

    def ralling(self):
        if self.tank < 3:
            print("油不夠，先去加油吧!")
        else:
            self.tank -= 3
            print("跑山去")

# 以下為汽車實例與功能實踐的範例，汽車可以執行所有從交通工具（基礎類別）繼承來的功能，已能執行開關車門的功能，但不能跑山
car1 = Car("銀色")
car1.change_color("綠色")
car1.show_color()
car1.drive()
car1.refuel()
car1.drive()
car1.open_door()
car1.drive()

print("--------------------")

# 以下為機車實例與功能實踐的範例，機車可以執行所有從交通工具（基礎類別）繼承來的功能，也能跑山，但不能開關車門
moto1 = Moto()
moto1.refuel()
moto1.drive()
moto1.ralling()
moto1.ralling()

