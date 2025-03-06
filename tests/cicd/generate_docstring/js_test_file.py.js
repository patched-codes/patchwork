
/**
 * Computes the sum of two numbers.
 * @param {number}  a - The first number to add.
 * @param {number}  b - The second number to add.
 * @returns {number} The sum of the two numbers.
 */
function a_plus_b(a, b) {
    return a + b;
}

/**
 * Compares two objects based on the values associated with a specified key.
 * @param {string} keymap - The key based on which the comparison is made.
 * @param {Object} a - The first object to be compared.
 * @param {Object} b - The second object to be compared.
 * @returns {number} Returns -1 if the value corresponding to the key in the first object is less than in the second object, 
 *                      1 if greater, or 0 if they are equal.
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
 * Executes a given SQL query on a SQLite database and processes each result with a callback function.
 * @param {Object} db - The SQLite database instance on which the query will be executed.
 * @param {string} query - The SQL query to be executed on the database.
 * @param {function} callback - The function to be called for each row in the result set of the query.
 * @returns {void} Does not return a value.
 */
const sqlite = (db, query, callback) => {
    db.serialize(function () {
        db.each(query, callback);
    });
}