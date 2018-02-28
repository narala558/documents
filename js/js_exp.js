// js

const x = 1;


// list the properties of a JavaScript object
var myObject = 'foo';
var keys = Object.keys(myObject);


// determine the class of an object
Object.prototype.toString.call(myObject);


// JavaScript has function scope;
// functions get their own scope but other blocks do not.
if (true){
    var i = 5;
}
i;
// not undefined as you'd expect in a block-scoped language


// closures
// the inner function has access to all the outer function's variables, even after the outer function exits


"This is a string".charAt(0);


"Hello world".substring(0, 5);


"Hello".length;
console.log("Hello".length);

// auto scroll to bottom
var interval = setInterval(function() {window.scrollTo(0,document.body.scrollHeight); }, 1000);
