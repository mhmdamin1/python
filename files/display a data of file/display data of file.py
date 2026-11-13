#mhmd amiin
def file_len(driversdata):
    with open(driversdata) as dd:
        for i, line in enumerate(dd):
            pass
        return i + 1

print("num of drivers in file =  ", file_len("drivers data.txt"))

drivers = {}
with open("drivers data.txt") as f:
    for line in f:
        name, equal_sign,  value = line.split()
        drivers[name] = int(value)
        driver = input("enter driver name: ")
        if driver in drivers:
            print(f"{name} has won the champion for {value} times")
        else:
            print("not founded")


"""
the output:

num of lines in file =   5
enter driver name: hamilton
hamilton has won the champion for 7 times

"""
