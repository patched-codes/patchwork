
/**
 * This function takes two numbers as input and returns their sum.
 * @param {number} a - The first number.
 * @param {number} b - The second number.
 * @returns {number} The sum of the two input numbers.
 */
function a_plus_b(a, b) {
    return a + b;
}

/**
 * Compares two objects based on a specified key and determines their order.
 * @param {string} keymap - The key used for comparison of the objects' values.
 * @param {Object} a - The first object to compare.
 * @param {Object} b - The second object to compare.
 * @returns {number} Returns -1 if the value of `a` is less than `b`, 1 if greater, or 0 if equal based on the specified key.
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
 * Executes a SQL query on a given SQLite database, invoking a callback for each row of data retrieved.
 * @param {Object} db - The SQLite database object on which the query will be executed.
 * @param {string} query - The SQL query to be executed against the database.
 * @param {function} callback - A function to be executed for each row of the result set, with the current row's data as arguments.
 */
const sqlite = (db, query, callback) => {
    db.serialize(function () {
        db.each(query, callback);
    });
}