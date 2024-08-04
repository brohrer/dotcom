import sys
import numpy as np

MAX_VAL = sys.float_info.max
MIN_VAL = sys.float_info.min


class BucketTree:
    def __init__(self, max_buckets=100):
        self.max_buckets = int(max_buckets)
        if self.max_buckets < 0:
            raise ValueError(
                f"'BucketTree.max_buckets' ({self.max_buckets}) " +
                "needs to be non-negative."
            )
        self.n_buckets = 0
        self.buckets = [None] * self.max_buckets
        self.full = False

        self.highs = np.zeros(self.max_buckets)
        self.lows = np.zeros(self.max_buckets)
        self.leaves = np.zeros(self.max_buckets, dtype=bool)
        self.levels = -np.ones(self.max_buckets, dtype=int)

        self.root = Bucket()
        self._add_bucket(self.root)

    def _add_bucket(self, bucket):
        if self.full:
            return

        bucket.i_bucket = self.n_buckets
        self.buckets[self.n_buckets] = bucket
        self.highs[self.n_buckets] = bucket.hi
        self.lows[self.n_buckets] = bucket.lo
        self.leaves[self.n_buckets] = True
        self.levels[self.n_buckets] = 0

        self.n_buckets += 1
        if self.n_buckets == self.max_buckets:
            self.full = True

    def bin(self, val):
        bins = np.zeros(self.max_buckets)
        i_match = np.where(np.logical_and(
            val >= self.lows[:self.n_buckets],
            val < self.highs[:self.n_buckets]
        ))[0]

        # There should always be at least one matchig bin.
        assert i_match.size > 0

        bins[i_match] = 1.0
        return bins


class Bucket:
    def __init__(self, lo=MIN_VAL, hi=MAX_VAL, leaf=True, level=0):
        # The low and high limits of the range for this bucket.
        # The range is inclusive of the low value and exclusive of the high value.
        self.lo = float(lo)
        self.hi = float(hi)

        if self.hi <= self.lo:
            raise ValueError(
                f"'Bucket.hi' ({self.hi}) needs to be higher than 'Bucket.lo' ({self.lo})."
            )

        # The depth of the bucket tree at which this node sits.
        self.level = int(level)
        if self.level < 0:
            raise ValueError(f"'Bucket.level' ({self.level}) needs to be non-negative.")

        self.leaf = leaf

if __name__ == "__main__":
    # A short demo

    bt = BucketTree()

    for _ in range(10_000):
        bt.bin(np.random.sample())

    print(f"BucketTree has {bt.n_buckets} buckets")
    i_bucket = np.random.randint(bt.n_buckets)
    print(f"Randomly selected bucket {i_bucket} has")
    print(f"    lo = {bt.lo[i_bucket]}")
    print(f"    hi = {bt.hi[i_bucket]}")
    print(f"    level = {bt.level[i_bucket]}")
    # print(f"    {}")
