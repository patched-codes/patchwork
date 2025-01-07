const assert = require('assert');

function a_plus_b(a, b) {
    return a + b;
}

const compare = function (keymap, a, b) {
    if (a[keymap] < b[keymap]) {
        return -1;
    } else if (a[keymap] > b[keymap]) {
        return 1;
    } else {
        return 0;
    }
}

describe('a_plus_b', function() {
    it('should return the sum of two numbers', function() {
        assert.strictEqual(a_plus_b(1, 2), 3);
        assert.strictEqual(a_plus_b(-1, 1), 0);
    });
});

describe('compare', function() {
    it('should compare two objects based on given key', function() {
        assert.strictEqual(compare('value', {value: 1}, {value: 2}), -1);
        assert.strictEqual(compare('value', {value: 2}, {value: 1}), 1);
        assert.strictEqual(compare('value', {value: 1}, {value: 1}), 0);
    });
});
