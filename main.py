"""
Done in 10 min
"""
import random as r


def open_txt(filename = "quotes.txt"):
    list = []
    with open(filename, 'r') as file:
        for i in file.readlines():
            list.append(i[:-1])
    return list


def random(list):
    number = r.choice(list)
    return number


def main():
    response = input("Type 0 to exit the program or type 1 for a quote: ")
    while True:

        if response == "1":
            print(random(open_txt()))
        elif response == "0":
            break
        else:
            print("Try again bro \n")
        response = input("Type 0 to exit the program or type 1 for a quote: ")


if __name__ == "__main__":
    main()