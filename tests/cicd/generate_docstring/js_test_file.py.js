
/**
 * Calculates the sum of two numbers.
 * @param {number}  a - The first number to be added.
 * @param {number}  b - The second number to be added.
 * @returns {number} The sum of the two numbers.
 */
function a_plus_b(a, b) {
    return a + b;
}

/**
 * Compares two objects based on the value of a specified key.
 * This function returns -1, 1, or 0 if the value of the given key in the first object
 * is less than, greater than, or equal to the value of the key in the second object, respectively.
 * @param {string} keymap - The key used to extract comparison values from the objects.
 * @param {Object} a - The first object for comparison.
 * @param {Object} b - The second object for comparison.
 * @returns {number} A number indicating the relative order of the objects based on the key's value.
 *                    Returns -1 if the value of key in `a` is less than in `b`, 
 *                    1 if greater, and 0 if they are equal.
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
 * Executes a SQL query on a database using the serialize method and iterates over each row in the result set.
 * @param {Object} db - The database connection object to execute the query on.
 * @param {string} query - The SQL query to be executed on the database.
 * @param {function} callback - The callback function to be executed for each row in the result set. 
 */
const sqlite = (db, query, callback) => {
    db.serialize(function () {
        db.each(query, callback);
    });
}