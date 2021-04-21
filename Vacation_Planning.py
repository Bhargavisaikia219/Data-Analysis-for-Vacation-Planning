"""
Q.
You're planning a vacation, and you need to decide which city you want to visit. You have shortlisted four cities and identified the return flight cost, daily hotel cost, and weekly car rental cost. While renting a car, you need to pay for entire weeks, even if you return the car sooner.

City	Return Flight ($)	Hotel per day ($)	Weekly Car Rental ($)
Paris	        200             	20              	200
London	        250	                30              	120
Dubai	        370	                15	                 80
Mumbai	        450	                10	                 70

Answer the following questions using the data above:

1) If you're planning a 1-week long trip, which city should you visit to spend the least amount of money?
2) How does the answer to the previous question change if you change the trip's duration to four days, ten days or two weeks?
3) If your total budget for the trip is $1000, which city should you visit to maximize the duration of your trip? Which city should you visit if you want to minimize the duration?
4) How does the answer to the previous question change if your budget is $600, $2000, or $1500?

"""
def vacation(city, flight_price, hotel_per_day, car_rent):

    total_amount=flight_price+(hotel_per_day * n)+car_rent
    d[city] = total_amount

d = {}


n = int(input("Duration of trip(in days):\n"))

vacation("Paris",200,20,200)
vacation("London",250,30,120)
vacation("Dubai",370,15,80)
vacation("Mumbai",450,10,70)

list1 = list2 = []

for i in d:
    list1=list1+[i]
    list2=list2+[d[i]]
print(list1,list2)


def least_amount():
    for i in range(0, len(list2)):
        if list2[i] == min(list2):
            print("\nYou should visit {} to spend the least amount of money".format(list1[i]))
            list1[i]
#Q.1)
if n==7 :
    least_amount()

#Q.2)
elif n==4 or n==10 or n==14:
    least_amount()

else:
    print("\nInvalid duration entry. Can't calculate for the given entry!!!\n")

