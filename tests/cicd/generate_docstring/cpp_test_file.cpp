#include <string>
#include <vector>
#include <random>
#include <algorithm>
#include <sqlite3.h>


template<typename T>
/**
 * Adds two numbers of a generic type.
 * 
 * @param a The first number to be added.
 * @param b The second number to be added.
 * @return The sum of the two numbers.
 */
T a_plus_b(T a, T b) {
    return a + b;
}


/**
 * Executes a SQL query on a given SQLite database and returns the results.
 *
 * @param db Pointer to an SQLite database object.
 * @param query SQL query string to be executed on the database.
 * @return A 2D vector of strings, where each inner vector represents a row 
 *         from the query result, and each string in the inner vector represents
 *         a field in the row. Returns an empty vector if the query fails.
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
 * Compares two items based on a key derived from each item using a provided key-mapping function.
 * 
 * This function leverages a key-mapping function (key_map) to generate comparable values from the given items
 * and returns an integer indicative of their comparison. The possible return values are:
 *   - -1 if the key derived from the first item is less than that from the second,
 *   - 1 if the key derived from the first item is greater than that from the second,
 *   - 0 if both keys are equal.
 *
 * @param key_map A function that takes an item and produces a comparable key.
 * @param item1 The first item to be compared.
 * @param item2 The second item to be compared.
 * @return An integer representing the result of the comparison: -1, 0, or 1.
 */
int compare(F key_map, const T& item1, const T& item2) {
    auto val1 = key_map(item1);
    auto val2 = key_map(item2);

    if (val1 < val2) return -1;
    if (val1 > val2) return 1;
    return 0;
}


/**
 * Generates a random string consisting of alphabetic characters (both upper and lower case).
 * 
 * @param length The length of the random string to generate.
 * @return A random string of the specified length consisting of alphabetic characters.
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