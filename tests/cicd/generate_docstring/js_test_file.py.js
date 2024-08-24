
/**
 * This function adds two numbers.
 * @param {number} a - The first number to be added
 * @param {number} b - The second number to be added
 * @returns {number} The sum of the two numbers
 */
function a_plus_b(a, b) {
    return a + b;
}

/**
 * Executes a SQLite query on the provided database and runs the callback function for each row returned.
 * @param {Object} db - The SQLite database connection.
 * @param {string} query - The SQL query to be executed.
 * @param {function} callback - The callback function to handle each row of the result set.
 */
const sqlite = (db, query, callback) => {
    db.serialize(function () {
        db.each(query, callback);
    });
}

/**
 * Compares two objects based on a specified key in the key map.
 * @param {string} keymap - The key to compare the objects by.
 * @param {object} a - The first object to compare.
 * @param {object} b - The second object to compare.
 * @returns {number} - Returns -1 if a[keymap] < b[keymap], 1 if a[keymap] > b[keymap], or 0 if they are equal.
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