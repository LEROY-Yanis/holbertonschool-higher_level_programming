#!/usr/bin/node

const numbers = process.argv.slice(2).map(Number);

if (numbers.length < 2) {
  console.log(0);
} else {
  const sorted = numbers.sort((a, b) => b - a);
  console.log(sorted[1]);
}
