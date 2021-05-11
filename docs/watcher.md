# Watcher

The watcher listens to the new blocks, parses them, and assembly the information into the zone-neutral data structures. Watcher only works with one zone, so you need to run a separate watcher for each zone.

```The MoZ watcher is a standalone process that takes 3 input arguments.```

3 input arguments via docker container:

* chain id (network)
* rabbitmq connector
* graphql endpoint

3 input arguments directly without script:

* a zone RPC address
* a starting block number
* rabbitmq connector

and listens to the given zone starting from the given block number.

## Responsibilies

The newly created object of the ```block``` type is sent to the queue in [message broker](broker.md).

```
block {
   height: <number>
   chain_id: <string>
   time: <timestamp>
   messages: array [message] (transaction in real)
}
```

messages:
* transaction(not message in real)
* transfer
* ibcTransfer
* openChannel
* createConnection
* createClient
* createChannel
* closeChannel

```
transaction {
   sender: <string>
   hash: <string>
   accepted: <bool>
   messages: array [message]
}

transfer {
   sender: <string>
   recipient: <string>
   amount: array[
      amount: <number>, 
      coin: <string>
   ]
}

createClient {
   clientId: <string>
   clientType: <string>
   chainId: <string>
}

createConnection {
   connectionID: <string>
   clientID: <string>
}

createChannel {
   channelID: <string>
   connectionID: <string>
   portID: <string>
}

openChannel {
   channelID: <string>
}

closeChannel {
   channelID: <string>
}

ibcTransfer {
   channelID: <string>
   sender: <string>
   recipient: <string>
   amount: array[
      amount: <number>, 
      coin: <string>
   ]
}
```
## Possible errors

> 1) The watcher can't decode the block using the libraries every time the block contains MsgCreateValidator. It looks like a problem with the public key ```*types.Any```.

> 2) Error when sometimes decoding MsgUpdateClient. The error was corrected if you fixed it in the cosmos-sdk source code. Need to add a type decoding parameter as it couldn't decode from a string.
> ```Amount uint64 protobuf:"varint,2,opt,name=amount,proto3" json:"amount,string,omitempty"```
> <br>It was necessary to add string. The file is located here:
> ```cosmos-sdk@v0.40.0-rc3/x/ibc/applications/transfer/types/transfer.pb.go```
> <br>And here is the link to the file on github: [transfer.pb.go#L33](https://github.com/cosmos/cosmos-sdk/blob/v0.40.0-rc3/x/ibc/applications/transfer/types/transfer.pb.go#L33) 
