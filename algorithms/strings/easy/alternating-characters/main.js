function processData(input) {
  input = input.trim().split('\n');
  caseCount = parseInt(input[0]);
  for (var i = 1; i <= caseCount; i++) {
    matches = input[i].match(/AA+|BB+/g) || [' '];
    console.log(matches.reduce(function(a,b) {
      return a + (b.length - 1);
    }, 0));
  }
} 

process.stdin.resume();
process.stdin.setEncoding("ascii");
_input = "";
process.stdin.on("data", function (input) {
  _input += input;
});

process.stdin.on("end", function () {
  processData(_input);
});
