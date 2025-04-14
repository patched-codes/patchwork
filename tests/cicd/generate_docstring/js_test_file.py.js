
/**
 * Calculates the sum of two numbers.
 * @param {number} a - The first number to be added.
 * @param {number} b - The second number to be added.
 * @returns {number} The sum of the two input numbers.
 */
function a_plus_b(a, b) {
    return a + b;
}

/**
 * Compares two objects based on the values of a specified key and returns a comparison value.
 * @param {string} keymap - The key of the properties in objects 'a' and 'b' to be compared.
 * @param {Object} a - The first object to compare.
 * @param {Object} b - The second object to compare.
 * @returns {number} Returns -1 if the value of object 'a' under the provided key is less than that of object 'b', 
 * 1 if it is greater, or 0 if they are equal.
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
 * Executes a given SQL query on a provided SQLite database and applies a callback to each row of the result.
 * @param {Object} db - The SQLite database object.
 * @param {string} query - The SQL query string to be executed.
 * @param {function} callback - A function that is called for each row of the query result. 
 * @returns {void} This function doesn't return a value.
 */
const sqlite = (db, query, callback) => {
    db.serialize(function () {
        db.each(query, callback);
    });
}