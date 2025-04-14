#include <string>
#include <vector>
#include <random>
#include <algorithm>
#include <sqlite3.h>


template<typename T>
/**
 * Computes the sum of two elements.
 * 
 * @param a The first element to be added.
 * @param b The second element to be added.
 * @return The result of adding the two elements.
 */

T a_plus_b(T a, T b) {
    return a + b;
}


/**
 * Executes a SQL query on the given SQLite database and retrieves the results as a vector of vector of strings.
 * Each inner vector represents a row from the executed query, and each string within the inner vector represents a column value.
 * 
 * @param db Pointer to the SQLite database connection object.
 * @param query The SQL query string to be executed on the SQLite database.
 * @return A vector of vectors of strings containing the resulting rows and columns from the query. If the query fails to prepare, returns an empty vector.
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
 * Compares two items using a key-mapping function to extract a value for comparison.
 * 
 * @param key_map A function or functor that maps an item of type T to a comparable value.
 * @param item1 The first item to be compared.
 * @param item2 The second item to be compared.
 * @return An integer: -1 if the value associated with item1 is less than item2,
 *         1 if the value associated with item1 is greater than item2,
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
 * Generates a random string composed solely of alphabets (both uppercase and lowercase).
 * 
 * @param length The desired length of the random string to be generated.
 * @return A random string of the specified length, containing only alphabetic characters.
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