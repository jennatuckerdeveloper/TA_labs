/* # Practice: Rarest

Save your solution in a directory in `practice/` named `rarest`.
Your HTML file should be named `index.html` and your JS file named `site.js` in that directory.

Given an object that maps names to ages, write a function `findRarestValue(obj)` that returns the rarest (least frequently occuring) age.

```js
var namesToAges = {
    'Alyssa': 22,
    'Charley': 25,
    'Dan': 25,
    'Jeff': 20,
    'Kasey': 20,
    'Kim': 20,
    'Morgan': 25,
    'Ryan': 25,
    'Stef': 22
};

// 22 only appears twice; 20 appears three times; 25, four times
findRarestValue(namesToAges);  //> 22
```

## Advanced

Write a function `findRarestKeys(obj)` that returns a list of all the properties with that rarest age.

```js
findRarestKeys(namesToAges);  //> ['Alyssa', 'Stef']
*/

var namesToAges = {
    'Alyssa': 22,
    'Charley': 25,
    'Dan': 25,
    'Jeff': 20,
    'Kasey': 20,
    'Kim': 20,
    'Morgan': 25,
    'Ryan': 25,
    'Stef': 22
};

var findLowestOccurence = function (obj) {
    var vals = Object.values(obj);

    var occurence = {};


    for (var i=0; i < vals.length; i++) {
        if (vals[i] in occurence) {
            occurence[vals[i]] += 1
        } else {
            occurence[vals[i]] = 1
        }
    }
    console.log(occurence);
    var occs = Object.values(occurence);
    occs.sort();
    var lowest_occurence = occs[0];

    for (var key in occurence) {
        if (occurence[key] === lowest_occurence) {
            // console.log("Rarest age " + key);
            var rarest = key;
            }
    }
    return rarest
};

var the_lowest = findLowestOccurence(namesToAges);
console.log(the_lowest);


var whoIsYoungest = function (obj, rarest) {
    var all_youngest = [];
    for (var key in obj) {
        if (obj[key] == rarest) {
            var my_string = (key + " : " + obj[key]);
            console.log(my_string);
            all_youngest.push(my_string);

        }
    }
    return all_youngest
};

var the_youngest = whoIsYoungest(namesToAges, the_lowest);
console.log(the_youngest);



var my_array = [23, 46, 76, 58, 769];
for (var i in my_array) {
    console.log(my_array[i])
}