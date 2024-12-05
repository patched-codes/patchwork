package org.example

import java.sql.Connection
import java.sql.ResultSet
import kotlin.random.Random


/**
 * Computes the sum of two numbers of type Number and returns the result as a Double.
 * 
 * @param a The first number to be added.
 * @param b The second number to be added.
 * @return The sum of the two numbers as a Double.
 */
fun <T : Number> aPlusB(a: T, b: T): Double = a.toDouble() + b.toDouble()


/**
 * Executes a SQL query on the provided SQLite database connection and returns the results as a list of rows.
 * Each row is represented as a list of objects, where each object corresponds to a column value.
 * 
 * @param db The database connection to be used for executing the SQL query.
 * @param query The SQL query to be executed against the database.
 * @return A list of rows resulting from the query, with each row being a list of column values.
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
 * Compares two items of type T based on their keys mapped by a given function. The keys
 * are of type R and must be comparable. Returns -1 if the key of the first item is less 
 * than the key of the second item, 1 if greater, and 0 if they are equal.
 * 
 * @param keyMap A function that maps an item of type T to a comparable key of type R.
 * @param item1 The first item to compare.
 * @param item2 The second item to compare.
 * @return An integer representing the result of the comparison: -1 if item1 < item2, 
 * 1 if item1 > item2, and 0 if they are equal based on their mapped keys.
 */
fun <T, R : Comparable<R>> compare(keyMap: (T) -> R, item1: T, item2: T): Int {
    return when {
        keyMap(item1) < keyMap(item2) -> -1
        keyMap(item1) > keyMap(item2) -> 1
        else -> 0
    }
}


/**
 * Generates a random string consisting of alphabets (both lowercase and uppercase) of a specified length.
 * 
 * @param length The desired length of the random string.
 * @return A random string of the specified length composed of alphabetic characters.
 */
fun randomAlphabets(length: Int): String {
    val charPool = ('a'..'z') + ('A'..'Z')
    return (1..length)
        .map { charPool[Random.nextInt(0, charPool.size)] }
        .joinToString("")
}
