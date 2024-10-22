function betterThanAverage(arr) {
    var sum = 0;
    let average = sum / arr.length;
    var count = 0;

    for (let i = 0; i < arr.length; i++) {
        sum += arr[i];
    }
    

    for (let z = 0; z < arr.length; z++) {
        if (arr[z] > average) {
            count++;
        }
    }
    return count;
}
var result = betterThanAverage([6, 8, 3, 10, -2, 5, 9]);
console.log(result); // we expect back 4