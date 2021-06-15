def divisors(num):
    divisors = [i for i in range(1, num + 1) if num % i == 0]
    return divisors
    
def run():
    num = input("Insert a number: ")
    assert num.isnumeric() and int(num) > 0, "Debes ingresar solo un número positivo"
    print(divisors(int(num)))
    print("End")

if __name__ == "__main__":
    run()