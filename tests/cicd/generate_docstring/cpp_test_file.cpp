#include <string>
#include <vector>
#include <random>
#include <algorithm>
#include <sqlite3.h>


template<typename T>
/**
 * Adds two elements of the same type and returns their sum.
 * 
 * @param a The first element to be added.
 * @param b The second element to be added.
 * @return The sum of the two elements.
 */
T a_plus_b(T a, T b) {
    return a + b;
}


/**
 * Executes an SQL query on the provided SQLite database and retrieves the result as a vector of string vectors.
 * Each inner vector represents a row from the result set, and each string in the inner vector represents a column value.
 * 
 * @param db SQLite database connection object used to execute the query.
 * @param query SQL query string to be executed on the database.
 * @return Result of the executed query as a vector of vectors of strings. Each inner vector is a row of column values.
 *         Returns an empty vector if the query preparation fails or there are no results.
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
 * Compares two items using the specified key mapping function.
 * 
 * This function applies the key mapping function `key_map` to both input items
 * `item1` and `item2`, and compares the resulting values. It returns -1 if the 
 * first item's mapped value is less than the second item's mapped value, 1 if 
 * the first item's mapped value is greater, and 0 if both mapped values are equal.
 * 
 * @param key_map A function or callable object that maps an item of type `T` 
 *                to a comparable value.
 * @param item1 The first item to compare.
 * @param item2 The second item to compare.
 * @return An integer indicating the comparison result: -1 if `item1` is less 
 *         than `item2`, 1 if `item1` is greater, and 0 if they are equal.
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
 * The string includes both uppercase and lowercase characters.
 * 
 * @param length The length of the random string to be generated.
 * @return A random string composed of alphabetic characters of the given length.
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