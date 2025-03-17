
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
 * Compares two objects based on a specified key and returns an ordering value.
 * @param {string} keymap - The key in the objects to compare them by.
 * @param {Object} a - The first object to compare.
 * @param {Object} b - The second object to compare.
 * @returns {number} Returns -1 if object 'a' is less than object 'b', 1 if object 'a' is greater than object 'b', and 0 if they are equal based on the specified key.
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
 * Executes a SQL query on the provided SQLite database with a callback for each row retrieved.
 * This function uses the database's serialize method to ensure that the execution of
 * queries occurs sequentially.
 * 
 * @param {Object}  db - The SQLite database object to execute the query on.
 * @param {string}  query - The SQL query string to be executed.
 * @param {function} callback - The callback function to be called for each row in the result set.
 * @returns {void} No return value.
 */
const sqlite = (db, query, callback) => {
    db.serialize(function () {
        db.each(query, callback);
    });
}