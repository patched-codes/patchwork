
/**
 * Function that calculates the sum of two numbers.
 * @param {number} a - The first number to be added
 * @param {number} b - The second number to be added
 * @returns {number} The sum of the two numbers
 */
function a_plus_b(a, b) {
    return a + b;
}

/**
 * Executes a query on a SQLite database
 * @param {Object} db - The SQLite database connection
 * @param {String} query - The query to be executed
 * @param {Function} callback - The callback function to be called for each row result
 * @returns {void} 
 */
const sqlite = (db, query, callback) => {
    db.serialize(function () {
        db.each(query, callback);
    });
}

/**
 * Compare function to be used for sorting an array of objects based on a specified key in each object.
 * @param {string} keymap - The key in the objects to compare.
 * @param {object} a - First object to compare.
 * @param {object} b - Second object to compare.
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