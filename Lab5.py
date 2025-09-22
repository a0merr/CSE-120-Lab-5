import csv
def get_weather(city, month):
    with open('C:/Users/andre/PycharmProjects/PythonProject/weather_temps.csv', mode='r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            if row['City'] == city and row['Month'] == month:
             return row['High'], row['Low']
    return None, None

city = input("Enter the city: ")
month = input("Enter the month: ")
high, low = get_weather(city, month)
if high and low:
    print(f"The average high is {high} and the average low is {low}.")
else:
    print(f"The average  are not available.")
