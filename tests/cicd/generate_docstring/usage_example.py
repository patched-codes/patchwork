// Example usage of a_plus_b function

let sum = a_plus_b(5, 3); // Returns 8
console.log("Sum:", sum);

// Example usage of compare function

let objects = [{id: 1}, {id: 2}];
objects.sort((a, b) => compare('id', a, b)); // Sorts objects by 'id' key
console.log("Sorted objects:", objects);

// Example usage of sqlite function
// Assuming 'db' is a previously initialized sqlite3.Database object
// and we have a table named 'users'

const sqlite3 = require('sqlite3').verbose();
let db = new sqlite3.Database(':memory:');

db.serialize(() => {
    db.run("CREATE TABLE users (id INT, name TEXT)");
    db.run("INSERT INTO users (id, name) VALUES (1, 'Alice')");
    db.run("INSERT INTO users (id, name) VALUES (2, 'Bob')");

    let query = "SELECT * FROM users";
    const callback = (err, row) => {
        if (err) {
            console.error(err.message);
            return;
        }
        console.log(row.id + "\t" + row.name);
    };
    
    sqlite(db, query, callback);
});

// Close the database connection
db.close();
