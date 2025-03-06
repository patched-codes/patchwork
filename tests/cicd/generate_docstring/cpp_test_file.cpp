#include <string>
#include <vector>
#include <random>
#include <algorithm>
#include <sqlite3.h>


template<typename T>
/**
 * Adds two values of the same type.
 * 
 * @param a The first value to add.
 * @param b The second value to add.
 * @return The sum of the two input values.
 */
T a_plus_b(T a, T b) {
    return a + b;
}


/**
 * Executes a given SQL query on a SQLite database and retrieves the result as a vector of string vectors.
 * Each vector within the vector represents a row of the result set, with each string representing a column value.
 * 
 * @param db A pointer to the SQLite database object on which to execute the query.
 * @param query The SQL query string to be executed.
 * @return A vector of vectors of strings, where each inner vector represents a row of the query result.
 *         If the preparation of the query fails, an empty vector is returned.
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
 * Compares two items based on values derived from a key mapping function.
 * The comparison is performed by mapping each item to a value using the 
 * provided key mapping function, and then comparing these values.
 * 
 * @param key_map A function or callable object transforming an item into a comparable value.
 * @param item1 The first item to be compared.
 * @param item2 The second item to be compared.
 * @return -1 if the value derived from item1 is less than the value derived from item2,
 *          1 if the value derived from item1 is greater than the value derived from item2,
 *          0 if both derived values are equal.
 */

int compare(F key_map, const T& item1, const T& item2) {
    auto val1 = key_map(item1);
    auto val2 = key_map(item2);

    if (val1 < val2) return -1;
    if (val1 > val2) return 1;
    return 0;
}


/**
 * Generates a random string of alphabets with a specified length.
 * The string contains both uppercase and lowercase letters.
 * 
 * @param length The length of the random string to generate.
 * @return A randomly generated string of alphabets with the specified length.
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