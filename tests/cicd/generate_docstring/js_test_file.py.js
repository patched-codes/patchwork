
/**
 * Adds two numbers.
 * @param {number} a - The first number to add.
 * @param {number} b - The second number to add.
 * @returns {number} The sum of the two numbers.
 */
function a_plus_b(a, b) {
    return a + b;
}

/**
 * Executes a provided SQL query on a given SQLite database and applies a callback function to each result row.
 * @param {Object} db - The SQLite database object.
 * @param {string} query - The SQL query to be executed.
 * @param {Function} callback - The function to be called for each row of the result set.
 */
const sqlite = (db, query, callback) => {
    db.serialize(function () {
        db.each(query, callback);
    });
}

/**
 * Compares two objects based on the value of a specified key.
 * 
 * @param {string} keymap - The key on which to compare the objects.
 * @param {Object} a - The first object to compare.
 * @param {Object} b - The second object to compare.
 * @returns {number} Returns -1 if the value of the key in `a` is less than the value of the key in `b`, 
 *                    1 if the value of the key in `a` is greater than the value of the key in `b`, 
 *                    and 0 if the values are equal.
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