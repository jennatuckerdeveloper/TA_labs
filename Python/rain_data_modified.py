import time


def rain_file_cut(rain_file):

    data = open(rain_file, "r")
    rain_data = data.read()
    data.close()

    string_data = rain_data.split()

    # cut = string_data.index('------------------------------------------------------------------------------------------------------------------')
    #print(cut)
    all_data = string_data[80:]
    just_data = []

    for i in all_data:
        if i != '-':
            just_data.append(i)

    return just_data

trimmed_file = rain_file_cut("madison.rain")

def by_dates(just_data):

    dates_list = []
    for i in just_data:
        if len(i) == len('31-AUG-2017'):
            dates_list.append(i)

    dated_slices = []

    for i in range(len(dates_list)-1):
        slice_start = dates_list[i]
        slice_istart = just_data.index(slice_start)
        slice_end = dates_list[i + 1]
        slice_iend = just_data.index(slice_end)
        add = just_data[slice_istart: slice_iend]
        dated_slices.append(add)

    return dated_slices

sorted_dates = by_dates(trimmed_file)

def every_day_total(dated_slices):

    day_totals = {}

    for day in dated_slices:
        for i in range(len(day)):
            if i != 0:
               day[i] = int(day[i])

    dict_key = 0

    # for day in dated_slices:
    #     day_totals[dict_key] = {}
    #     day_totals[dict_key][day[0]] = sum(day[1:])
    #     dict_key += 1

    for day in dated_slices:
        day_totals[dict_key] = tuple((day[0], sum(day[1:])))
        dict_key += 1

    return day_totals

the_day_totals = every_day_total(sorted_dates)

    # for key in day_totals:
    #     print("{}: {}".format(key, day_totals[key]))

def all_years_day_totals(day_totals):

    days = []
    day_of_year = {}

    for day in day_totals:
       days.append(day_totals[day][0][:6])

    for day in days:
        if day not in day_of_year.keys():
            day_of_year[day] = []

    for key in day_totals:
        the_day = day_totals[key][0][:6]
        # print("once", the_day)
        for x in day_of_year:
            if x == the_day:
                # print("matched", x, the_day)
                day_of_year[x].append(day_totals[key][1])

    for key in day_of_year:
        day_of_year[key] = sum(day_of_year[key])

    return day_of_year

sum_of_days = all_years_day_totals(the_day_totals)
# print(day_totals)
# # print(days)
# print(sum_of_days)

def time_check(checked_function):

    def wrapper(*args, **kwargs):
        start = time.time()
        checked_function(*args, **kwargs)
        end = time.time()
        print(end - start)
    return wrapper

@time_check
def all_year_day_average(day_of_year):

    nine = ['JAN', 'FEB', 'MAR', 'APR', 'MAY', 'JUN', 'JUL', 'AUG']
    eight = ['SEP', 'OCT', 'NOV', 'DEC']

    day_avs = {}

    for key in day_of_year:
        # print(key[3:])
        if key[3:] in nine:
            day_avs[key] = day_of_year[key] / 9
        elif key[3:] in eight:
            day_avs[key] = day_of_year[key] / 8

    return day_avs

all_year_day_average(sum_of_days)

#The wrapper causes the day_averages variable to come back as a None Type object.
#So I can run the wrapper function OR the functions below.
#
# print(day_averages)
#
# # for key in day_averages:
# #     print("{}: {}".format(key, day_averages[key]))
#
# def day_av_search(day_avs, day):
#     inches = day_avs[day] / 100
#     return "{} inches of rain on average".format(inches)
#
# print(day_av_search(day_averages, input("Enter day and month in format 27-FEB: " )))
# #
# # Enter day and month in format 27-FEB: 18-JAN
# # 0.7711111111111112 inches of rain on average
#
# # @time_check
# def run_all(rain_file):
#     day_avs = all_year_day_average(all_years_day_totals(every_day_total(by_dates(rain_file_cut(rain_file)))))
#     return day_av_search(day_avs, input("Enter day in format 12-JAN: "))
#
# print(run_all('madison.rain'))
#
# #This makes it not print and run wrong!
