_input = "";
process.stdin
  .on("data", input => _input += input)
  .on("end", () => {
    [i, j, k] = _input.trim().split(' ').map( n => parseInt(n));
    count = 0;

    for (var x = i; x <= j; x++) {
      if (Math.abs(x - x.toString().split('').reverse().join('')) % k == 0) {
        count += 1;
      }
    }

    console.log(count);
  }
);
