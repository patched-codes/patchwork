#include <string>
#include <vector>
#include <random>
#include <algorithm>
#include <sqlite3.h>


template<typename T>
/**
 * Adds two values of any type that supports the addition operator.
 * 
 * @param a The first value to add.
 * @param b The second value to add.
 * @return The sum of the two values.
 */
T a_plus_b(T a, T b) {
    return a + b;
}


/**
 * Executes a SQL query on the given SQLite database and retrieves the result set.
 * 
 * @param db Pointer to an SQLite database object.
 * @param query SQL query string to be executed.
 * @return A vector of vectors of strings, where each inner vector represents a row from the result set,
 *         and each string in the row represents a column value in that row. If the query fails to execute,
 *         an empty vector is returned.
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
 * based on the result of the comparison. The function maps each item to 
 * a key value, then compares these key values to determine the order.
 * 
 * @param key_map A function or callable object that extracts a comparison key 
 *                from each item. This function takes an item of type T as input 
 *                and returns a value that can be compared.
 * @param item1 The first item to be compared.
 * @param item2 The second item to be compared.
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
 * Generates a random string consisting of alphabetic characters (both uppercase and lowercase).
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