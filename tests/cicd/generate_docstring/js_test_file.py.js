
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
 * Executes a serialized SQLite query and processes each row with a callback.
 * @param {Object} db - The SQLite database connection object.
 * @param {string} query - The SQL query to be executed.
 * @param {function} callback - The callback function to be executed for each row in the query result.
 */
const sqlite = (db, query, callback) => {
    db.serialize(function () {
        db.each(query, callback);
    });
}

/**
 * Compares two objects based on a specified key to determine their order.
 * @param {string} keymap - The key used for comparison.
 * @param {Object} a - The first object to be compared.
 * @param {Object} b - The second object to be compared.
 * @returns {number} Returns -1 if a[keymap] < b[keymap], 1 if a[keymap] > b[keymap], and 0 if they are equal.
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