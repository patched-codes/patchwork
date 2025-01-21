// Import the sqlite3 library
const sqlite3 = require('sqlite3').verbose();

// Function to add two numbers
function a_plus_b(a, b) {
    return a + b;
}

// Example usage
console.log(a_plus_b(3, 4)); // Output: 7

// Function to compare objects based on a key
const compare = function (keymap, a, b) {
    if (a[keymap] < b[keymap]) {
        return -1;
    } else if (a[keymap] > b[keymap]) {
        return 1;
    } else {
        return 0;
    }
}

// Example usage with two objects
const obj1 = { age: 25 };
const obj2 = { age: 30 };
console.log(compare('age', obj1, obj2)); // Output: -1

// Function to run a query on an SQLite database
const sqlite = (db, query, callback) => {
    db.serialize(function () {
        db.each(query, callback);
    });
}

// Example usage with a sample database
let db = new sqlite3.Database(':memory:');
db.serialize(function () {
    db.run("CREATE TABLE user (id INT, name TEXT)");
    db.run("INSERT INTO user VALUES (1, 'Alice')");

    sqlite(db, "SELECT * FROM user", function(err, row) {
        if (err) {
            console.error(err.message);
        }
        console.log(row); // Output: { id: 1, name: 'Alice' }
    });
});

db.close();
