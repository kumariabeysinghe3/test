# calculate a user’s total holiday cost, which includes the plane cost, hotel cost, and car rental cost
#ask user the city they are flying to, number of nights and rental days and store input
city_flight = input("Please enter the city you are flying to from the following options: Australia, New York, London or Spain: ")
num_nights = int(input("Please enter the number of nights you will be staying at the hotel: "))
rental_days = int(input("Please enter the number of days you will be renting a car: "))

#calculate hotel cost:
def hotel_cost(num_nights):
    #calculate hotel total cost which is number of nights multiplied by $60 per night
    return num_nights * 60 

#calculate plane cost:
def plane_cost(city_flight):
    #calculate plane cost based on city: 
    if city_flight == "Australia":
        return 1000
    elif city_flight == "New York":
        return 700
    elif city_flight == "London":
        return 500
    elif city_flight == "Spain":
        return 400
    else:
        print("Please enter a city from the options")
    return plane_cost 

#calculate total car rental cost:
def car_rental(rental_days):
    #calculate car rental by rental days multiplied by $50 per day 
    return rental_days * 50 

#using the functions above, calculate the total holiday cost and print the results
def holiday_cost(num_nights, city_flight, rental_days):
    total = hotel_cost(num_nights) + plane_cost(city_flight) + car_rental(rental_days)
    return total

#calculate total 
total= holiday_cost(num_nights, city_flight, rental_days)

#print all holiday details
print ("\nHOLIDAY SUMMARY")
print(f"\nCity: {city_flight}")
print(f"\nHotel nights and cost: {num_nights},${hotel_cost(num_nights)}")
print(f"\nCar rental days and cost: {rental_days},${car_rental(rental_days)}")
print(f"\nFlight cost: ${plane_cost(city_flight)}")
print(f"\nTotal holiday cost: ${total}")