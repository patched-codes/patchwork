// Example using a_plus_b
console.log(a_plus_b(5, 3)); // Outputs: 8

// Example using compare
const obj1 = {name: 'Alice'};
const obj2 = {name: 'Bob'};
console.log(compare('name', obj1, obj2)); // Outputs: -1 (since 'Alice' < 'Bob')

// Example using sqlite (Note: requires 'sqlite3' package and a SQLite database setup)
const sqlite3 = require('sqlite3').verbose();
const database = new sqlite3.Database(':memory:');

sqlite(
    database,
    "CREATE TABLE test (info TEXT); INSERT INTO test (info) VALUES ('value1'), ('value2');",
    (err, row) => {
        if (err) { throw err; }
        console.log(row.info); // Outputs: value1, then value2
    }
);
