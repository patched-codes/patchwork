package org.example

import java.sql.Connection
import java.sql.ResultSet
import kotlin.random.Random


/**
 * Sums two numbers of type Number and returns the result as a Double.
 * 
 * This generic function takes two parameters of type Number (or its subtypes)
 * and converts them to Double before performing addition. This ensures that 
 * the result is precise and can handle various numeric types.
 * 
 * @param a The first numeric value to be added.
 * @param b The second numeric value to be added.
 * @return The sum of a and b as a Double.
 */
fun <T : Number> aPlusB(a: T, b: T): Double = a.toDouble() + b.toDouble()


/**
 * Executes a given SQL query on the provided database connection and returns the results.
 * 
 * The method uses the provided connection to execute the query and prepare a list of 
 * rows where each row is represented as a list of objects (corresponding to the columns).
 * 
 * @param db The database connection used to execute the query.
 * @param query The SQL query string to be executed.
 * @return A list of lists, where each inner list represents a row of the query result 
 *         with each element corresponding to a column value.
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
 * Compares two items of type T based on a key obtained from a key-mapping function.
 * The result of the comparison is determined by comparing the keys, which must be of a type that implements the Comparable interface.
 * 
 * @param keyMap A function that takes an item of type T and returns a key of type R, where R is Comparable.
 * @param item1 The first item to compare.
 * @param item2 The second item to compare.
 * @return An integer result of the comparison: -1 if the key of item1 is less than the key of item2, 1 if the key of item1 is greater than the key of item2, or 0 if they are equal.
 */
fun <T, R : Comparable<R>> compare(keyMap: (T) -> R, item1: T, item2: T): Int {
    return when {
        keyMap(item1) < keyMap(item2) -> -1
        keyMap(item1) > keyMap(item2) -> 1
        else -> 0
    }
}


/**
 * Generates a random string of alphabets of specified length.
 * The string includes both lowercase and uppercase letters.
 * 
 * @param length The length of the random string to generate.
 * @return A string composed of random alphabetic characters.
 */
fun randomAlphabets(length: Int): String {
    val charPool = ('a'..'z') + ('A'..'Z')
    return (1..length)
        .map { charPool[Random.nextInt(0, charPool.size)] }
        .joinToString("")
}