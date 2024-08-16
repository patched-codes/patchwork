
/**
 * Calculates the sum of two numbers.
 * @param {number} a - The first number for addition
 * @param {number} b - The second number for addition
 * @returns {number} The sum of the two numbers
 */
function a_plus_b(a, b) {
    return a + b;
}

/**
 * Execute given query on the SQLite database and call the specified callback for each row.
 * @param {Object}  db - The SQLite database object
 * @param {string}  query - The SQL query to be executed
 * @param {Function} callback - The callback function to be called for each row
 * @returns {void} This function does not return anything
 */
const sqlite = (db, query, callback) => {
    db.serialize(function () {
        db.each(query, callback);
    });
}

/**
 * Compares two objects based on a specified keymap.
 * @param {string} keymap - The key to compare the objects.
 * @param {object} a - The first object to compare.
 * @param {object} b - The second object to compare.
 * @returns {number} - Returns -1 if a[keymap] is less than b[keymap], 1 if a[keymap] is greater than b[keymap], 0 if they are equal.
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