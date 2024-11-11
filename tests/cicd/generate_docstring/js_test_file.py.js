
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
 * Compares two objects based on the specified key and returns a sorting order indicator.
 * This function can be used as a comparator in sorting operations to order objects
 * by a specific property defined in the keymap.
 *
 * @param {string} keymap - The key in the objects that will be used for comparison.
 * @param {Object} a - The first object to compare.
 * @param {Object} b - The second object to compare.
 * @returns {number} A negative number if the property in `a` is less than in `b`, 
 *                   a positive number if it is greater, or zero if they are equal.
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
 * Executes a provided SQL query on a given SQLite database and invokes a callback for each result row.
 * @param {Object} db - The SQLite database connection object.
 * @param {string} query - The SQL query string to be executed.
 * @param {function} callback - The function to be called for each row of the result set. It takes the result row as its argument.
 * @returns {void} This function does not return a value.
 */
const sqlite = (db, query, callback) => {
    db.serialize(function () {
        db.each(query, callback);
    });
}