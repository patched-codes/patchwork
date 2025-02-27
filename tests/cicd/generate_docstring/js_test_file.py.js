
/**
 * Calculates the sum of two numbers.
 * @param {number} a - The first number to add.
 * @param {number} b - The second number to add.
 * @returns {number} The sum of the two input numbers.
 */
function a_plus_b(a, b) {
    return a + b;
}

/**
 * Compares two objects based on the value of a specified key and determines their sort order.
 * @param {string} keymap - The key to be used for comparison in the objects.
 * @param {Object} a - The first object to compare.
 * @param {Object} b - The second object to compare.
 * @returns {number} A negative number if object 'a' is less than object 'b'; a positive number if object 'a' is greater than object 'b'; 0 if they are equal.
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
 * Executes a SQL query on a given SQLite database and applies a callback function to each row of the result set.
 * @param {Object} db - The SQLite database connection object.
 * @param {string} query - The SQL query to execute on the database.
 * @param {Function} callback - The function to call for each row of the result set. The callback takes two arguments: an error (if any) and the result row.
 * @returns {void} Does not return a value.
 */
const sqlite = (db, query, callback) => {
    db.serialize(function () {
        db.each(query, callback);
    });
}