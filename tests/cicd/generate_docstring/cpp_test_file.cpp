#include <string>
#include <vector>
#include <random>
#include <algorithm>
#include <sqlite3.h>


template<typename T>
/**
 * Computes the sum of two values of a generic type.
 * 
 * @param a The first value to be added.
 * @param b The second value to be added.
 * @return The sum of the first and second values.
 */
T a_plus_b(T a, T b) {
    return a + b;
}


/**
 * Executes a given SQL query on a specified SQLite database and returns the results.
 * 
 * @param db A pointer to the SQLite database object on which the query is executed.
 * @param query A string containing the SQL query to be executed.
 * @return A 2D vector of strings, where each sub-vector represents a row of the result set.
 *         Each element in a sub-vector corresponds to a column in the row.
 *         If the query fails, an empty 2D vector is returned.
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
 * Compares two items based on the values extracted using a provided key mapping function.
 * 
 * @param key_map A function that extracts the comparison key from an item.
 * @param item1 The first item to be compared.
 * @param item2 The second item to be compared.
 * @return An integer, -1 if the comparison key of item1 is less than that of item2,
 *         1 if greater, and 0 if both are equal.
 */
int compare(F key_map, const T& item1, const T& item2) {
    auto val1 = key_map(item1);
    auto val2 = key_map(item2);

    if (val1 < val2) return -1;
    if (val1 > val2) return 1;
    return 0;
}


/**
 * Generates a random string of alphabets (both uppercase and lowercase) of a specified length.
 * 
 * @param length The length of the random string to be generated.
 * @return A random string consisting of alphabets with the specified length.
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