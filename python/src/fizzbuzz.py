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
        return (self.convert(i) for i in range(1, 101))

if __name__ == "__main__":
    [print(item) for item in FizzBuzz().print()]
