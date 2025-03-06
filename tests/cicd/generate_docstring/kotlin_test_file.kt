package org.example

import java.sql.Connection
import java.sql.ResultSet
import kotlin.random.Random


/**
 * Computes the sum of two numbers, converting them to Double for calculation. 
 * This function can accept any type of number (such as Int, Float, or Double) 
 * and returns the sum as a Double.
 * 
 * @param a The first number, a generic type that extends Number.
 * @param b The second number, a generic type that extends Number.
 * @return The sum of the two numbers as a Double.
 */
fun <T : Number> aPlusB(a: T, b: T): Double = a.toDouble() + b.toDouble()


/**
 * Executes a SQL query on a given database connection and returns the results as a list of rows,
 * where each row is represented as a list of column values.
 * 
 * @param db The Connection object representing the database connection to be used for executing the query.
 * @param query The SQL query string to be executed on the provided database connection.
 * @return A list of lists, where each inner list represents a row from the query result set and contains objects for each column value.
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
 * Compares two items of generic type T using a specified key mapping function and returns an integer
 * representing their ordering based on their mapped values.
 * 
 * @param keyMap A function that takes an item of type T and returns a comparable value of type R,
 *               which is used to compare the items.
 * @param item1 The first item of type T to be compared.
 * @param item2 The second item of type T to be compared.
 * @return An integer less than 0 if `item1` is less than `item2`, greater than 0 if `item1`
 *         is greater than `item2`, or 0 if they are equal.
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
 * This function creates a string consisting of random alphabetical characters
 * ranging from 'a' to 'z' and 'A' to 'Z'. The desired length of the result can
 * be specified by the parameter.
 * 
 * @param length The length of the random string to generate.
 * @return A random string consisting of uppercase and lowercase alphabetic characters.
 */
fun randomAlphabets(length: Int): String {
    val charPool = ('a'..'z') + ('A'..'Z')
    return (1..length)
        .map { charPool[Random.nextInt(0, charPool.size)] }
        .joinToString("")
}