package org.example

import java.sql.Connection
import java.sql.ResultSet
import kotlin.random.Random


/**
 * Computes the sum of two numbers of a generic type that extends the Number class. 
 * Both input numbers are converted to Double for the addition, and the result is returned as a Double.
 * 
 * @param a The first number to be added, which must be a subtype of Number.
 * @param b The second number to be added, which must be a subtype of Number.
 * @return The sum of the two numbers as a Double.
 */
fun <T : Number> aPlusB(a: T, b: T): Double = a.toDouble() + b.toDouble()


/**
 * Executes a SQL query on the provided database connection and returns the results.
 * 
 * @param db The database connection used to execute the query.
 * @param query The SQL query to be executed.
 * @return A list of lists where each inner list represents a row from the query result,
 *         and each element within the inner list corresponds to a column value in that row.
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
 * Compares two items based on a given key mapping function and returns an integer indicating their order.
 * 
 * @param <T> the type of items to compare
 * @param <R> the type of the comparable key extracted from the items
 * @param keyMap a function that maps an item of type T to a comparable key of type R
 * @param item1 the first item to compare
 * @param item2 the second item to compare
 * @return an integer less than zero if item1 is less than item2, zero if they are equal, and greater than zero if item1 is greater than item2
 */
fun <T, R : Comparable<R>> compare(keyMap: (T) -> R, item1: T, item2: T): Int {
    return when {
        keyMap(item1) < keyMap(item2) -> -1
        keyMap(item1) > keyMap(item2) -> 1
        else -> 0
    }
}


/**
 * Generates a random string consisting of lowercase and uppercase alphabets.
 *
 * @param length The desired length of the generated random string.
 * @return A string of random alphabets with the specified length.
 */
fun randomAlphabets(length: Int): String {
    val charPool = ('a'..'z') + ('A'..'Z')
    return (1..length)
        .map { charPool[Random.nextInt(0, charPool.size)] }
        .joinToString("")
}