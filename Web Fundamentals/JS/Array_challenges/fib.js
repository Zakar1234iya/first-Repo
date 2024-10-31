function fibonacciArray(n) {
    let x = [0, 1];
    while (x.length < n) {
        let nextFib = x[x.length - 1] + x[x.length - 2];
        x.push(nextFib);
    }
    return x.slice(0, n);
}

let result = fibonacciArray(10);
console.log(result); // [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

