const assert = require('assert');

describe('a_plus_b', () => {
    it('should return the sum of two numbers', () => {
        assert.strictEqual(a_plus_b(1, 2), 3);
        assert.strictEqual(a_plus_b(-1, -1), -2);
        assert.strictEqual(a_plus_b(1.5, 2.5), 4);
    });
});

describe('compare', () => {
    let keymap;
    before(() => { keymap = 'key'; });

    it('should return -1 when a[keymap] < b[keymap]', () => {
        const a = { key: 1 };
        const b = { key: 2 };
        assert.strictEqual(compare(keymap, a, b), -1);
    });

    it('should return 1 when a[keymap] > b[keymap]', () => {
        const a = { key: 3 };
        const b = { key: 2 };
        assert.strictEqual(compare(keymap, a, b), 1);
    });

    it('should return 0 when a[keymap] == b[keymap]', () => {
        const a = { key: 1 };
        const b = { key: 1 };
        assert.strictEqual(compare(keymap, a, b), 0);
    });
});

describe('sqlite', () => {
    it('should execute query and callback for each row', (done) => {
        const db = {
            serialize: function (fn) { fn(); },
            each: function (query, callback) {
                assert.strictEqual(query, 'SELECT * FROM test');
                callback(null, { id: 1 }, (err, row) => {
                    assert.strictEqual(row.id, 1);
                    done();
                });
            }
        };
        sqlite(db, 'SELECT * FROM test', (err, row) => {});
    });
});
