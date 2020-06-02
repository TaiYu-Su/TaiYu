class Person:
    # 前後皆雙底線是系統函式
    def __init__(self, name, age):
        self.name:str = name
        self.age:int = age

    def greet(self):
        print(f"I'm {self.name}, {self.age} years old.")

    def change_name(self, new_name):
        self.name = new_name

# 繼承: class後面加上(_要繼承的def_)
# 複寫: 直接更改def內容
class ChinesePerson(Person):
    def __init__(self, name, age, zodiac_sign):
        # 拉上一個層級的初始化: super().
        # super().__init__(name, age) # 與下面一樣的結果
        super(ChinesePerson, self).__init__(name, age)
        super().greet()
        # self.name: str = name
        # self.age: int = age
        self.zodiac_sign = zodiac_sign

    def greet(self):
        print(f"我是{self.name}，{self.age}歲，屬{self.zodiac_sign}。")

p1 = Person("Bob", 18)
# p2 = Person("Alice", 20)
p1.greet()
# p2.greet()
# p1.name = "Kevin"
# p1.greet()
# print(p1.name, p1.age)
# print(p2.name, p2.age)
# p1.change_name("Kevin")
# p1.greet()

cp1 = ChinesePerson("張三", 30, "龍")
# print(cp1.name)
cp1.greet()
