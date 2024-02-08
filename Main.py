'''
NAME
    Main

DESCRIPTION
    This module provides a class to search by licence plate prefix or by city

Created on February 5, 2024

@author: Ryan O'Valley
'''

# reads in the montana counties csv
with open("MontanaCounties.csv", "r") as file:
    file.readline()
    lines = file.readlines()
    licensePlates = {}
    for line in lines:
        line = line.strip()
        data = line.split(",")
        prefix = data[2]
        county = data[0]
        countySeat = data[1]
        licensePlates[prefix] = {"county": county, "countySeat": countySeat}

# reads in the montana cities csv
with open("MontanaCities.csv", "r") as file:
    lines = file.readlines()
    cityNames = {}
    for line in lines:
        line = line.strip()
        data = line.split(",")
        cityName = data[0]
        prefix = data[1]
        countyName = data[2]
        cityNames[cityName] = {"prefix": prefix, "county": countyName}


# method to look up county or county seat or both by license plate prefix
def lookupByLicensePlatePrefix(licensePlates):
    while True:
        prefix = input("Enter a license plate prefix or enter 'q' to quit: ")
        if prefix == "q":
            break
        if prefix not in licensePlates:
            print("non-existent prefix")
        else:
            info = input("Do you need the county or county seat or both?")
            if info == "county":
                print("County:")
                print(licensePlates[prefix]["county"])
            elif info == "county seat":
                print("County seat:")
                print(licensePlates[prefix]["countySeat"])
            elif info == "both":
                print("County:")
                print(licensePlates[prefix]["county"])
                print("County Seat:")
                print(licensePlates[prefix]["countySeat"])
            else:
                print("Invalid option")


# method to look up county by city name or append a new city with prefix and county to montana cities
def lookupByCity(cityNames):
    while True:
        cityName = input("Enter the city name or enter 'q' to quit: ")
        cityName = cityName
        if cityName == "q":
            break
        # check to see if the city is in city names and print county
        if cityName in cityNames:
            print("County:")
            print(cityNames[cityName]["county"])
        # check to see if the city name is not in city names and append to csv
        if cityName not in cityNames:
            prefix = input("Enter a prefix: ")
            countyName = input("Enter the county name: ")
            countyName = countyName
            cityNames[cityName] = {"prefix": prefix, "county": countyName}
            with open("MontanaCities.csv", "a") as file:
                file.write(cityName)
                file.write(",")
                file.write(prefix)
                file.write(",")
                file.write(countyName)
                file.write("\n")
            prefix = cityNames[cityName]["prefix"]
            countyName = cityNames[cityName]["county"]
            print("Prefix:")
            print(prefix)
            print("County name:")
            print(countyName)


# method to select witch option you want to use lookup by prefix or by city or quit
def main():
    while True:
        print("0 - quit")
        print("1 - lookup by license plate prefix")
        print("2 - lookup by city")
        userInput = input("Choose an option: ")
        if userInput == "0":
            break
        elif userInput == "1":
            lookupByLicensePlatePrefix(licensePlates)
        elif userInput == "2":
            lookupByCity(cityNames)
        else:
            print("Invalid option")
    print("program has ended")


if __name__ == "__main__":
    main()
