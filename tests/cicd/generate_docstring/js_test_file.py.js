
/**
 * Adds two numbers
 * @param {number} a - The first number to be added
 * @param {number} b - The second number to be added
 * @returns {number} The sum of the two numbers
 */
function a_plus_b(a, b) {
    return a + b;
}

/**
 * Executes a query on a SQLite database
 * @param {Object} db - The SQLite database object
 * @param {string} query - The SQL query to be executed
 * @param {Function} callback - The callback function to handle each row returned by the query
 * @returns {void} 
 */
const sqlite = (db, query, callback) => {
    db.serialize(function () {
        db.each(query, callback);
    });
}

/**
 * Compare function to sort objects based on a specific key in the keymap
 * @param {string} keymap - The key to compare the objects by
 * @param {object} a - The first object to compare
 * @param {object} b - The second object to compare
 * @returns {number} - A negative number if a[keymap] < b[keymap], a positive number if a[keymap] > b[keymap], 0 if equal
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