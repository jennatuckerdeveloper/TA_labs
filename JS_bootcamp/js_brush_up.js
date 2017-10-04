//an object using literal notation

var dog_daycare  = {
    name: 'BowTown',
    employees: 12,
    capacity: 32,
    optimal_capacity: 20,
    minimum_viable_capacity: 10,
    current_attendees: 28,
    addDog: function () {this.current_attendees = this.current_attendees + 1}
};

// console.log(dog_daycare.name);
dog_daycare.addDog();
// console.log(dog_daycare.current_attendees);

var classroom = {};
classroom.location = 'West Hall';
classroom.capacity = 32;
classroom.accessibility = 'ADA';


classroom.shrink = function(num) {this.capacity = this.capacity - num};

classroom.shrink(4);

// console.log(classroom['location']);

// the properties keys do not need to be put in as strings
// they are called this way using dot notation
/* but they are called as strings using bracket notation */

// the same object fo classroom could be made with constructor notation
// the only difference would be var classroom = new Object()

// a constructor template

function Car(maker, model, mpg) {
    this.maker = maker;
    this.model = model;
    this.mpg = mpg;
    this.mpg_hw = this.mpg * 1.38
}

var CRV = new Car("Honda", "CR-V", 22);
var Accord = new Car("Honda", "Accord", 28);


delete dog_daycare.employees;

var place = document.getElementById('div1');
var loc = window.location;
place.innerHTML = loc;