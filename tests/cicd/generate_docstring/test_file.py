// Tests for js_test_file.js using Jest

const { a_plus_b, compare, sqlite } = require('./path_to_js_file');

test('a_plus_b should return the sum of two numbers', () => {
    expect(a_plus_b(1, 2)).toBe(3);
    expect(a_plus_b(-1, -1)).toBe(-2);
    expect(a_plus_b(0, 0)).toBe(0);
});

test('compare should compare objects based on a keymap', () => {
    const a = { name: 'Alice', age: 30 };
    const b = { name: 'Bob', age: 25 };
    expect(compare('age', a, b)).toBe(1);
    expect(compare('age', b, a)).toBe(-1);
    const c = { name: 'Charlie', age: 30 };
    expect(compare('age', a, c)).toBe(0);
});

test('sqlite should execute query and call callback with each row', done => {
    const mockDb = {
        serialize: jest.fn(fn => fn()),
        each: jest.fn((query, cb) => {
            cb(null, { id: 1, name: 'Alice' });
            cb(null, { id: 2, name: 'Bob' });
        })
    };
    const mockCallback = jest.fn();
    sqlite(mockDb, 'SELECT * FROM users', mockCallback);

    expect(mockDb.serialize).toHaveBeenCalled();
    expect(mockDb.each).toHaveBeenCalledWith('SELECT * FROM users', expect.any(Function));
    expect(mockCallback).toHaveBeenCalledTimes(2);
    expect(mockCallback).toHaveBeenCalledWith(null, { id: 1, name: 'Alice' });
    expect(mockCallback).toHaveBeenCalledWith(null, { id: 2, name: 'Bob' });
    done();
});
