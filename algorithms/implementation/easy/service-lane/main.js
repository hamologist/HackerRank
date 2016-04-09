_input = "";
process.stdin
  .on("data", input => _input += input)
  .on("end", () => {
    lines = _input.trim().split('\n')
      .map( line => line.split(' ').map( ele => parseInt(ele) )).splice(1);
    lane = lines.shift();
    lines.forEach( x => console.log(Math.min.apply(null, lane.slice(x[0], x[1]+1))) );
  }
);
