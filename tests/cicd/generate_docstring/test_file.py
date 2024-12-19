const assert = require('assert');

function testAPlusB() {
    assert.strictEqual(a_plus_b(2, 3), 5);
    assert.strictEqual(a_plus_b(-1, 1), 0);
}

function testCompare() {
    assert.strictEqual(compare('age', { age: 20 }, { age: 25 }), -1);
    assert.strictEqual(compare('age', { age: 30 }, { age: 30 }), 0);
    assert.strictEqual(compare('name', { name: 'Alice' }, { name: 'Bob' }), -1);
}

function testSqlite() {
    // Mock database and callback function for testing
    let mockDb = {
        serialize: function (fn) { fn(); },
        each: function (query, callback) {
            const data = [{ id: 1, name: "Test" }];
            data.forEach(callback);
        }
    };
    sqlite(mockDb, "SELECT * FROM test", (err, row) => {
        assert.strictEqual(row.id, 1);
        assert.strictEqual(row.name, "Test");
    });
}

testAPlusB();
testCompare();
testSqlite();
console.log('All tests passed');
