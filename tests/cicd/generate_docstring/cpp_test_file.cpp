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
 * Executes an SQL query on a given SQLite database and returns the results.
 * 
 * @param db A pointer to the SQLite database connection.
 * @param query The SQL query to be executed on the database.
 * @return A 2D vector containing the results of the SQL query. Each inner vector represents a row, 
 *         and each string within an inner vector represents a column value from that row.
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
 * Compares two items using a key mapping function and returns an integer
 * based on their relative order. This function is useful for sorting 
 * where a specific key extracted from objects is the criterion for comparison.
 * 
 * @param key_map A function or callable entity that takes an item of type T 
 *                and returns a value to be used as the key for comparison.
 * @param item1 The first item to be compared.
 * @param item2 The second item to be compared.
 * @return An integer that indicates the relative order of the items:
 *         - Returns -1 if the key of item1 is less than the key of item2.
 *         - Returns 1 if the key of item1 is greater than the key of item2.
 *         - Returns 0 if both keys are equal.
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
 * The string will include a mix of both lowercase and uppercase letters.
 * 
 * @param length The length of the random string to be generated.
 * @return A random string consisting of alphabets with the specified length.
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