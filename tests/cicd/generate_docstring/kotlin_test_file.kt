package org.example

import java.sql.Connection
import java.sql.ResultSet
import kotlin.random.Random


/**
 * Calculates the sum of two numerical values and returns the result as a Double.
 * 
 * @param a A numerical value of type T, where T extends Number.
 * @param b A numerical value of type T, where T extends Number.
 * @return The sum of a and b converted to a Double.
 */
fun <T : Number> aPlusB(a: T, b: T): Double = a.toDouble() + b.toDouble()


/**
 * Executes a given SQL query on a provided database connection and returns the result as a list of rows,
 * where each row is a list of column values.
 * 
 * Each element in the returned list represents a row from the result set, and each row is represented
 * as a list of values, corresponding to the columns in the result set.
 * 
 * @param db The database connection on which to execute the query.
 * @param query The SQL query to execute.
 * @return A list of lists, where each inner list contains the column values for a row from the result set.
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
 * Compares two items of generic type T based on a key extracted by a provided key mapping function.
 * The comparison is based on the natural ordering of the extracted keys which must implement Comparable.
 *
 * @param keyMap A function that maps each item of type T to a value of type R, where R is Comparable.
 * @param item1 The first item of type T to be compared.
 * @param item2 The second item of type T to be compared.
 * @return An integer indicating the comparison result: -1 if the key of item1 is less than the key of item2,
 *         1 if the key of item1 is greater than the key of item2, or 0 if both keys are equal.
 */
fun <T, R : Comparable<R>> compare(keyMap: (T) -> R, item1: T, item2: T): Int {
    return when {
        keyMap(item1) < keyMap(item2) -> -1
        keyMap(item1) > keyMap(item2) -> 1
        else -> 0
    }
}


/**
 * Generates a random string of alphabets with the specified length.
 * The string will contain both uppercase and lowercase letters.
 * 
 * @param length The desired length of the random alphabetic string.
 * @return A randomly generated string consisting of both uppercase and lowercase alphabets.
 */
fun randomAlphabets(length: Int): String {
    val charPool = ('a'..'z') + ('A'..'Z')
    return (1..length)
        .map { charPool[Random.nextInt(0, charPool.size)] }
        .joinToString("")
}