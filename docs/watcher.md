# Watcher

The watcher listens to the new blocks, parses them, and assembly the information into the zone-neutral data structures. Watcher only works with one zone, so you need to run a separate watcher for each zone.

The MoZ watcher is a standalone process that takes 2 input arguments: 

* a zone RPC address
* a starting block number

and listens to the given zone starting from the given block number.

## Responsibilies

The newly created object of the ```block``` type is sent to the queue.

```
block {
   chain_id: <string>, the zone chain id
   block_time: <timestamp> 
   block_num: <number>
   txs: array [transaction]
}

transaction {
   hash: <string>
   msgs: array [message]
}

message {
   transfer_info: {
     sender: <address>
     recipient: <address>
     quantity: <int>
     precision: <smallint>
     token: <code>
   }
   type: (send | receive | open_channel | open_connection | open_client | unknown)
   ibc: true | false
   ibc_channel_id: <string>
   ibc_connection_id: <string>
   ibc_client_id: <string>
}
```
