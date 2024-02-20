def primesum(self, A):
    def isprime(n):
        if n == 1:
            return False
        if n == 2:
            return True
        for i in range(2, round(n**0.5)+1):
            if n % i == 0:
                return False
        return True
    for i in range(2, A):
        if isprime(i) and isprime(A-i):
            return [i, A-i]

#correct
#только на будущее, не очень красиво def внутрь def заносить
