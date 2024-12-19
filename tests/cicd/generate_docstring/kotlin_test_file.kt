package org.example

import java.sql.Connection
import java.sql.ResultSet
import kotlin.random.Random


/**
 * Adds two numbers of a numeric type and returns their sum as a Double.
 * 
 * @param a The first number of a generic numeric type T.
 * @param b The second number of a generic numeric type T.
 * @return The sum of a and b as a Double.
 */
fun <T : Number> aPlusB(a: T, b: T): Double = a.toDouble() + b.toDouble()


/**
 * Executes the given SQL query on the provided database connection and returns the result as a list of lists, 
 * where each inner list represents a row and each element within the inner list represents a column's value.
 * 
 * @param db The database connection to execute the query on.
 * @param query The SQL query to be executed.
 * @return A list of lists containing the result of the query, where each inner list corresponds to a row in the result set.
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
 * Compares two items of type T based on a key derived from them, which is of type R that implements Comparable.
 * This function returns an integer that indicates the ordering of the items.
 * 
 * @param keyMap A function that takes an item of type T and returns a key of type R used for comparison.
 * @param item1 The first item of type T to be compared.
 * @param item2 The second item of type T to be compared.
 * @return An integer: -1 if item1 is less than item2, 1 if item1 is greater than item2, and 0 if both are equal.
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
 * The string contains both uppercase and lowercase letters.
 * 
 * @param length The number of characters in the generated string.
 * @return A randomly generated string of alphabets with the given length.
 */
fun randomAlphabets(length: Int): String {
    val charPool = ('a'..'z') + ('A'..'Z')
    return (1..length)
        .map { charPool[Random.nextInt(0, charPool.size)] }
        .joinToString("")
}