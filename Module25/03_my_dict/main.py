class MyDict(dict):
    def get(self, key, default=0):
        return super().get(key, default)


def_dict = {0: 'a', 1: 'b', 3: 'c'}

dict_1 = MyDict(def_dict)
print(dict_1.get(1))
