#!/usr/bin/node

function myFunction () {
  let myVar = 'Nick';
  console.log(myVar); // "John"
  myVar = 'juan';
  if (true) {
    let myVar = 'John';
    console.log(myVar); // "John"
    // actually, myVar being function scoped, we just erased the previous myVar value "Nick" for "John"
  }
  console.log(myVar); // "John" - see how the instructions in the if block affected this value
}

myFunction();
//console.log(myVar); // Throws a ReferenceError, myVar is not accessible outside the function.
