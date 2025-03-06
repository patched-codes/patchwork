
/**
 * Adds two numbers and returns the result.
 * @param {number} a - The first number to add.
 * @param {number} b - The second number to add.
 * @returns {number} The sum of the two numbers.
 */
function a_plus_b(a, b) {
    return a + b;
}

/**
 * Compares two objects based on a specific key.
 * It returns -1 if the value of the key in object 'a' is less than in object 'b',
 * 1 if it's greater, and 0 if they are equal.
 * 
 * @param {string} keymap - The key to compare the objects by.
 * @param {Object} a - The first object to compare.
 * @param {Object} b - The second object to compare.
 * @returns {number} A number indicating the relative order of the objects: -1, 0, or 1.
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
 * Executes a SQL query on the given database and calls the callback function for each row in the result set.
 * @param {Object} db - The SQLite database object on which the query is executed.
 * @param {string} query - The SQL query to be executed.
 * @param {Function} callback - The callback function to be executed for each row resulting from the query.
 * @returns {void} Does not return a value.
 */

const sqlite = (db, query, callback) => {
    db.serialize(function () {
        db.each(query, callback);
    });
}