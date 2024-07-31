
/**
 * Adds two numbers together.
 * @param {number} a - The first number to be added
 * @param {number} b - The second number to be added
 * @returns {number} The sum of the two numbers
 */
function a_plus_b(a, b) {
    return a + b;
}

/**
 * Executes the provided query on the SQLite database using the given callback function for each result row.
 * @param {Object} db - The SQLite database object to execute the query on.
 * @param {string} query - The SQL query to be executed on the database.
 * @param {function} callback - The callback function to be executed for each result row returned by the query.
 * @returns {void} This function does not return any value.
 */
const sqlite = (db, query, callback) => {
    db.serialize(function () {
        db.each(query, callback);
    });
}

/**
 * Compares two objects based on the specified key in the keymap.
 * @param {string} keymap - The key to compare the objects by.
 * @param {object} a - The first object to compare.
 * @param {object} b - The second object to compare.
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