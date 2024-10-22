function alwaysHungry(arr) {
    let foundFood = false;
    for (let i = 0; i < arr.length; i++) {
        if (arr[i] === "food") {
            console.log("yummy");
            foundFood = true;
        }
    }
    if (!foundFood) {
        console.log("I'm hungry");
    }
}

alwaysHungry([3.14, "food", "pie", true, "food"]); // "yummy", "yummy"
alwaysHungry([4, 1, 5, 7, 2]); // "I'm hungry"
