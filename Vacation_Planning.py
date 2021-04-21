def vacation(city, flight_price, hotel_per_day, car_rent):

    total_amount=flight_price+(hotel_per_day * n)+car_rent
    d[city] = total_amount

d = {}


n = int(input("Duration of trip(in days):\n"))

vacation("Paris",200,20,200)
vacation("London",250,30,120)
vacation("Dubai",370,15,80)
vacation("Mumbai",450,10,70)

print(d)