#include <string>
#include <vector>
#include <random>
#include <algorithm>
#include <sqlite3.h>


template<typename T>
/**
 * Adds two elements of type T and returns the result.
 * 
 * @param a The first element to be added.
 * @param b The second element to be added.
 * @return The sum of the two elements of type T.
 */

T a_plus_b(T a, T b) {
    return a + b;
}


/**
 * Executes a SQL query on a given SQLite database and returns the results.
 * 
 * @param db A pointer to the SQLite database connection.
 * @param query A string representing the SQL query to be executed.
 * @return A vector of vectors of strings, where each inner vector represents a row in the result set, 
 *         and each string in the inner vector represents a column value of that row.
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
 * Compares two items using a key mapping function.
 * 
 * This function applies the given key mapping function to each of the two items 
 * and compares the resulting values to determine their relative order.
 * 
 * @param key_map A function or functor that takes an item of type T and returns 
 *                a comparable value.
 * @param item1 The first item to be compared.
 * @param item2 The second item to be compared.
 * @return An integer indicating the comparison result: -1 if the value of item1 
 *         is less than the value of item2, 1 if the value of item1 is greater 
 *         than the value of item2, and 0 if they are equal.
 */
int compare(F key_map, const T& item1, const T& item2) {
    auto val1 = key_map(item1);
    auto val2 = key_map(item2);

    if (val1 < val2) return -1;
    if (val1 > val2) return 1;
    return 0;
}


/**
 * Generates a random string composed of alphabetic characters (both lowercase and uppercase).
 * 
 * @param length The length of the random string to be generated.
 * @return A random string of the specified length containing alphabetic characters.
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