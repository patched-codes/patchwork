package org.example

import java.sql.Connection
import java.sql.ResultSet
import kotlin.random.Random


/**
 * Computes the sum of two numbers of type Number and returns the result as a Double.
 * 
 * @param a The first number to be added, constrained to the Number type.
 * @param b The second number to be added, constrained to the Number type.
 * @return The double-precision sum of the two input numbers.
 */

fun <T : Number> aPlusB(a: T, b: T): Double = a.toDouble() + b.toDouble()


/**
 * Executes a given SQL query on a provided database connection and returns the result as a list of rows,
 * where each row is a list of column values. The query is executed using a statement that is automatically
 * managed and closed by the function.
 * 
 * @param db The database connection on which the query will be executed.
 * @param query The SQL query to be executed as a String.
 * @return A list of lists, where each inner list represents a row from the query result. Each element in 
 *         the inner list corresponds to a column value from that row. Returns an empty list if no results
 *         are found.
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
 * Compares two items of type T using a mapping function to extract Comparable key values.
 * 
 * @param keyMap A function that takes an item of type T and returns a key of type R, which must be Comparable.
 * @param item1 The first item of type T to be compared.
 * @param item2 The second item of type T to be compared.
 * @return An integer representing the comparison result: -1 if item1 is less than item2; 
 *         1 if item1 is greater than item2; 0 if they are equal.
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
 * 
 * @param length The length of the random string to generate.
 * @return A string composed of random letters from the English alphabet, including both uppercase and lowercase letters.
 */
fun randomAlphabets(length: Int): String {
    val charPool = ('a'..'z') + ('A'..'Z')
    return (1..length)
        .map { charPool[Random.nextInt(0, charPool.size)] }
        .joinToString("")
}