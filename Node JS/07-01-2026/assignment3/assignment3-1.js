class Calculator {
  constructor(initialValue = 0) {
    this.value = initialValue; // set initial value to perform operations on
  }

  add(num) {
    this.value += num;
    return this;
  }

  subtract(num) {
    this.value -= num;
    return this;
  }

  multiply(num) {
    this.value *= num;
    return this;
  }

  divide(num) {
    if (num === 0) {
      throw new Error("Cannot divide by 0");
    }
    this.value /= num;
    return this;
  }

  getResult() {
    return this.value;
  }
}

const calc = new Calculator(5);
const result = calc.add(15).subtract(5).multiply(2).divide(5).getResult(); // function chaining 

console.log("Result is : " + result);
