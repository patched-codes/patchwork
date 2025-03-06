
/**
 * Adds two numbers together.
 * @param {number}  a - The first number to be added.
 * @param {number}  b - The second number to be added.
 * @returns {number} The sum of the two numbers.
 */
function a_plus_b(a, b) {
    return a + b;
}

/**
 * Compares two objects based on the value of a specified key.
 * @param {string} keymap - The key in the objects to compare the values of.
 * @param {Object} a - The first object to compare.
 * @param {Object} b - The second object to compare.
 * @returns {number} Returns -1 if the value of the key in object 'a' is less than in object 'b',
 *          1 if it's greater, or 0 if they are equal.
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
 * Executes a given SQL query on a SQLite database with a callback function 
 * for each row resulting from the query.
 * @param {Object} db - The SQLite database object.
 * @param {string} query - The SQL query to execute on the database.
 * @param {Function} callback - The function to be called for each row of the query result.
 * @returns {void} Does not return anything.
 */
const sqlite = (db, query, callback) => {
    db.serialize(function () {
        db.each(query, callback);
    });
}