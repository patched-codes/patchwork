#include <string>
#include <vector>
#include <random>
#include <algorithm>
#include <sqlite3.h>


template<typename T>
/**
 * Computes the sum of two values of the same type.
 * 
 * @param a The first value.
 * @param b The second value.
 * @return The result of adding 'a' and 'b'.
 */

T a_plus_b(T a, T b) {
    return a + b;
}


/**
 * Executes an SQL query on the specified SQLite database and retrieves the results.
 * 
 * @param db A pointer to the SQLite database object.
 * @param query A string containing the SQL query to be executed.
 * @return A 2D vector of strings where each sub-vector represents a row of results and each string represents a column value.
 */
std::vector<std::vector<std::string>> sqlite(sqlite3* db, const std::string& query) {
    std::vector<std::vector<std::string>> results;
    sqlite3_stmt* stmt;

    if (sqlite3_prepare_v2(db, query.c_str(), -1, &stmt, nullptr) != SQLITE_OK) {
        return results;
    }

    while (sqlite3_step(stmt) == SQLITE_ROW) {
        std::vector<std::string> row;
        for (int i = 0; i < sqlite3_column_count(stmt); i++) {
            const unsigned char* text = sqlite3_column_text(stmt, i);
            if (text) {
                row.push_back(std::string(reinterpret_cast<const char*>(text)));
            } else {
                row.push_back("");
            }
        }
        results.push_back(row);
    }

    sqlite3_finalize(stmt);
    return results;
}


template<typename T, typename F>
/**
 * Compares two items based on a key mapping function and returns 
 * an integer indicating their relative order.
 *
 * The key mapping function is applied to both items to obtain values 
 * which are then compared. The result of the comparison is:
 * - -1 if the value of the first item is less than the value of the second item.
 * -  1 if the value of the first item is greater than the value of the second item.
 * -  0 if the values of both items are equal.
 * 
 * @param key_map A function that maps an item to a comparable value.
 * @param item1 The first item to compare.
 * @param item2 The second item to compare.
 * @return An integer that is negative if `item1` is less than `item2`, 
 *         positive if `item1` is greater than `item2`, and zero if they are equal.
 */
int compare(F key_map, const T& item1, const T& item2) {
    auto val1 = key_map(item1);
    auto val2 = key_map(item2);

    if (val1 < val2) return -1;
    if (val1 > val2) return 1;
    return 0;
}


/**
 * Generates a random string consisting of uppercase and lowercase alphabets.
 * 
 * @param length The desired length of the generated string.
 * @return A string of random alphabets with the specified length.
 */
std::string random_alphabets(int length) {
    static const std::string chars =
        "abcdefghijklmnopqrstuvwxyz"
        "ABCDEFGHIJKLMNOPQRSTUVWXYZ";

    static std::random_device rd;
    static std::mt19937 generator(rd());
    static std::uniform_int_distribution<> distribution(0, chars.size() - 1);

    std::string result;
    result.reserve(length);

    for (int i = 0; i < length; ++i) {
        result += chars[distribution(generator)];
    }

    return result;
}