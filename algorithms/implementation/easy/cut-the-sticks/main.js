_input = ""
process.stdin
  .on("data", input => _input += input)
  .on("end", () => {
    test = _input.trim().split('\n')
      .map( x => x.split(' ').map( y => parseInt(y) ) ).splice(1)[0];
    while(test.length) {
      minVal = Math.min.apply(null, test);
      len = test.length;
      test = test.filter( x => (x - minVal) > 0 ? true : false );
      console.log(len);
    }
  }
);
