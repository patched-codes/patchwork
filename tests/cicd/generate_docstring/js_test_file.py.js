
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
 * Execute a SQLite query on the given database
 * @param {Object} db - Database connection object
 * @param {string} query - The SQLite query to be executed
 * @param {function} callback - The callback function to handle each row of the result
 */
const sqlite = (db, query, callback) => {
    db.serialize(function () {
        db.each(query, callback);
    });
}

/**
 * Compare function to sort objects based on the value of a specified key
 * @param {string} keymap - The key to compare the objects by
 * @param {Object} a - The first object to compare
 * @param {Object} b - The second object to compare
 * @returns {number} Returns -1 if a[keymap] < b[keymap], 1 if a[keymap] > b[keymap], and 0 if they are equal
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