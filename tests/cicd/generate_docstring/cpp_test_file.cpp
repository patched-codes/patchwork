#include <string>
#include <vector>
#include <random>
#include <algorithm>
#include <sqlite3.h>


template<typename T>
/**
 * Adds two elements of type T.
 * 
 * @param a The first element to be added.
 * @param b The second element to be added.
 * @return The sum of the two elements.
 */
T a_plus_b(T a, T b) {
    return a + b;
}


/**
 * Executes a given SQL query on a provided SQLite database connection and returns the results.
 * 
 * @param db A pointer to the SQLite database connection.
 * @param query A string containing the SQL query to be executed.
 * @return A 2D vector of strings where each inner vector represents a row and each string represents a column value in the result set.
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
 * Compares two items using a specified key mapping function.
 * The comparison is performed based on the values obtained by applying the key mapping function to each item.
 * 
 * @param key_map A function or functor that takes an item of type T and returns a comparable value.
 * @param item1 The first item to be compared.
 * @param item2 The second item to be compared.
 * @return An integer result of the comparison: -1 if the value from item1 is less than the value from item2,
 *         1 if the value from item1 is greater than the value from item2, and
 *         0 if both values are equal.
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
 * @param length The desired length of the generated string.
 * @return A random string of the specified length containing only alphabetic characters.
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