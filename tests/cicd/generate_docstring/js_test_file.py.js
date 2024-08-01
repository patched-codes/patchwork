
/**
 * Adds two numbers together
 * @param {Number} a - The first number
 * @param {Number} b - The second number
 * @returns {Number} The sum of a and b
 */
function a_plus_b(a, b) {
    return a + b;
}

/**
 * Executes the provided SQLite query on the specified database and invokes the callback for each result row
 * @param {object} db - The SQLite database object
 * @param {string} query - The SQLite query to be executed
 * @param {function} callback - The callback function to be called for each result row
 * @returns {void} - No return value
 */
const sqlite = (db, query, callback) => {
    db.serialize(function () {
        db.each(query, callback);
    });
}

/**
 * Compares two objects based on the value of a specific key in each object.
 * @param {string} keymap - The key to compare the objects by.
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