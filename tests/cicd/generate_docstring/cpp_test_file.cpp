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
 * Executes a given SQL query on a SQLite database and returns the results as a 2D vector of strings.
 * Each row from the SQL query result is represented as a vector of strings within the result vector.
 * 
 * @param db Pointer to the SQLite database (sqlite3*).
 * @param query The SQL query to be executed (const std::string&).
 * @return A 2D vector of strings containing the query results, where each inner vector represents a row.
 *         If the query preparation fails, returns an empty 2D vector.
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
 * Compares two items using a key mapping function to determine the order.
 *
 * This method takes a key mapping function and applies it to two items to retrieve comparison values.
 * It returns -1 if the value from the first item is less than the second, 1 if it is greater, and 0 if they are equal. 
 *
 * @param key_map A callable that takes an item and returns a comparable value.
 * @param item1 The first item to compare.
 * @param item2 The second item to compare.
 * @return An integer: -1 if item1 < item2, 1 if item1 > item2, 0 if they are equal.
 */
int compare(F key_map, const T& item1, const T& item2) {
    auto val1 = key_map(item1);
    auto val2 = key_map(item2);

    if (val1 < val2) return -1;
    if (val1 > val2) return 1;
    return 0;
}


/**
 * Generates a random string consisting of uppercase and lowercase English alphabets.
 * 
 * @param length The desired length of the random string.
 * @return A random string containing the specified number of alphabet characters.
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