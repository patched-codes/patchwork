#include <string>
#include <vector>
#include <random>
#include <algorithm>
#include <sqlite3.h>


template<typename T>
/**
 * Adds two elements of a generic type T.
 * 
 * @param a The first element to be added.
 * @param b The second element to be added.
 * @return The sum of the two elements.
 */
T a_plus_b(T a, T b) {
    return a + b;
}


/**
 * Executes a given SQL query on the provided SQLite database and retrieves the results as a 
 * vector of vectors of strings, where each inner vector represents a row in the query result.
 * 
 * @param db Pointer to an SQLite database connection.
 * @param query The SQL query to be executed as a string.
 * @return A vector of vectors of strings representing the query result set. Each inner vector 
 *         corresponds to a row, with each string in the row corresponding to a column value.
 *         If the query execution fails, returns an empty vector.
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
 * @param key_map A function that takes an item and returns its key for comparison.
 * @param item1 The first item to be compared.
 * @param item2 The second item to be compared.
 * @return -1 if item1 is less than item2, 1 if item1 is greater than item2, 
 *         and 0 if they are equal based on the mapped keys.
 */
int compare(F key_map, const T& item1, const T& item2) {
    auto val1 = key_map(item1);
    auto val2 = key_map(item2);

    if (val1 < val2) return -1;
    if (val1 > val2) return 1;
    return 0;
}


/**
 * Generates a random string of alphabets with specified length.
 * 
 * @param length The desired length of the random string to be generated.
 * @return A string composed of randomly selected alphabets from the English alphabet, both lowercase and uppercase.
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