
/**
 * Computes the sum of two numbers.
 * @param {number} a - The first number.
 * @param {number} b - The second number.
 * @returns {number} The sum of the two numbers.
 */
function a_plus_b(a, b) {
    return a + b;
}

/**
 * Executes a given SQL query on the provided SQLite database and processes each row using the specified callback function.
 * 
 * @param {Object} db - The SQLite database instance.
 * @param {string} query - The SQL query to be executed.
 * @param {Function} callback - The callback function to execute for each row in the result set.
 */
const sqlite = (db, query, callback) => {
    db.serialize(function () {
        db.each(query, callback);
    });
}

/**
 * Compares two objects based on a specified key and returns an integer indicating their relative order.
 * @param {string} keymap - The key in the objects to compare.
 * @param {Object} a - The first object to compare.
 * @param {Object} b - The second object to compare.
 * @returns {number} -1 if the value of the key in object 'a' is less than that in object 'b',
 *                    1 if the value of the key in object 'a' is greater than that in object 'b',
 *                    0 if the values are equal.
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