package org.example

import java.sql.Connection
import java.sql.ResultSet
import kotlin.random.Random


/**
 * Adds two numbers of a generic type that extends Number and returns the result as a Double.
 * 
 * @param a First number to add, must be of a type that extends Number.
 * @param b Second number to add, must be of a type that extends Number.
 * @return The sum of the two numbers as a Double.
 */
fun <T : Number> aPlusB(a: T, b: T): Double = a.toDouble() + b.toDouble()


/**
 * Executes a SQL query on a given SQLite database connection and returns the result as a list of rows,
 * where each row is represented as a list of objects corresponding to the columns in the result set.
 * 
 * @param db The database connection used to execute the query.
 * @param query The SQL query string to be executed.
 * @return A list of lists, where each inner list represents a row in the query result, containing objects for each column.
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
 * Compares two items based on a key extracted by the provided key mapping function.
 * Returns -1 if the key of the first item is less than the key of the second item,
 * 1 if it is greater, and 0 if they are equal.
 * 
 * @param <T> The type of the items to be compared.
 * @param <R> The type of the key, which must be comparable.
 * @param keyMap A function that maps an item to its key for comparison.
 * @param item1 The first item to be compared.
 * @param item2 The second item to be compared.
 * @return An integer -1, 0, or 1 based on the comparison of the keys.
 */
fun <T, R : Comparable<R>> compare(keyMap: (T) -> R, item1: T, item2: T): Int {
    return when {
        keyMap(item1) < keyMap(item2) -> -1
        keyMap(item1) > keyMap(item2) -> 1
        else -> 0
    }
}


/**
 * Generates a random string composed of alphabetic characters (both uppercase and lowercase)
 * with a specified length.
 * 
 * @param length The length of the resulting random alphabetic string.
 * @return A string of randomly selected alphabetic characters with the specified length.
 */
fun randomAlphabets(length: Int): String {
    val charPool = ('a'..'z') + ('A'..'Z')
    return (1..length)
        .map { charPool[Random.nextInt(0, charPool.size)] }
        .joinToString("")
}