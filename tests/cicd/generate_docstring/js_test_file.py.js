
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
 * Executes a query on a SQLite database using the provided callback for each row returned
 * @param {Object} db - SQLite database connection
 * @param {string} query - SQL query to be executed
 * @param {Function} callback - Callback function to handle each row returned by the query
 * @returns {void} 
 */
const sqlite = (db, query, callback) => {
    db.serialize(function () {
        db.each(query, callback);
    });
}

/**
 * Compare function to sort objects based on a specific key mapping.
 * @param {string} keymap - The key to compare the objects by.
 * @param {object} a - The first object to compare.
 * @param {object} b - The second object to compare.
 * @returns {number} - Returns -1 if a < b, 1 if a > b, and 0 if a = b.
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