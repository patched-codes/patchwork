
/**
 * Adds two numbers and returns the result
 * @param {number} a - The first number to be added
 * @param {number} b - The second number to be added
 * @returns {number} The sum of the two input numbers
 */
function a_plus_b(a, b) {
    return a + b;
}

/**
 * Executes the provided query on the SQLite database
 * @param {Object} db - The SQLite database instance
 * @param {string} query - The SQL query to be executed
 * @param {Function} callback - The callback function to handle each row of the result
 */
const sqlite = (db, query, callback) => {
    db.serialize(function () {
        db.each(query, callback);
    });
}

/**
 * Compares two objects based on a specific key in the keymap.
 * @param {string} keymap - The key in the objects to compare.
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