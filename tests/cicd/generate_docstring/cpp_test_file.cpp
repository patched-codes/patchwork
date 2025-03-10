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
 * @return The sum of the two input values.
 */
T a_plus_b(T a, T b) {
    return a + b;
}


/**
 * Executes a SQL query on the given SQLite database and retrieves the results.
 * Each row in the result is represented as a vector of strings, and all rows are stored in a vector.
 * If the query fails to prepare or execute, an empty result set is returned.
 * 
 * @param db A pointer to an open SQLite database object.
 * @param query A constant reference to a string containing the SQL query to be executed.
 * @return A vector of vectors of strings representing the rows and columns of the query result.
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
 * Compares two items using a mapping function to extract comparable keys from each item.
 * The function returns -1 if the first item is less than the second, 1 if it's greater, 
 * and 0 if they are equal based on the mapping values.
 * 
 * @param key_map A function or functor that extracts a comparable key from the items.
 * @param item1 The first item to compare.
 * @param item2 The second item to compare.
 * @return An integer: -1 if the key of item1 is less than the key of item2, 
 *         1 if the key of item1 is greater than the key of item2, or 0 if they are equal.
 */
int compare(F key_map, const T& item1, const T& item2) {
    auto val1 = key_map(item1);
    auto val2 = key_map(item2);

    if (val1 < val2) return -1;
    if (val1 > val2) return 1;
    return 0;
}


/**
 * Generates a random string composed of alphabets both in uppercase and lowercase.
 *
 * @param length The length of the random string to be generated.
 * @return A string of the specified length containing random alphabetic characters.
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