
/**
 * Adds two numbers together.
 * @param {number} a - The first number to add.
 * @param {number} b - The second number to add.
 * @returns {number} The sum of the two numbers.
 */
function a_plus_b(a, b) {
    return a + b;
}

/**
 * Compares two objects based on the values associated with a specified key.
 * @param {string} keymap - The key whose associated values in the objects are to be compared.
 * @param {Object} a - The first object to compare.
 * @param {Object} b - The second object to compare.
 * @returns {number} Returns -1 if the value of `a` is less than the value of `b`, 
 * 1 if the value of `a` is greater than the value of `b`, or 0 if they are equal.
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
 * Executes a query on a SQLite database and processes each result row with a provided callback function.
 * The database connection is operated in serialize mode, ensuring that queries are executed sequentially.
 * 
 * @param {Object} db - The SQLite database connection object.
 * @param {string} query - The SQL query to be executed on the database.
 * @param {Function} callback - The callback function to be executed for each result row from the query.
 */
const sqlite = (db, query, callback) => {
    db.serialize(function () {
        db.each(query, callback);
    });
}