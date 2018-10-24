#%%

# クラスを作成
class Person:
    # クラス変数(インスタンス毎ではなく、クラス毎で管理)
    count = 0

    # __init__ はコンストラクタ
    def __init__(self,name,age):
        # インスタンスが生成された時にカウントを1増加
        Person.count = Person.count + 1

        self.name = name
        self.age = age

    def getName(self):
        return self.name
    
    def getAge(self):
        return self.age

    # クラスメソッド(インスタンスからではなく、クラスから使う)
    @classmethod
    def getCount(cls): # clsはクラス名をもらう為の引数
        return cls.count

# Personのインスタンスを作成
per1 = Person("河村",26)
per2 = Person("佐藤",24)

print(per1.getName(),"さんは",per1.getAge(),"才です。")
print(per2.getName(),"さんは",per2.getAge(),"才です。")

print("合計人数は",Person.getCount(),"人です。")