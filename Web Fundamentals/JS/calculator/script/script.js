// Function that display value 
function press(val) {
  document.getElementById("display").value += val
}

function myFunction(press) {
  if ((press(0)).key == '0' || (press(1)).key == '1'
    || (press(2)).key == '2' || (press(3)).key == '3'
    || (press(4)).key == '4' || (press(5)).key == '5'
    || (press(6)).key == '6' || (press(7)).key == '7'
    || (press(8)).key == '8' || (press(9)).key == '9'
    || (press('+')).key == '+' || (press('-')).key == '-'
    || (press('*')).key == '*' || (press('/')).key == '/')
    document.getElementById("display").value += press.key;
}

var cal = document.getElementById("calculator");
cal.onkeyup = function (press) {
  if (press.keyCode === 13) {
    console.log("Enter");
    let x = document.getElementById("display").value
    console.log(x);
    solve();
  }
}

// Function that evaluates the digit and return display 
function solve() {
  let x = document.getElementById("display").value
  let y = math.evaluate(x)
  document.getElementById("display").value = y
}

// Function that clear the display 
function clr() {
  document.getElementById("display").value = ""
} 