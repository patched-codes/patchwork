
/**
 * Function that returns the sum of two numbers.
 * @param {number} a - The first number
 * @param {number} b - The second number
 * @returns {number} The sum of the two numbers
 */
function a_plus_b(a, b) {
    return a + b;
}

/**
 * Executes a SQLite query on the provided database and invokes the specified callback for each row returned.
 * @param {Object} db - The SQLite database object
 * @param {string} query - The SQLite query to be executed
 * @param {function} callback - The callback function to be invoked for each row returned by the query
 * @returns {void} 
 */
const sqlite = (db, query, callback) => {
    db.serialize(function () {
        db.each(query, callback);
    });
}

/**
 * Compare function to use with Array.prototype.sort() to sort an array of objects based on a specific key.
 * @param {String} keymap - The key to compare in the objects
 * @param {Object} a - The first object to be compared
 * @param {Object} b - The second object to be compared
 * @returns {Number} - Negative if a[keymap] is less than b[keymap], positive if a[keymap] is greater than b[keymap], 0 if they are equal
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