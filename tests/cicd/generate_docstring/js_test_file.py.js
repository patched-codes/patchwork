
/**
 * Function that calculates the sum of two numbers.
 * @param {number} a - The first number
 * @param {number} b - The second number
 * @returns {number} The sum of the two numbers
 */
function a_plus_b(a, b) {
    return a + b;
}

/**
 * Executes a SQLite query on the given database and calls the provided callback function for each result row
 * @param {Object} db - The SQLite database connection
 * @param {string} query - The SQL query to be executed
 * @param {Function} callback - The callback function to be called for each row of the result
 * @returns {void} 
 */
const sqlite = (db, query, callback) => {
    db.serialize(function () {
        db.each(query, callback);
    });
}

/**
 * Compare function to be used for sorting objects based on a specific key in keymap
 * @param {string} keymap - The key in the objects to compare
 * @param {Object} a - The first object to compare
 * @param {Object} b - The second object to compare
 * @returns {number} - Returns -1 if a[keymap] < b[keymap], 1 if a[keymap] > b[keymap], or 0 if equal
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