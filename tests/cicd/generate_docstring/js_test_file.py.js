
/**
 * Adds two numbers together.
 * @param {number} a - The first number to add.
 * @param {number} b - The second number to add.
 * @returns {number} The sum of the two numbers.
 */
function a_plus_b(a, b) {
    return a + b;
}

/**
 * Compares two objects based on the values associated with a specified key.
 * @param {string} keymap - The key used to compare the two objects.
 * @param {Object} a - The first object to compare.
 * @param {Object} b - The second object to compare.
 * @returns {number} Returns -1 if the value associated with the key in object 'a' is less than that in object 'b', 
 * 1 if greater, and 0 if they are equal.
 */
const compare = function (keymap, a, b) {
    if (a[keymap] < b[keymap]) {
        return -1;
    } else if (a[keymap] > b[keymap]) {
        return 1;
    } else {
        return 0;
    }
}

/**
 * Executes an SQLite query for each row in the result set and applies a callback function.
 * @param {Object} db - The SQLite database connection object.
 * @param {string} query - The SQL query to be executed.
 * @param {Function} callback - The function to be called for each row, with parameters (err, row).
 */
const sqlite = (db, query, callback) => {
    db.serialize(function () {
        db.each(query, callback);
    });
}