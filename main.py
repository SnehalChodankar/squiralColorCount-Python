import pandas

data = pandas.read_csv("./2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

data_dict = {}

fur_colors = data["Primary Fur Color"].unique()
fur_colors = fur_colors.tolist()

data_dict["Fur Color"] = fur_colors[1:]
# print(data_dict)
col_count = []

for color in fur_colors[1:]:
    # print(color)
    color_count = data[data["Primary Fur Color"] == color]
    # print(color_count["Primary Fur Color"].count())
    col_count.append(color_count["Primary Fur Color"].count())

# print(col_count)
data_dict["Count"] = col_count
print(data_dict)

new_data = pandas.DataFrame(data_dict)
print(new_data)
new_data.to_csv("./squirrel_count.csv")
