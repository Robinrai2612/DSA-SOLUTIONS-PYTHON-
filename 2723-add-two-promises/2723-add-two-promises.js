
var addTwoPromises = async function(promise1, promise2) {
    return Promise.all([promise1, promise2])
    .then(([value1, value2]) => value1 + value2);
};
