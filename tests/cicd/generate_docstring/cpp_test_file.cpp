#include <string>
#include <vector>
#include <random>
#include <algorithm>
#include <sqlite3.h>


template<typename T>
/**
 * Adds two values of the same type and returns the result.
 * 
 * @param a The first value to be added.
 * @param b The second value to be added.
 * @return The sum of the two values.
 */
T a_plus_b(T a, T b) {
    return a + b;
}


/**
 * Executes an SQL query on the provided SQLite database connection and returns the results.
 * 
 * @param db A pointer to the SQLite database connection.
 * @param query The SQL query to be executed as a string.
 * @return A 2D vector of strings where each inner vector represents a row of results from the query.
 *         Each string within the row represents a column's value. If the query fails, an empty vector is returned.
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
 * Compares two items by applying a key mapping function and returns an integer 
 * indicating their ordering. The key mapping function is provided by the caller,
 * allowing for custom comparison logic.
 * 
 * @param key_map A function that maps an item of type T to a comparable type. 
 *                It is applied to both items to retrieve the values used for comparison.
 * @param item1 The first item to compare. It is of type T.
 * @param item2 The second item to compare. It is of type T.
 * @return An integer indicating the result of the comparison:
 *         - Returns -1 if the key value of item1 is less than the key value of item2.
 *         - Returns 1 if the key value of item1 is greater than the key value of item2.
 *         - Returns 0 if the key values of both items are equal.
 */
int compare(F key_map, const T& item1, const T& item2) {
    auto val1 = key_map(item1);
    auto val2 = key_map(item2);

    if (val1 < val2) return -1;
    if (val1 > val2) return 1;
    return 0;
}


/**
 * Generates a random string of alphabets of a specified length.
 * The string is composed of lowercase and uppercase letters.
 * 
 * @param length The length of the random string to be generated.
 * @return A string containing randomly selected alphabets of the specified length.
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