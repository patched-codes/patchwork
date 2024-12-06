#include <string>
#include <vector>
#include <random>
#include <algorithm>
#include <sqlite3.h>


template<typename T>
/**
 * Adds two values of a generic type.
 * 
 * @param a The first operand of the addition.
 * @param b The second operand of the addition.
 * @return The result of adding a and b.
 */
T a_plus_b(T a, T b) {
    return a + b;
}


/**
 * Executes an SQL query on a given SQLite database and returns the results.
 * 
 * This function prepares and executes an SQL statement using the provided query string on a given SQLite database connection. 
 * It retrieves all resulting rows and columns as strings, storing them in a 2D vector, with each sub-vector representing a row.
 * 
 * @param db Pointer to the SQLite database connection, which should be valid and open.
 * @param query SQL query string to be executed on the database.
 * @return A 2D vector of strings where each sub-vector represents a row, and each string within a sub-vector represents a column value.
 *         Returns an empty vector if the query cannot be prepared or if there are no results.
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
 * Compares two items using a key mapping function to determine their order.
 * 
 * The comparison is made by applying a key mapping function to both items and
 * returning an integer based on their relative magnitude. If the mapped value
 * of the first item is less than the second, -1 is returned. If greater, 1 is
 * returned. If equal, 0 is returned.
 * 
 * @param key_map A function or function object that extracts a comparable key from each item.
 * @param item1 The first item to be compared.
 * @param item2 The second item to be compared.
 * @return An integer representing the order of the items: 
 *         -1 if the first item is less;
 *          1 if the first item is greater;
 *          0 if both items are equal.
 */
int compare(F key_map, const T& item1, const T& item2) {
    auto val1 = key_map(item1);
    auto val2 = key_map(item2);

    if (val1 < val2) return -1;
    if (val1 > val2) return 1;
    return 0;
}


/**
 * Generates a random string of alphabets of the specified length.
 * The string consists of both lowercase and uppercase English letters.
 * 
 * @param length The length of the random string to be generated.
 * @return A random string of alphabets of the specified length.
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