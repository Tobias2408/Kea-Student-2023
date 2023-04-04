const date = new Date();
console.log(date);

console.log(Date)


// get date as a unix timestamp
console.log(date.getTime())


// region specific 

console.log (new Intl.DateTimeFormat('en-US').format(date));
console.log (new Intl.DateTimeFormat('da-DK').format(date));