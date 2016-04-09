_input = "";
process.stdin
  .on('data', input => _input += input )
  .on('end', () => {
    lines = _input.trim().split('\n')
      .map( line => line.split(' ').map( x => parseInt(x) ) );
    n = lines[0][0], k = lines[0][1], prob = lines[1], special = 0, page = 0;
    prob.forEach( x => {
      pages = Math.ceil(x/k);
      for (var i = page+1; i <= page + pages; i++) {
        offset = i - (page+1);
        for (var j = (k*offset)+1; j <= Math.min(x, (k*offset)+k); j++) {
          j == i && special++;
        }
      }
      page += pages;
    });
    console.log(special);
  }
);
