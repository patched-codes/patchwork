package org.example

import java.sql.Connection
import java.sql.ResultSet
import kotlin.random.Random


/**
 * Calculates the sum of two numbers and returns the result as a Double.
 * 
 * This function takes two parameters of type Number and adds them together
 * after converting them to Double, ensuring the returned result is a Double.
 *
 * @param a The first number to be added, of generic type T constrained to Number.
 * @param b The second number to be added, of generic type T constrained to Number.
 * @return The sum of the two numbers as a Double.
 */
fun <T : Number> aPlusB(a: T, b: T): Double = a.toDouble() + b.toDouble()


/**
 * Executes a given SQL query on the specified database connection and retrieves the results.
 * 
 * @param db A Connection object representing the database connection.
 * @param query A String containing the SQL query to be executed.
 * @return A List of Lists, where each inner list represents a row of the query result set,
 *         and each element within the inner list represents a column value of that row.
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
 * Compares two items based on a key extracted from each item using a specified mapping function.
 * The comparison is performed using the natural order of the extracted keys.
 * 
 * @param keyMap A function that extracts a comparable key from each item.
 * @param item1 The first item to compare.
 * @param item2 The second item to compare.
 * @return An integer representing the comparison result: -1 if the key of item1 is less than the key of item2,
 *         1 if the key of item1 is greater than the key of item2, or 0 if they are equal.
 */
fun <T, R : Comparable<R>> compare(keyMap: (T) -> R, item1: T, item2: T): Int {
    return when {
        keyMap(item1) < keyMap(item2) -> -1
        keyMap(item1) > keyMap(item2) -> 1
        else -> 0
    }
}


/**
 * Generates a random string composed of alphabetic characters with a specified length.
 * 
 * @param length The length of the generated string.
 * @return A string containing randomly selected alphabetic characters with the specified length.
 */
fun randomAlphabets(length: Int): String {
    val charPool = ('a'..'z') + ('A'..'Z')
    return (1..length)
        .map { charPool[Random.nextInt(0, charPool.size)] }
        .joinToString("")
}