
/**
 * Adds two numbers together
 * @param {number} a - The first number to be added
 * @param {number} b - The second number to be added
 * @returns {number} The sum of a and b
 */
function a_plus_b(a, b) {
    return a + b;
}

/**
 * Executes a query on a SQLite database
 * @param {Object} db - the SQLite database object
 * @param {string} query - the SQL query to be executed
 * @param {Function} callback - the callback function to handle each row result
 * @returns {void} 
 */
const sqlite = (db, query, callback) => {
    db.serialize(function () {
        db.each(query, callback);
    });
}

/**
 * Compares the values of two objects based on a specified key
 * @param {string} keymap - The key to compare the objects on
 * @param {Object} a - The first object for comparison
 * @param {Object} b - The second object for comparison
 * @returns {number} - Returns -1 if a[keymap] is less than b[keymap], 1 if a[keymap] is greater than b[keymap], or 0 if they are equal
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