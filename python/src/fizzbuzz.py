class FizzBuzz:
    def convert(self, num):
        if num % 3 == 0 and num % 5 == 0:
            return "FizzBuzz"
        elif num % 3 == 0:
            return "Fizz"
        elif num % 5 == 0:
            return "Buzz"
        else:
            return str(num)

    def print(self):
        for i in range(1, 101):
            print(self.convert(i))

if __name__ == "__main__":
    FizzBuzz().print()
