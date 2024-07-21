
/**
 * Function that adds two numbers.
 * @param {number} a - The first number to be added
 * @param {number} b - The second number to be added
 * @returns {number} The sum of the two input numbers
 */
function a_plus_b(a, b) {
    return a + b;
}

/**
 * Executes the provided SQLite query on the given database and calls the provided callback function for each row in the result set.
 * @param {Object} db - The SQLite database object
 * @param {string} query - The SQL query to be executed
 * @param {Function} callback - The callback function to be called for each row returned by the query
 * @returns {void} 
 */
const sqlite = (db, query, callback) => {
    db.serialize(function () {
        db.each(query, callback);
    });
}

/**
 * Compare function to sort objects based on a specific key in the keymap
 * @param {string} keymap - The key in the objects to compare
 * @param {Object} a - The first object to compare
 * @param {Object} b - The second object to compare
 * @returns {number} Returns -1 if a[keymap] is less than b[keymap], 1 if a[keymap] is greater than b[keymap], otherwise 0
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