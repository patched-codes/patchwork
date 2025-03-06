package org.example

import java.sql.Connection
import java.sql.ResultSet
import kotlin.random.Random


/**
 * Adds two numbers of type T, where T extends Number, and returns their sum as a Double.
 * Converts the input numbers to Double before performing the addition.
 * 
 * @param a The first number to be added, of a type that extends Number.
 * @param b The second number to be added, of a type that extends Number.
 * @return The sum of the parameters a and b as a Double.
 */
fun <T : Number> aPlusB(a: T, b: T): Double = a.toDouble() + b.toDouble()


/**
 * Executes the given SQL query on the provided database connection and returns the results.
 * The results are structured as a list of rows, where each row is a list of column values.
 * 
 * @param db The database connection to be used for executing the query.
 * @param query The SQL query to be executed.
 * @return A list of lists, where each inner list represents a row and contains column values retrieved from the result set. 
 *         Each value is of type Any? to handle potential nulls.
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
 * Compares two items of type T based on a key extracted from each item using the provided key mapping function.
 * The key is of a type R, which must be comparable, to determine the order between the items.
 * Returns an integer indicating the comparison result: 
 * -1 if the key of item1 is less than the key of item2,
 * 1 if the key of item1 is greater than the key of item2,
 * or 0 if both keys are equal.
 * 
 * @param keyMap A function that maps an item of type T to a comparable key of type R.
 * @param item1 The first item to compare.
 * @param item2 The second item to compare.
 * @return An integer result of the comparison: -1, 0, or 1.
 */
fun <T, R : Comparable<R>> compare(keyMap: (T) -> R, item1: T, item2: T): Int {
    return when {
        keyMap(item1) < keyMap(item2) -> -1
        keyMap(item1) > keyMap(item2) -> 1
        else -> 0
    }
}


/**
 * Generates a random string composed of alphabets (both uppercase and lowercase).
 * 
 * @param length The desired length of the generated random string.
 * @return A string containing random alphabets with the specified length.
 */
fun randomAlphabets(length: Int): String {
    val charPool = ('a'..'z') + ('A'..'Z')
    return (1..length)
        .map { charPool[Random.nextInt(0, charPool.size)] }
        .joinToString("")
}