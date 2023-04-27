let listOfRandomNumbers = [];
for (let i = 0; i < 50; i++) {
  listOfRandomNumbers.push(Math.floor(Math.random() * 100) + 1);
}

let listOfNumbers = "";
for(var i = 0; i < listOfRandomNumbers.length; i++) {
    listOfNumbers += i;
}
console.log(listOfNumbers);
