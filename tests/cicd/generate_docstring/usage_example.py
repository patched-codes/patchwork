// Example usage of a_plus_b function
console.log(a_plus_b(2, 3)); // Output: 5

// Usage of compare function to sort an array of objects
const data = [{id: 3}, {id: 1}, {id: 2}];
console.log(data.sort((a, b) => compare('id', a, b))); // Output: [{id: 1}, {id: 2}, {id: 3}]

// Example usage of sqlite function (requires SQLite and Node.js to run)
const sqlite3 = require('sqlite3').verbose();
let db = new sqlite3.Database(':memory:');

db.serialize(() => {
    db.run("CREATE TABLE user (id INT, name TEXT)");
    db.run("INSERT INTO user VALUES (1, 'Alice')");
    db.run("INSERT INTO user VALUES (2, 'Bob')");

    sqlite(db, "SELECT * FROM user", (err, row) => {
        if (err) {
            throw err;
        }
        console.log(row);
    });

    db.close();
});
