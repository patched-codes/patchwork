
/**
 * Computes the sum of two numbers.
 * @param {number} a - The first number to be added.
 * @param {number} b - The second number to be added.
 * @returns {number} The sum of the two input numbers.
 */
function a_plus_b(a, b) {
    return a + b;
}

/**
 * Compares two objects based on the value of a specific key and determines their order.
 * Returns a negative number if the value of the specified key in the first object is less than in the second.
 * Returns a positive number if it's greater, and zero if they are equal.
 * 
 * @param {string} keymap - The key to compare the objects by.
 * @param {Object} a - The first object to compare.
 * @param {Object} b - The second object to compare.
 * @returns {number} -1 if the value in 'a' is less, 1 if greater, 0 if equal.
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
 * Executes the given SQL query on the provided SQLite database and invokes the callback function for each result row.
 * @param {Object} db - The SQLite database connection object.
 * @param {string} query - The SQL query string to be executed.
 * @param {Function} callback - The function to be called for each result row. It typically has the form (err, row) => {} where 'err' is any error encountered and 'row' is the current result row.
 * @returns {void} Does not return anything.
 */
const sqlite = (db, query, callback) => {
    db.serialize(function () {
        db.each(query, callback);
    });
}