# Message broker

By default, the project uses the RabbitMQ message broker with one queue. All [watchers](watcher.md) write data to it, and the [processor/processors](processor.md) take data from the queue in portions.

If there are multiple processors, a separate queue must be created for each processor.