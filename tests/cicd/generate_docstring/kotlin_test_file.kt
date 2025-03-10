package org.example

import java.sql.Connection
import java.sql.ResultSet
import kotlin.random.Random


/**
 * Adds two numbers of type Number and returns their sum as a Double.
 * 
 * @param a First number to be added. Must be of type Number.
 * @param b Second number to be added. Must be of type Number.
 * @return The sum of the two numbers as a Double.
 */
fun <T : Number> aPlusB(a: T, b: T): Double = a.toDouble() + b.toDouble()


/**
 * Executes a SQL query on the provided database connection and returns the result as a list of rows,
 * where each row is represented as a list of column values. Each value can be of any type, including null.
 * 
 * @param db The database connection to be used for executing the query.
 * @param query The SQL query string to be executed against the database.
 * @return A list of lists containing the query result, where each inner list represents a row with
 *         column values in the order they appear in the result set.
 */
fun sqlite(db: Connection, query: String): List<List<Any?>> {
    db.createStatement().use { statement ->
        statement.executeQuery(query).use { resultSet ->
            val results = mutableListOf<List<Any?>>()
            val columnCount = resultSet.metaData.columnCount

            while (resultSet.next()) {
                val row = mutableListOf<Any?>()
                for (i in 1..columnCount) {
                    row.add(resultSet.getObject(i))
                }
                results.add(row)
            }
            return results
        }
    }
}


/**
 * Compares two items using a key mapping function and returns an integer result.
 * The comparison is based on the result of applying the keyMap function to each item,
 * where the result is a Comparable object.
 * 
 * @param keyMap A function that takes an item of type T and returns a comparable key of type R.
 * @param item1 The first item to be compared.
 * @param item2 The second item to be compared.
 * @return Returns -1 if item1 is less than item2, 1 if item1 is greater than item2,
 *         and 0 if both items are equal based on their comparable keys.
 */
fun <T, R : Comparable<R>> compare(keyMap: (T) -> R, item1: T, item2: T): Int {
    return when {
        keyMap(item1) < keyMap(item2) -> -1
        keyMap(item1) > keyMap(item2) -> 1
        else -> 0
    }
}


/**
 * Generates a random string composed of alphabetic characters of given length.
 * It selects random characters from a pool of uppercase and lowercase English letters.
 * 
 * @param length The number of characters the resulting string should have.
 * @return A string of randomly selected alphabetic characters with the specified length.
 */
fun randomAlphabets(length: Int): String {
    val charPool = ('a'..'z') + ('A'..'Z')
    return (1..length)
        .map { charPool[Random.nextInt(0, charPool.size)] }
        .joinToString("")
}