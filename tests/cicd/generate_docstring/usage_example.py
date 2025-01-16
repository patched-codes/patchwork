// Function that adds two numbers
function a_plus_b(a, b) {
    return a + b;
}

console.log(a_plus_b(3, 4)); // Output: 7

// Function to compare two items based on a specific property
const compare = function (keymap, a, b) {
    if (a[keymap] < b[keymap]) {
        return -1;
    } else if (a[keymap] > b[keymap]) {
        return 1;
    } else {
        return 0;
    }
}

const obj1 = { age: 30 };
const obj2 = { age: 25 };

console.log(compare('age', obj1, obj2)); // Output: 1

// Function to execute a SQL query using SQLite
const sqlite = (db, query, callback) => {
    db.serialize(function () {
        db.each(query, callback);
    });
}

// Example usage of `sqlite` is context-dependent (requires a database connection)
