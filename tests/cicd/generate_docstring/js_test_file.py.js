
/**
 * Calculates and returns the sum of two numbers.
 * @param {number} a - The first number to be added.
 * @param {number} b - The second number to be added.
 * @returns {number} The sum of the two numbers.
 */
function a_plus_b(a, b) {
    return a + b;
}

/**
 * Compares two objects based on the value of a specified key and returns a numerical value indicating their relative order.
 * @param {string} keymap - The key in the objects 'a' and 'b' that will be used for comparison.
 * @param {Object} a - The first object to be compared.
 * @param {Object} b - The second object to be compared.
 * @returns {number} A negative value if the value in 'a' is less than in 'b', a positive value if greater, and 0 if they are equal.
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
 * Executes a SQL query on the provided database connection and processes each row with the callback function.
 * 
 * @param {Object} db - The SQLite database connection object.
 * @param {string} query - The SQL query to execute on the database.
 * @param {Function} callback - The function that will be called for each row of the result set.
 */
const sqlite = (db, query, callback) => {
    db.serialize(function () {
        db.each(query, callback);
    });
}