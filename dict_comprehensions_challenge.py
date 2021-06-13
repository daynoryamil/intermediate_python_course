import math

def run():
    
    my_dict = {i:round(math.sqrt(i),2) for i in range(1, 1001)}
    print(my_dict)

if __name__ == "__main__":
    run()