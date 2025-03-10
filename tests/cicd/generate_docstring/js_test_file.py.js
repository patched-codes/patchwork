
/**
 * Returns the summation of two numbers.
 * @param {number} a - The first number to add.
 * @param {number} b - The second number to add.
 * @returns {number} The result of adding a and b.
 */
function a_plus_b(a, b) {
    return a + b;
}

/**
 * Compares two objects based on the value of a specified key.
 * Returns -1 if the value for the key in the first object is less than in the second,
 * 1 if it is greater, and 0 if they are equal.
 * 
 * @param {string} keymap - The key to be used for comparison.
 * @param {Object} a - The first object to compare.
 * @param {Object} b - The second object to compare.
 * @returns {number} Returns -1, 0, or 1, depending on the comparison of the values.
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
 * Executes a provided query on a given SQLite database and invokes a callback for each result row.
 * @param {Object} db - The SQLite database object on which the query will be executed.
 * @param {string} query - The SQL query string to be executed against the database.
 * @param {function} callback - A function to be called for each row of the result set. The function receives the current row as an argument.
 * @returns {void} Does not return a value.
 */
const sqlite = (db, query, callback) => {
    db.serialize(function () {
        db.each(query, callback);
    });
}