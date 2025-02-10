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
 * @return The sum of the two input values.
 */
T a_plus_b(T a, T b) {
    return a + b;
}


/**
 * Executes an SQL query on the provided SQLite database and retrieves the results.
 * 
 * @param db Pointer to an SQLite database connection object.
 * @param query A string containing the SQL query to be executed.
 * @return A vector of vectors of strings, where each inner vector represents a row retrieved by the query.
 *         Each row vector contains strings representing the text data of the columns for that row.
 *         If the query fails, an empty vector is returned.
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
 * Compares two items using a mapping function to extract comparison values from each item.
 * The function returns -1 if the first item is less than the second, 1 if the first item is greater than the second,
 * and 0 if both items are equal according to the mapped values.
 * 
 * @param key_map A function or callable object that extracts a comparison value from an item of type T.
 * @param item1 The first item to compare.
 * @param item2 The second item to compare.
 * @return An integer indicating the result of the comparison: -1 if item1 < item2, 1 if item1 > item2, and 0 if they are equal.
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
 * The string consists of both lowercase and uppercase English characters.
 *
 * @param length The length of the random string to be generated.
 * @return A random string composed of alphabetic characters of the specified length.
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