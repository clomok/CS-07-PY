def returned_list(first, second):
    return [first, second]

def returned_dict(first, second):
    return {first: second}

def returned_tup(first, second):
    return first, second

def returned_none(first, second):
    res = first + second

def main():
    first_val = input("Enter 1st value: ")
    second_val = input("Enter 2nd value: ")
    list_res = returned_list(first_val, second_val)
    dict_res = returned_dict(first_val, second_val)
    tup_res = returned_tup(first_val, second_val)
    none_res = returned_none(first_val, second_val)
    print(f"{list_res} and the type is {type(list_res)}")
    print(f"{dict_res} and the type is {type(dict_res)}")
    print(f"{tup_res} and the type is {type(tup_res)}")
    print(f"{none_res} and the type is {type(none_res)}")

main()