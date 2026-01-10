console.log("START");

setTimeout(() => {
  console.log("setTimeout");
}, 0);

setImmediate(() => {
  console.log("setImmediate");
});

process.nextTick(() => {
  console.log("process.nextTick");
});

console.log("END");

/* 
- Synchronous tasks will execute first 
- Then asynchronous tasks will execute in following order:
    -> process.nextTick
    -> setTimeout or setImmediate
- so the output will be 
    START
    END
    process.nextTick
    setTimeout
    setImmediate
*/
