package org.example

import java.sql.Connection
import java.sql.ResultSet
import kotlin.random.Random


/**
 * Adds two numbers of type Number together after converting them to Double.
 * This function is generic and works for any type that extends Number.
 * 
 * @param a The first number to add, of a type that extends Number.
 * @param b The second number to add, of a type that extends Number.
 * @return The sum of the two numbers as a Double.
 */
fun <T : Number> aPlusB(a: T, b: T): Double = a.toDouble() + b.toDouble()


/**
 * Executes a SQL query on a database connection and retrieves the results as a list of rows,
 * with each row represented as a list of column values.
 *
 * @param db The database connection used to execute the query.
 * @param query The SQL query to execute.
 * @return A list of lists where each inner list represents a row returned by the query,
 *         and each element in the inner list represents a column value from that row.
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
 * Compares two items based on a key extracted from each item using the provided key mapping function.
 * The comparison is done based on the natural ordering of the extracted key values.
 * 
 * @param keyMap a function that extracts a comparable key from each item
 * @param item1 the first item to compare
 * @param item2 the second item to compare
 * @return -1 if the key of item1 is less than the key of item2, 1 if greater, and 0 if they are equal
 */

fun <T, R : Comparable<R>> compare(keyMap: (T) -> R, item1: T, item2: T): Int {
    return when {
        keyMap(item1) < keyMap(item2) -> -1
        keyMap(item1) > keyMap(item2) -> 1
        else -> 0
    }
}


/**
 * Generates a random string of alphabetic characters with the specified length.
 * The generated string includes both uppercase and lowercase letters.
 * 
 * @param length The desired length of the generated string of alphabets.
 * @return A string consisting of randomly selected alphabets of the given length.
 */

fun randomAlphabets(length: Int): String {
    val charPool = ('a'..'z') + ('A'..'Z')
    return (1..length)
        .map { charPool[Random.nextInt(0, charPool.size)] }
        .joinToString("")
}