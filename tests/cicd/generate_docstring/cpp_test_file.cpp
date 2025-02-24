#include <string>
#include <vector>
#include <random>
#include <algorithm>
#include <sqlite3.h>


template<typename T>
/**
 * Adds two values of the same type together.
 * 
 * @param a The first value to be added.
 * @param b The second value to be added.
 * @return The sum of a and b.
 */
T a_plus_b(T a, T b) {
    return a + b;
}


/**
 * Executes a SQL query on the provided SQLite database and returns the results as a vector of string vectors.
 *
 * @param db A pointer to the SQLite database connection.
 * @param query The SQL query string to be executed.
 * @return A vector of vectors of strings where each inner vector represents a row from the query result,
 *         and each string within an inner vector represents a column value from that row. If the query
 *         fails or there are no results, an empty vector is returned.
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
 * Compares two items based on a key mapping function.
 * The function applies the key mapping to both items,
 * then compares the resulting values.
 * 
 * @param key_map A function that takes an item of type T and returns a key value that can be compared.
 * @param item1 The first item of type T to compare.
 * @param item2 The second item of type T to compare.
 * @return An integer: -1 if the key of item1 is less than the key of item2,
 *         1 if the key of item1 is greater than the key of item2,
 *         0 if both keys are equal.
 */
int compare(F key_map, const T& item1, const T& item2) {
    auto val1 = key_map(item1);
    auto val2 = key_map(item2);

    if (val1 < val2) return -1;
    if (val1 > val2) return 1;
    return 0;
}


/**
 * Generates a random string composed of uppercase and lowercase alphabets.
 * 
 * @param length The desired length of the resulting random string.
 * @return A randomly generated string of the specified length containing 
 *         only alphabetical characters (uppercase and lowercase).
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