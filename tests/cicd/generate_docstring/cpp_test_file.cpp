#include <string>
#include <vector>
#include <random>
#include <algorithm>
#include <sqlite3.h>


template<typename T>
/**
 * Adds two values of the same type.
 * 
 * @param a The first value to be added.
 * @param b The second value to be added.
 * @return The sum of the first and second values.
 */
T a_plus_b(T a, T b) {
    return a + b;
}


/**
 * Executes a SQL query on the given SQLite database and retrieves the results in a vector of vectors of strings.
 * Each inner vector represents a row of the resulting table, with each string in the vector representing
 * the text of each column in that row.
 * 
 * @param db The SQLite database connection pointer on which the query will be executed.
 * @param query The SQL query string to be executed against the database.
 * @return A vector of vectors of strings, where each vector represents a row from the result set, and each 
 * string within the vector represents a column value as text from that row. Returns an empty vector if the 
 * query fails to execute.
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
 * Compares two items using a key mapping function.
 * 
 * @param key_map A function that maps an item of type T to a comparable value of type F.
 * @param item1 The first item to compare.
 * @param item2 The second item to compare.
 * @return An integer that is -1 if the value mapped from item1 is less than that from item2,
 *         1 if the value mapped from item1 is greater than that from item2, and 0 if they are equal.
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
 * The string includes both lowercase and uppercase letters.
 * 
 * @param length The length of the random string to be generated.
 * @return A string composed of randomly selected alphabetic characters with the specified length.
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