package org.example

import java.sql.Connection
import java.sql.ResultSet
import kotlin.random.Random


/**
 * Calculates the sum of two numbers and returns the result as a Double.
 * This function accepts any type that is a subtype of Number.
 * 
 * @param a The first number to be added, must be a subtype of Number.
 * @param b The second number to be added, must be a subtype of Number.
 * @return The sum of 'a' and 'b' as a Double.
 */
fun <T : Number> aPlusB(a: T, b: T): Double = a.toDouble() + b.toDouble()


/**
 * Executes a SQL query on the provided database connection and returns the result as a list of rows,
 * where each row is represented as a list of column values. This method fetches all results into memory.
 * 
 * @param db The database connection used to create a statement for executing the SQL query.
 * @param query The SQL query string to be executed on the database.
 * @return A list of rows, where each row is a list of column values represented as Any?.
 *         If the query yields no results, an empty list is returned.
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
 * Compares two items of type T based on a key extracted using the keyMap function.
 * The key is required to be of a type that implements Comparable.
 *
 * @param keyMap A function that extracts a Comparable key from an item of type T.
 * @param item1 The first item to compare.
 * @param item2 The second item to compare.
 * @return An integer indicating the comparison result: -1 if item1 is less than item2, 
 *         1 if item1 is greater than item2, or 0 if they are equal based on the key extracted.
 */

fun <T, R : Comparable<R>> compare(keyMap: (T) -> R, item1: T, item2: T): Int {
    return when {
        keyMap(item1) < keyMap(item2) -> -1
        keyMap(item1) > keyMap(item2) -> 1
        else -> 0
    }
}


/**
 * Generates a random string composed of uppercase and lowercase alphabets.
 * 
 * @param length The desired length of the generated string.
 * @return A string of the specified length containing randomly ordered alphabets.
 */
fun randomAlphabets(length: Int): String {
    val charPool = ('a'..'z') + ('A'..'Z')
    return (1..length)
        .map { charPool[Random.nextInt(0, charPool.size)] }
        .joinToString("")
}