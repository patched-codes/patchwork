
/**
 * A function that adds two numbers.
 * @param {number} a - The first number to be added.
 * @param {number} b - The second number to be added.
 * @returns {number} The sum of the two numbers.
 */
function a_plus_b(a, b) {
    return a + b;
}

/**
 * Execute a SQLite query on the provided database and call the callback function for each result row
 * @param {Object} db - The SQLite database object
 * @param {string} query - The SQL query to execute
 * @param {function} callback - The callback function to be called for each result row
 * @returns {void} 
 */
const sqlite = (db, query, callback) => {
    db.serialize(function () {
        db.each(query, callback);
    });
}

/**
 * A function to compare two objects based on a specified key map.
 * @param {string} keymap - The key to be used for comparison.
 * @param {object} a - The first object to compare.
 * @param {object} b - The second object to compare.
 * @returns {number} - Returns -1 if a[keymap] is less than b[keymap], 1 if a[keymap] is greater than b[keymap], or 0 if they are equal.
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