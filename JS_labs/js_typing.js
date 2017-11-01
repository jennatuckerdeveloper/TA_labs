// console.log("test");

// dynamic function, or function using constructor

let of = new Function("sumA", "sumB", "return sumA + sumB");

console.log(of(4, 5));

// This shows the Function object constructor
// That is a JS global object

console.log (typeof NaN);
console.log(typeof Number.prototype.toFixed);
console.log(typeof Number.prototype.toPrecision);
console.log(typeof Number.prototype.toExponential);
console.log(of.prototype);

// What's a prototype?
// Objects that contain functions and data to make types of objects

