
function highPass(arr, cutoff) {
    let filteredArr = [];
    for (let x = 0; x < arr.length; x++) {
        if (arr[x] > cutoff) {
            filteredArr.push(arr[x]);
        }
    }
    return filteredArr;
}

let result = highPass([6, 8, 3, 10, -2, 5, 9], 5);
console.log(result); // [6, 8, 10, 9]
