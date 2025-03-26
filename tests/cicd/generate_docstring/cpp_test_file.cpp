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
 * @return The sum of the two values.
 */
T a_plus_b(T a, T b) {
    return a + b;
}


/**
 * Executes a SQL query on a given SQLite database and returns the results as a vector of string vectors.
 *
 * This function prepares and executes a SQL query on the provided SQLite database connection,
 * then extracts the results row by row. Each row is represented as a vector of strings, and the
 * collection of these rows is returned as a vector of vectors of strings.
 *
 * @param db A pointer to an SQLite database connection object.
 * @param query The SQL query to be executed as a standard string.
 * @return A vector of vectors of strings representing the result set of the query. 
 * Each inner vector corresponds to a row, and each string in the inner vector corresponds 
 * to a column value in that row. If the query preparation fails, returns an empty vector.
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
 * Compares two items using a specified key mapping function and returns an integer
 * to signify whether the first item is less than, greater than, or equal to the second.
 * 
 * @param key_map A function object or lambda that takes an item and returns a comparable key.
 * @param item1 The first item to compare.
 * @param item2 The second item to compare.
 * @return Returns -1 if item1 is less than item2, 1 if item1 is greater than item2, 
 *         and 0 if item1 and item2 are equal based on the keys obtained through key_map.
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
 * The string includes both uppercase and lowercase letters.
 * 
 * @param length The length of the random string to generate.
 * @return A random string consisting of uppercase and lowercase alphabets.
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