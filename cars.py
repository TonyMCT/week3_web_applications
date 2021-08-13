#import locale
import json
import sys
#from reports import generate as report
#from emails import generate as email_generate
#from emails import send as email_send

def loadJsonData():
    # Opening JSON file
    f = open('car_sales.json','r')
    data = json.load(f)
    sortdata = sorted(data,key=lambda i: i['total_sales'])
    # Closing file
    f.close()
    return sortdata

def format_car(car):
    return "{} {} ({})".format(car["car_make"], car["car_model"], car["car_year"])

def process_data(data):

    locale.setlocale(locale.LC_ALL, 'en_US.UTF8')
    max_revenue = {"revenue": 0}
    sales = {"total_sales": 0}
    bestCar = {}

    for item in data:
        car_price = float(item['price'].replace('$', ''))
        car_total_sales = float(item['total_sales'])
        car_revenue = car_price * car_total_sales
        if car_revenue > max_revenue["revenue"]:
            item["revenue"] = car_revenue
            max_revenue = item
        if item['total_sales'] > sales["total_sales"]:
            sales = item
        if not item['car']['car_year'] in bestCar.keys():
           bestCar[item['car']['car_year']] = item['total_sales']
        else:
            bestCar[item['car']['car_year']] += item['total_sales']

        bestCarValue = bestCar.values()            
        maxValue= max(bestCarValue)
        maxKey = max(bestCar, key = bestCar.get)

    summaryList = [
        "The {} generated the most revenue: ${}".format(format_car(max_revenue['car']), max_revenue['revenue']),
        "The {} had the most sales: {}".format(sales['car']['car_model'], sales['total_sales']),
        "The most popular year was {} with {} sales.".format(maxKey, maxValue)
    ]
    return summaryList

def carsToTable(carsData):
    tableData = [["ID", "Car", "Price", "Total Sales"]]
    for item in carsData:
        tableData.append([item["id"], format_car(item["car"]), item["price"], item["total_sales"]])
    return tableData

processlist = process_data(loadJsonData())
print(processlist)
