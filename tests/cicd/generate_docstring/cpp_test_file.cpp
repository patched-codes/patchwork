#include <string>
#include <vector>
#include <random>
#include <algorithm>
#include <sqlite3.h>


template<typename T>
/**
 * Computes the sum of two values of the same type.
 * 
 * @param a The first value to be added.
 * @param b The second value to be added.
 * @return The result of adding the two values.
 */
T a_plus_b(T a, T b) {
    return a + b;
}


/**
 * Executes a SQL query on the given SQLite database and retrieves the results.
 * 
 * This function prepares and executes the provided SQL query on the specified
 * SQLite database and returns the results in a two-dimensional vector of strings,
 * where each inner vector represents a row from the query result.
 * 
 * @param db A pointer to the SQLite database connection object.
 * @param query A string containing the SQL query to be executed.
 * @return A vector of vectors of strings, where each inner vector represents
 *         a row from the query result set. Each string in a row represents a
 *         column value. If the query fails to prepare, returns an empty 
 *         vector.
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
 * This function applies the key mapping function to both items and compares
 * the resulting values to determine their relative order. It returns -1 if
 * item1 is less than item2, 1 if item1 is greater than item2, and 0 if they
 * are equal.
 *
 * @param key_map A callable that takes an item of type T and returns a comparable value.
 * @param item1 The first item to be compared.
 * @param item2 The second item to be compared.
 * @return An integer indicating the result of the comparison: -1, 0, or 1.
 */
int compare(F key_map, const T& item1, const T& item2) {
    auto val1 = key_map(item1);
    auto val2 = key_map(item2);

    if (val1 < val2) return -1;
    if (val1 > val2) return 1;
    return 0;
}


/**
 * Generates a random string of alphabets with the specified length.
 * The string includes both lowercase and uppercase letters.
 * 
 * @param length The length of the random string to be generated.
 * @return A random string of alphabets of the specified length.
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