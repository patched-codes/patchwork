
/**
 * Calculates the sum of two numbers.
 * @param {number} a - The first number to be added.
 * @param {number} b - The second number to be added.
 * @returns {number} The sum of the two given numbers.
 */
function a_plus_b(a, b) {
    return a + b;
}

/**
 * Executes a given SQL query on a serialized SQLite database connection.
 * @param {object}  db - The SQLite database connection object.
 * @param {string}  query - The SQL query to be executed.
 * @param {function} callback - The callback function to be invoked for each row resulting from the query.
 * @returns {void} This function does not return a value.
 */
const sqlite = (db, query, callback) => {
    db.serialize(function () {
        db.each(query, callback);
    });
}

/**
 * Compares two objects based on the value of a specified key.
 * @param {string} keymap - The key to use for comparison.
 * @param {Object} a - The first object to compare.
 * @param {Object} b - The second object to compare.
 * @returns {number} Returns -1 if the value of the key in object 'a' is less than the value of the key in object 'b',
 *          1 if the value of the key in object 'a' is greater than the value of the key in object 'b',
 *          and 0 if both values are equal.
 */
const compare= function (keymap, a, b) {
    if (a[keymap] < b[keymap]) {
        return -1;
    } else if (a[keymap] > b[keymap]) {
        return 1;
    } else {
        return 0;
    }
}