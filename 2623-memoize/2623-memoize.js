function memoize(fn) {
  const cache = {};
  const callCounts = {};

  return function (...args) {
    const key = JSON.stringify(args);
    callCounts[key] = (callCounts[key] || 0) + 1;

    if (cache[key] !== undefined) {
      return cache[key];
    } else {
      const result = fn(...args);
      cache[key] = result;
      return result;
    }
  };
}

function memoizeSum(a, b) {
  return a + b;
}

function memoizeFactorial(n) {
  if (n <= 1) {
    return 1;
  } else {
    return n * memoizeFactorial(n - 1);
  }
}

function memoizeFib(n) {
  if (n <= 1) {
    return 1;
  } else {
    return memoizeFib(n - 1) + memoizeFib(n - 2);
  }
}

function memoizeFunction(fnName) {
  switch (fnName) {
    case "sum":
      return memoize(memoizeSum);
    case "factorial":
      return memoize(memoizeFactorial);
    case "fib":
      return memoize(memoizeFib);
    default:
      throw new Error("Invalid function name.");
  }
}

function executeActions(fnName, actions, values) {
  const memoizedFn = memoizeFunction(fnName);
  const results = [];

  for (let i = 0; i < actions.length; i++) {
    if (actions[i] === "call") {
      const result = memoizedFn(...values[i]);
      results.push(result);
    } else if (actions[i] === "getCallCount") {
      const key = JSON.stringify(values[i]);
      const callCount = callCounts[key] || 0;
      results.push(callCount);
    }
  }

  return results;
}

// // Example 1
// const fnName1 = "sum";
// const actions1 = ["call", "call", "getCallCount", "call", "getCallCount"];
// const values1 = [[2, 2], [2, 2], [], [1, 2], []];
// const output1 = executeActions(fnName1, actions1, values1);
// console.log(output1); // Output: [4, 4, 1, 3, 2]

// // Example 2
// const fnName2 = "factorial";
// const actions2 = ["call", "call", "call", "getCallCount", "call", "getCallCount"];
// const values2 = [[2], [3], [2], [], [3], []];
// const output2 = executeActions(fnName2, actions2, values2);
// console.log(output2); // Output: [2, 6, 2, 2, 6, 2]

// // Example 3
// const fnName3 = "fib";
// const actions3 = ["call", "getCallCount"];
// const values3 = [[5], []];
// const output3 = executeActions(fnName3, actions3, values3);
// console.log(output3); // Output: [8, 1]
// ``
