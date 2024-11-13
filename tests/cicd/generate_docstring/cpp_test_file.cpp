#include <string>
#include <vector>
#include <random>
#include <algorithm>
#include <sqlite3.h>


template<typename T>
/**
 * Adds two values of any type that supports the addition operator.
 * 
 * @param a The first value to be added.
 * @param b The second value to be added.
 * @return The sum of the two input values.
 */

T a_plus_b(T a, T b) {
    return a + b;
}


/**
 * Executes an SQL query on a given SQLite database and returns the results.
 * 
 * @param db A pointer to the SQLite database connection.
 * @param query The SQL query string to be executed.
 * @return A 2D vector containing the result of the query, where each inner vector represents a row of the result set, and each string in the inner vector corresponds to a column in that row. Returns an empty vector if the query fails or there are no results.
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
 * Compares two items using a provided key mapping function.
 * 
 * This function takes a key mapping function and two items, and returns an integer
 * based on the comparison of the keys derived from the items using the key_map function.
 * Returns -1 if the key of item1 is less than the key of item2, 
 * 1 if the key of item1 is greater than the key of item2, 
 * and 0 if the keys are equal.
 * 
 * @param key_map A function that maps an item to a comparable key.
 * @param item1 The first item to compare.
 * @param item2 The second item to compare.
 * @return -1, 0, or 1 based on the comparison of item1 and item2 keys.
 */
int compare(F key_map, const T& item1, const T& item2) {
    auto val1 = key_map(item1);
    auto val2 = key_map(item2);

    if (val1 < val2) return -1;
    if (val1 > val2) return 1;
    return 0;
}


/**
 * Generates a random string composed of uppercase and lowercase alphabets.
 * 
 * @param length The length of the random string to generate.
 * @return A random string of specified length consisting of letters from 'a' to 'z' and 'A' to 'Z'.
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