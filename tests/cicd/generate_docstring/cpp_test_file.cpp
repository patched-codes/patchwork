#include <string>
#include <vector>
#include <random>
#include <algorithm>
#include <sqlite3.h>


template<typename T>
/**
 * Computes the sum of two elements of type T.
 * 
 * @param a The first element to be added.
 * @param b The second element to be added.
 * @return The result of adding elements a and b.
 */
T a_plus_b(T a, T b) {
    return a + b;
}


/**
 * Executes an SQL query on the given SQLite database and retrieves the result.
 * 
 * This function prepares and executes the provided SQL query using the given
 * SQLite database connection. It reads the resulting rows and columns, storing
 * them in a vector of vectors of strings. Each inner vector represents a single
 * row, with each string representing the text of each column. In case of an error
 * in preparing the statement, it returns an empty result set.
 * 
 * @param db Pointer to the SQLite database connection object.
 * @param query SQL query to be executed on the database.
 * @return A vector of vectors of strings containing the results of the query.
 *         Returns an empty vector if the query cannot be prepared.
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
 * Compares two items based on a key extracted using a key mapping function.
 * 
 * @param key_map A callable function or functor that extracts a key from each item for comparison.
 * @param item1 The first item to compare.
 * @param item2 The second item to compare.
 * @return An integer indicating the result of the comparison: -1 if the key of item1 is less than the key of item2,
 *         1 if the key of item1 is greater than the key of item2, or 0 if the keys are equal.
 */
int compare(F key_map, const T& item1, const T& item2) {
    auto val1 = key_map(item1);
    auto val2 = key_map(item2);

    if (val1 < val2) return -1;
    if (val1 > val2) return 1;
    return 0;
}


/**
 * Generates a random string of alphabets consisting of both uppercase and lowercase characters.
 * 
 * @param length The length of the random string to generate.
 * @return A random string of the specified length made up of alphabetical characters.
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