function fibonacciArray(n) {
    let fibArr = [0, 1];
    while (fibArr.length < n) {
        let nextFib = fibArr[fibArr.length - 1] + fibArr[fibArr.length - 2];
        fibArr.push(nextFib);
    }
    return fibArr.slice(0, n);
}

let result = fibonacciArray(10);
console.log(result); // [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

