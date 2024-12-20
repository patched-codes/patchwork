package org.example

import java.sql.Connection
import java.sql.ResultSet
import kotlin.random.Random


/**
 * Sums two numbers and returns the result as a double.
 * This function accepts inputs of any type that extends the Number class.
 * 
 * @param a the first number to be added.
 * @param b the second number to be added.
 * @return the sum of the two numbers as a Double.
 */
fun <T : Number> aPlusB(a: T, b: T): Double = a.toDouble() + b.toDouble()


/**
 * Executes a SQL query on the provided database connection and returns the results as a list of rows, 
 * where each row is represented as a list of column values.
 * 
 * @param db A Connection object representing the database connection.
 * @param query A SQL query string to be executed.
 * @return A list of lists, where each inner list represents a row from the query result,
 * with each element corresponding to a value in the row. Values may be null if the database column is nullable.
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
 * Compares two items based on a key extracted from each item using a provided key mapping function.
 * The function returns an integer indicating the ordering of the two items:
 * - Returns -1 if the key of the first item is less than the key of the second item.
 * - Returns 1 if the key of the first item is greater than the key of the second item.
 * - Returns 0 if the keys of both items are equal.
 *
 * @param keyMap A function that extracts a comparable key from each item.
 * @param item1 The first item to be compared.
 * @param item2 The second item to be compared.
 * @return An integer indicating the ordering: -1 if item1 < item2, 1 if item1 > item2, or 0 if they are equal.
 */
fun <T, R : Comparable<R>> compare(keyMap: (T) -> R, item1: T, item2: T): Int {
    return when {
        keyMap(item1) < keyMap(item2) -> -1
        keyMap(item1) > keyMap(item2) -> 1
        else -> 0
    }
}


/**
 * Generates a random string of alphabets consisting of both lowercase and uppercase letters.
 * 
 * @param length The desired length of the random string.
 * @return A string consisting of randomly selected alphabets with the specified length.
 */
fun randomAlphabets(length: Int): String {
    val charPool = ('a'..'z') + ('A'..'Z')
    return (1..length)
        .map { charPool[Random.nextInt(0, charPool.size)] }
        .joinToString("")
}