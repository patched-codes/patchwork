
/**
 * Calculates the sum of two numbers.
 * @param {number} a - The first number to be added.
 * @param {number} b - The second number to be added.
 * @returns {number} The sum of the two numbers.
 */
function a_plus_b(a, b) {
    return a + b;
}

/**
 * Compares two objects based on the value of a specified property.
 * @param {string} keymap - The property name used for comparison.
 * @param {Object} a - The first object to be compared.
 * @param {Object} b - The second object to be compared.
 * @returns {number} Returns -1 if the value of the specified property in the first object is less than 
 * the second, 1 if it is greater, and 0 if they are equal.
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
 * Executes a SQL query on the provided database using each row as input to the specified callback function.
 * @param {Object} db - The SQLite database instance on which to execute the query.
 * @param {string} query - The SQL query to be executed on the database.
 * @param {Function} callback - The function to be called for each row returned by the query.
 * @returns {void} No return value.
 */
const sqlite = (db, query, callback) => {
    db.serialize(function () {
        db.each(query, callback);
    });
}