class Solution:
    def fizzBuzz(self, n: int) -> list[str]:
        return [self._fb(i) for i in range(1, n + 1)]

    def _fb(self, n: int) -> str:
        fizz = n % 3 == 0
        buzz = n % 5 == 0

        if not fizz and not buzz:
            return str(n)

        return ("Fizz" if fizz else "") + ("Buzz" if buzz else "")
