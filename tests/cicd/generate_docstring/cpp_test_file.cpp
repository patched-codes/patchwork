#include <string>
#include <vector>
#include <random>
#include <algorithm>
#include <sqlite3.h>


template<typename T>
/**
 * Computes the sum of two values of the same type.
 * 
 * @param a First value to be added.
 * @param b Second value to be added.
 * @return The sum of a and b.
 */
T a_plus_b(T a, T b) {
    return a + b;
}


/**
 * Executes an SQL query on a SQLite database and returns the results as a vector of vectors of strings.
 * Each inner vector represents a row of the result set, with each element as a string representing a column value.
 * If the query fails to prepare, an empty result set is returned.
 * 
 * @param db A pointer to the SQLite database connection object.
 * @param query A string containing the SQL query to be executed on the database.
 * @return A vector of vectors containing the result set where each vector represents a single row of the result.
 *         Each column value is a string.
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
 * Compares two items using a key mapping function and returns an integer indicating their order.
 * 
 * @param key_map A function that maps an item to a comparable value used for comparison.
 * @param item1 The first item to compare.
 * @param item2 The second item to compare.
 * @return Returns -1 if the value from item1 is less than the value from item2, 
 *         1 if the value from item1 is greater than the value from item2,
 *         or 0 if both values are equal.
 */

int compare(F key_map, const T& item1, const T& item2) {
    auto val1 = key_map(item1);
    auto val2 = key_map(item2);

    if (val1 < val2) return -1;
    if (val1 > val2) return 1;
    return 0;
}


/**
 * Generates a random string composed of lowercase and uppercase alphabets.
 * 
 * @param length The desired length of the random string to be generated.
 * @return A string containing random alphabetic characters of the specified length.
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