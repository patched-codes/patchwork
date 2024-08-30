
/**
 * Adds two numbers together.
 * @param {number} a - The first number.
 * @param {number} b - The second number.
 * @returns {number} The sum of the two numbers.
 */
function a_plus_b(a, b) {
    return a + b;
}

/**
 * Executes a SQLite query on the provided database and processes each resulting row using the provided callback function.
 * 
 * @param {object} db - The SQLite database connection object.
 * @param {string} query - The SQL query to execute.
 * @param {function} callback - The callback function to invoke for each row in the query result. The callback receives the arguments (err, row).
 * @returns {void} This function does not return a value.
 */
const sqlite = (db, query, callback) => {
    db.serialize(function () {
        db.each(query, callback);
    });
}

/**
 * Compares two objects based on a specified key and returns the sorting order.
 * @param {string} keymap - The key on which to compare the two objects.
 * @param {Object} a - The first object to be compared.
 * @param {Object} b - The second object to be compared.
 * @returns {number} - Returns -1 if `a[keymap]` is less than `b[keymap]`, 1 if `a[keymap]` is greater than `b[keymap]`, and 0 if they are equal.
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