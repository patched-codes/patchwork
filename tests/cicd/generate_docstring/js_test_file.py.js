
/**
 * This function returns the sum of two numbers.
 * @param {number} a - The first number
 * @param {number} b - The second number
 * @returns {number} The sum of the two numbers
 */
function a_plus_b(a, b) {
    return a + b;
}

/**
 * Executes a SQLite query on the provided database and calls a callback function on each row returned by the query.
 * @param {Object} db - The SQLite database object to execute the query on.
 * @param {String} query - The SQL query to be executed on the database.
 * @param {Function} callback - The callback function to be called on each row returned by the query.
 * @returns {void} This function does not return anything directly. Callback function is called on each row result.
 */
const sqlite = (db, query, callback) => {
    db.serialize(function () {
        db.each(query, callback);
    });
}

/**
 * Compares two objects based on a specified key in the object
 * @param {string} keymap - The key to compare objects by
 * @param {object} a - The first object to compare
 * @param {object} b - The second object to compare
 * @returns {number} Returns -1 if a's key value is less than b's key value, 1 if a's key value is greater than b's key value, or 0 if they are equal
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