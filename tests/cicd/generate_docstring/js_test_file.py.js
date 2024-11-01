
/**
 * Computes the sum of two numbers.
 * @param {number} a - The first operand in the sum.
 * @param {number} b - The second operand in the sum.
 * @returns {number} The sum of the two input numbers.
 */
function a_plus_b(a, b) {
    return a + b;
}

/**
 * Compares two objects based on the value of the specified key in a keymap.
 * Returns -1 if the value of the key in object 'a' is less than in object 'b',
 * 1 if greater, and 0 if they are equal.
 * 
 * @param {string} keymap - The key in the objects 'a' and 'b' to compare.
 * @param {Object} a - The first object to compare.
 * @param {Object} b - The second object to compare.
 * @returns {number} Returns -1, 0, or 1 based on the comparison.
 */
const compare = function (keymap, a, b) {
    if (a[keymap] < b[keymap]) {
        return -1;
    } else if (a[keymap] > b[keymap]) {
        return 1;
    } else {
        return 0;
    }
}

/**
 * Executes an SQL query on a SQLite database in serialized mode and processes each row of the result set using a callback function.
 * @param {Object} db - The SQLite database object on which the query will be executed.
 * @param {string} query - The SQL query to be run against the database.
 * @param {Function} callback - The function to be called for each row in the result set. The function receives the row data as an argument.
 * @returns {void} This function does not return a value.
 */
const sqlite = (db, query, callback) => {
    db.serialize(function () {
        db.each(query, callback);
    });
}