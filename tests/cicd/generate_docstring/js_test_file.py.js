
/**
 * Calculates the sum of two numbers.
 * @param {number} a - The first number 
 * @param {number} b - The second number
 * @returns {number} The sum of the two numbers
 */
function a_plus_b(a, b) {
    return a + b;
}

/**
 * Executes a SQLite query on the provided database and invokes a callback for each row returned.
 * @param {Object} db - The SQLite database instance
 * @param {string} query - The SQL query to be executed
 * @param {function} callback - The callback function to be invoked for each row returned
 * @returns {void} 
 */
const sqlite = (db, query, callback) => {
    db.serialize(function () {
        db.each(query, callback);
    });
}

/**
 * Compares the values of two objects based on a specified key.
 * @param {string} keymap - The key to compare the values of the objects.
 * @param {object} a - The first object to compare.
 * @param {object} b - The second object to compare.
 * @returns {number} - Returns -1 if a[keymap] is less than b[keymap], 1 if a[keymap] is greater than b[keymap], or 0 if they are equal.
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