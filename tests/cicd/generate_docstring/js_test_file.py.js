
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