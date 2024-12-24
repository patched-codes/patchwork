// Example usage of a_plus_b function
console.log(a_plus_b(10, 5)); // Output: 15

// Example usage of compare function
const obj1 = { name: 'Alice', age: 25 };
const obj2 = { name: 'Bob', age: 30 };

console.log(compare('age', obj1, obj2)); // Output: -1

// Example usage of sqlite function with a hypothetical database object
const fakeDB = {
    serialize: function(callback) { callback(); },
    each: function(query, callback) {
        callback({ id: 1, name: 'Alice' });
        callback({ id: 2, name: 'Bob' });
    }
};

sqlite(fakeDB, "SELECT * FROM users", (row) => {
    console.log(row); // Output: { id: 1, name: 'Alice' }, then { id: 2, name: 'Bob' }
});
