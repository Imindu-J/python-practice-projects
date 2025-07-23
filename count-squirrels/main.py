import pandas


data = pandas.read_csv("004 2018-Central-Park-Squirrel-Census-Squirrel-Data.csv")

fur_color = data["Primary Fur Color"]

gray_count = len(data[fur_color == "Gray"])
cinnamon_count = len(data[fur_color == "Cinnamon"])
black_count = len(data[fur_color == "Black"])

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [gray_count, cinnamon_count, black_count]
}

new_data = pandas.DataFrame(data_dict)
new_data.to_csv("squirrel_count.csv")
