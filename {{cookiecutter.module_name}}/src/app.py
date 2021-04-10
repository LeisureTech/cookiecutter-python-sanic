def how_much_to_pay_by_hour(pay_per_hour, hour_per_day):
    total_hour_per_week = hour_per_day * 7
    return pay_per_hour * total_hour_per_week


def how_much_to_pay(*args):
    result = 0
    for num in args:
        result += num
    return result


def average(*args):
    count = 0
    sum = 0
    for num in args:
        sum += num
        count += 1
    if count == 0:
        return 0
    else:
        return sum/count


RESTAURANT_PER_WEEK = 700
GROCERY_PER_WEEK = 1200

ELECTRICITY = 400
RENT = 9986.43
WATER = 160
WARM = 210
INVESTMENT = 5000
DANISH = 1200


def how_much_to_pay_in_month():

    pay_by_week = how_much_to_pay(RESTAURANT_PER_WEEK, GROCERY_PER_WEEK)

    pay_by_month = how_much_to_pay(ELECTRICITY, RENT, WATER, WARM, INVESTMENT, DANISH)

    return pay_by_week * 4 + pay_by_month


print("How much you must pay by month:", how_much_to_pay_in_month(), "DKK")

def how_much_I_earn_in_month():

    return 24400

print("How much do you save:", how_much_I_earn_in_month() - how_much_to_pay_in_month(), "DKK")