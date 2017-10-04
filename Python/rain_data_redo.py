def get_rain_file(file_name):

    data = open(file_name, "r")
    rain_data = data.readlines()
    data.close()

    no_intro = rain_data[11:]

    just_data = []

    for line in no_intro:
        just_data.append(line.split())

    day_totals = []

    for line in just_data:
        day_totals.append(tuple([line[0], line[1]]))

    return day_totals

day_totals = get_rain_file("madison.rain")
# for line in day_totals:
#     print(line)

def check_day(day):
    for line in day_totals:
        if line[0] == day:
            return "{} had {} inches of rain.".format(line[0], (int(line[1]) / 100))
#
# print(check_day(input("Enter day in format 12-DEC-2009: ")))

def day_with_most_rain():
    rainfall = []
    for line in day_totals:
        if line[1] != '-':
            rainfall.append(int(line[1]))
    # print(rainfall)
    most = max(rainfall)
    # print(most)
    for line in day_totals:
        if int(line[1]) == most:
            return "{} had the most rain at {} inches".format(line[0], int(line[1]) / 100)

print(day_with_most_rain())


def year_with_most_rain():
    year_totals = {}
    for i in day_totals:
        rain = i[1]
        if rain != '-':
            number = int(i[1])
        if i[0][-4:] not in year_totals:
            year_totals[i[0][-4:]] = number
        else:
            year_totals[i[0][-4:]] += number
    values = []
    for i in year_totals.values():
        values.append(i)
    most = max(values)
    for i in year_totals:
        if year_totals[i] == most:
            return "{} had the most rain with {} inches".format(i, year_totals[i] / 100)

print(year_with_most_rain())


def create_day_averages(day_totals):

    day_averages = {}
    times_counted = {}

    for i in day_totals:
        rainfall = i[1]
        if rainfall != '-':
            number = int(rainfall)
        if i[0][:6] not in day_averages:
            day_averages[i[0][:6]] = number
            times_counted[i[0][:6]] = 1
        else:# i[0][:6] in day_averages:
            day_averages[i[0][:6]] += number
            times_counted[i[0][:6]] += 1
    return day_averages, times_counted

day_averages, times_counted = create_day_averages(day_totals)

# #
# for key in day_averages:
#     print(key, day_averages[key])

# for key in times_counted:
#     print(key, times_counted[key])

def find_day_average(day):
    for key in day_averages:
        if key == day:
            # print(day_averages[day], times_counted[day])
            result = int(day_averages[day]) / int(times_counted[day])
    return "{}: {} inches.".format(day, result / 100)
#
print(find_day_average(input("To get the average for a day, enter a date in format 12-MAY: ")))

def wettest_day():
    averages = []
    for i in day_averages.values():
        # print(i)
        averages.append(i)
    most = max(averages)
    for i in day_averages:
        if day_averages[i] == most:
            # return day_averages[i]
            return "{} was the wettest day with an average of {} inches.".format(i, day_averages[i] / times_counted[i] / 100)

print(wettest_day())

