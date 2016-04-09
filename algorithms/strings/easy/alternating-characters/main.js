function processData(input) {
  lines = input.trim().split('\n');
  lines.shift();
  lines.forEach( (line) => {
    matches = line.match(/AA+|BB+/g);
    console.log(matches ? matches.reduce( (a,b) => a + (b.length - 1), 0) : 0);
  });
} 

_input = "";
process.stdin
  .on("data", (input) => _input += input)
  .on("end", () => processData(_input));
