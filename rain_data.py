"""

This version gets doubles, since I did not recognize tha the first column after the date was the total.

# Practice: Rain

The city of Portland has rain gauges that keep track of rainfall.
[A website](http://or.water.usgs.gov/non-usgs/bes/) has text data tables the history of all the daily measurements at these gauges.

It looks like:

```
Daily  Hourly data -->

   Date     Total    0   1
--------------------------
25-MAR-2016     0    0   0
24-MAR-2016     6    0   1
23-MAR-2016     -    -   -
MORE...

```

The amounts are in hundredths of inches or are a `-` if the sensor was broken.

Print out a summary of the data:

* The specific date with the most rain.
* The year with the most rain.

#### Note:
1. The header has a totally different format than the data itself.  You will have to slice out the header lines from all the lines you read.

2. You can split a string by whitespace into a list of strings using `.split()`.

3. Extract the date sting from the date columns.

4. If there are any days with `-` for data, explicitly drop them from your dataset.

5. Avoid using un-named "pairs" outside of dictionaries.

6. If you need to group together individual instances of a date and a rainfall amount use a tuple! ( Or perhaps look at the namedtuple form collections. )

## Advanced

*   Find and print the day of the year with the most rain on average.
    E.g. December 30th has 1" of rain on average.

*   Allow someone to type in a date in the future and, using the average value for that day of the year, predict the amount of rain.

## Super Advanced

* URL open the [main listing website](http://or.water.usgs.gov/non-usgs/bes/).
Parse it and allow the user to select statistics from the available rain gauges.

Python gives you a module called `urllib.request` you can use a function `urllib.request.urlopen(url)` which returns a file-like object.
Look at [the docs](https://docs.python.org/3/library/urllib.request.html#module-urllib.request) for that module.

One little difference is the file-like object doesn't return strings, it returns **bytes**.
The following code snippet reads Pride and Prejudice into a list of strings:

```py
import urllib.request

with urllib.request.urlopen('http://www.gutenberg.org/ebooks/1342.txt.utf-8') as pride_and_prejudice_file:
  lines = [byte_line.decode('utf-8') for byte_line in pride_and_prejudice_file]
```

Read up on using [Pip and PyPI](/notes/py-pip.md) and installing third-party packages.
Use the `beautifulsoup` package to parse the HTML of that page.
You shouldn't hard code in any input other than the listing URL.

"""

data = open("madison.rain", "r")
rain_data = data.read()
data.close()
# print(rain_data)
string_data = rain_data.split()
# print(string_data)
#
cut = string_data.index('------------------------------------------------------------------------------------------------------------------')
# print(cut)
#
all_data = string_data[80:]
just_data = []

for i in all_data:
    if i != '-':
        just_data.append(i)

# for i in just_data:
#     print(i)
start = 0
end = 16
# while end <len(just_data):
#     print(just_data[start:end])
#     start += 16
#     end += 16

dates_list = []
for i in just_data:
    if len(i) == len('31-AUG-2017'):
        dates_list.append(i)
# for i in dates_list:
#     print(dates_list)

dated_slices = []

for i in range(len(dates_list)-1):
    slice_start = dates_list[i]
    slice_istart = just_data.index(slice_start)
    slice_end = dates_list[i + 1]
    slice_iend = just_data.index(slice_end)
    add = just_data[slice_istart: slice_iend]
    dated_slices.append(add)

# for i in dated_slices:
#     print(i)

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

# print(day_totals)

# for key in day_totals:
#     print("{}: {}".format(key, day_totals[key]))

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

# print(day_totals)
# # print(days)
# print(day_of_year)



nine = ['JAN', 'FEB', 'MAR', 'APR', 'MAY', 'JUN', 'JUL', 'AUG']
eight = ['SEP', 'OCT', 'NOV', 'DEC']

day_avs = {}

for key in day_of_year:
    # print(key[3:])
    if key[3:] in nine:
        day_avs[key] = day_of_year[key] / 9
    elif key[3:] in eight:
        day_avs[key] = day_of_year[key] / 8

# print(day_avs)
#
# for key in day_avs:
#     print("{}: {}".format(key, day_avs[key]))

def day_av_search(day):
    inches = day_avs[day] / 100
    return "{} inches of rain on average".format(inches)

print(day_av_search(input("Enter day and month in format 27-FEB: " )))

"""
This currently creates a dictionary with every day's total 
AND a separate dictionary with mon/day total added from across all the years.  So if I divide that, it's the second answer.
"""