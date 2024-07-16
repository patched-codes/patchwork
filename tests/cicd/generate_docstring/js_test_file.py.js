
/**
 * Adds two numbers together.
 * @param {number} a - The first number
 * @param {number} b - The second number
 * @returns {number} The sum of a and b
 */
function a_plus_b(a, b) {
    return a + b;
}

/**
 * Executes a SQLite query on the database
 * @param {Object} db - The SQLite database object
 * @param {string} query - The SQL query to be executed
 * @param {function} callback - The callback function to handle the results
 * @returns {void} - This function does not return anything
 */
const sqlite = (db, query, callback) => {
    db.serialize(function () {
        db.each(query, callback);
    });
}

/**
 * Compares the values of a specified key in two objects.
 * @param {string} keymap - The key to compare the values of in the objects.
 * @param {object} a - The first object.
 * @param {object} b - The second object.
 * @returns {number} Returns -1 if a[keymap] is less than b[keymap], 1 if a[keymap] is greater than b[keymap], or 0 if they are equal.
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