#!/usr/bin/node

const converted = parseInt(process.argv[2]);

if (Number.isNaN(converted)) {
  console.log('Not a number');
} else {
  console.log('My number: ' + converted);
}
