#include <string>
#include <vector>
#include <random>
#include <algorithm>
#include <sqlite3.h>


template<typename T>
/**
 * Computes the sum of two values.
 * 
 * @param a The first value to be added.
 * @param b The second value to be added.
 * @return The sum of the two values.
 */
T a_plus_b(T a, T b) {
    return a + b;
}


/**
 * Executes an SQL query on the provided SQLite database connection and returns the results in a 2D vector.
 * Each sub-vector represents a row, and each string within a sub-vector is a column value.
 * 
 * @param db Pointer to the SQLite database connection.
 * @param query SQL query string to be executed.
 * @return A vector of vectors containing query results as strings. Each vector represents a row from the query result.
 *         If the query fails to prepare, an empty vector is returned.
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
 * Compares two items using a specified key mapping function and returns an integer 
 * indicating their relative order. The provided key_map function is applied to each 
 * item to extract a comparable value, and the comparison is based on these values.
 * 
 * @param key_map A function that takes an item of type T and returns a comparable value
 * @param item1 The first item to be compared
 * @param item2 The second item to be compared
 * @return An integer: -1 if the value mapped from item1 is less than that from item2,
 *         1 if it is greater, and 0 if they are equal.
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
 * The string consists of randomly selected characters from a set of uppercase
 * and lowercase English alphabets.
 * 
 * @param length The desired length of the random alphabetic string.
 *               Must be non-negative, as it specifies the number of characters
 *               in the generated string.
 * @return A randomly generated string of alphabets with the specified length.
 *         The string includes characters from both lowercase and uppercase
 *         English alphabets.
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