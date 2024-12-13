package org.example

import java.sql.Connection
import java.sql.ResultSet
import kotlin.random.Random


/**
 * Adds two numbers of a type that extends Number and returns the result as a Double.
 *
 * This function takes two generic parameters, both of which must extend the Number class,
 * and computes their sum by converting them to Double.
 * 
 * @param a The first number to add, which extends the Number class.
 * @param b The second number to add, which extends the Number class.
 * @return The sum of the two numbers as a Double.
 */
fun <T : Number> aPlusB(a: T, b: T): Double = a.toDouble() + b.toDouble()


/**
 * Executes an SQL query on a given database connection and retrieves the results.
 * 
 * @param db The database connection used to execute the query.
 * @param query The SQL query to be executed.
 * @return A list of lists, where each inner list represents a row from the result set, and each element in the inner list represents a column value of that row.
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
 * Compares two items based on a specified key extracted by the keyMap function.
 * 
 * @param <T> The type of the items to be compared.
 * @param <R> The type of the key, which must be Comparable.
 * @param keyMap A function that takes an item of type T and returns a Comparable key of type R.
 * @param item1 The first item of type T to compare.
 * @param item2 The second item of type T to compare.
 * @return An integer indicating whether the key for item1 is less than, equal to, or greater than the key for item2.
 *         Returns -1 if item1's key is less than item2's key, 1 if greater, and 0 if they are equal.
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
 * The string includes both uppercase and lowercase letters.
 * 
 * @param length The length of the random string to be generated.
 * @return A string consisting of randomly selected alphabetic characters.
 */
fun randomAlphabets(length: Int): String {
    val charPool = ('a'..'z') + ('A'..'Z')
    return (1..length)
        .map { charPool[Random.nextInt(0, charPool.size)] }
        .joinToString("")
}