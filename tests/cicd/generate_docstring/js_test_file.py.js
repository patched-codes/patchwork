
/**
 * Adds two numbers together.
 * @param {number} a - The first number to add.
 * @param {number} b - The second number to add.
 * @returns {number} The sum of the two input numbers.
 */
function a_plus_b(a, b) {
    return a + b;
}

/**
 * Compares two objects based on the values of a specified key.
 * @param {string} keymap - The key used to compare the two objects.
 * @param {Object} a - The first object to compare.
 * @param {Object} b - The second object to compare.
 * @returns {number} -1 if the value of `a[keymap]` is less than `b[keymap]`, 1 if greater, or 0 if they are equal.
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
 * Executes a given SQL query on the provided database and processes
 * each result row using the specified callback function.
 * 
 * @param {Object} db - The database connection object to execute the query on.
 * @param {string} query - The SQL query string to be executed.
 * @param {Function} callback - The function to be called for every row of the query result. 
 *                              Receives each row as an argument.
 * @returns {void}
 */
const sqlite = (db, query, callback) => {
    db.serialize(function () {
        db.each(query, callback);
    });
}