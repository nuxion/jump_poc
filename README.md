# POC jump consistent hash

A POC of the jump consistent hash paper[1]

Rebalance cost depends on the operation (up or down) and how more or less node are added. 

Sacling up or down requires a full scan of each node (some possible workaround could be adding a index, see: https://github.com/chrislusf/vasto/issues/15)
But scaling up one node at a time, usually requires ~30% of data move.  


## References

1. http://arxiv.org/pdf/1406.2294v1.pdf

