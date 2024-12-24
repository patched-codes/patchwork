// Example usage of a_plus_b function
const sum = a_plus_b(5, 3);
console.log('Sum:', sum); // Output: Sum: 8

// Example usage of compare function
const arr = [{ age: 25 }, { age: 30 }];
arr.sort((a, b) => compare('age', a, b));
console.log('Sorted by age:', arr);

// Assume `db` is a sqlite3.Database instance
const db = require('sqlite3').verbose().Database(':memory:'); 
const query = 'SELECT 1';
sqlite(db, query, (err, row) => {
    if (err) throw err;
    console.log('Query result:', row);
});
