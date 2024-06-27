
/**
 * Function to add two numbers.
 * @param {number} a - The first number to be added.
 * @param {number} b - The second number to be added.
 * @returns {number} The sum of the two numbers.
 */
function a_plus_b(a, b) {
    return a + b;
}

/**
 * Executes a SQLite query on the provided database connection and invokes the provided callback function for each row in the result set.
 * @param {Object} db - The SQLite database connection object
 * @param {String} query - The SQLite query to be executed
 * @param {Function} callback - The callback function to be executed for each row in the result set
 */
const sqlite = (db, query, callback) => {
    db.serialize(function () {
        db.each(query, callback);
    });
}

/**
 * Compare function to sort objects based on a specific key in the keymap.
 * @param {String} keymap - The key in the objects to compare.
 * @param {Object} a - The first object to compare.
 * @param {Object} b - The second object to compare.
 * @returns {Number} - Returns -1 if a[keymap] < b[keymap], 1 if a[keymap] > b[keymap], or 0 if they are equal.
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