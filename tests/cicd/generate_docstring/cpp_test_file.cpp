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
 * @return The sum of the two values, a and b.
 */
T a_plus_b(T a, T b) {
    return a + b;
}


/**
 * Executes a SQL query on the given SQLite database and retrieves the results.
 *
 * This function prepares and executes the provided SQL query on the specified SQLite database.
 * It fetches all resulting rows and columns, storing each column's value as a string in a 
 * vector of vectors of strings.
 * Each inner vector represents a row, with columns as elements.
 *
 * @param db A pointer to the SQLite database object.
 * @param query A string containing the SQL query to be executed.
 * @return A vector of vectors of strings, where each inner vector corresponds to a row retrieved
 *         from the database; returns an empty vector if preparation or execution fails.
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
 * This function takes a key mapping function and two items of the same type,
 * and compares them based on their mapped values. The result of the comparison
 * can be -1, 0, or 1, indicating the relative order of the two items.
 * 
 * @param key_map A function that maps an item to a comparable value.
 * @param item1 The first item to compare.
 * @param item2 The second item to compare.
 * @return -1 if the mapped value of item1 is less than that of item2,
 *         1 if the mapped value of item1 is greater than that of item2,
 *         or 0 if both mapped values are equal.
 */
int compare(F key_map, const T& item1, const T& item2) {
    auto val1 = key_map(item1);
    auto val2 = key_map(item2);

    if (val1 < val2) return -1;
    if (val1 > val2) return 1;
    return 0;
}


/**
 * Generates a random string composed of alphabetic characters of specified length.
 * The generated string includes both uppercase and lowercase letters.
 * 
 * @param length An integer specifying the desired length of the random string.
 * @return A randomly-generated string of alphabetic characters of the specified length.
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