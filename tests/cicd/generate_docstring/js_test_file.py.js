
/**
 * Adds two numbers together.
 * @param {number} a - The first number to add.
 * @param {number} b - The second number to add.
 * @returns {number} The sum of a and b.
 */
function a_plus_b(a, b) {
    return a + b;
}

/**
 * Executes a SQLite query on the given database
 * @param {Object} db - The SQLite database object
 * @param {string} query - The SQL query to execute
 * @param {Function} callback - The callback function to handle each row of the result
 * @returns {void} This function doesn't return a value
 */
const sqlite = (db, query, callback) => {
    /**
     * Serializes database operations and executes a query for each row
     * @param {string} query - The SQL query to execute
     * @param {function} callback - The function to call for each row returned
     * @returns {undefined} This method doesn't return a value
     */
    
    db.serialize(function () {
        db.each(query, callback);
    });
}

/**
 * Compares two objects based on a specified key
 * @param {string} keymap - The key to use for comparison
 * @param {Object} a - The first object to compare
 * @param {Object} b - The second object to compare
 * @returns {number} -1 if a[keymap] < b[keymap], 1 if a[keymap] > b[keymap], 0 if equal
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