import { shoutNumber } from "./fizzbuzz.js";

describe("has a valid result", () => {
  it("should return Fizz", () => {
    const result = shoutNumber(3);
    expect(result).toBe("Fizz");
  });
  it("should return Buzz", () => {
    const result = shoutNumber(5);
    expect(result).toBe("Buzz");
  });
  it("should return FizzBuzz", () => {
    const result = shoutNumber(15);
    expect(result).toBe("FizzBuzz");
  });
});
