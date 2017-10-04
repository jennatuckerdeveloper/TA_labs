def fancy_number(number):
    return "({}) {}-{}".format(number[0:3], number[3:6], number[6:10])

# print(fancy_number(input("Enter an 10-digit phone number: ")))

def converter(distance, original, final):
    if original == "mi" and final == "km":
        return int(distance) * 1.60934
    if original == "ft" and final == "mi":
        return int(distance) * 0.000189394

print(converter(input("Enter distance: "), (input("Is this ft or mi? ")), (input("Do you want km or mi? "))))
