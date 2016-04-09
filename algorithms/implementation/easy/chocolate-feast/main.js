_input = "";
process.stdin
  .on("data", input => _input += input )
  .on("end", () => {
    lines = _input.trim().split('\n')
      .map( line => line.split(' ').map( x => parseInt(x) ) ).splice(1);
    lines.forEach( line => {
      n = line[0], c = line[1], m = line[2];
      count = n/c|0;
      w = count;
      while(w/m|0) {
        r = w/m|0;
        count += r;
        w = (w + r) - (m * r);
      }
      console.log(count);
    });
  }
);
