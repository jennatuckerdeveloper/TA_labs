/*
- *FRONT3
- *STRING-TIMES
- *STRING-BITS
- *STRING-SPLOSION
*/

/*
3. front3

Given a string, we'll say that the front is the first 3 chars of the string.
If the string length is less than 3, the front is whatever is there.
Return a new string which is 3 copies of the front.

front3('Java') → 'JavJavJav'
front3('Chocolate') → 'ChoChoCho'
front3('abc') → 'abcabcabc'

*/

const front3 = function (str) {
    const three = str.substring(0,3);
    return three + three + three
};

console.log(front3('Java'));
console.log(front3('Chocolate'));
console.log(front3('abc') );


/*

4. strinTimes

Given a string and a non-negative int n, return a larger string that is n copies of the original string.

stringTimes('Hi', 2) → 'HiHi'
stringTimes('Hi', 3) → 'HiHiHi'
stringTimes('Hi', 1) → 'Hi'

 */

const stringTimes = function (str, n) {
    let to_return = "";
    for (let i = 0; i < n; i++) {
        to_return = to_return + str
    }
    return to_return
};

console.log(stringTimes('Hi', 2));
console.log(stringTimes('Hi', 3));
console.log(stringTimes('Hi', 1));

const stringTimesP = function (str, n) {
    return Array(n).fill(str).join('')
};

console.log(stringTimesP('Hi', 2));
console.log(stringTimesP('Hi', 3));
console.log(stringTimesP('Hi', 1));


/*

Given a string, return a new string made of every other char starting with the first,
so "Hello" yields "Hlo".

stringBits('Hello') → 'Hlo'
stringBits('Hi') → 'H'
stringBits('Heeololeo') → 'Hello'

 */

const stringBits = function (str) {
    let to_return = '';
    for (i in str) {
        if (i % 2 === 0) {
            to_return = to_return + str[i]
        }
    }
    return to_return
};

console.log(stringBits('Hello'));
console.log(stringBits('Hi'));
console.log(stringBits('Heeololeo'));

const stringBitsN = (string) => {
    let out = '';
    for (let i = 0; i < string.length; i+=2) {
        out += string[i]
    }
    return out
}

const stringBitsP = (string) => {
    return string.split('').filter((c, i) => i % 2 === 0).join()
}

console.log(stringBitsN('Hello'));
console.log(stringBitsN('Hi'));
console.log(stringBitsN('Heeololeo'));

console.log(stringBitsP('Hello'));
console.log(stringBitsP('Hi'));
console.log(stringBitsP('Heeololeo'));

/*

6. stringSplosion

Given a non-empty string like "Code" return a string like "CCoCodCode".

stringSplosion('Code') → 'CCoCodCode'
stringSplosion('abc') → 'aababc'
stringSplosion('ab') → 'aab'

 */

const stringSplosion = function (str) {
    let to_return = '';
    for (let i = 0; i < str.length + 1; i++) {
        to_return = to_return + str.substring(0,i)
    }
    return to_return
};

console.log(stringSplosion('Code'));
console.log(stringSplosion('abc'));
console.log(stringSplosion('ab'));

const stringSplosionN = (string) => {
   return Array(string.length).fill(string).map((v, i) => v.slice(0,i+1)).join("")
}

const stringSplosionP = (string) => {
    return Array(str.length).fill(str).reduce((total, v, i) => total + v.slice(0, i + 1), '')
}

//Study:  forEach, reduce, map, filter
// for i of array
// array.forEach is comparable to for i of
// functional compared with imperative -- functional compared with declarative
// attempt to not mutate data or declare variables

