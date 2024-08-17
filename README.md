# Bucket Tree

An online hierarchical binning algorithm:

* **Binning**: A bucket tree sorts observations into
[bins](https://en.wikipedia.org/wiki/Data_binning), or buckets, according to their
value. Each bin has an upper and lower bound, and contains all the observed
values that fall between them.

* **Hierarchical**: Each bucket can have two child buckets. Together the two
child buckets will cover the same range of values that their parent does.
Child buckets can have children of their own, making a
[binary tree](https://en.wikipedia.org/wiki/Binary_tree) structure.

* **Online**: A bucket tree handles values
[one at a time](https://en.wikipedia.org/wiki/Online_algorithm),
rather than in a large
batch. It starts as a single root bucket and grows to accomodate observed
values as they are accumulated. When a bucket collects enough observations,
and if a good diving threshold can be found, two child buckets are created for it.

## How to use it

Install at the command line.

```bash
python3 -m pip install bucket_tree
```

Put it in a Python script.

```python
from buckettree.bucket_tree import BucketTree

bt = BucketTree()

for _ in range(10_000):
    bin_memberships = bt.bin(np.random.sample())
```

## API Reference

### class `BucketTree(max_buckets=100)`

#### Attributes

- `buckets`, `List[Bucket]`: All of the buckets in the tree, in List form.

- `highs`, `numpy.ndarray(dtype=float)`: The `hi` bound of each bucket in the tree.

- `full`, `bool`: True if the maximum number of buckets have been created.

- `leaves`, `numpy.ndarray(dtype=bool)`: The leaf status of each bucket in the tree.

- `levels`, `numpy.ndarray(dtype=int)`:  The level of each bucket in the tree.

- `lows`, `numpy.ndarray(dtype=float)`: The `lo` bound of each bucket in the tree.

- `max_buckets`, `int`: The maximum number of buckets that can be created.

- `n_buckets`, `int`: The total number of buckets that have been created so far.

- `root`, `Bucket`: The bucket at the root of the tree.

#### Methods

**`bin(value)`**

- `value`, `float`: The floating-point value to bin and learn from.

- Returns `numpy.ndarray`: Array of floats of length `max_buckets`.
Each element is either 0.0 or 1.0, with 1.0 elements showing buckets in which
`value` belongs. (If a value belongs in a child bucket, it also belongs in the
parent bucket, so most values will belong to several buckets.)

---

### class `Bucket(bucket_size=100, lo=MIN_VAL, hi=MAX_VAL, leaf=True, level=0)`

#### Attributes

- `bucket_size`, `int`: After a bucket collects this many observations, it starts
trying to create child buckets.

- `hi`, `float`: The upper bound of the bucket's range.
The range *excludes* the `hi` value. 

- `i_bucket`, `int`: The index associated with this Bucket.

- `level`, `int`: The number of generations between this Bucket and
the root of the tree.

- `leaf`, `bool`: True only if this Bucket is a leaf on the tree.

- `lo`, `float`: The lower bound of the bucket's range.
The range *includes* the `lo` value. 

- `lo_child`

- `hi_child`

- `split_value`

#### Methods

---

### Constants

**`MAX_VAL`**

The maximum value of a float allowed by the system.

**`MIN_VAL`**

The minimum value of a float allowed by the system.
