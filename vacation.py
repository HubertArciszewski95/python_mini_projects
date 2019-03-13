""" What program should do
It's a vacation calculator, if you are planning a journey you can do it by using this program
1.counting hotel cost
2.Cost of plane travel, to some cities like Charlotte, Tampa, Pittsburgh, Los Angeles.
3.Cost of renting car with discounnt( one day rent=40$, if you rent for 7 lub more days you will get 50$ discount,
if 3 days or more discount will be 20$)
4. Also program include extra money for spending them on everything we wanted
To print cost of journey type print trip_cost(city, days, extra money)
"""


cities = {"Charlotte": 183, "Tampa": 220, "Pittsburgh": 222, "Los Angeles": 475}


def hotel_cost(nights):
    return 140 * nights


def rental_car_cost(days):
    cost = 40 * days
    if days >= 7:
        cost -= 50
    elif days >= 3:
        cost -= 20
    return cost


def trip_cost(city, days, spending_money):
    return cities[city] + hotel_cost(days) + \
        rental_car_cost(days) + spending_money


while True:
        print(f"You can fly to", [x for x in cities])
        city = input("To which city you want to fly?: ").capitalize()
        if city not in cities:
            print("You choose wrong city. Try again")
        else:
            break


days = int(input("How many days you want to stay?: "))
spending_money = int(input("How much money you want to take with you?: "))

vacation_cost = trip_cost(city, days, spending_money)
print(f"You vacation will cost {vacation_cost}")
