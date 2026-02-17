// simple REST API exposing QuickSort
const express = require('express');
const bodyParser = require('body-parser');

const app = express();
app.use(bodyParser.json());

function quickSortPure(arr) {
    if (arr.length <= 1) return arr.slice();
    const pivot = arr[Math.floor(arr.length / 2)];
    const less = [];
    const equal = [];
    const greater = [];
    for (let x of arr) {
        if (x < pivot) less.push(x);
        else if (x > pivot) greater.push(x);
        else equal.push(x);
    }
    return quickSortPure(less).concat(equal).concat(quickSortPure(greater));
}

app.post('/quicksort', (req, res) => {
    const { array } = req.body;
    if (!Array.isArray(array)) {
        return res.status(400).json({ error: 'Request must contain an array field.' });
    }
    const nums = array.map(n => Number(n));
    if (nums.some(n => isNaN(n))) {
        return res.status(400).json({ error: 'Array must contain only numbers.' });
    }
    const sorted = quickSortPure(nums);
    res.json({ sorted });
});

const port = process.env.PORT || 3000;
app.listen(port, () => {
    console.log(`Server listening on port ${port}`);
});