package org.example

import java.sql.Connection
import java.sql.ResultSet
import kotlin.random.Random


/**
 * Calculates the sum of two numbers and returns the result as a Double.
 * The function accepts any type that is a subtype of Number.
 * 
 * @param a The first number to add, of type Number.
 * @param b The second number to add, of type Number.
 * @return The sum of the two numbers as a Double.
 */
fun <T : Number> aPlusB(a: T, b: T): Double = a.toDouble() + b.toDouble()


/**
 * Executes the given SQL query using the provided database connection and returns the result as a list of rows,
 * where each row is a list of column values. Each column value can be of any type or nullable.
 * 
 * @param db The database connection to use for executing the query.
 * @param query The SQL query string to be executed.
 * @return A list of rows represented as lists of column values. Each row corresponds to a row in the result set,
 *         and each value in the row corresponds to a column value.
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
 * Compares two items of type T based on a key extracted by the keyMap function, 
 * which produces a comparable result of type R. The comparison is used to determine 
 * the ordering of the two items.
 * 
 * @param keyMap A function that takes an item of type T and returns a comparable key of type R.
 * @param item1 The first item to compare.
 * @param item2 The second item to compare.
 * @return An integer indicating the relative ordering: 
 *         -1 if item1 < item2, 1 if item1 > item2, or 0 if they are considered equal.
 */
fun <T, R : Comparable<R>> compare(keyMap: (T) -> R, item1: T, item2: T): Int {
    return when {
        keyMap(item1) < keyMap(item2) -> -1
        keyMap(item1) > keyMap(item2) -> 1
        else -> 0
    }
}


/**
 * Generates a random string of specified length consisting of uppercase and lowercase alphabets.
 * 
 * @param length The length of the random alphabetic string to be generated.
 * @return A random string consisting of alphabetical characters (both uppercase and lowercase) with the specified length.
 */
fun randomAlphabets(length: Int): String {
    val charPool = ('a'..'z') + ('A'..'Z')
    return (1..length)
        .map { charPool[Random.nextInt(0, charPool.size)] }
        .joinToString("")
}