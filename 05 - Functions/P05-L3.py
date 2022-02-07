global_var = 5
changed_global_var = 20
print(f"global var initial value is: {global_var}")
print(f"changed global var initial value is: {changed_global_var}")


def local_change():
    global_var = 10
    print(f"Inside function global_var: {global_var}")
    global changed_global_var
    changed_global_var = 30
    print(f"Inside function changed_global_var: {changed_global_var}")

local_change()
print(f"global var final value is: {global_var}")
print(f"changed global var final value is: {changed_global_var}")