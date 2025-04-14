
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
 * Compares two objects based on the values of the specified key in each object.
 * Returns -1 if the value from object 'a' is less than the value from object 'b',
 * 1 if it is greater, and 0 if they are equal.
 * 
 * @param {string}  keymap - The key in each object that will be used for comparison.
 * @param {Object}  a - The first object to compare.
 * @param {Object}  b - The second object to compare.
 * @returns {number} Returns -1, 0, or 1 depending on the comparison result.
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
 * Executes a SQL query on a SQLite database and processes each row returned by the query.
 * @param {Object} db - An instance of the SQLite database connection.
 * @param {String} query - The SQL query to be executed.
 * @param {Function} callback - A function to be called for each row of the query's result. 
 *                              The callback is invoked with the row's values as arguments.
 * @returns {undefined} Does not return a value.
 */
const sqlite = (db, query, callback) => {
    db.serialize(function () {
        db.each(query, callback);
    });
}