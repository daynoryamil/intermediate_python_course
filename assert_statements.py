def divisors(num):
    try:
        if num < 0:
            raise ValueError("Ingresa un número positivo")
        divisors = [i for i in range(1, num + 1) if num % i == 0]
        return divisors
    except ValueError as ve:
        print(ve)
        return False


def run():
    num = input("Insert a number: ")
    assert num.isnumeric(), "Debes ingresar un número"
    print(divisors(int(num)))
    print("End")
   

if __name__ == "__main__":
    run()