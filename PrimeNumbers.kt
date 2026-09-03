class PrimeNumbers {
    fun getPrimesLessThan(n: Int): List<Int> {
        val primes = mutableListOf<Int>()
        for (i in 2 until n) {
            if (isPrime(i)) {
                primes.add(i)
            }
        }
        return primes
    }

    fun isPrime(n: Int): Boolean {
        if (n <= 1) return false
        var i = 2
        while (i * i <= n) {
            if (n % i == 0) return false
            i++
        }
        return true
    }
}

fun main() {
    val primeNumbers = PrimeNumbers()
    val n = 50
    val primes = primeNumbers.getPrimesLessThan(n)
    println("Prime numbers less than $n:")
    println(primes)
}
