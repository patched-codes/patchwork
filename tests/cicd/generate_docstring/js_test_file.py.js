
/**
 * Computes the addition of two numbers.
 * @param {number} a - The first number to be added.
 * @param {number} b - The second number to be added.
 * @returns {number} The sum of the two input numbers.
 */
function a_plus_b(a, b) {
    return a + b;
}

/**
 * Compares two objects based on the value of a specified key and returns an integer 
 * indicating their relative order in the sort. It returns -1 if the first object's key 
 * value is less than the second; 1 if greater; and 0 if they are equal.
 * 
 * @param {string} keymap - The key on which the comparison is made.
 * @param {Object} a - The first object to compare.
 * @param {Object} b - The second object to compare.
 * @returns {number} -1 if `a[keymap]` is less than `b[keymap]`, 1 if `a[keymap]` is 
 * greater than `b[keymap]`, and 0 if they are equal.
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
 * Executes a provided SQL query on the specified SQLite database and processes each row using the provided callback function.
 * @param {Object} db - The SQLite database object on which the query will be executed.
 * @param {string} query - The SQL query to be executed on the database.
 * @param {function} callback - The function to be called for each row of the result set, receiving the database row as an argument.
 */
const sqlite = (db, query, callback) => {
    db.serialize(function () {
        db.each(query, callback);
    });
}