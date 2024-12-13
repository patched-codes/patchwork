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

const sqlite = (db, query, callback) => {
    db.serialize(function () {
        db.each(query, callback);
    });
}

// Unit Tests
describe('Test a_plus_b', function() {
    it('should return the sum of two numbers', function() {
        assert.strictEqual(a_plus_b(1, 2), 3);
        assert.strictEqual(a_plus_b(-1, 1), 0);
        assert.strictEqual(a_plus_b(0, 0), 0);
    });
});

describe('Test compare', function() {
    it('should compare two objects based on a key', function() {
        const obj1 = { name: 'Alice' };
        const obj2 = { name: 'Bob' };
        assert.strictEqual(compare('name', obj1, obj2), -1);
        assert.strictEqual(compare('name', obj2, obj1), 1);
        assert.strictEqual(compare('name', obj1, obj1), 0);
    });
});

// Note: Testing 'sqlite' function is not included as it requires a database connection
