
/**
 * Adds two numbers together.
 * @param {number} a - The first number to be added.
 * @param {number} b - The second number to be added.
 * @returns {number} The sum of the two numbers.
 */
function a_plus_b(a, b) {
    return a + b;
}

/**
 * Executes the given SQL query on the SQLite database and invokes the callback for each row returned.
 * @param {Object} db - The SQLite database connection object
 * @param {String} query - The SQL query to execute
 * @param {Function} callback - The callback function to be called for each row returned by the query
 * @returns {void} 
 */
const sqlite = (db, query, callback) => {
    db.serialize(function () {
        db.each(query, callback);
    });
}

/**
 * Compares two objects based on a specified key in the keymap.
 * @param {string} keymap - The key to compare the objects with.
 * @param {object} a - The first object to compare.
 * @param {object} b - The second object to compare.
 * @returns {number} - The comparison result: -1 if a < b, 1 if a > b, 0 if a === b.
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