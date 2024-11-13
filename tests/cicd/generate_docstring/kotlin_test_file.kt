package org.example

import java.sql.Connection
import java.sql.ResultSet
import kotlin.random.Random


/**
 * Returns the sum of two numeric values as a Double.
 * This function takes two parameters of any type that extends the Number class,
 * converts them to Double, and returns their sum.
 * 
 * @param a The first numeric value.
 * @param b The second numeric value.
 * @return The sum of the two numbers as a Double.
 */
fun <T : Number> aPlusB(a: T, b: T): Double = a.toDouble() + b.toDouble()


/**
 * Executes a SQL query on a given SQLite database connection and returns the results.
 * This function retrieves the data from the result set and stores each row as a list of objects.
 * 
 * @param db The SQLite database connection used to execute the query.
 * @param query The SQL query string to be executed on the database.
 * @return A list of lists, where each inner list represents a row of the query result, with each element in the list corresponding to a column value.
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
 * Compares two items based on a key extracted by a key mapping function, returning an integer 
 * indicating their ordering.
 * 
 * @param keyMap A function that extracts a comparable key from an item, used for comparison.
 * @param item1 The first item to be compared.
 * @param item2 The second item to be compared.
 * @return An integer: -1 if the key of item1 is less than the key of item2, 
 *         1 if the key of item1 is greater than the key of item2, 
 *         or 0 if the keys are equal.
 */
fun <T, R : Comparable<R>> compare(keyMap: (T) -> R, item1: T, item2: T): Int {
    return when {
        keyMap(item1) < keyMap(item2) -> -1
        keyMap(item1) > keyMap(item2) -> 1
        else -> 0
    }
}


/**
 * Generates a random string composed of alphabetic characters.
 * The string includes both uppercase and lowercase letters.
 * 
 * @param length The desired length of the random string.
 * @return A random string of the specified length containing only alphabetic characters.
 */
fun randomAlphabets(length: Int): String {
    val charPool = ('a'..'z') + ('A'..'Z')
    return (1..length)
        .map { charPool[Random.nextInt(0, charPool.size)] }
        .joinToString("")
}