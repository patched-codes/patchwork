#include <string>
#include <vector>
#include <random>
#include <algorithm>
#include <sqlite3.h>


template<typename T>
/**
 * Returns the sum of two elements.
 * 
 * @param a The first element to be added.
 * @param b The second element to be added.
 * @return The sum of the two elements.
 */
T a_plus_b(T a, T b) {
    return a + b;
}


/**
 * Executes a SQL query on the provided SQLite database and returns the results.
 * 
 * @param db Pointer to the SQLite database connection.
 * @param query The SQL query string to be executed.
 * @return A two-dimensional vector of strings, where each sub-vector represents a row of the query results. 
 *         Each string in the sub-vector represents a column value. 
 *         Returns an empty vector if preparation of the statement fails or if there are no results.
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
 * Compares two items using a given key mapping function and returns an integer 
 * indicating the relative order of the items.
 * 
 * @param key_map A function that takes an item and returns a value used for comparison.
 * @param item1 The first item to be compared.
 * @param item2 The second item to be compared.
 * @return An integer: -1 if the first item's key is less than the second's, 
 *         1 if the first item's key is greater than the second's, 
 *         and 0 if they are equal.
 */
int compare(F key_map, const T& item1, const T& item2) {
    auto val1 = key_map(item1);
    auto val2 = key_map(item2);

    if (val1 < val2) return -1;
    if (val1 > val2) return 1;
    return 0;
}


/**
 * Generates a random string of alphabetic characters of specified length.
 * The generated string consists of both uppercase and lowercase letters.
 * 
 * @param length The desired length of the random string to be generated.
 * @return A randomly generated string composed of alphabetic characters with the specified length.
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