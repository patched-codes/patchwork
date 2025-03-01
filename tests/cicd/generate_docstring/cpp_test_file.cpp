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
 * @return The sum of the two elements.
 */

T a_plus_b(T a, T b) {
    return a + b;
}


/**
 * Executes a SQL query on a SQLite database and retrieves the results.
 * 
 * @param db A pointer to the SQLite database instance.
 * @param query The SQL query to be executed as a string.
 * @return A vector of rows, where each row is represented as a vector of strings. Each string corresponds to a column value in the result set. If the query fails, an empty vector is returned.
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
 * Compares two generic items using a key-mapping function and returns an integer
 * indicating their relative order.
 * 
 * @param key_map A function that extracts a comparable key from an item of type T.
 * @param item1 The first item to compare.
 * @param item2 The second item to compare.
 * @return An integer: -1 if the key of item1 is less than the key of item2,
 *         1 if the key of item1 is greater than the key of item2, 
 *         and 0 if both keys are equal.
 */

int compare(F key_map, const T& item1, const T& item2) {
    auto val1 = key_map(item1);
    auto val2 = key_map(item2);

    if (val1 < val2) return -1;
    if (val1 > val2) return 1;
    return 0;
}


/**
 * Generates a random string consisting of uppercase and lowercase alphabets of a specified length.
 * 
 * @param length The length of the random string to generate.
 * @return A random string of alphabetic characters with the specified length.
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