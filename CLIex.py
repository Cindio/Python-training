import requests
import sys
import json

# TODO: add more exception handling
h_content = {'Content-Type': 'application/json'}
h_close = {'Connection': 'Close'}
reply = requests.get('http://localhost:3000/cars?_sort=id')

key_names = ["id", "brand", "model", "production_year", "convertible"]
key_widths = [10, 15, 10, 20, 15]

def check_server(cid=None):
    addr = "http://localhost:3000/cars"
    if cid:
        addr = "http://localhost:3000/cars/" + cid
    reply = requests.head(addr)
    if reply:
        return True
# when invoked without arguments simply checks if server responds;
# invoked with car ID checks if the ID is present in the database;


def print_menu():
    print("1. List cars")
    print("2. Add new car")
    print("3. Delete car")
    print("4. Update car")
    print("5. Check if brand or model in database")
    print("0. Exit")


def read_user_choice():
    menu_choice = input("Enter your choice: 0...5: ")
    if int(menu_choice) in range(0, 6):
        return menu_choice
    else:
        print("not a valid choice")


def print_header():
    header_string = "VINTAGE CARS DATABASE".center(75)
    hyphen = "-" * 77
    print("+" + hyphen + "+")
    print("|", header_string, "|")
    print("+" + hyphen + "+")
    print()
    for (n, w) in zip(key_names, key_widths):
        upper = n.upper()
        print(upper.ljust(w), end='| ')
    print()

def print_car(car):
    for (n, w) in zip(key_names, key_widths):
        print(str(car[n]).ljust(w), end='| ')
    print()

def list_cars(json):
    print_header()
    if type(json) is list:
        for car in json:
            print_car(car)
    elif type(json) is dict:
        if json:
            print_car(json)
        else:
            print("Database is empty")
    print("\n")


def name_is_valid(name):
    if name.isalpha:
        return True
    elif " " in name and name.isalpha:
        print(f'{name} is valid')
        return True
    else:
        return False


def enter_id():
    car_id = input("Enter ID: ")
    if car_id.isdigit():
        return car_id
    else:
        print("Needs to be an integer number")


def enter_production_year():
    year = input("Enter production year: ")
    if int(year) in range(1900, 2024):
        print(year)
        return year
    else:
        return None


def enter_name():
    what = input("Enter the brand or model: ")
    if name_is_valid(what):
        response = requests.get("http://localhost:3000/cars")
        cars_list = response.json()
        counter = 0
        for item in cars_list:
            item_dic = item
            item_values = item_dic.values()
            if what in item_values:
                counter += 1
        print(f'{what} is in the database', counter, "time/s")
    else:
        return None


def enter_convertible():
    convertible = input("Enter y if it is a convertible, otherwise enter n: ")
    print(convertible)
    if convertible == "y":
        convertible = True
        return convertible
    if convertible == "n":
        convertible = False
        return convertible
    else:
        return None


def delete_car():
    menu_delete = input("Input ID to delete: ")
    addr = "http://localhost:3000/cars/" + menu_delete
    response = requests.delete(addr)
    if response.status_code == requests.codes.ok:
        print("Received a positive response from the server.")
    else:
        print("The server response was negative, sorry.")
    requests.get("http://localhost:3000/cars")


def input_car_data():
    car_id = enter_id()
    if car_id:
        brand = input("Enter brand: ")
        if name_is_valid(brand):
            model = input("Enter model: ")
            if name_is_valid(model):
                prod_year = enter_production_year()
        convert = enter_convertible()
        car = {'id': car_id, 'brand': brand, 'model': model, 'production_year': prod_year, 'convertible': convert}
        return car
    else:
        return None


def add_car():
    car = input_car_data()
    response = requests.post("http://localhost:3000/cars", headers=h_content, json=car)
    response = requests.get("http://localhost:3000/cars")


def update_car():
    update_id = enter_id()
    addr = "http://localhost:3000/cars/" + update_id
    response = requests.get(addr)
    if response:
        print("The car does exist. So now you will enter all data, including new")
        change_car = input_car_data()
        addr = "http://localhost:3000/cars/" + update_id
        response = requests.put(addr, headers=h_content, json=change_car)
        response = requests.get("http://localhost:3000/cars")


while True:
    if not check_server():
        print("Server is not responding - quitting!")
        exit(1)
    print_menu()
    choice = read_user_choice()
    if choice == '0':
        print("Bye!")
        exit(0)
    elif choice == '1':
        list_cars(reply.json())
    elif choice == '2':
        add_car()
    elif choice == '3':
        delete_car()
    elif choice == '4':
        update_car()
    elif choice == '5':
        enter_name()
