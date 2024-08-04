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

bt = BucketTree(n_max_buckets=100)

```
---------------------------------
recycling bin

A hierarchical online quantizer (HOQ)
Binner
Slicer
Dicer
Chunker
Divisive clustering
Incisor
decisor
decision 
incize
(multidimensional) hierarchical online incremental dynamic adaptive binning
hierarchical online binning
DAB
nibling
bilbo
bolger

discretization
quantization

taxonomist
sorte
binner
carabiner
biner
a person who sorts things
bin tree
bucket tree


https://en.wikipedia.org/wiki/Data_binning



