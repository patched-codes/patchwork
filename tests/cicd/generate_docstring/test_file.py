const assert = require('assert');

describe('a_plus_b', () => {
    it('should return the sum of two numbers', () => {
        assert.strictEqual(a_plus_b(1, 2), 3);
        assert.strictEqual(a_plus_b(-1, -1), -2);
        assert.strictEqual(a_plus_b(0, 0), 0);
    });
});

describe('compare', () => {
    it('should compare objects based on keymap, returning -1, 0, or 1', () => {
        const objA = { key: 1 };
        const objB = { key: 2 };
        assert.strictEqual(compare('key', objA, objB), -1);
        assert.strictEqual(compare('key', objB, objA), 1);
        assert.strictEqual(compare('key', objA, objA), 0);
    });
});

describe('sqlite', () => {
    it('should run the query and execute the callback on each result', (done) => {
        const mockDb = {
            serialize: (fn) => fn(),
            each: (query, callback) => {
                assert.strictEqual(query, 'SELECT * FROM table');
                callback(null, { id: 1 });
                callback(null, { id: 2 });
                done();
            }
        };
        sqlite(mockDb, 'SELECT * FROM table', (err, row) => {
            assert.ifError(err);
            assert.ok(row.id);
        });
    });
});
