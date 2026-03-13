def kiem_tra_key(key, dictionary):
    return key in dictionary
dict_test = {"a": 1, "b": 2}
print(kiem_tra_key("a", dict_test))
print(kiem_tra_key("c", dict_test))