// Example usage of a_plus_b function
console.log(a_plus_b(3, 4)); // Output: 7

// Example usage of compare function
let objects = [
    { name: "Alice", age: 25 },
    { name: "Bob", age: 30 }
];
objects.sort((a, b) => compare('age', a, b));
console.log(objects); // Output: sorted by age

// Example usage of sqlite function with a mock database object
const mockDb = {
    serialize: (callback) => callback(),
    each: (query, callback) => {
        const mockData = [{ id: 1, name: "Alice" }];
        mockData.forEach((row) => callback(row));
    }
};

sqlite(mockDb, "SELECT * FROM users", (row) => console.log(row)); // Output: { id: 1, name: "Alice" }
