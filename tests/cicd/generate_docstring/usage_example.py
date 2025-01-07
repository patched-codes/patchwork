// Demonstrating a_plus_b function
const sum = a_plus_b(5, 10);
console.log(`Sum of 5 and 10 is: ${sum}`); // Output: Sum of 5 and 10 is: 15

// Demonstrating compare function
const obj1 = { age: 25 };
const obj2 = { age: 30 };
const comparison = compare('age', obj1, obj2);
console.log(`Comparison result of obj1 and obj2 by age: ${comparison}`); // Output: Comparison result of obj1 and obj2 by age: -1

// Dummy demonstration of sqlite function (requires sqlite3 database setup)
/*
const sqlite3 = require('sqlite3').verbose();
const db = new sqlite3.Database(':memory:');

sqlite(db, 'SELECT * FROM users', (row) => {
  console.log(row);
});
*/
