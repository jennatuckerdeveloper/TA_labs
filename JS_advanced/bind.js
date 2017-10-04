console.log("WORKING");

const myObject = {};
myObject.x = 12;
myObject.y = 13;
myObject.z = function() {return this.x + this.y};
//    console.log(myObject);
const myfunc = myObject.z;
console.log(myfunc());
const myboundfunc = myfunc.bind(myObject);
console.log(myboundfunc());

