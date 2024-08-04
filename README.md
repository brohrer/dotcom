# Bucket Tree

An online hierarchical binning algorithm.

* **Binning**: A bucket tree sorts observations into bins, or buckets, according to their
value. Each bin has an upper and lower bound, and contains all the observed
values that fall between them.

* **Hierarchical**: Each bucket can have two child buckets. Together the two
child buckets will cover the same range of values that their parent does.
Child buckets can have children of their own, making a
[binary tree](https://en.wikipedia.org/wiki/Binary_tree) structure.

* **Online**: A bucket tree handles values one at a time, rather than in a large
batch. It starts as a single root bucket and grows to accomodate observed
values as they are accumulated. When a bucket collects enough observations,
and if a good diving threshold can be found, two child buckets are created for it.

## How to use it

```bash
python3 -m pip install bucket_tree
```


```python
from bucket_tree import BucketTree

bt = BucketTree(max_buckets=100)

```

## API

### Constants

**`MAX_VAL`**

**`MIN_VAL`**

---

### class `BucketTree`

#### Attributes

#### Methods

**`BucketTree(max_buckets=100)`**

Creates a new `BucketTree` object.

- `max_buckets` is the maximum number of buckets the tree is allowed to create.

---

### class `Bucket`

#### Attributes

#### Methods

**`Bucket(lo=MIN_VAL, hi=MAX_VAL, level=0)`**

Creates a new `Bucket` object.

- `lo` is the lower bound of the bucket's range. The range *includes* the `lo` value. 

- `hi` is the upper bound of the bucket's range. The range *excludes* the `hi` value. 
