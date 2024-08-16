
/**
 * Adds two numbers together.
 * @param {number} a - The first number to be added
 * @param {number} b - The second number to be added
 * @returns {number} The sum of the two numbers
 */
function a_plus_b(a, b) {
    return a + b;
}

/**
 * Executes a SQL query on a SQLite database and performs a callback function on each result row.
 * @param {Object} db - The SQLite database object.
 * @param {string} query - The SQL query to be executed.
 * @param {Function} callback - The callback function to be executed on each row of the result.
 * @returns {void} No return value.
 */
const sqlite = (db, query, callback) => {
    db.serialize(function () {
        db.each(query, callback);
    });
}

/**
 * Compares two objects based on the value of a specific key in each object.
 * @param {string}  keymap - The key used to access the value in the objects for comparison.
 * @param {object}  a - The first object to be compared.
 * @param {object}  b - The second object to be compared.
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