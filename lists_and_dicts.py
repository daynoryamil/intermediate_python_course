def run():
    my_list = [1, "Hello", True, 4.5]
    my_dict = {"firstname":"Daynor", "lastname":"Bautista"}

    super_list = [
        {"firstname":"Daynor", "lastname":"Bautista"},
        {"firstname":"Pame", "lastname":"Perez"},
        {"firstname":"Joel", "lastname":"Conde"},
        {"firstname":"Rosa", "lastname":"Choque"},
        {"firstname":"Mauricio", "lastname":"Bautista"},
    ]

    super_dict ={
        "nautral_nums":[1,2,3,4,5],
        "integer_nums":[-1,-2,0,1,2],
        "floating_nums":[1.1,4.5,6.4]
    }

    print("-Dict-")

    for key, value in super_dict.items():
        print(key, "-",value)
    
    print("-List-")

    for values in super_list:
        for key, value in values.items():
            print(value, end=" ")
        print("", sep="\n")

if __name__ == "__main__":
    run()