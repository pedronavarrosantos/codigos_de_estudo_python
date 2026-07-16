print("Por favor, insira um ano para verificar se é bissexto ou não:")

year = int(input())

def leap_year(year):
    if (year % 4) == 0:
        if (year % 100) == 0:
            if (year % 400) == 0:
                print(f"{year} é um ano bissexto")
            else:
                print(f"{year} não é um ano bissexto")
        print(f"{year} é um ano bissexto")
    else:
        print(f"{year} não é um ano bissexto")

leap_year(year)
