import * as Console from "console";

export class FizzBuzz {
  convert(num: number): string {
    if (num % 3 === 0 && num % 5 === 0) {
      return "FizzBuzz";
    } else if (num % 3 === 0) {
      return "Fizz";
    } else if (num % 5 === 0) {
      return "Buzz";
    } else {
      return num.toString();
    }
  }

  print(log: typeof console.log = console.log) {
    for (let i = 0; i < 101; i++) {
      log(this.convert(i));
    }
  }
}
