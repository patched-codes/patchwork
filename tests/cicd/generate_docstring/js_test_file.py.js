
/**
 * Adds two numbers together
 * @param {number} a - The first number
 * @param {number} b - The second number
 * @returns {number} The sum of a and b
 */
function a_plus_b(a, b) {
    return a + b;
}

/**
 * Executes a SQLite query on the provided database
 * @param {Object} db - The SQLite database object
 * @param {string} query - The SQL query to be executed
 * @param {function} callback - The callback function to handle the results of the query
 * @returns {void} This function does not return anything directly, but results are passed to the callback function
 */
const sqlite = (db, query, callback) => {
    db.serialize(function () {
        db.each(query, callback);
    });
}

/**
 * Compares two objects based on a specified key.
 * @param {string} keymap - The key used to access the value for comparison in the objects.
 * @param {object} a - The first object to compare.
 * @param {object} b - The second object to compare.
 * @returns {number} Returns -1 if a < b, 1 if a > b, and 0 if a is equal to b.
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