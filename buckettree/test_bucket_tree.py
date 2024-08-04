import sys
from buckettree.bucket_tree import BucketTree, Bucket


def test_bucket_initialization():
    bucket = Bucket(lo=-1.0, hi=1.0, leaf=False, level=2)
    assert type(bucket.lo) == float
    assert bucket.lo == -1.0
    assert type(bucket.hi) == float
    assert bucket.hi == 1.0
    assert type(bucket.level) == int
    assert bucket.level == 2
    assert bucket.leaf = False


def test_bucket_bounds():
    caught = False
    try:
        bucket = Bucket(lo=10.0, hi=-10.0)
    except ValueError:
        caught = True
    assert caught

    caught = False
    try:
        bucket = Bucket(level=-3)
    except ValueError:
        caught = True
    assert caught


def test_bucket_tree_initialization():
    bt = BucketTree()
    assert bt.max_buckets == 100
    assert bt.n_buckets == 1
    assert bt.full == False
    assert bt.buckets[0] == bt.root
    assert bt.root.lo == sys.float_info.min
    assert bt.root.hi == sys.float_info.max
    assert bt.root.leaf == True
    assert bt.root.level == 0

    assert bt.highs[0] == sys.float_info.min
    assert bt.lows[0] == sys.float_info.max
    assert bt.leaves[0] == True
    assert bt.levels[0] == 0


def test_bucket_tree_bounds():
    caught = False
    try:
        bt = BucketTree(max_bins=-100)
    except ValueError:
        caught = True
    assert caught


def test_bucket_tree_binning():
    bt = BucketTree()
    bin_membership = bt.bin(1.0)

    assert bt.n_buckets == 1
    assert bin_membership[0] == 1.0
