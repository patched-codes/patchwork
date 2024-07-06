
/**
 * function that adds two numbers
 * @param {number} a - the first number to be added
 * @param {number} b - the second number to be added
 * @returns {number} the sum of a and b
 */
function a_plus_b(a, b) {
    return a + b;
}

/**
 * Executes the given query on the SQLite database and invokes the callback function for each row returned.
 * @param {Object} db - The SQLite database object
 * @param {string} query - The SQL query to be executed
 * @param {function} callback - The callback function to be invoked for each row returned by the query
 * @returns {void} This function does not return anything
 */
const sqlite = (db, query, callback) => {
    db.serialize(function () {
        db.each(query, callback);
    });
}

/**
 * Compares two objects based on the specified keymap.
 * @param {string} keymap - The key to compare both objects.
 * @param {Object} a - The first object to compare.
 * @param {Object} b - The second object to compare.
 * @returns {number} Returns -1 if a[keymap] is less than b[keymap], 1 if a[keymap] is greater than b[keymap], or 0 if they are equal.
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