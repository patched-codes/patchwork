#include <string>
#include <vector>
#include <random>
#include <algorithm>
#include <sqlite3.h>


template<typename T>
/**
 * Adds two values of type T.
 * 
 * @param a The first value to be added.
 * @param b The second value to be added.
 * @return The sum of the two values.
 */

T a_plus_b(T a, T b) {
    return a + b;
}


/**
 * Executes a SQL query on the given SQLite database and returns the results as 
 * a vector of string vectors, where each inner vector represents a row from the 
 * query result.
 * 
 * @param db A pointer to the SQLite database object.
 * @param query A string representing the SQL query to execute.
 * @return A vector of vectors of strings, where each inner vector represents a 
 *         row from the query result. If the query preparation fails, an empty 
 *         vector is returned.
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
 * Compares two items by applying a key mapping function and returns an integer based on the comparison.
 *
 * @param key_map A callable function or functor that extracts a comparable value from the items.
 * @param item1 The first item to be compared.
 * @param item2 The second item to be compared.
 * @return -1 if the value from item1 is less than the value from item2, 
 *         1 if the value from item1 is greater than the value from item2, 
 *         0 if both values are equal.
 */
int compare(F key_map, const T& item1, const T& item2) {
    auto val1 = key_map(item1);
    auto val2 = key_map(item2);

    if (val1 < val2) return -1;
    if (val1 > val2) return 1;
    return 0;
}


/**
 * Generates a random string composed of uppercase and lowercase alphabets with specified length.
 * 
 * @param length The desired length of the random string.
 * @return A random string of the specified length consisting of uppercase and lowercase alphabets.
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