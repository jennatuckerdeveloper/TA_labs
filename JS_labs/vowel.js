/*

<!DOCTYPE html>
<html>
<head>

</head>
<div>Hello World</div>
<label for="letterbox">Enter a letter to check if it's a vowel.</label>
<br>
<input id="letterbox" type="text">
<br>
<input id="submit" type="submit" placeholder="Enter a letter...">
<div id="response"></div>
<script src="vowel.js"></script>
</body>
</html>

*/

var submit = document.getElementById('submit');

submit.onclick = function(){
    var input = document.getElementById('letterbox').value;
    var vowels = "aeiouAEIOU";
    var place = document.getElementById('response');
    if (vowels.indexOf(input) !== -1) {
       place.innerText = "This is a vowel."
    } else {
       place.innerText = "This is not a vowel."
}
};

console.log(/[aeiou]/.test('y')); // false
console.log(/[aeiou]/.test('a')); //true
console.log(/[aeiou]/.test('i')); // true
console.log(/[aeiou]/.test('x')); // false

console.log(/aeiou/.test('i')); // false
console.log(/aeiou/.test('aeiou')); //true
// console.log('aeiou'.test('i'));  // These don't work.
// console.log('aeiou'.test('aeiou')); // These don't work.

// var str = "The best things in life are free";
// var patt = new RegExp("e");
// var res = patt.test(str);
// console.log(res)

var str = "Hello world";
var find = /Hello/g;
var result = find.test(str);
console.log(result);

// RegExpObject.test(string);


