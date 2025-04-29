#include <string>
#include <vector>
#include <random>
#include <algorithm>
#include <sqlite3.h>


template<typename T>
/**
 * Adds two values of the same type.
 * 
 * @param a The first value to be added.
 * @param b The second value to be added.
 * @return The result of adding a and b.
 */
T a_plus_b(T a, T b) {
    return a + b;
}


/**
 * Executes a SQL query on the given SQLite database and returns the results.
 * 
 * @param db A pointer to the SQLite database object.
 * @param query A string containing the SQL query to be executed.
 * @return A vector of vectors of strings where each sub-vector represents a row from the query result,
 *         with each string in the sub-vector corresponding to a column value. Returns an empty vector
 *         if the query fails to prepare.
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
 * Compares two items based on a key mapping function and returns an integer indicating their order.
 * 
 * @param key_map A function that extracts a comparison key from an item.
 * @param item1 The first item to be compared.
 * @param item2 The second item to be compared.
 * @return -1 if the first item is less than the second, 1 if the first item is greater than the second, 
 *         and 0 if they are equal based on the mapping function.
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
 * @param length The length of the random string to be generated.
 * @return A random string containing only alphabetic characters with the specified length.
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