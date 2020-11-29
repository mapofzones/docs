# Tx processor

The MoZ processor is a standalone process that listens to a queue for new blocks. There can be multiple processors. In this case, every processor must listen to his own queue. 
 
## Responsiblities

The processor gets performs the following functions:

* get a new block from the queue
* recognize a type of the messages
* process each message according to its type. For example, it can be an updating of the MoZ stats in case of an ibc transfer or adding a new record into the database if it's an ibc init message
* update the database with the latest processed block number
 
## Possible errors

The processor will reject a new block if it has wrong block number (higher, or lower than expected)