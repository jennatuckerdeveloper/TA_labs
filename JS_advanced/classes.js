console.log("classes.js working");

// making an object



let obj1 = {
    x: 12,
    y: 13,
    z: function() {return this.x + this.y}
};

// console.log(obj1);
// console.log(obj1.x, obj1.y, obj1.z());

// making a function to construct objects

// use a global function and use this to assign parameters and methods

// use new Type to instantiate instances

function Friend (name, bday, met, years) {
    this.name = name;
    this.bday = bday;
    this.met = met;
    this.years = years;
    this.happy = function () {
        return "Happy bday " + name + "!"
    };
}

Friend.prototype.greeting = function() {
    alert('Hi! I am' + this.name + '.')
}

let fe = new Friend("Elizabeth", "April 23", "Sep 2008", 13);


// the equivalent of inheritance
// use a global function with all parameters
// use "parent class" name dot "call" with this as first parameter and all inherited parameters
// use this to map other parameters

function Coworker (name, bday, met, job) {
    Friend.call(this, name, bday, met);
    this.job = job;
}


Coworker.prototype = Object.create(Friend.prototype);
Coworker.prototype.constructor = Coworker;

let john = new Coworker ("John", "Dec 5", "July 2016", "Greythorn PH");
console.log(fe);

console.log(typeof(fe));
console.log(fe.happy());
// fe.greeting();


console.log(john);
console.log(john.happy());

// the method property not attached to a parameter was inherited

console.log(Object.getOwnPropertyNames(Friend.prototype));
console.log(Object.getOwnPropertyNames(Coworker.prototype));

console.log(Friend.prototype.greeting);
console.log(Coworker.prototype.greeting);


// john.greeting();


console.log(Object.getOwnPropertyNames(Friend.prototype));
console.log(Object.getOwnPropertyNames(Coworker.prototype));
console.log(">>.", Coworker.prototype.greeting);
console.log(john);

john.greeting();
console.log(Coworker.prototype.constructor);
console.log(john.job);

console.log(Object.getOwnPropertyNames(window));

// I can't figure out why this was a problem when the child had the parent's constructor.
// Somehow, it still did not require the parameter I left out of the parent.
// Somehow, it still included the unique parameter that I passed to the child.
// So WHAT IS constructor?

