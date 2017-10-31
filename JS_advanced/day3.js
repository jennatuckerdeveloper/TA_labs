console.log("day3 working");

/*
Arrow functions do not change this in an object.
 */

/*

1. not-string

Given a string, return a new string where "not " has been added to the front. However, if the string already begins with "not", return the string unchanged.

notString('candy') → 'not candy'
notString('x') → 'not x'
notString('not bad') → 'not bad'

*/

let notString = function(str) {
    if (str.substring(0,3) === "not") {
        return str.substring(4)
    } else {
        return "not " + str
    }
};
//
// console.log(notString("not string")); // string
// console.log(notString("string")); // not string

// startsWith("not") is faster


/*
2. Missing-char

Given a non-empty string and an int n, return a new string where the char at index n has been removed.
The value of n will be a valid index of a char in the original string (i.e. n will be in the range 0..len(str)-1 inclusive).

missingChar('kitten', 1) → 'ktten'
missingChar('kitten', 0) → 'itten'
missingChar('kitten', 4) → 'kittn'
*/

const missingChar = function(str, n) {
    const place = str.charAt(n);
    const changed = str.replace(place, "");
    return changed
};

//This can be collapsed into one line.

// console.log(missingChar('kitten', 1));
// console.log(missingChar('kitten', 0));
// console.log(missingChar('kitten', 4));

const missingCharNick = (s, i) => {
   return s.slice(0, i) + s.slice(i + 1, s.length)
}

// confuses PyCharm

/*

1. makeBricks

We want to make a row of bricks that is goal inches long.
We have a number of small bricks (1 inch each) and big bricks (5 inches each).
Return True if it is possible to make the goal by choosing from the given bricks.
This is a little harder than it looks and can be done without any loops.

See also: Introduction to MakeBricks

eslint-disable no-console
const makeBricks = (small, big, goal) => {}

console.assert(makeBricks(3, 1, 8) === true)
console.assert(makeBricks(3, 1, 9) === false)
console.assert(makeBricks(3, 2, 10) === true)
const makeBricks = (small, big, goal) => {}

*/

const makeBricks = function (smalls, bigs, inches) {
    let bigs_usable = Math.floor(inches / 5);   // 0 or whole positive integer
    let bigs_comparison = bigs - bigs_usable;   // How many bigs do you have compared with how many you could use?
    if (bigs_comparison >= 0) {                 // I have more than enough or just enough big bricks as I could use.
        let smalls_needed = inches - (bigs_usable * 5);
        return (smalls >= smalls_needed)
    } else if (bigs_comparison < 0) {           // I don't have as many bigs as I could use.
        if (bigs > 0) {
            let covered = (bigs * 5);
            let smalls_neeeded = inches - covered;
            return (smalls >= smalls_needed)
        } else {                                // I don't have any big bricks.
            return (smalls >= inches)
        }
    }
};

const makeBricksN = (small, big, goal) => Math.min(big, Math.floor(goal / 5)) * 5 + small >= goal


const makeBricksAlex = function (s, b, g) {
  return g === (new Array(b).fill(5).concat(new Array(s).fill(1))).reduce((length, brick) => length + brick > g ? length : length + brick, 0)
}

// console.log("True tests: ");
// console.log(makeBricks(3, 1, 8)); //true
// console.log(makeBricks(3, 2, 10)); //true
// console.log(makeBricks(4, 3, 13)); //true
// console.log(makeBricks(0, 3, 15)); //true
// console.log(makeBricks(7, 0, 7)); //true
// console.log(makeBricks(5, 5, 14)); //true
// console.log(makeBricks(5, 0, 5)); //true
// console.log(makeBricks(0, 1, 5)); //true
//
//
// console.log("False tests: ");
// console.log(makeBricks(0, 0, 5)); //false
// console.log(makeBricks(4, 2, 17)); //false
// console.log(makeBricks(3, 1, 9)); //false
// console.log(makeBricks(8, 0, 9)); //false
// console.log(makeBricks(0, 5, 9)); //false
/*

Bistromathics:

*/

// console.log("Bistromathics");

const receipt = function (costOfItems, tip) {
    const subtotal = costOfItems.reduce(function(prev, cur) {
        return prev + cur;
    });

    const total = subtotal * (1 + .09 + (tip/100));
    return total.toFixed(2)
};

const bill = receipt([10, 9, 25], 20);


const splitTheBill = function(total, people_array) {
    let split = (total / (people_array.length));
    let base = split.toString();
    let short = base.substring(0,5);
    let short_num = Number(short).toFixed(2);
    console.log(short_num, typeof(short_num));
    let extra_penny = !(base.length === short.length);
    const to_print = [];
    for (person in people_array) {
        if (extra_penny && person === "0") {
            const extra = (split + .01).toFixed(2);
            console.log(extra);
            to_print.push(people_array[0] + " owes $" + extra);
        } else {
            to_print.push(people_array[person] + " owes $" + short_num)
        }
    }
     return to_print
};

console.log(splitTheBill(bill, ["Victoria", "Joseph", "Jessie"]));
console.log(splitTheBill(80.80, ["Victoria", "Joseph", "Jessie"]));
console.log(splitTheBill(69.17, ["Victoria", "Joseph", "Jessie", "Joe"]));
console.log(splitTheBill(80.00, ["Victoria", "Joseph", "Jessie"]));

//This kind of doesn't work when the change comes out to an even two decimal places.
//It gives the first person two extra pennies that could go to the other two.

/*


The Bistromathic Drive is a wonderful new method of crossing vast interstellar
distances without all the dangerous mucking about with Improbability Factors.
Bistromathics itself is simply a revolutionary new way of understanding the
behaviour of numbers. Just as Einstein observed that time was not an absolute
but depended on the observer's movement in space, and that space was not an
absolute, but depended on the observer's movement in time, it is now realised
that numbers are not absolute, but depended on the observer's movement in
restaurants.  -Hitchhiker’s Guide to the Galaxy
In order to fully understand the nature of Bistromathics and come closer to implementing it for our stardrives,
you have been tasked with the following:

Write a function called receipt that:

Takes 1 argument, the subtotal (total cost of the meal, without tax or tip)
Returns the total cost, based on a 9% tax and a 15% tip.
For example:
> receipt(20)
> '$24.80'

Complete these if you have extra time and want to take on a challenge!

Modify your receipt function in the following ways:

Take an additional argument, tip, to specify the percentage of tip to leave. For example, receipt(20, 10) should return 23.8.
Replace the subtotal argument with an array called costsPerItem, which is an array containing the prices for each item ordered in the meal.
Compute the subtotal from the costsPerItem array and calculate the total cost with tax and tip.
Round to the nearest cent.
For example:

> receipt([10, 9, 25], 20)
> '$56.76'

>>>>>UP TO HERE NOW<<<<<

Write a function called splitTheBill that:

Takes 2 arguments, the total cost (i.e. with tax and tip included), and an array of string names (e.g. ["Victoria", "Jessie", "Joseph"])
For each person, returns an item in an array for the amount that they owe in the form of "[name] owes $[money]"
Splits the amount owed per person as evenly as possible among the number of people.
Note that money cannot exceed 2 decimal places (e.g. you cannot have $12.255) and the sum of each part should still add exactly up to the total cost.
For example:

> splitTheBill(122.27, ["Victoria", "Joseph", "Jessie"])

> "Victoria owes $40.76"
. "Joseph owes $40.76"
. "Jessie owes $40.75"

*/

