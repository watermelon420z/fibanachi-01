
def main():
    num = int(input("Введите число: "))
    print(fibonachi(num))

def fibonachi(num):
    Ni = 1
    N_i = 0

    while(num > 1):
        N_temp = Ni
        Ni += N_i
        N_i = N_temp
        num -= 1
    return Ni

if __name__ == '__main__':
    main()
