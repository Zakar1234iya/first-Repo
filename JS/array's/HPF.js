function highPass(arr, cutoff) {
    let filteredArr = [];
    for (let i = 0; i < arr.length; i++) {
        if (arr[i] > cutoff) {
            filteredArr.push(arr[i]);
        }
    }
    return filteredArr;
}

let result = highPass([6, 8, 3, 10, -2, 5, 9], 5);
console.log(result); // [6, 8, 10, 9]
