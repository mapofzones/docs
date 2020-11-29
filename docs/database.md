# Database

## Flat tables

![flat](img/db_flat_tables.png)

## Core tables

![core](img/db_core.png)

## Temporary tables

![temp](img/db_temp.png)

## Functions

### get_total_stats

get_total_stats(period_in_hours integer, step_in_hours integer)
<br>
RETURNS SETOF temp_t_total_stats

### get_full_stats_for_each_zone

get_full_stats_for_each_zone(period_in_hours integer, step_in_hours integer)
<br>
RETURNS SETOF temp_t_full_stats_for_each