
/**
 * Function that calculates the sum of two numbers.
 * @param {number}  a - The first number
 * @param {number}  b - The second number
 * @returns {number} The sum of the two numbers
 */
function a_plus_b(a, b) {
    return a + b;
}

/**
 * Execute a given query on a SQLite database and call the specified callback function for each row
 * @param {Object} db - The SQLite database connection
 * @param {String} query - The SQL query to execute
 * @param {Function} callback - The callback function to be called for each row returned by the query
 * @returns {void} - This function does not return anything
 */
const sqlite = (db, query, callback) => {
    db.serialize(function () {
        db.each(query, callback);
    });
}

/**
 * Compares two objects based on the value of a specific key.
 * @param {String} keymap - The key to compare the objects by.
 * @param {Object} a - The first object to compare.
 * @param {Object} b - The second object to compare.
 * @returns {Number} Returns -1 if a[keymap] is less than b[keymap], 1 if a[keymap] is greater than b[keymap], and 0 if they are equal.
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