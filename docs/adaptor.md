# Adaptor

![Architecture-adaptor](img/map-of-zones-Adaptor.jpg)

The statistics adaptor updates statistics in [flat tables](database.md#flat-tables), by default every 10 seconds + runtime.
The adaptor makes a query in [PL/pgSQL functions](database.md#functions) and [tables](database.md#core-tables), and then updates the values in [flat tables](database.md#flat-tables) with the received data.