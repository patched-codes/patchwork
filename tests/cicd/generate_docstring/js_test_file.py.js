
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
 * Compares two objects based on the value of a specified key and determines their order.
 * Returns -1 if the value in the first object is less than the value in the second object,
 * 1 if the value in the first object is greater, or 0 if they are equal.
 * 
 * @param {string} keymap - The key used to access the value to compare within each object.
 * @param {Object} a - The first object to compare.
 * @param {Object} b - The second object to compare.
 * @returns {number} - Returns -1, 0, or 1 based on the comparison.
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
 * Executes a SQL query on the given SQLite database and applies a callback function to each result row.
 * @param {object} db - The SQLite database connection object.
 * @param {string} query - The SQL query string to be executed on the database.
 * @param {function} callback - The callback function to be invoked for each row of the query result. 
 * @returns {void} Executes the query and processes the results via the callback, but does not return any value.
 */
const sqlite = (db, query, callback) => {
    db.serialize(function () {
        db.each(query, callback);
    });
}