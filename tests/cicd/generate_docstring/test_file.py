const assert = require('assert');

describe('a_plus_b', function() {
    it('should return the sum of two numbers', function() {
        assert.strictEqual(a_plus_b(1, 2), 3);
        assert.strictEqual(a_plus_b(-1, -1), -2);
        assert.strictEqual(a_plus_b(0, 0), 0);
    });
});

describe('compare', function() {
    it('should compare objects based on a keymap', function() {
        const obj1 = { key: 'a' };
        const obj2 = { key: 'b' };
        assert.strictEqual(compare('key', obj1, obj2), -1);
        assert.strictEqual(compare('key', obj2, obj1), 1);
        assert.strictEqual(compare('key', obj1, obj1), 0);
    });
});
