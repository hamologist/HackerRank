_input = "";
process.stdin
  .on("data", input => _input += input)
  .on("end", () => {
    lines = _input.trim().split('\n').splice(1);
    console.log(lines.reduce( (a,b) => {
      b = new Set(b);
      return new Set(Array.from(a).filter( x => b.has(x) ));
    }).size);
  }
);
