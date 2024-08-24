
/**
 * Adds two numbers together.
 * @param {number}  a - The first number to be added.
 * @param {number}  b - The second number to be added.
 * @returns {number} The sum of a and b.
 */
function a_plus_b(a, b) {
    return a + b;
}

/**
 * A function that runs a SQLite query on the provided database and invokes the callback for each row returned.
 * @param {Object} db - The SQLite database instance
 * @param {string} query - The SQLite query to be executed
 * @param {function} callback - The callback function to be invoked for each row returned by the query
 * @returns {void} This function does not return anything
 */

const sqlite = (db, query, callback) => {
    db.serialize(function () {
        db.each(query, callback);
    });
}

/**
 * Compares two objects based on a specified key in the objects.
 * @param {string} keymap - The key to compare the objects by.
 * @param {object} a - The first object to compare.
 * @param {object} b - The second object to compare.
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