import {FizzBuzz} from "../src/fizzbuzz";


describe("FizzBuzz", () => {
  const fb = new FizzBuzz();

  it("Non-multiple of three or five are preserved", () => {
    expect(fb.convert(1)).toBe("1");
    expect(fb.convert(4)).toBe("4");
  });

  it("Multiple of three are Fizz", () => {
    expect(fb.convert(3)).toBe("Fizz");
    expect(fb.convert(6)).toBe("Fizz");
  });

  it("Multiple of five are Buzz", () => {
    expect(fb.convert(5)).toBe("Buzz");
    expect(fb.convert(10)).toBe("Buzz");
  });

  it("Multiple of three and five are FizzBuzz", () => {
    expect(fb.convert(15)).toBe("FizzBuzz");
    expect(fb.convert(30)).toBe("FizzBuzz");
  });

  it("should print all the numbers up to 100", () => {
    let result = "";
    const log = (message?: any) => {
      result += message;
      result += "\n";
    };

    fb.print(log);

    expect(result).toMatchSnapshot();
  });
});

