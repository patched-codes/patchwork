
/**
 * Adds two numbers together.
 * @param {number} a - The first number to be added.
 * @param {number} b - The second number to be added.
 * @returns {number} The sum of the two numbers.
 */
function a_plus_b(a, b) {
    return a + b;
}

/**
 * A function that executes a query on a SQLite database
 * @param {Object} db - The SQLite database object
 * @param {string} query - The SQL query to be executed
 * @param {function} callback - The callback function to handle each row returned by the query
 * @returns {void} This function does not return anything
 */
const sqlite = (db, query, callback) => {
    db.serialize(function () {
        db.each(query, callback);
    });
}

/**
 * Compare function to sort objects based on the value of a specific key
 * @param {string} keymap - The key to compare the objects by
 * @param {Object} a - The first object to compare
 * @param {Object} b - The second object to compare
 * @returns {number} - Returns -1 if a[keymap] is less than b[keymap], 1 if a[keymap] is greater than b[keymap], and 0 if they are equal
 */
const compare= function (keymap, a, b) {
    if (a[keymap] < b[keymap]) {
        return -1;
    } else if (a[keymap] > b[keymap]) {
        return 1;
    } else {
        return 0;
    }
}