const assert = require('assert');

describe('a_plus_b', function() {
    it('should return the sum of two numbers', function() {
        assert.strictEqual(a_plus_b(2, 3), 5);
        assert.strictEqual(a_plus_b(-1, 1), 0);
        assert.strictEqual(a_plus_b(0, 0), 0);
    });
});

describe('compare', function() {
    it('should compare two objects based on a given keymap', function() {
        const keymap = 'value';
        const a = {value: 1};
        const b = {value: 2};
        assert.strictEqual(compare(keymap, a, b), -1);
        assert.strictEqual(compare(keymap, b, a), 1);
        assert.strictEqual(compare(keymap, a, a), 0);
    });
});

describe('sqlite', function() {
    it('should execute a query on the database and call the callback for each result', function(done) {
        const mockDb = {
            serialize: function(callback) {
                callback();
            },
            each: function(query, callback) {
                const result = {id: 1, name: 'test'};
                callback(null, result);
            }
        };
        sqlite(mockDb, 'SELECT * FROM test', function(err, row) {
            assert.strictEqual(row.id, 1);
            assert.strictEqual(row.name, 'test');
            done();
        });
    });
});
