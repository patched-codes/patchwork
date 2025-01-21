const assert = require('assert');

describe('a_plus_b', function() {
    it('should return the sum of two numbers', function() {
        assert.strictEqual(a_plus_b(1, 2), 3);
        assert.strictEqual(a_plus_b(-1, 1), 0);
    });
});

describe('compare', function() {
    it('should compare objects based on a key', function() {
        const keymap = 'value';
        const a = {'value': 1};
        const b = {'value': 2};
        assert.strictEqual(compare(keymap, a, b), -1);
        assert.strictEqual(compare(keymap, b, a), 1);
        assert.strictEqual(compare(keymap, a, a), 0);
    });
});

describe('sqlite', function() {
    it('should execute a query on a database and trigger a callback per row', function(done) {
        const mockDb = {
            serialize: function(fn) { fn(); },
            each: function(query, callback) {
                callback(null, { a: 1 });
                callback(null, { b: 2 });
            }
        };
        const result = [];
        sqlite(mockDb, 'SELECT *', function(err, row) {
            if (err) throw err;
            result.push(row);
            if(result.length === 2) {
                assert.deepStrictEqual(result, [{ a: 1 }, { b: 2 }]);
                done();
            }
        });
    });
});
