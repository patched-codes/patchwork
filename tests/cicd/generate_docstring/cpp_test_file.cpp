#include <string>
#include <vector>
#include <random>
#include <algorithm>
#include <sqlite3.h>


template<typename T>
/**
 * Adds two values of the same type together.
 * 
 * @param a The first value of type T to be added.
 * @param b The second value of type T to be added.
 * @return The sum of a and b.
 */
T a_plus_b(T a, T b) {
    return a + b;
}


/**
 * Executes a SQL query on the provided SQLite database and retrieves the results.
 * 
 * This function prepares the SQL statement, executes it, and fetches all the rows returned
 * by the query into a vector of vectors of strings. Each inner vector represents a row in
 * the result set and each string within the inner vector represents a column value. It 
 * returns an empty result set if the query preparation fails.
 * 
 * @param db Pointer to an SQLite database connection (sqlite3*).
 * @param query The SQL query to be executed against the database.
 * @return A vector of vector of strings containing the result set. Each inner vector 
 * represents a row with its column values as strings. Returns an empty vector if the SQL 
 * statement couldn't be prepared or if there are no results.
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
 * Compares two items using a key extraction function and returns an integer indicating their order.
 *
 * @param key_map A function or callable object that extracts a key from an item for comparison.
 * @param item1 The first item to compare.
 * @param item2 The second item to compare.
 * @return -1 if the key from item1 is less than the key from item2, 
 *         1 if the key from item1 is greater than the key from item2,
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
 * @param length The length of the random string to be generated.
 * @return A string of the specified length containing random alphabetic characters.
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