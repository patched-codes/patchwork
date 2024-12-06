
/**
 * Calculates the sum of two numbers.
 * @param {number} a - The first number to be added.
 * @param {number} b - The second number to be added.
 * @returns {number} The sum of the two numbers.
 */
function a_plus_b(a, b) {
    return a + b;
}

/**
 * Compares two objects based on the value of a specified key.
 * Returns -1 if the value in object 'a' is less than the value in object 'b',
 *  returns 1 if greater, and returns 0 if they are equal.
 * @param {string} keymap - The key of the objects to compare.
 * @param {Object} a - The first object in the comparison.
 * @param {Object} b - The second object in the comparison.
 * @returns {number} Returns -1, 0, or 1 based on the comparison result.
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
 * Executes a provided SQL query on the given SQLite database instance and 
 * applies a callback function to each row of the result set.
 * @param {object} db - The SQLite database instance on which to execute the query.
 * @param {string} query - The SQL query to be executed on the database.
 * @param {function} callback - The function to be executed for each row of the result set.
 * @returns {void}
 */
const sqlite = (db, query, callback) => {
    db.serialize(function () {
        db.each(query, callback);
    });
}