
/**
 * Computes the sum of two numbers.
 * @param {number} a - The first number to add.
 * @param {number} b - The second number to add.
 * @returns {number} The sum of the two input numbers.
 */
function a_plus_b(a, b) {
    return a + b;
}

/**
 * Compares two objects based on a specified property key and
 * returns an integer indicating their relative order.
 * 
 * @param {string}  keymap - The property key used to compare the objects.
 * @param {Object}  a      - The first object to compare.
 * @param {Object}  b      - The second object to compare.
 * @returns {number} Returns -1 if the value of 'a' is less than 'b'; 
 *                  returns 1 if the value of 'a' is greater than 'b'; 
 *                  returns 0 if they are equal.
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
 * Executes a SQLite query and applies a callback function to each row of the result set.
 * @param {object} db - An instance of the SQLite database to perform operations on.
 * @param {string} query - The SQL query string to be executed.
 * @param {function} callback - The function to be called for each row of the query result.
 */
const sqlite = (db, query, callback) => {
    db.serialize(function () {
        db.each(query, callback);
    });
}