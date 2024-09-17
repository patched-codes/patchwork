
/**
 * Adds two numbers together and returns the result.
 * @param {number} a - The first number to add.
 * @param {number} b - The second number to add.
 * @returns {number} The sum of the two input numbers.
 */
function a_plus_b(a, b) {
    return a + b;
}

/**
 * Executes a SQL query on the specified database and processes each row of the result set using a callback function.
 * @param {Object} db - The SQLite database instance on which to execute the query.
 * @param {string} query - The SQL query string to be executed.
 * @param {function} callback - The function to be called for each row in the result set.
 * @returns {void} No return value.
 */
const sqlite = (db, query, callback) => {
    db.serialize(function () {
        db.each(query, callback);
    });
}

/**
 * Compares two objects based on the value of the specified key.
 * @param {String} keymap - The key in the objects to compare by.
 * @param {Object} a - The first object to compare.
 * @param {Object} b - The second object to compare.
 * @returns {Number} Returns -1 if the value of the key in `a` is less than in `b`, 
 *                  1 if the value of the key in `a` is greater than in `b`, 
 *                  and 0 if they are equal.
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