
/**
 * Function that adds two numbers.
 * @param {number} a - The first number to be added.
 * @param {number} b - The second number to be added.
 * @returns {number} The sum of the two numbers.
 */
function a_plus_b(a, b) {
    return a + b;
}

/**
 * Execute a SQLite query on the provided database.
 * @param {Object} db - The SQLite database object
 * @param {string} query - The SQL query to be executed
 * @param {function} callback - The callback function to handle each row returned by the query
 * @returns {void} This function does not return anything explicitly, the results are handled via the callback function.
 */
const sqlite = (db, query, callback) => {
    db.serialize(function () {
        db.each(query, callback);
    });
}

/**
 * Compares two objects based on a specified key within each object.
 * @param {string} keymap - The key used to retrieve the value for comparison in the objects a and b.
 * @param {object} a - The first object to be compared.
 * @param {object} b - The second object to be compared.
 * @returns {number} Returns -1 if a[keymap] is less than b[keymap], 1 if a[keymap] is greater than b[keymap], and 0 if they are equal.
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