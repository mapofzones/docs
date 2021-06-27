# Schema Types

<details>
  <summary><strong>Table of Contents</strong></summary>

  * [Query](#query)
  * [Objects](#objects)
    * [blocks_log](#blocks_log)
    * [channels_stats](#channels_stats)
    * [channels_stats_aggregate](#channels_stats_aggregate)
    * [channels_stats_aggregate_fields](#channels_stats_aggregate_fields)
    * [channels_stats_avg_fields](#channels_stats_avg_fields)
    * [channels_stats_max_fields](#channels_stats_max_fields)
    * [channels_stats_min_fields](#channels_stats_min_fields)
    * [channels_stats_stddev_fields](#channels_stats_stddev_fields)
    * [channels_stats_stddev_pop_fields](#channels_stats_stddev_pop_fields)
    * [channels_stats_stddev_samp_fields](#channels_stats_stddev_samp_fields)
    * [channels_stats_sum_fields](#channels_stats_sum_fields)
    * [channels_stats_var_pop_fields](#channels_stats_var_pop_fields)
    * [channels_stats_var_samp_fields](#channels_stats_var_samp_fields)
    * [channels_stats_variance_fields](#channels_stats_variance_fields)
    * [headers](#headers)
    * [headers_aggregate](#headers_aggregate)
    * [headers_aggregate_fields](#headers_aggregate_fields)
    * [headers_avg_fields](#headers_avg_fields)
    * [headers_max_fields](#headers_max_fields)
    * [headers_min_fields](#headers_min_fields)
    * [headers_stddev_fields](#headers_stddev_fields)
    * [headers_stddev_pop_fields](#headers_stddev_pop_fields)
    * [headers_stddev_samp_fields](#headers_stddev_samp_fields)
    * [headers_sum_fields](#headers_sum_fields)
    * [headers_var_pop_fields](#headers_var_pop_fields)
    * [headers_var_samp_fields](#headers_var_samp_fields)
    * [headers_variance_fields](#headers_variance_fields)
    * [subscription_root](#subscription_root)
    * [zone_nodes](#zone_nodes)
    * [zone_nodes_aggregate](#zone_nodes_aggregate)
    * [zone_nodes_aggregate_fields](#zone_nodes_aggregate_fields)
    * [zone_nodes_max_fields](#zone_nodes_max_fields)
    * [zone_nodes_min_fields](#zone_nodes_min_fields)
    * [zones_graphs](#zones_graphs)
    * [zones_graphs_aggregate](#zones_graphs_aggregate)
    * [zones_graphs_aggregate_fields](#zones_graphs_aggregate_fields)
    * [zones_graphs_avg_fields](#zones_graphs_avg_fields)
    * [zones_graphs_max_fields](#zones_graphs_max_fields)
    * [zones_graphs_min_fields](#zones_graphs_min_fields)
    * [zones_graphs_stddev_fields](#zones_graphs_stddev_fields)
    * [zones_graphs_stddev_pop_fields](#zones_graphs_stddev_pop_fields)
    * [zones_graphs_stddev_samp_fields](#zones_graphs_stddev_samp_fields)
    * [zones_graphs_sum_fields](#zones_graphs_sum_fields)
    * [zones_graphs_var_pop_fields](#zones_graphs_var_pop_fields)
    * [zones_graphs_var_samp_fields](#zones_graphs_var_samp_fields)
    * [zones_graphs_variance_fields](#zones_graphs_variance_fields)
    * [zones_stats](#zones_stats)
    * [zones_stats_aggregate](#zones_stats_aggregate)
    * [zones_stats_aggregate_fields](#zones_stats_aggregate_fields)
    * [zones_stats_avg_fields](#zones_stats_avg_fields)
    * [zones_stats_max_fields](#zones_stats_max_fields)
    * [zones_stats_min_fields](#zones_stats_min_fields)
    * [zones_stats_stddev_fields](#zones_stats_stddev_fields)
    * [zones_stats_stddev_pop_fields](#zones_stats_stddev_pop_fields)
    * [zones_stats_stddev_samp_fields](#zones_stats_stddev_samp_fields)
    * [zones_stats_sum_fields](#zones_stats_sum_fields)
    * [zones_stats_var_pop_fields](#zones_stats_var_pop_fields)
    * [zones_stats_var_samp_fields](#zones_stats_var_samp_fields)
    * [zones_stats_variance_fields](#zones_stats_variance_fields)
  * [Inputs](#inputs)
    * [Boolean_comparison_exp](#boolean_comparison_exp)
    * [Int_comparison_exp](#int_comparison_exp)
    * [String_comparison_exp](#string_comparison_exp)
    * [blocks_log_bool_exp](#blocks_log_bool_exp)
    * [blocks_log_order_by](#blocks_log_order_by)
    * [blocks_log_pk_columns_input](#blocks_log_pk_columns_input)
    * [channels_stats_aggregate_order_by](#channels_stats_aggregate_order_by)
    * [channels_stats_avg_order_by](#channels_stats_avg_order_by)
    * [channels_stats_bool_exp](#channels_stats_bool_exp)
    * [channels_stats_max_order_by](#channels_stats_max_order_by)
    * [channels_stats_min_order_by](#channels_stats_min_order_by)
    * [channels_stats_order_by](#channels_stats_order_by)
    * [channels_stats_pk_columns_input](#channels_stats_pk_columns_input)
    * [channels_stats_stddev_order_by](#channels_stats_stddev_order_by)
    * [channels_stats_stddev_pop_order_by](#channels_stats_stddev_pop_order_by)
    * [channels_stats_stddev_samp_order_by](#channels_stats_stddev_samp_order_by)
    * [channels_stats_sum_order_by](#channels_stats_sum_order_by)
    * [channels_stats_var_pop_order_by](#channels_stats_var_pop_order_by)
    * [channels_stats_var_samp_order_by](#channels_stats_var_samp_order_by)
    * [channels_stats_variance_order_by](#channels_stats_variance_order_by)
    * [headers_aggregate_order_by](#headers_aggregate_order_by)
    * [headers_avg_order_by](#headers_avg_order_by)
    * [headers_bool_exp](#headers_bool_exp)
    * [headers_max_order_by](#headers_max_order_by)
    * [headers_min_order_by](#headers_min_order_by)
    * [headers_order_by](#headers_order_by)
    * [headers_pk_columns_input](#headers_pk_columns_input)
    * [headers_stddev_order_by](#headers_stddev_order_by)
    * [headers_stddev_pop_order_by](#headers_stddev_pop_order_by)
    * [headers_stddev_samp_order_by](#headers_stddev_samp_order_by)
    * [headers_sum_order_by](#headers_sum_order_by)
    * [headers_var_pop_order_by](#headers_var_pop_order_by)
    * [headers_var_samp_order_by](#headers_var_samp_order_by)
    * [headers_variance_order_by](#headers_variance_order_by)
    * [jsonb_comparison_exp](#jsonb_comparison_exp)
    * [numeric_comparison_exp](#numeric_comparison_exp)
    * [timestamp_comparison_exp](#timestamp_comparison_exp)
    * [zone_nodes_aggregate_order_by](#zone_nodes_aggregate_order_by)
    * [zone_nodes_bool_exp](#zone_nodes_bool_exp)
    * [zone_nodes_max_order_by](#zone_nodes_max_order_by)
    * [zone_nodes_min_order_by](#zone_nodes_min_order_by)
    * [zone_nodes_order_by](#zone_nodes_order_by)
    * [zone_nodes_pk_columns_input](#zone_nodes_pk_columns_input)
    * [zones_graphs_aggregate_order_by](#zones_graphs_aggregate_order_by)
    * [zones_graphs_avg_order_by](#zones_graphs_avg_order_by)
    * [zones_graphs_bool_exp](#zones_graphs_bool_exp)
    * [zones_graphs_max_order_by](#zones_graphs_max_order_by)
    * [zones_graphs_min_order_by](#zones_graphs_min_order_by)
    * [zones_graphs_order_by](#zones_graphs_order_by)
    * [zones_graphs_pk_columns_input](#zones_graphs_pk_columns_input)
    * [zones_graphs_stddev_order_by](#zones_graphs_stddev_order_by)
    * [zones_graphs_stddev_pop_order_by](#zones_graphs_stddev_pop_order_by)
    * [zones_graphs_stddev_samp_order_by](#zones_graphs_stddev_samp_order_by)
    * [zones_graphs_sum_order_by](#zones_graphs_sum_order_by)
    * [zones_graphs_var_pop_order_by](#zones_graphs_var_pop_order_by)
    * [zones_graphs_var_samp_order_by](#zones_graphs_var_samp_order_by)
    * [zones_graphs_variance_order_by](#zones_graphs_variance_order_by)
    * [zones_stats_aggregate_order_by](#zones_stats_aggregate_order_by)
    * [zones_stats_avg_order_by](#zones_stats_avg_order_by)
    * [zones_stats_bool_exp](#zones_stats_bool_exp)
    * [zones_stats_max_order_by](#zones_stats_max_order_by)
    * [zones_stats_min_order_by](#zones_stats_min_order_by)
    * [zones_stats_order_by](#zones_stats_order_by)
    * [zones_stats_pk_columns_input](#zones_stats_pk_columns_input)
    * [zones_stats_stddev_order_by](#zones_stats_stddev_order_by)
    * [zones_stats_stddev_pop_order_by](#zones_stats_stddev_pop_order_by)
    * [zones_stats_stddev_samp_order_by](#zones_stats_stddev_samp_order_by)
    * [zones_stats_sum_order_by](#zones_stats_sum_order_by)
    * [zones_stats_var_pop_order_by](#zones_stats_var_pop_order_by)
    * [zones_stats_var_samp_order_by](#zones_stats_var_samp_order_by)
    * [zones_stats_variance_order_by](#zones_stats_variance_order_by)
  * [Enums](#enums)
    * [blocks_log_select_column](#blocks_log_select_column)
    * [channels_stats_select_column](#channels_stats_select_column)
    * [headers_select_column](#headers_select_column)
    * [order_by](#order_by)
    * [zone_nodes_select_column](#zone_nodes_select_column)
    * [zones_graphs_select_column](#zones_graphs_select_column)
    * [zones_stats_select_column](#zones_stats_select_column)
  * [Scalars](#scalars)
    * [Boolean](#boolean)
    * [Float](#float)
    * [Int](#int)
    * [String](#string)
    * [jsonb](#jsonb)
    * [numeric](#numeric)
    * [timestamp](#timestamp)

</details>

## Query (query_root)
<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>blocks_log</strong></td>
<td valign="top">[<a href="#blocks_log">blocks_log</a>!]!</td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">distinct_on</td>
<td valign="top">[<a href="#blocks_log_select_column">blocks_log_select_column</a>!]</td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">limit</td>
<td valign="top"><a href="#int">Int</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">offset</td>
<td valign="top"><a href="#int">Int</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">order_by</td>
<td valign="top">[<a href="#blocks_log_order_by">blocks_log_order_by</a>!]</td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">where</td>
<td valign="top"><a href="#blocks_log_bool_exp">blocks_log_bool_exp</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>blocks_log_by_pk</strong></td>
<td valign="top"><a href="#blocks_log">blocks_log</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">zone</td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>channels_stats</strong></td>
<td valign="top">[<a href="#channels_stats">channels_stats</a>!]!</td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">distinct_on</td>
<td valign="top">[<a href="#channels_stats_select_column">channels_stats_select_column</a>!]</td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">limit</td>
<td valign="top"><a href="#int">Int</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">offset</td>
<td valign="top"><a href="#int">Int</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">order_by</td>
<td valign="top">[<a href="#channels_stats_order_by">channels_stats_order_by</a>!]</td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">where</td>
<td valign="top"><a href="#channels_stats_bool_exp">channels_stats_bool_exp</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>channels_stats_aggregate</strong></td>
<td valign="top"><a href="#channels_stats_aggregate">channels_stats_aggregate</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">distinct_on</td>
<td valign="top">[<a href="#channels_stats_select_column">channels_stats_select_column</a>!]</td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">limit</td>
<td valign="top"><a href="#int">Int</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">offset</td>
<td valign="top"><a href="#int">Int</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">order_by</td>
<td valign="top">[<a href="#channels_stats_order_by">channels_stats_order_by</a>!]</td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">where</td>
<td valign="top"><a href="#channels_stats_bool_exp">channels_stats_bool_exp</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>channels_stats_by_pk</strong></td>
<td valign="top"><a href="#channels_stats">channels_stats</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">channel_id</td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">client_id</td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">connection_id</td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">zone</td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>headers</strong></td>
<td valign="top">[<a href="#headers">headers</a>!]!</td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">distinct_on</td>
<td valign="top">[<a href="#headers_select_column">headers_select_column</a>!]</td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">limit</td>
<td valign="top"><a href="#int">Int</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">offset</td>
<td valign="top"><a href="#int">Int</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">order_by</td>
<td valign="top">[<a href="#headers_order_by">headers_order_by</a>!]</td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">where</td>
<td valign="top"><a href="#headers_bool_exp">headers_bool_exp</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>headers_aggregate</strong></td>
<td valign="top"><a href="#headers_aggregate">headers_aggregate</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">distinct_on</td>
<td valign="top">[<a href="#headers_select_column">headers_select_column</a>!]</td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">limit</td>
<td valign="top"><a href="#int">Int</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">offset</td>
<td valign="top"><a href="#int">Int</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">order_by</td>
<td valign="top">[<a href="#headers_order_by">headers_order_by</a>!]</td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">where</td>
<td valign="top"><a href="#headers_bool_exp">headers_bool_exp</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>headers_by_pk</strong></td>
<td valign="top"><a href="#headers">headers</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">timeframe</td>
<td valign="top"><a href="#int">Int</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>zone_nodes</strong></td>
<td valign="top">[<a href="#zone_nodes">zone_nodes</a>!]!</td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">distinct_on</td>
<td valign="top">[<a href="#zone_nodes_select_column">zone_nodes_select_column</a>!]</td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">limit</td>
<td valign="top"><a href="#int">Int</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">offset</td>
<td valign="top"><a href="#int">Int</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">order_by</td>
<td valign="top">[<a href="#zone_nodes_order_by">zone_nodes_order_by</a>!]</td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">where</td>
<td valign="top"><a href="#zone_nodes_bool_exp">zone_nodes_bool_exp</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>zone_nodes_aggregate</strong></td>
<td valign="top"><a href="#zone_nodes_aggregate">zone_nodes_aggregate</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">distinct_on</td>
<td valign="top">[<a href="#zone_nodes_select_column">zone_nodes_select_column</a>!]</td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">limit</td>
<td valign="top"><a href="#int">Int</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">offset</td>
<td valign="top"><a href="#int">Int</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">order_by</td>
<td valign="top">[<a href="#zone_nodes_order_by">zone_nodes_order_by</a>!]</td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">where</td>
<td valign="top"><a href="#zone_nodes_bool_exp">zone_nodes_bool_exp</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>zone_nodes_by_pk</strong></td>
<td valign="top"><a href="#zone_nodes">zone_nodes</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">rpc_addr</td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>zones_graphs</strong></td>
<td valign="top">[<a href="#zones_graphs">zones_graphs</a>!]!</td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">distinct_on</td>
<td valign="top">[<a href="#zones_graphs_select_column">zones_graphs_select_column</a>!]</td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">limit</td>
<td valign="top"><a href="#int">Int</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">offset</td>
<td valign="top"><a href="#int">Int</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">order_by</td>
<td valign="top">[<a href="#zones_graphs_order_by">zones_graphs_order_by</a>!]</td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">where</td>
<td valign="top"><a href="#zones_graphs_bool_exp">zones_graphs_bool_exp</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>zones_graphs_aggregate</strong></td>
<td valign="top"><a href="#zones_graphs_aggregate">zones_graphs_aggregate</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">distinct_on</td>
<td valign="top">[<a href="#zones_graphs_select_column">zones_graphs_select_column</a>!]</td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">limit</td>
<td valign="top"><a href="#int">Int</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">offset</td>
<td valign="top"><a href="#int">Int</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">order_by</td>
<td valign="top">[<a href="#zones_graphs_order_by">zones_graphs_order_by</a>!]</td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">where</td>
<td valign="top"><a href="#zones_graphs_bool_exp">zones_graphs_bool_exp</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>zones_graphs_by_pk</strong></td>
<td valign="top"><a href="#zones_graphs">zones_graphs</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">source</td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">target</td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">timeframe</td>
<td valign="top"><a href="#int">Int</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>zones_stats</strong></td>
<td valign="top">[<a href="#zones_stats">zones_stats</a>!]!</td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">distinct_on</td>
<td valign="top">[<a href="#zones_stats_select_column">zones_stats_select_column</a>!]</td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">limit</td>
<td valign="top"><a href="#int">Int</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">offset</td>
<td valign="top"><a href="#int">Int</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">order_by</td>
<td valign="top">[<a href="#zones_stats_order_by">zones_stats_order_by</a>!]</td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">where</td>
<td valign="top"><a href="#zones_stats_bool_exp">zones_stats_bool_exp</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>zones_stats_aggregate</strong></td>
<td valign="top"><a href="#zones_stats_aggregate">zones_stats_aggregate</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">distinct_on</td>
<td valign="top">[<a href="#zones_stats_select_column">zones_stats_select_column</a>!]</td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">limit</td>
<td valign="top"><a href="#int">Int</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">offset</td>
<td valign="top"><a href="#int">Int</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">order_by</td>
<td valign="top">[<a href="#zones_stats_order_by">zones_stats_order_by</a>!]</td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">where</td>
<td valign="top"><a href="#zones_stats_bool_exp">zones_stats_bool_exp</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>zones_stats_by_pk</strong></td>
<td valign="top"><a href="#zones_stats">zones_stats</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">timeframe</td>
<td valign="top"><a href="#int">Int</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">zone</td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
</tbody>
</table>

## Objects

### blocks_log

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>last_processed_block</strong></td>
<td valign="top"><a href="#int">Int</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>last_updated_at</strong></td>
<td valign="top"><a href="#timestamp">timestamp</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>zone</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
</tbody>
</table>

### channels_stats

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>channel_id</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>client_id</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>connection_id</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_1d</strong></td>
<td valign="top"><a href="#int">Int</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_1d_diff</strong></td>
<td valign="top"><a href="#int">Int</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_1d_failed</strong></td>
<td valign="top"><a href="#int">Int</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_1d_failed_diff</strong></td>
<td valign="top"><a href="#int">Int</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_30d</strong></td>
<td valign="top"><a href="#int">Int</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_30d_diff</strong></td>
<td valign="top"><a href="#int">Int</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_30d_failed</strong></td>
<td valign="top"><a href="#int">Int</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_30d_failed_diff</strong></td>
<td valign="top"><a href="#int">Int</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_7d</strong></td>
<td valign="top"><a href="#int">Int</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_7d_diff</strong></td>
<td valign="top"><a href="#int">Int</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_7d_failed</strong></td>
<td valign="top"><a href="#int">Int</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_7d_failed_diff</strong></td>
<td valign="top"><a href="#int">Int</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>is_opened</strong></td>
<td valign="top"><a href="#boolean">Boolean</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>zone</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>zone_counerparty</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
</tbody>
</table>

### channels_stats_aggregate

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>aggregate</strong></td>
<td valign="top"><a href="#channels_stats_aggregate_fields">channels_stats_aggregate_fields</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>nodes</strong></td>
<td valign="top">[<a href="#channels_stats">channels_stats</a>!]!</td>
<td></td>
</tr>
</tbody>
</table>

### channels_stats_aggregate_fields

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>avg</strong></td>
<td valign="top"><a href="#channels_stats_avg_fields">channels_stats_avg_fields</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>count</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">columns</td>
<td valign="top">[<a href="#channels_stats_select_column">channels_stats_select_column</a>!]</td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">distinct</td>
<td valign="top"><a href="#boolean">Boolean</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>max</strong></td>
<td valign="top"><a href="#channels_stats_max_fields">channels_stats_max_fields</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>min</strong></td>
<td valign="top"><a href="#channels_stats_min_fields">channels_stats_min_fields</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>stddev</strong></td>
<td valign="top"><a href="#channels_stats_stddev_fields">channels_stats_stddev_fields</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>stddev_pop</strong></td>
<td valign="top"><a href="#channels_stats_stddev_pop_fields">channels_stats_stddev_pop_fields</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>stddev_samp</strong></td>
<td valign="top"><a href="#channels_stats_stddev_samp_fields">channels_stats_stddev_samp_fields</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>sum</strong></td>
<td valign="top"><a href="#channels_stats_sum_fields">channels_stats_sum_fields</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>var_pop</strong></td>
<td valign="top"><a href="#channels_stats_var_pop_fields">channels_stats_var_pop_fields</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>var_samp</strong></td>
<td valign="top"><a href="#channels_stats_var_samp_fields">channels_stats_var_samp_fields</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>variance</strong></td>
<td valign="top"><a href="#channels_stats_variance_fields">channels_stats_variance_fields</a></td>
<td></td>
</tr>
</tbody>
</table>

### channels_stats_avg_fields

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_1d</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_1d_diff</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_1d_failed</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_1d_failed_diff</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_30d</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_30d_diff</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_30d_failed</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_30d_failed_diff</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_7d</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_7d_diff</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_7d_failed</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_7d_failed_diff</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
</tbody>
</table>

### channels_stats_max_fields

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>channel_id</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>client_id</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>connection_id</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_1d</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_1d_diff</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_1d_failed</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_1d_failed_diff</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_30d</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_30d_diff</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_30d_failed</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_30d_failed_diff</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_7d</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_7d_diff</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_7d_failed</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_7d_failed_diff</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>zone</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>zone_counerparty</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td></td>
</tr>
</tbody>
</table>

### channels_stats_min_fields

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>channel_id</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>client_id</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>connection_id</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_1d</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_1d_diff</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_1d_failed</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_1d_failed_diff</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_30d</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_30d_diff</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_30d_failed</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_30d_failed_diff</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_7d</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_7d_diff</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_7d_failed</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_7d_failed_diff</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>zone</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>zone_counerparty</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td></td>
</tr>
</tbody>
</table>

### channels_stats_stddev_fields

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_1d</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_1d_diff</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_1d_failed</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_1d_failed_diff</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_30d</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_30d_diff</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_30d_failed</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_30d_failed_diff</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_7d</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_7d_diff</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_7d_failed</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_7d_failed_diff</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
</tbody>
</table>

### channels_stats_stddev_pop_fields

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_1d</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_1d_diff</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_1d_failed</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_1d_failed_diff</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_30d</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_30d_diff</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_30d_failed</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_30d_failed_diff</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_7d</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_7d_diff</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_7d_failed</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_7d_failed_diff</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
</tbody>
</table>

### channels_stats_stddev_samp_fields

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_1d</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_1d_diff</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_1d_failed</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_1d_failed_diff</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_30d</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_30d_diff</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_30d_failed</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_30d_failed_diff</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_7d</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_7d_diff</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_7d_failed</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_7d_failed_diff</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
</tbody>
</table>

### channels_stats_sum_fields

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_1d</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_1d_diff</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_1d_failed</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_1d_failed_diff</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_30d</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_30d_diff</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_30d_failed</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_30d_failed_diff</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_7d</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_7d_diff</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_7d_failed</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_7d_failed_diff</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td></td>
</tr>
</tbody>
</table>

### channels_stats_var_pop_fields

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_1d</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_1d_diff</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_1d_failed</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_1d_failed_diff</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_30d</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_30d_diff</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_30d_failed</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_30d_failed_diff</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_7d</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_7d_diff</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_7d_failed</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_7d_failed_diff</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
</tbody>
</table>

### channels_stats_var_samp_fields

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_1d</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_1d_diff</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_1d_failed</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_1d_failed_diff</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_30d</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_30d_diff</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_30d_failed</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_30d_failed_diff</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_7d</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_7d_diff</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_7d_failed</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_7d_failed_diff</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
</tbody>
</table>

### channels_stats_variance_fields

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_1d</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_1d_diff</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_1d_failed</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_1d_failed_diff</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_30d</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_30d_diff</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_30d_failed</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_30d_failed_diff</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_7d</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_7d_diff</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_7d_failed</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_7d_failed_diff</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
</tbody>
</table>

### headers

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>channels_cnt_active_period</strong></td>
<td valign="top"><a href="#int">Int</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>channels_cnt_active_period_diff</strong></td>
<td valign="top"><a href="#int">Int</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>channels_cnt_all</strong></td>
<td valign="top"><a href="#int">Int</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>channels_cnt_open</strong></td>
<td valign="top"><a href="#int">Int</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>channels_cnt_period</strong></td>
<td valign="top"><a href="#int">Int</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>channels_percent_active_period</strong></td>
<td valign="top"><a href="#int">Int</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>channels_percent_active_period_diff</strong></td>
<td valign="top"><a href="#int">Int</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>chart</strong></td>
<td valign="top"><a href="#jsonb">jsonb</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">path</td>
<td valign="top"><a href="#string">String</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>relations_cnt_open</strong></td>
<td valign="top"><a href="#int">Int</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>timeframe</strong></td>
<td valign="top"><a href="#int">Int</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>top_zone_pair</strong></td>
<td valign="top"><a href="#jsonb">jsonb</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">path</td>
<td valign="top"><a href="#string">String</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>zones_cnt_all</strong></td>
<td valign="top"><a href="#int">Int</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>zones_cnt_period</strong></td>
<td valign="top"><a href="#int">Int</a>!</td>
<td></td>
</tr>
</tbody>
</table>

### headers_aggregate

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>aggregate</strong></td>
<td valign="top"><a href="#headers_aggregate_fields">headers_aggregate_fields</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>nodes</strong></td>
<td valign="top">[<a href="#headers">headers</a>!]!</td>
<td></td>
</tr>
</tbody>
</table>

### headers_aggregate_fields

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>avg</strong></td>
<td valign="top"><a href="#headers_avg_fields">headers_avg_fields</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>count</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">columns</td>
<td valign="top">[<a href="#headers_select_column">headers_select_column</a>!]</td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">distinct</td>
<td valign="top"><a href="#boolean">Boolean</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>max</strong></td>
<td valign="top"><a href="#headers_max_fields">headers_max_fields</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>min</strong></td>
<td valign="top"><a href="#headers_min_fields">headers_min_fields</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>stddev</strong></td>
<td valign="top"><a href="#headers_stddev_fields">headers_stddev_fields</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>stddev_pop</strong></td>
<td valign="top"><a href="#headers_stddev_pop_fields">headers_stddev_pop_fields</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>stddev_samp</strong></td>
<td valign="top"><a href="#headers_stddev_samp_fields">headers_stddev_samp_fields</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>sum</strong></td>
<td valign="top"><a href="#headers_sum_fields">headers_sum_fields</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>var_pop</strong></td>
<td valign="top"><a href="#headers_var_pop_fields">headers_var_pop_fields</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>var_samp</strong></td>
<td valign="top"><a href="#headers_var_samp_fields">headers_var_samp_fields</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>variance</strong></td>
<td valign="top"><a href="#headers_variance_fields">headers_variance_fields</a></td>
<td></td>
</tr>
</tbody>
</table>

### headers_avg_fields

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>channels_cnt_active_period</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>channels_cnt_active_period_diff</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>channels_cnt_all</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>channels_cnt_open</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>channels_cnt_period</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>channels_percent_active_period</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>channels_percent_active_period_diff</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>relations_cnt_open</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>timeframe</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>zones_cnt_all</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>zones_cnt_period</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
</tbody>
</table>

### headers_max_fields

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>channels_cnt_active_period</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>channels_cnt_active_period_diff</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>channels_cnt_all</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>channels_cnt_open</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>channels_cnt_period</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>channels_percent_active_period</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>channels_percent_active_period_diff</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>relations_cnt_open</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>timeframe</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>zones_cnt_all</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>zones_cnt_period</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td></td>
</tr>
</tbody>
</table>

### headers_min_fields

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>channels_cnt_active_period</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>channels_cnt_active_period_diff</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>channels_cnt_all</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>channels_cnt_open</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>channels_cnt_period</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>channels_percent_active_period</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>channels_percent_active_period_diff</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>relations_cnt_open</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>timeframe</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>zones_cnt_all</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>zones_cnt_period</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td></td>
</tr>
</tbody>
</table>

### headers_stddev_fields

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>channels_cnt_active_period</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>channels_cnt_active_period_diff</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>channels_cnt_all</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>channels_cnt_open</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>channels_cnt_period</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>channels_percent_active_period</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>channels_percent_active_period_diff</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>relations_cnt_open</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>timeframe</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>zones_cnt_all</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>zones_cnt_period</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
</tbody>
</table>

### headers_stddev_pop_fields

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>channels_cnt_active_period</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>channels_cnt_active_period_diff</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>channels_cnt_all</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>channels_cnt_open</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>channels_cnt_period</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>channels_percent_active_period</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>channels_percent_active_period_diff</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>relations_cnt_open</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>timeframe</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>zones_cnt_all</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>zones_cnt_period</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
</tbody>
</table>

### headers_stddev_samp_fields

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>channels_cnt_active_period</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>channels_cnt_active_period_diff</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>channels_cnt_all</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>channels_cnt_open</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>channels_cnt_period</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>channels_percent_active_period</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>channels_percent_active_period_diff</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>relations_cnt_open</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>timeframe</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>zones_cnt_all</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>zones_cnt_period</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
</tbody>
</table>

### headers_sum_fields

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>channels_cnt_active_period</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>channels_cnt_active_period_diff</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>channels_cnt_all</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>channels_cnt_open</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>channels_cnt_period</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>channels_percent_active_period</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>channels_percent_active_period_diff</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>relations_cnt_open</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>timeframe</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>zones_cnt_all</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>zones_cnt_period</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td></td>
</tr>
</tbody>
</table>

### headers_var_pop_fields

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>channels_cnt_active_period</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>channels_cnt_active_period_diff</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>channels_cnt_all</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>channels_cnt_open</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>channels_cnt_period</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>channels_percent_active_period</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>channels_percent_active_period_diff</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>relations_cnt_open</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>timeframe</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>zones_cnt_all</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>zones_cnt_period</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
</tbody>
</table>

### headers_var_samp_fields

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>channels_cnt_active_period</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>channels_cnt_active_period_diff</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>channels_cnt_all</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>channels_cnt_open</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>channels_cnt_period</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>channels_percent_active_period</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>channels_percent_active_period_diff</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>relations_cnt_open</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>timeframe</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>zones_cnt_all</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>zones_cnt_period</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
</tbody>
</table>

### headers_variance_fields

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>channels_cnt_active_period</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>channels_cnt_active_period_diff</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>channels_cnt_all</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>channels_cnt_open</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>channels_cnt_period</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>channels_percent_active_period</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>channels_percent_active_period_diff</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>relations_cnt_open</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>timeframe</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>zones_cnt_all</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>zones_cnt_period</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
</tbody>
</table>

### subscription_root

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>blocks_log</strong></td>
<td valign="top">[<a href="#blocks_log">blocks_log</a>!]!</td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">distinct_on</td>
<td valign="top">[<a href="#blocks_log_select_column">blocks_log_select_column</a>!]</td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">limit</td>
<td valign="top"><a href="#int">Int</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">offset</td>
<td valign="top"><a href="#int">Int</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">order_by</td>
<td valign="top">[<a href="#blocks_log_order_by">blocks_log_order_by</a>!]</td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">where</td>
<td valign="top"><a href="#blocks_log_bool_exp">blocks_log_bool_exp</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>blocks_log_by_pk</strong></td>
<td valign="top"><a href="#blocks_log">blocks_log</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">zone</td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>channels_stats</strong></td>
<td valign="top">[<a href="#channels_stats">channels_stats</a>!]!</td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">distinct_on</td>
<td valign="top">[<a href="#channels_stats_select_column">channels_stats_select_column</a>!]</td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">limit</td>
<td valign="top"><a href="#int">Int</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">offset</td>
<td valign="top"><a href="#int">Int</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">order_by</td>
<td valign="top">[<a href="#channels_stats_order_by">channels_stats_order_by</a>!]</td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">where</td>
<td valign="top"><a href="#channels_stats_bool_exp">channels_stats_bool_exp</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>channels_stats_aggregate</strong></td>
<td valign="top"><a href="#channels_stats_aggregate">channels_stats_aggregate</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">distinct_on</td>
<td valign="top">[<a href="#channels_stats_select_column">channels_stats_select_column</a>!]</td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">limit</td>
<td valign="top"><a href="#int">Int</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">offset</td>
<td valign="top"><a href="#int">Int</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">order_by</td>
<td valign="top">[<a href="#channels_stats_order_by">channels_stats_order_by</a>!]</td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">where</td>
<td valign="top"><a href="#channels_stats_bool_exp">channels_stats_bool_exp</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>channels_stats_by_pk</strong></td>
<td valign="top"><a href="#channels_stats">channels_stats</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">channel_id</td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">client_id</td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">connection_id</td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">zone</td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>headers</strong></td>
<td valign="top">[<a href="#headers">headers</a>!]!</td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">distinct_on</td>
<td valign="top">[<a href="#headers_select_column">headers_select_column</a>!]</td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">limit</td>
<td valign="top"><a href="#int">Int</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">offset</td>
<td valign="top"><a href="#int">Int</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">order_by</td>
<td valign="top">[<a href="#headers_order_by">headers_order_by</a>!]</td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">where</td>
<td valign="top"><a href="#headers_bool_exp">headers_bool_exp</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>headers_aggregate</strong></td>
<td valign="top"><a href="#headers_aggregate">headers_aggregate</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">distinct_on</td>
<td valign="top">[<a href="#headers_select_column">headers_select_column</a>!]</td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">limit</td>
<td valign="top"><a href="#int">Int</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">offset</td>
<td valign="top"><a href="#int">Int</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">order_by</td>
<td valign="top">[<a href="#headers_order_by">headers_order_by</a>!]</td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">where</td>
<td valign="top"><a href="#headers_bool_exp">headers_bool_exp</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>headers_by_pk</strong></td>
<td valign="top"><a href="#headers">headers</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">timeframe</td>
<td valign="top"><a href="#int">Int</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>zone_nodes</strong></td>
<td valign="top">[<a href="#zone_nodes">zone_nodes</a>!]!</td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">distinct_on</td>
<td valign="top">[<a href="#zone_nodes_select_column">zone_nodes_select_column</a>!]</td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">limit</td>
<td valign="top"><a href="#int">Int</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">offset</td>
<td valign="top"><a href="#int">Int</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">order_by</td>
<td valign="top">[<a href="#zone_nodes_order_by">zone_nodes_order_by</a>!]</td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">where</td>
<td valign="top"><a href="#zone_nodes_bool_exp">zone_nodes_bool_exp</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>zone_nodes_aggregate</strong></td>
<td valign="top"><a href="#zone_nodes_aggregate">zone_nodes_aggregate</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">distinct_on</td>
<td valign="top">[<a href="#zone_nodes_select_column">zone_nodes_select_column</a>!]</td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">limit</td>
<td valign="top"><a href="#int">Int</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">offset</td>
<td valign="top"><a href="#int">Int</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">order_by</td>
<td valign="top">[<a href="#zone_nodes_order_by">zone_nodes_order_by</a>!]</td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">where</td>
<td valign="top"><a href="#zone_nodes_bool_exp">zone_nodes_bool_exp</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>zone_nodes_by_pk</strong></td>
<td valign="top"><a href="#zone_nodes">zone_nodes</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">rpc_addr</td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>zones_graphs</strong></td>
<td valign="top">[<a href="#zones_graphs">zones_graphs</a>!]!</td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">distinct_on</td>
<td valign="top">[<a href="#zones_graphs_select_column">zones_graphs_select_column</a>!]</td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">limit</td>
<td valign="top"><a href="#int">Int</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">offset</td>
<td valign="top"><a href="#int">Int</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">order_by</td>
<td valign="top">[<a href="#zones_graphs_order_by">zones_graphs_order_by</a>!]</td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">where</td>
<td valign="top"><a href="#zones_graphs_bool_exp">zones_graphs_bool_exp</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>zones_graphs_aggregate</strong></td>
<td valign="top"><a href="#zones_graphs_aggregate">zones_graphs_aggregate</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">distinct_on</td>
<td valign="top">[<a href="#zones_graphs_select_column">zones_graphs_select_column</a>!]</td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">limit</td>
<td valign="top"><a href="#int">Int</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">offset</td>
<td valign="top"><a href="#int">Int</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">order_by</td>
<td valign="top">[<a href="#zones_graphs_order_by">zones_graphs_order_by</a>!]</td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">where</td>
<td valign="top"><a href="#zones_graphs_bool_exp">zones_graphs_bool_exp</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>zones_graphs_by_pk</strong></td>
<td valign="top"><a href="#zones_graphs">zones_graphs</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">source</td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">target</td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">timeframe</td>
<td valign="top"><a href="#int">Int</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>zones_stats</strong></td>
<td valign="top">[<a href="#zones_stats">zones_stats</a>!]!</td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">distinct_on</td>
<td valign="top">[<a href="#zones_stats_select_column">zones_stats_select_column</a>!]</td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">limit</td>
<td valign="top"><a href="#int">Int</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">offset</td>
<td valign="top"><a href="#int">Int</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">order_by</td>
<td valign="top">[<a href="#zones_stats_order_by">zones_stats_order_by</a>!]</td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">where</td>
<td valign="top"><a href="#zones_stats_bool_exp">zones_stats_bool_exp</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>zones_stats_aggregate</strong></td>
<td valign="top"><a href="#zones_stats_aggregate">zones_stats_aggregate</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">distinct_on</td>
<td valign="top">[<a href="#zones_stats_select_column">zones_stats_select_column</a>!]</td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">limit</td>
<td valign="top"><a href="#int">Int</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">offset</td>
<td valign="top"><a href="#int">Int</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">order_by</td>
<td valign="top">[<a href="#zones_stats_order_by">zones_stats_order_by</a>!]</td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">where</td>
<td valign="top"><a href="#zones_stats_bool_exp">zones_stats_bool_exp</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>zones_stats_by_pk</strong></td>
<td valign="top"><a href="#zones_stats">zones_stats</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">timeframe</td>
<td valign="top"><a href="#int">Int</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">zone</td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
</tbody>
</table>

### zone_nodes

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>is_alive</strong></td>
<td valign="top"><a href="#boolean">Boolean</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>last_checked_at</strong></td>
<td valign="top"><a href="#timestamp">timestamp</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>rpc_addr</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>zone</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
</tbody>
</table>

### zone_nodes_aggregate

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>aggregate</strong></td>
<td valign="top"><a href="#zone_nodes_aggregate_fields">zone_nodes_aggregate_fields</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>nodes</strong></td>
<td valign="top">[<a href="#zone_nodes">zone_nodes</a>!]!</td>
<td></td>
</tr>
</tbody>
</table>

### zone_nodes_aggregate_fields

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>count</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">columns</td>
<td valign="top">[<a href="#zone_nodes_select_column">zone_nodes_select_column</a>!]</td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">distinct</td>
<td valign="top"><a href="#boolean">Boolean</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>max</strong></td>
<td valign="top"><a href="#zone_nodes_max_fields">zone_nodes_max_fields</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>min</strong></td>
<td valign="top"><a href="#zone_nodes_min_fields">zone_nodes_min_fields</a></td>
<td></td>
</tr>
</tbody>
</table>

### zone_nodes_max_fields

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>last_checked_at</strong></td>
<td valign="top"><a href="#timestamp">timestamp</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>rpc_addr</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>zone</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td></td>
</tr>
</tbody>
</table>

### zone_nodes_min_fields

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>last_checked_at</strong></td>
<td valign="top"><a href="#timestamp">timestamp</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>rpc_addr</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>zone</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td></td>
</tr>
</tbody>
</table>

### zones_graphs

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>channels_cnt_active</strong></td>
<td valign="top"><a href="#int">Int</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>channels_cnt_open</strong></td>
<td valign="top"><a href="#int">Int</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>channels_percent_active</strong></td>
<td valign="top"><a href="#numeric">numeric</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>source</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>target</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>timeframe</strong></td>
<td valign="top"><a href="#int">Int</a>!</td>
<td></td>
</tr>
</tbody>
</table>

### zones_graphs_aggregate

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>aggregate</strong></td>
<td valign="top"><a href="#zones_graphs_aggregate_fields">zones_graphs_aggregate_fields</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>nodes</strong></td>
<td valign="top">[<a href="#zones_graphs">zones_graphs</a>!]!</td>
<td></td>
</tr>
</tbody>
</table>

### zones_graphs_aggregate_fields

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>avg</strong></td>
<td valign="top"><a href="#zones_graphs_avg_fields">zones_graphs_avg_fields</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>count</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">columns</td>
<td valign="top">[<a href="#zones_graphs_select_column">zones_graphs_select_column</a>!]</td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">distinct</td>
<td valign="top"><a href="#boolean">Boolean</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>max</strong></td>
<td valign="top"><a href="#zones_graphs_max_fields">zones_graphs_max_fields</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>min</strong></td>
<td valign="top"><a href="#zones_graphs_min_fields">zones_graphs_min_fields</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>stddev</strong></td>
<td valign="top"><a href="#zones_graphs_stddev_fields">zones_graphs_stddev_fields</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>stddev_pop</strong></td>
<td valign="top"><a href="#zones_graphs_stddev_pop_fields">zones_graphs_stddev_pop_fields</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>stddev_samp</strong></td>
<td valign="top"><a href="#zones_graphs_stddev_samp_fields">zones_graphs_stddev_samp_fields</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>sum</strong></td>
<td valign="top"><a href="#zones_graphs_sum_fields">zones_graphs_sum_fields</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>var_pop</strong></td>
<td valign="top"><a href="#zones_graphs_var_pop_fields">zones_graphs_var_pop_fields</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>var_samp</strong></td>
<td valign="top"><a href="#zones_graphs_var_samp_fields">zones_graphs_var_samp_fields</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>variance</strong></td>
<td valign="top"><a href="#zones_graphs_variance_fields">zones_graphs_variance_fields</a></td>
<td></td>
</tr>
</tbody>
</table>

### zones_graphs_avg_fields

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>channels_cnt_active</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>channels_cnt_open</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>channels_percent_active</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>timeframe</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
</tbody>
</table>

### zones_graphs_max_fields

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>channels_cnt_active</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>channels_cnt_open</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>channels_percent_active</strong></td>
<td valign="top"><a href="#numeric">numeric</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>source</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>target</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>timeframe</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td></td>
</tr>
</tbody>
</table>

### zones_graphs_min_fields

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>channels_cnt_active</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>channels_cnt_open</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>channels_percent_active</strong></td>
<td valign="top"><a href="#numeric">numeric</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>source</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>target</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>timeframe</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td></td>
</tr>
</tbody>
</table>

### zones_graphs_stddev_fields

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>channels_cnt_active</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>channels_cnt_open</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>channels_percent_active</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>timeframe</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
</tbody>
</table>

### zones_graphs_stddev_pop_fields

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>channels_cnt_active</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>channels_cnt_open</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>channels_percent_active</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>timeframe</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
</tbody>
</table>

### zones_graphs_stddev_samp_fields

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>channels_cnt_active</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>channels_cnt_open</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>channels_percent_active</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>timeframe</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
</tbody>
</table>

### zones_graphs_sum_fields

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>channels_cnt_active</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>channels_cnt_open</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>channels_percent_active</strong></td>
<td valign="top"><a href="#numeric">numeric</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>timeframe</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td></td>
</tr>
</tbody>
</table>

### zones_graphs_var_pop_fields

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>channels_cnt_active</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>channels_cnt_open</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>channels_percent_active</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>timeframe</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
</tbody>
</table>

### zones_graphs_var_samp_fields

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>channels_cnt_active</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>channels_cnt_open</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>channels_percent_active</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>timeframe</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
</tbody>
</table>

### zones_graphs_variance_fields

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>channels_cnt_active</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>channels_cnt_open</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>channels_percent_active</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>timeframe</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
</tbody>
</table>

### zones_stats

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>channels_cnt_active_period</strong></td>
<td valign="top"><a href="#int">Int</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>channels_cnt_active_period_diff</strong></td>
<td valign="top"><a href="#int">Int</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>channels_cnt_open</strong></td>
<td valign="top"><a href="#int">Int</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>channels_num</strong></td>
<td valign="top"><a href="#int">Int</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>channels_percent_active_period</strong></td>
<td valign="top"><a href="#int">Int</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>channels_percent_active_period_diff</strong></td>
<td valign="top"><a href="#int">Int</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>chart</strong></td>
<td valign="top"><a href="#jsonb">jsonb</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">path</td>
<td valign="top"><a href="#string">String</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_percent</strong></td>
<td valign="top"><a href="#numeric">numeric</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_failed</strong></td>
<td valign="top"><a href="#int">Int</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_failed_diff</strong></td>
<td valign="top"><a href="#int">Int</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_in</strong></td>
<td valign="top"><a href="#int">Int</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_in_diff</strong></td>
<td valign="top"><a href="#int">Int</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_in_failed</strong></td>
<td valign="top"><a href="#int">Int</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_in_rating</strong></td>
<td valign="top"><a href="#int">Int</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_in_rating_diff</strong></td>
<td valign="top"><a href="#int">Int</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_in_weight</strong></td>
<td valign="top"><a href="#numeric">numeric</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_out</strong></td>
<td valign="top"><a href="#int">Int</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_out_diff</strong></td>
<td valign="top"><a href="#int">Int</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_out_failed</strong></td>
<td valign="top"><a href="#int">Int</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_out_rating</strong></td>
<td valign="top"><a href="#int">Int</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_out_rating_diff</strong></td>
<td valign="top"><a href="#int">Int</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_out_weight</strong></td>
<td valign="top"><a href="#numeric">numeric</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>relations_cnt_open</strong></td>
<td valign="top"><a href="#int">Int</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>timeframe</strong></td>
<td valign="top"><a href="#int">Int</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_active_addresses</strong></td>
<td valign="top"><a href="#int">Int</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_active_addresses_diff</strong></td>
<td valign="top"><a href="#int">Int</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_active_addresses_rating</strong></td>
<td valign="top"><a href="#int">Int</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_active_addresses_rating_diff</strong></td>
<td valign="top"><a href="#int">Int</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_active_addresses_weight</strong></td>
<td valign="top"><a href="#numeric">numeric</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_coin_turnover_amount</strong></td>
<td valign="top"><a href="#numeric">numeric</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_coin_turnover_amount_diff</strong></td>
<td valign="top"><a href="#numeric">numeric</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_ibc_txs</strong></td>
<td valign="top"><a href="#int">Int</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_ibc_txs_diff</strong></td>
<td valign="top"><a href="#int">Int</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_ibc_txs_rating</strong></td>
<td valign="top"><a href="#int">Int</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_ibc_txs_rating_diff</strong></td>
<td valign="top"><a href="#int">Int</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_ibc_txs_weight</strong></td>
<td valign="top"><a href="#numeric">numeric</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_txs</strong></td>
<td valign="top"><a href="#int">Int</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_txs_diff</strong></td>
<td valign="top"><a href="#int">Int</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_txs_rating</strong></td>
<td valign="top"><a href="#int">Int</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_txs_rating_diff</strong></td>
<td valign="top"><a href="#int">Int</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_txs_weight</strong></td>
<td valign="top"><a href="#numeric">numeric</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>zone</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
</tbody>
</table>

### zones_stats_aggregate

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>aggregate</strong></td>
<td valign="top"><a href="#zones_stats_aggregate_fields">zones_stats_aggregate_fields</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>nodes</strong></td>
<td valign="top">[<a href="#zones_stats">zones_stats</a>!]!</td>
<td></td>
</tr>
</tbody>
</table>

### zones_stats_aggregate_fields

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>avg</strong></td>
<td valign="top"><a href="#zones_stats_avg_fields">zones_stats_avg_fields</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>count</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">columns</td>
<td valign="top">[<a href="#zones_stats_select_column">zones_stats_select_column</a>!]</td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">distinct</td>
<td valign="top"><a href="#boolean">Boolean</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>max</strong></td>
<td valign="top"><a href="#zones_stats_max_fields">zones_stats_max_fields</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>min</strong></td>
<td valign="top"><a href="#zones_stats_min_fields">zones_stats_min_fields</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>stddev</strong></td>
<td valign="top"><a href="#zones_stats_stddev_fields">zones_stats_stddev_fields</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>stddev_pop</strong></td>
<td valign="top"><a href="#zones_stats_stddev_pop_fields">zones_stats_stddev_pop_fields</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>stddev_samp</strong></td>
<td valign="top"><a href="#zones_stats_stddev_samp_fields">zones_stats_stddev_samp_fields</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>sum</strong></td>
<td valign="top"><a href="#zones_stats_sum_fields">zones_stats_sum_fields</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>var_pop</strong></td>
<td valign="top"><a href="#zones_stats_var_pop_fields">zones_stats_var_pop_fields</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>var_samp</strong></td>
<td valign="top"><a href="#zones_stats_var_samp_fields">zones_stats_var_samp_fields</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>variance</strong></td>
<td valign="top"><a href="#zones_stats_variance_fields">zones_stats_variance_fields</a></td>
<td></td>
</tr>
</tbody>
</table>

### zones_stats_avg_fields

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>channels_cnt_active_period</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>channels_cnt_active_period_diff</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>channels_cnt_open</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>channels_num</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>channels_percent_active_period</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>channels_percent_active_period_diff</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_percent</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_failed</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_failed_diff</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_in</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_in_diff</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_in_failed</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_in_rating</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_in_rating_diff</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_in_weight</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_out</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_out_diff</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_out_failed</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_out_rating</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_out_rating_diff</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_out_weight</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>relations_cnt_open</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>timeframe</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_active_addresses</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_active_addresses_diff</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_active_addresses_rating</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_active_addresses_rating_diff</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_active_addresses_weight</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_coin_turnover_amount</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_coin_turnover_amount_diff</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_ibc_txs</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_ibc_txs_diff</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_ibc_txs_rating</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_ibc_txs_rating_diff</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_ibc_txs_weight</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_txs</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_txs_diff</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_txs_rating</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_txs_rating_diff</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_txs_weight</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
</tbody>
</table>

### zones_stats_max_fields

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>channels_cnt_active_period</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>channels_cnt_active_period_diff</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>channels_cnt_open</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>channels_num</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>channels_percent_active_period</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>channels_percent_active_period_diff</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_percent</strong></td>
<td valign="top"><a href="#numeric">numeric</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_failed</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_failed_diff</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_in</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_in_diff</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_in_failed</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_in_rating</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_in_rating_diff</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_in_weight</strong></td>
<td valign="top"><a href="#numeric">numeric</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_out</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_out_diff</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_out_failed</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_out_rating</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_out_rating_diff</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_out_weight</strong></td>
<td valign="top"><a href="#numeric">numeric</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>relations_cnt_open</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>timeframe</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_active_addresses</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_active_addresses_diff</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_active_addresses_rating</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_active_addresses_rating_diff</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_active_addresses_weight</strong></td>
<td valign="top"><a href="#numeric">numeric</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_coin_turnover_amount</strong></td>
<td valign="top"><a href="#numeric">numeric</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_coin_turnover_amount_diff</strong></td>
<td valign="top"><a href="#numeric">numeric</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_ibc_txs</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_ibc_txs_diff</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_ibc_txs_rating</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_ibc_txs_rating_diff</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_ibc_txs_weight</strong></td>
<td valign="top"><a href="#numeric">numeric</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_txs</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_txs_diff</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_txs_rating</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_txs_rating_diff</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_txs_weight</strong></td>
<td valign="top"><a href="#numeric">numeric</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>zone</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td></td>
</tr>
</tbody>
</table>

### zones_stats_min_fields

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>channels_cnt_active_period</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>channels_cnt_active_period_diff</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>channels_cnt_open</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>channels_num</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>channels_percent_active_period</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>channels_percent_active_period_diff</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_percent</strong></td>
<td valign="top"><a href="#numeric">numeric</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_failed</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_failed_diff</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_in</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_in_diff</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_in_failed</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_in_rating</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_in_rating_diff</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_in_weight</strong></td>
<td valign="top"><a href="#numeric">numeric</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_out</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_out_diff</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_out_failed</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_out_rating</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_out_rating_diff</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_out_weight</strong></td>
<td valign="top"><a href="#numeric">numeric</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>relations_cnt_open</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>timeframe</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_active_addresses</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_active_addresses_diff</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_active_addresses_rating</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_active_addresses_rating_diff</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_active_addresses_weight</strong></td>
<td valign="top"><a href="#numeric">numeric</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_coin_turnover_amount</strong></td>
<td valign="top"><a href="#numeric">numeric</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_coin_turnover_amount_diff</strong></td>
<td valign="top"><a href="#numeric">numeric</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_ibc_txs</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_ibc_txs_diff</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_ibc_txs_rating</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_ibc_txs_rating_diff</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_ibc_txs_weight</strong></td>
<td valign="top"><a href="#numeric">numeric</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_txs</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_txs_diff</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_txs_rating</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_txs_rating_diff</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_txs_weight</strong></td>
<td valign="top"><a href="#numeric">numeric</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>zone</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td></td>
</tr>
</tbody>
</table>

### zones_stats_stddev_fields

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>channels_cnt_active_period</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>channels_cnt_active_period_diff</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>channels_cnt_open</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>channels_num</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>channels_percent_active_period</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>channels_percent_active_period_diff</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_percent</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_failed</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_failed_diff</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_in</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_in_diff</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_in_failed</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_in_rating</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_in_rating_diff</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_in_weight</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_out</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_out_diff</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_out_failed</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_out_rating</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_out_rating_diff</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_out_weight</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>relations_cnt_open</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>timeframe</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_active_addresses</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_active_addresses_diff</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_active_addresses_rating</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_active_addresses_rating_diff</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_active_addresses_weight</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_coin_turnover_amount</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_coin_turnover_amount_diff</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_ibc_txs</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_ibc_txs_diff</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_ibc_txs_rating</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_ibc_txs_rating_diff</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_ibc_txs_weight</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_txs</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_txs_diff</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_txs_rating</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_txs_rating_diff</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_txs_weight</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
</tbody>
</table>

### zones_stats_stddev_pop_fields

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>channels_cnt_active_period</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>channels_cnt_active_period_diff</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>channels_cnt_open</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>channels_num</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>channels_percent_active_period</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>channels_percent_active_period_diff</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_percent</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_failed</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_failed_diff</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_in</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_in_diff</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_in_failed</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_in_rating</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_in_rating_diff</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_in_weight</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_out</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_out_diff</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_out_failed</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_out_rating</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_out_rating_diff</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_out_weight</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>relations_cnt_open</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>timeframe</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_active_addresses</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_active_addresses_diff</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_active_addresses_rating</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_active_addresses_rating_diff</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_active_addresses_weight</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_coin_turnover_amount</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_coin_turnover_amount_diff</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_ibc_txs</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_ibc_txs_diff</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_ibc_txs_rating</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_ibc_txs_rating_diff</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_ibc_txs_weight</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_txs</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_txs_diff</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_txs_rating</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_txs_rating_diff</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_txs_weight</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
</tbody>
</table>

### zones_stats_stddev_samp_fields

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>channels_cnt_active_period</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>channels_cnt_active_period_diff</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>channels_cnt_open</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>channels_num</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>channels_percent_active_period</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>channels_percent_active_period_diff</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_percent</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_failed</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_failed_diff</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_in</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_in_diff</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_in_failed</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_in_rating</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_in_rating_diff</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_in_weight</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_out</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_out_diff</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_out_failed</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_out_rating</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_out_rating_diff</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_out_weight</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>relations_cnt_open</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>timeframe</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_active_addresses</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_active_addresses_diff</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_active_addresses_rating</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_active_addresses_rating_diff</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_active_addresses_weight</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_coin_turnover_amount</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_coin_turnover_amount_diff</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_ibc_txs</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_ibc_txs_diff</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_ibc_txs_rating</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_ibc_txs_rating_diff</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_ibc_txs_weight</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_txs</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_txs_diff</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_txs_rating</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_txs_rating_diff</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_txs_weight</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
</tbody>
</table>

### zones_stats_sum_fields

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>channels_cnt_active_period</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>channels_cnt_active_period_diff</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>channels_cnt_open</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>channels_num</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>channels_percent_active_period</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>channels_percent_active_period_diff</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_percent</strong></td>
<td valign="top"><a href="#numeric">numeric</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_failed</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_failed_diff</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_in</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_in_diff</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_in_failed</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_in_rating</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_in_rating_diff</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_in_weight</strong></td>
<td valign="top"><a href="#numeric">numeric</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_out</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_out_diff</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_out_failed</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_out_rating</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_out_rating_diff</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_out_weight</strong></td>
<td valign="top"><a href="#numeric">numeric</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>relations_cnt_open</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>timeframe</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_active_addresses</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_active_addresses_diff</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_active_addresses_rating</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_active_addresses_rating_diff</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_active_addresses_weight</strong></td>
<td valign="top"><a href="#numeric">numeric</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_coin_turnover_amount</strong></td>
<td valign="top"><a href="#numeric">numeric</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_coin_turnover_amount_diff</strong></td>
<td valign="top"><a href="#numeric">numeric</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_ibc_txs</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_ibc_txs_diff</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_ibc_txs_rating</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_ibc_txs_rating_diff</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_ibc_txs_weight</strong></td>
<td valign="top"><a href="#numeric">numeric</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_txs</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_txs_diff</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_txs_rating</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_txs_rating_diff</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_txs_weight</strong></td>
<td valign="top"><a href="#numeric">numeric</a></td>
<td></td>
</tr>
</tbody>
</table>

### zones_stats_var_pop_fields

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>channels_cnt_active_period</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>channels_cnt_active_period_diff</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>channels_cnt_open</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>channels_num</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>channels_percent_active_period</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>channels_percent_active_period_diff</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_percent</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_failed</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_failed_diff</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_in</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_in_diff</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_in_failed</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_in_rating</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_in_rating_diff</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_in_weight</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_out</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_out_diff</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_out_failed</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_out_rating</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_out_rating_diff</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_out_weight</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>relations_cnt_open</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>timeframe</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_active_addresses</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_active_addresses_diff</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_active_addresses_rating</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_active_addresses_rating_diff</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_active_addresses_weight</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_coin_turnover_amount</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_coin_turnover_amount_diff</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_ibc_txs</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_ibc_txs_diff</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_ibc_txs_rating</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_ibc_txs_rating_diff</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_ibc_txs_weight</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_txs</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_txs_diff</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_txs_rating</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_txs_rating_diff</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_txs_weight</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
</tbody>
</table>

### zones_stats_var_samp_fields

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>channels_cnt_active_period</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>channels_cnt_active_period_diff</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>channels_cnt_open</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>channels_num</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>channels_percent_active_period</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>channels_percent_active_period_diff</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_percent</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_failed</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_failed_diff</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_in</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_in_diff</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_in_failed</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_in_rating</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_in_rating_diff</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_in_weight</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_out</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_out_diff</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_out_failed</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_out_rating</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_out_rating_diff</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_out_weight</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>relations_cnt_open</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>timeframe</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_active_addresses</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_active_addresses_diff</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_active_addresses_rating</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_active_addresses_rating_diff</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_active_addresses_weight</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_coin_turnover_amount</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_coin_turnover_amount_diff</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_ibc_txs</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_ibc_txs_diff</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_ibc_txs_rating</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_ibc_txs_rating_diff</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_ibc_txs_weight</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_txs</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_txs_diff</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_txs_rating</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_txs_rating_diff</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_txs_weight</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
</tbody>
</table>

### zones_stats_variance_fields

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>channels_cnt_active_period</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>channels_cnt_active_period_diff</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>channels_cnt_open</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>channels_num</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>channels_percent_active_period</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>channels_percent_active_period_diff</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_percent</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_failed</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_failed_diff</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_in</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_in_diff</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_in_failed</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_in_rating</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_in_rating_diff</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_in_weight</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_out</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_out_diff</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_out_failed</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_out_rating</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_out_rating_diff</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_out_weight</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>relations_cnt_open</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>timeframe</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_active_addresses</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_active_addresses_diff</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_active_addresses_rating</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_active_addresses_rating_diff</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_active_addresses_weight</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_coin_turnover_amount</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_coin_turnover_amount_diff</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_ibc_txs</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_ibc_txs_diff</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_ibc_txs_rating</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_ibc_txs_rating_diff</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_ibc_txs_weight</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_txs</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_txs_diff</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_txs_rating</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_txs_rating_diff</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_txs_weight</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
</tbody>
</table>

## Inputs

### Boolean_comparison_exp

<table>
<thead>
<tr>
<th colspan="2" align="left">Field</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>_eq</strong></td>
<td valign="top"><a href="#boolean">Boolean</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>_gt</strong></td>
<td valign="top"><a href="#boolean">Boolean</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>_gte</strong></td>
<td valign="top"><a href="#boolean">Boolean</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>_in</strong></td>
<td valign="top">[<a href="#boolean">Boolean</a>!]</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>_is_null</strong></td>
<td valign="top"><a href="#boolean">Boolean</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>_lt</strong></td>
<td valign="top"><a href="#boolean">Boolean</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>_lte</strong></td>
<td valign="top"><a href="#boolean">Boolean</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>_neq</strong></td>
<td valign="top"><a href="#boolean">Boolean</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>_nin</strong></td>
<td valign="top">[<a href="#boolean">Boolean</a>!]</td>
<td></td>
</tr>
</tbody>
</table>

### Int_comparison_exp

<table>
<thead>
<tr>
<th colspan="2" align="left">Field</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>_eq</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>_gt</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>_gte</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>_in</strong></td>
<td valign="top">[<a href="#int">Int</a>!]</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>_is_null</strong></td>
<td valign="top"><a href="#boolean">Boolean</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>_lt</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>_lte</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>_neq</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>_nin</strong></td>
<td valign="top">[<a href="#int">Int</a>!]</td>
<td></td>
</tr>
</tbody>
</table>

### String_comparison_exp

<table>
<thead>
<tr>
<th colspan="2" align="left">Field</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>_eq</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>_gt</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>_gte</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>_ilike</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>_in</strong></td>
<td valign="top">[<a href="#string">String</a>!]</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>_is_null</strong></td>
<td valign="top"><a href="#boolean">Boolean</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>_like</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>_lt</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>_lte</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>_neq</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>_nilike</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>_nin</strong></td>
<td valign="top">[<a href="#string">String</a>!]</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>_nlike</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>_nsimilar</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>_similar</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td></td>
</tr>
</tbody>
</table>

### blocks_log_bool_exp

<table>
<thead>
<tr>
<th colspan="2" align="left">Field</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>_and</strong></td>
<td valign="top">[<a href="#blocks_log_bool_exp">blocks_log_bool_exp</a>]</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>_not</strong></td>
<td valign="top"><a href="#blocks_log_bool_exp">blocks_log_bool_exp</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>_or</strong></td>
<td valign="top">[<a href="#blocks_log_bool_exp">blocks_log_bool_exp</a>]</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>last_processed_block</strong></td>
<td valign="top"><a href="#int_comparison_exp">Int_comparison_exp</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>last_updated_at</strong></td>
<td valign="top"><a href="#timestamp_comparison_exp">timestamp_comparison_exp</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>zone</strong></td>
<td valign="top"><a href="#string_comparison_exp">String_comparison_exp</a></td>
<td></td>
</tr>
</tbody>
</table>

### blocks_log_order_by

<table>
<thead>
<tr>
<th colspan="2" align="left">Field</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>last_processed_block</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>last_updated_at</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>zone</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
</tbody>
</table>

### blocks_log_pk_columns_input

<table>
<thead>
<tr>
<th colspan="2" align="left">Field</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>zone</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
</tbody>
</table>

### channels_stats_aggregate_order_by

<table>
<thead>
<tr>
<th colspan="2" align="left">Field</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>avg</strong></td>
<td valign="top"><a href="#channels_stats_avg_order_by">channels_stats_avg_order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>count</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>max</strong></td>
<td valign="top"><a href="#channels_stats_max_order_by">channels_stats_max_order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>min</strong></td>
<td valign="top"><a href="#channels_stats_min_order_by">channels_stats_min_order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>stddev</strong></td>
<td valign="top"><a href="#channels_stats_stddev_order_by">channels_stats_stddev_order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>stddev_pop</strong></td>
<td valign="top"><a href="#channels_stats_stddev_pop_order_by">channels_stats_stddev_pop_order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>stddev_samp</strong></td>
<td valign="top"><a href="#channels_stats_stddev_samp_order_by">channels_stats_stddev_samp_order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>sum</strong></td>
<td valign="top"><a href="#channels_stats_sum_order_by">channels_stats_sum_order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>var_pop</strong></td>
<td valign="top"><a href="#channels_stats_var_pop_order_by">channels_stats_var_pop_order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>var_samp</strong></td>
<td valign="top"><a href="#channels_stats_var_samp_order_by">channels_stats_var_samp_order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>variance</strong></td>
<td valign="top"><a href="#channels_stats_variance_order_by">channels_stats_variance_order_by</a></td>
<td></td>
</tr>
</tbody>
</table>

### channels_stats_avg_order_by

<table>
<thead>
<tr>
<th colspan="2" align="left">Field</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_1d</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_1d_diff</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_1d_failed</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_1d_failed_diff</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_30d</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_30d_diff</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_30d_failed</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_30d_failed_diff</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_7d</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_7d_diff</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_7d_failed</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_7d_failed_diff</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
</tbody>
</table>

### channels_stats_bool_exp

<table>
<thead>
<tr>
<th colspan="2" align="left">Field</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>_and</strong></td>
<td valign="top">[<a href="#channels_stats_bool_exp">channels_stats_bool_exp</a>]</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>_not</strong></td>
<td valign="top"><a href="#channels_stats_bool_exp">channels_stats_bool_exp</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>_or</strong></td>
<td valign="top">[<a href="#channels_stats_bool_exp">channels_stats_bool_exp</a>]</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>channel_id</strong></td>
<td valign="top"><a href="#string_comparison_exp">String_comparison_exp</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>client_id</strong></td>
<td valign="top"><a href="#string_comparison_exp">String_comparison_exp</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>connection_id</strong></td>
<td valign="top"><a href="#string_comparison_exp">String_comparison_exp</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_1d</strong></td>
<td valign="top"><a href="#int_comparison_exp">Int_comparison_exp</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_1d_diff</strong></td>
<td valign="top"><a href="#int_comparison_exp">Int_comparison_exp</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_1d_failed</strong></td>
<td valign="top"><a href="#int_comparison_exp">Int_comparison_exp</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_1d_failed_diff</strong></td>
<td valign="top"><a href="#int_comparison_exp">Int_comparison_exp</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_30d</strong></td>
<td valign="top"><a href="#int_comparison_exp">Int_comparison_exp</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_30d_diff</strong></td>
<td valign="top"><a href="#int_comparison_exp">Int_comparison_exp</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_30d_failed</strong></td>
<td valign="top"><a href="#int_comparison_exp">Int_comparison_exp</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_30d_failed_diff</strong></td>
<td valign="top"><a href="#int_comparison_exp">Int_comparison_exp</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_7d</strong></td>
<td valign="top"><a href="#int_comparison_exp">Int_comparison_exp</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_7d_diff</strong></td>
<td valign="top"><a href="#int_comparison_exp">Int_comparison_exp</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_7d_failed</strong></td>
<td valign="top"><a href="#int_comparison_exp">Int_comparison_exp</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_7d_failed_diff</strong></td>
<td valign="top"><a href="#int_comparison_exp">Int_comparison_exp</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>is_opened</strong></td>
<td valign="top"><a href="#boolean_comparison_exp">Boolean_comparison_exp</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>zone</strong></td>
<td valign="top"><a href="#string_comparison_exp">String_comparison_exp</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>zone_counerparty</strong></td>
<td valign="top"><a href="#string_comparison_exp">String_comparison_exp</a></td>
<td></td>
</tr>
</tbody>
</table>

### channels_stats_max_order_by

<table>
<thead>
<tr>
<th colspan="2" align="left">Field</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>channel_id</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>client_id</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>connection_id</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_1d</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_1d_diff</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_1d_failed</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_1d_failed_diff</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_30d</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_30d_diff</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_30d_failed</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_30d_failed_diff</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_7d</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_7d_diff</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_7d_failed</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_7d_failed_diff</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>zone</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>zone_counerparty</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
</tbody>
</table>

### channels_stats_min_order_by

<table>
<thead>
<tr>
<th colspan="2" align="left">Field</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>channel_id</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>client_id</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>connection_id</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_1d</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_1d_diff</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_1d_failed</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_1d_failed_diff</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_30d</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_30d_diff</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_30d_failed</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_30d_failed_diff</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_7d</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_7d_diff</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_7d_failed</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_7d_failed_diff</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>zone</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>zone_counerparty</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
</tbody>
</table>

### channels_stats_order_by

<table>
<thead>
<tr>
<th colspan="2" align="left">Field</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>channel_id</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>client_id</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>connection_id</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_1d</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_1d_diff</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_1d_failed</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_1d_failed_diff</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_30d</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_30d_diff</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_30d_failed</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_30d_failed_diff</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_7d</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_7d_diff</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_7d_failed</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_7d_failed_diff</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>is_opened</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>zone</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>zone_counerparty</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
</tbody>
</table>

### channels_stats_pk_columns_input

<table>
<thead>
<tr>
<th colspan="2" align="left">Field</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>channel_id</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>client_id</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>connection_id</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>zone</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
</tbody>
</table>

### channels_stats_stddev_order_by

<table>
<thead>
<tr>
<th colspan="2" align="left">Field</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_1d</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_1d_diff</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_1d_failed</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_1d_failed_diff</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_30d</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_30d_diff</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_30d_failed</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_30d_failed_diff</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_7d</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_7d_diff</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_7d_failed</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_7d_failed_diff</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
</tbody>
</table>

### channels_stats_stddev_pop_order_by

<table>
<thead>
<tr>
<th colspan="2" align="left">Field</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_1d</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_1d_diff</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_1d_failed</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_1d_failed_diff</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_30d</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_30d_diff</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_30d_failed</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_30d_failed_diff</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_7d</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_7d_diff</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_7d_failed</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_7d_failed_diff</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
</tbody>
</table>

### channels_stats_stddev_samp_order_by

<table>
<thead>
<tr>
<th colspan="2" align="left">Field</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_1d</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_1d_diff</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_1d_failed</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_1d_failed_diff</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_30d</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_30d_diff</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_30d_failed</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_30d_failed_diff</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_7d</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_7d_diff</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_7d_failed</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_7d_failed_diff</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
</tbody>
</table>

### channels_stats_sum_order_by

<table>
<thead>
<tr>
<th colspan="2" align="left">Field</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_1d</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_1d_diff</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_1d_failed</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_1d_failed_diff</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_30d</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_30d_diff</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_30d_failed</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_30d_failed_diff</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_7d</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_7d_diff</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_7d_failed</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_7d_failed_diff</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
</tbody>
</table>

### channels_stats_var_pop_order_by

<table>
<thead>
<tr>
<th colspan="2" align="left">Field</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_1d</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_1d_diff</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_1d_failed</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_1d_failed_diff</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_30d</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_30d_diff</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_30d_failed</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_30d_failed_diff</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_7d</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_7d_diff</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_7d_failed</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_7d_failed_diff</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
</tbody>
</table>

### channels_stats_var_samp_order_by

<table>
<thead>
<tr>
<th colspan="2" align="left">Field</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_1d</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_1d_diff</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_1d_failed</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_1d_failed_diff</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_30d</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_30d_diff</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_30d_failed</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_30d_failed_diff</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_7d</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_7d_diff</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_7d_failed</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_7d_failed_diff</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
</tbody>
</table>

### channels_stats_variance_order_by

<table>
<thead>
<tr>
<th colspan="2" align="left">Field</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_1d</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_1d_diff</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_1d_failed</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_1d_failed_diff</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_30d</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_30d_diff</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_30d_failed</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_30d_failed_diff</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_7d</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_7d_diff</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_7d_failed</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_7d_failed_diff</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
</tbody>
</table>

### headers_aggregate_order_by

<table>
<thead>
<tr>
<th colspan="2" align="left">Field</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>avg</strong></td>
<td valign="top"><a href="#headers_avg_order_by">headers_avg_order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>count</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>max</strong></td>
<td valign="top"><a href="#headers_max_order_by">headers_max_order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>min</strong></td>
<td valign="top"><a href="#headers_min_order_by">headers_min_order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>stddev</strong></td>
<td valign="top"><a href="#headers_stddev_order_by">headers_stddev_order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>stddev_pop</strong></td>
<td valign="top"><a href="#headers_stddev_pop_order_by">headers_stddev_pop_order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>stddev_samp</strong></td>
<td valign="top"><a href="#headers_stddev_samp_order_by">headers_stddev_samp_order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>sum</strong></td>
<td valign="top"><a href="#headers_sum_order_by">headers_sum_order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>var_pop</strong></td>
<td valign="top"><a href="#headers_var_pop_order_by">headers_var_pop_order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>var_samp</strong></td>
<td valign="top"><a href="#headers_var_samp_order_by">headers_var_samp_order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>variance</strong></td>
<td valign="top"><a href="#headers_variance_order_by">headers_variance_order_by</a></td>
<td></td>
</tr>
</tbody>
</table>

### headers_avg_order_by

<table>
<thead>
<tr>
<th colspan="2" align="left">Field</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>channels_cnt_active_period</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>channels_cnt_active_period_diff</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>channels_cnt_all</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>channels_cnt_open</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>channels_cnt_period</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>channels_percent_active_period</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>channels_percent_active_period_diff</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>relations_cnt_open</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>timeframe</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>zones_cnt_all</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>zones_cnt_period</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
</tbody>
</table>

### headers_bool_exp

<table>
<thead>
<tr>
<th colspan="2" align="left">Field</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>_and</strong></td>
<td valign="top">[<a href="#headers_bool_exp">headers_bool_exp</a>]</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>_not</strong></td>
<td valign="top"><a href="#headers_bool_exp">headers_bool_exp</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>_or</strong></td>
<td valign="top">[<a href="#headers_bool_exp">headers_bool_exp</a>]</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>channels_cnt_active_period</strong></td>
<td valign="top"><a href="#int_comparison_exp">Int_comparison_exp</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>channels_cnt_active_period_diff</strong></td>
<td valign="top"><a href="#int_comparison_exp">Int_comparison_exp</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>channels_cnt_all</strong></td>
<td valign="top"><a href="#int_comparison_exp">Int_comparison_exp</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>channels_cnt_open</strong></td>
<td valign="top"><a href="#int_comparison_exp">Int_comparison_exp</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>channels_cnt_period</strong></td>
<td valign="top"><a href="#int_comparison_exp">Int_comparison_exp</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>channels_percent_active_period</strong></td>
<td valign="top"><a href="#int_comparison_exp">Int_comparison_exp</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>channels_percent_active_period_diff</strong></td>
<td valign="top"><a href="#int_comparison_exp">Int_comparison_exp</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>chart</strong></td>
<td valign="top"><a href="#jsonb_comparison_exp">jsonb_comparison_exp</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>relations_cnt_open</strong></td>
<td valign="top"><a href="#int_comparison_exp">Int_comparison_exp</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>timeframe</strong></td>
<td valign="top"><a href="#int_comparison_exp">Int_comparison_exp</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>top_zone_pair</strong></td>
<td valign="top"><a href="#jsonb_comparison_exp">jsonb_comparison_exp</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>zones_cnt_all</strong></td>
<td valign="top"><a href="#int_comparison_exp">Int_comparison_exp</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>zones_cnt_period</strong></td>
<td valign="top"><a href="#int_comparison_exp">Int_comparison_exp</a></td>
<td></td>
</tr>
</tbody>
</table>

### headers_max_order_by

<table>
<thead>
<tr>
<th colspan="2" align="left">Field</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>channels_cnt_active_period</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>channels_cnt_active_period_diff</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>channels_cnt_all</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>channels_cnt_open</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>channels_cnt_period</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>channels_percent_active_period</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>channels_percent_active_period_diff</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>relations_cnt_open</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>timeframe</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>zones_cnt_all</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>zones_cnt_period</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
</tbody>
</table>

### headers_min_order_by

<table>
<thead>
<tr>
<th colspan="2" align="left">Field</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>channels_cnt_active_period</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>channels_cnt_active_period_diff</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>channels_cnt_all</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>channels_cnt_open</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>channels_cnt_period</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>channels_percent_active_period</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>channels_percent_active_period_diff</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>relations_cnt_open</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>timeframe</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>zones_cnt_all</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>zones_cnt_period</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
</tbody>
</table>

### headers_order_by

<table>
<thead>
<tr>
<th colspan="2" align="left">Field</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>channels_cnt_active_period</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>channels_cnt_active_period_diff</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>channels_cnt_all</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>channels_cnt_open</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>channels_cnt_period</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>channels_percent_active_period</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>channels_percent_active_period_diff</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>chart</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>relations_cnt_open</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>timeframe</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>top_zone_pair</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>zones_cnt_all</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>zones_cnt_period</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
</tbody>
</table>

### headers_pk_columns_input

<table>
<thead>
<tr>
<th colspan="2" align="left">Field</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>timeframe</strong></td>
<td valign="top"><a href="#int">Int</a>!</td>
<td></td>
</tr>
</tbody>
</table>

### headers_stddev_order_by

<table>
<thead>
<tr>
<th colspan="2" align="left">Field</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>channels_cnt_active_period</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>channels_cnt_active_period_diff</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>channels_cnt_all</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>channels_cnt_open</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>channels_cnt_period</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>channels_percent_active_period</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>channels_percent_active_period_diff</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>relations_cnt_open</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>timeframe</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>zones_cnt_all</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>zones_cnt_period</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
</tbody>
</table>

### headers_stddev_pop_order_by

<table>
<thead>
<tr>
<th colspan="2" align="left">Field</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>channels_cnt_active_period</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>channels_cnt_active_period_diff</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>channels_cnt_all</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>channels_cnt_open</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>channels_cnt_period</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>channels_percent_active_period</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>channels_percent_active_period_diff</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>relations_cnt_open</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>timeframe</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>zones_cnt_all</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>zones_cnt_period</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
</tbody>
</table>

### headers_stddev_samp_order_by

<table>
<thead>
<tr>
<th colspan="2" align="left">Field</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>channels_cnt_active_period</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>channels_cnt_active_period_diff</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>channels_cnt_all</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>channels_cnt_open</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>channels_cnt_period</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>channels_percent_active_period</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>channels_percent_active_period_diff</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>relations_cnt_open</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>timeframe</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>zones_cnt_all</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>zones_cnt_period</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
</tbody>
</table>

### headers_sum_order_by

<table>
<thead>
<tr>
<th colspan="2" align="left">Field</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>channels_cnt_active_period</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>channels_cnt_active_period_diff</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>channels_cnt_all</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>channels_cnt_open</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>channels_cnt_period</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>channels_percent_active_period</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>channels_percent_active_period_diff</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>relations_cnt_open</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>timeframe</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>zones_cnt_all</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>zones_cnt_period</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
</tbody>
</table>

### headers_var_pop_order_by

<table>
<thead>
<tr>
<th colspan="2" align="left">Field</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>channels_cnt_active_period</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>channels_cnt_active_period_diff</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>channels_cnt_all</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>channels_cnt_open</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>channels_cnt_period</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>channels_percent_active_period</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>channels_percent_active_period_diff</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>relations_cnt_open</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>timeframe</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>zones_cnt_all</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>zones_cnt_period</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
</tbody>
</table>

### headers_var_samp_order_by

<table>
<thead>
<tr>
<th colspan="2" align="left">Field</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>channels_cnt_active_period</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>channels_cnt_active_period_diff</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>channels_cnt_all</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>channels_cnt_open</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>channels_cnt_period</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>channels_percent_active_period</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>channels_percent_active_period_diff</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>relations_cnt_open</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>timeframe</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>zones_cnt_all</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>zones_cnt_period</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
</tbody>
</table>

### headers_variance_order_by

<table>
<thead>
<tr>
<th colspan="2" align="left">Field</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>channels_cnt_active_period</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>channels_cnt_active_period_diff</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>channels_cnt_all</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>channels_cnt_open</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>channels_cnt_period</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>channels_percent_active_period</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>channels_percent_active_period_diff</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>relations_cnt_open</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>timeframe</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>zones_cnt_all</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>zones_cnt_period</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
</tbody>
</table>

### jsonb_comparison_exp

<table>
<thead>
<tr>
<th colspan="2" align="left">Field</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>_contained_in</strong></td>
<td valign="top"><a href="#jsonb">jsonb</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>_contains</strong></td>
<td valign="top"><a href="#jsonb">jsonb</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>_eq</strong></td>
<td valign="top"><a href="#jsonb">jsonb</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>_gt</strong></td>
<td valign="top"><a href="#jsonb">jsonb</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>_gte</strong></td>
<td valign="top"><a href="#jsonb">jsonb</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>_has_key</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>_has_keys_all</strong></td>
<td valign="top">[<a href="#string">String</a>!]</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>_has_keys_any</strong></td>
<td valign="top">[<a href="#string">String</a>!]</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>_in</strong></td>
<td valign="top">[<a href="#jsonb">jsonb</a>!]</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>_is_null</strong></td>
<td valign="top"><a href="#boolean">Boolean</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>_lt</strong></td>
<td valign="top"><a href="#jsonb">jsonb</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>_lte</strong></td>
<td valign="top"><a href="#jsonb">jsonb</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>_neq</strong></td>
<td valign="top"><a href="#jsonb">jsonb</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>_nin</strong></td>
<td valign="top">[<a href="#jsonb">jsonb</a>!]</td>
<td></td>
</tr>
</tbody>
</table>

### numeric_comparison_exp

<table>
<thead>
<tr>
<th colspan="2" align="left">Field</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>_eq</strong></td>
<td valign="top"><a href="#numeric">numeric</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>_gt</strong></td>
<td valign="top"><a href="#numeric">numeric</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>_gte</strong></td>
<td valign="top"><a href="#numeric">numeric</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>_in</strong></td>
<td valign="top">[<a href="#numeric">numeric</a>!]</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>_is_null</strong></td>
<td valign="top"><a href="#boolean">Boolean</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>_lt</strong></td>
<td valign="top"><a href="#numeric">numeric</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>_lte</strong></td>
<td valign="top"><a href="#numeric">numeric</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>_neq</strong></td>
<td valign="top"><a href="#numeric">numeric</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>_nin</strong></td>
<td valign="top">[<a href="#numeric">numeric</a>!]</td>
<td></td>
</tr>
</tbody>
</table>

### timestamp_comparison_exp

<table>
<thead>
<tr>
<th colspan="2" align="left">Field</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>_eq</strong></td>
<td valign="top"><a href="#timestamp">timestamp</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>_gt</strong></td>
<td valign="top"><a href="#timestamp">timestamp</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>_gte</strong></td>
<td valign="top"><a href="#timestamp">timestamp</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>_in</strong></td>
<td valign="top">[<a href="#timestamp">timestamp</a>!]</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>_is_null</strong></td>
<td valign="top"><a href="#boolean">Boolean</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>_lt</strong></td>
<td valign="top"><a href="#timestamp">timestamp</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>_lte</strong></td>
<td valign="top"><a href="#timestamp">timestamp</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>_neq</strong></td>
<td valign="top"><a href="#timestamp">timestamp</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>_nin</strong></td>
<td valign="top">[<a href="#timestamp">timestamp</a>!]</td>
<td></td>
</tr>
</tbody>
</table>

### zone_nodes_aggregate_order_by

<table>
<thead>
<tr>
<th colspan="2" align="left">Field</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>count</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>max</strong></td>
<td valign="top"><a href="#zone_nodes_max_order_by">zone_nodes_max_order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>min</strong></td>
<td valign="top"><a href="#zone_nodes_min_order_by">zone_nodes_min_order_by</a></td>
<td></td>
</tr>
</tbody>
</table>

### zone_nodes_bool_exp

<table>
<thead>
<tr>
<th colspan="2" align="left">Field</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>_and</strong></td>
<td valign="top">[<a href="#zone_nodes_bool_exp">zone_nodes_bool_exp</a>]</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>_not</strong></td>
<td valign="top"><a href="#zone_nodes_bool_exp">zone_nodes_bool_exp</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>_or</strong></td>
<td valign="top">[<a href="#zone_nodes_bool_exp">zone_nodes_bool_exp</a>]</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>is_alive</strong></td>
<td valign="top"><a href="#boolean_comparison_exp">Boolean_comparison_exp</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>last_checked_at</strong></td>
<td valign="top"><a href="#timestamp_comparison_exp">timestamp_comparison_exp</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>rpc_addr</strong></td>
<td valign="top"><a href="#string_comparison_exp">String_comparison_exp</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>zone</strong></td>
<td valign="top"><a href="#string_comparison_exp">String_comparison_exp</a></td>
<td></td>
</tr>
</tbody>
</table>

### zone_nodes_max_order_by

<table>
<thead>
<tr>
<th colspan="2" align="left">Field</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>last_checked_at</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>rpc_addr</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>zone</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
</tbody>
</table>

### zone_nodes_min_order_by

<table>
<thead>
<tr>
<th colspan="2" align="left">Field</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>last_checked_at</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>rpc_addr</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>zone</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
</tbody>
</table>

### zone_nodes_order_by

<table>
<thead>
<tr>
<th colspan="2" align="left">Field</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>is_alive</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>last_checked_at</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>rpc_addr</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>zone</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
</tbody>
</table>

### zone_nodes_pk_columns_input

<table>
<thead>
<tr>
<th colspan="2" align="left">Field</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>rpc_addr</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
</tbody>
</table>

### zones_graphs_aggregate_order_by

<table>
<thead>
<tr>
<th colspan="2" align="left">Field</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>avg</strong></td>
<td valign="top"><a href="#zones_graphs_avg_order_by">zones_graphs_avg_order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>count</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>max</strong></td>
<td valign="top"><a href="#zones_graphs_max_order_by">zones_graphs_max_order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>min</strong></td>
<td valign="top"><a href="#zones_graphs_min_order_by">zones_graphs_min_order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>stddev</strong></td>
<td valign="top"><a href="#zones_graphs_stddev_order_by">zones_graphs_stddev_order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>stddev_pop</strong></td>
<td valign="top"><a href="#zones_graphs_stddev_pop_order_by">zones_graphs_stddev_pop_order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>stddev_samp</strong></td>
<td valign="top"><a href="#zones_graphs_stddev_samp_order_by">zones_graphs_stddev_samp_order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>sum</strong></td>
<td valign="top"><a href="#zones_graphs_sum_order_by">zones_graphs_sum_order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>var_pop</strong></td>
<td valign="top"><a href="#zones_graphs_var_pop_order_by">zones_graphs_var_pop_order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>var_samp</strong></td>
<td valign="top"><a href="#zones_graphs_var_samp_order_by">zones_graphs_var_samp_order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>variance</strong></td>
<td valign="top"><a href="#zones_graphs_variance_order_by">zones_graphs_variance_order_by</a></td>
<td></td>
</tr>
</tbody>
</table>

### zones_graphs_avg_order_by

<table>
<thead>
<tr>
<th colspan="2" align="left">Field</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>channels_cnt_active</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>channels_cnt_open</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>channels_percent_active</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>timeframe</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
</tbody>
</table>

### zones_graphs_bool_exp

<table>
<thead>
<tr>
<th colspan="2" align="left">Field</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>_and</strong></td>
<td valign="top">[<a href="#zones_graphs_bool_exp">zones_graphs_bool_exp</a>]</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>_not</strong></td>
<td valign="top"><a href="#zones_graphs_bool_exp">zones_graphs_bool_exp</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>_or</strong></td>
<td valign="top">[<a href="#zones_graphs_bool_exp">zones_graphs_bool_exp</a>]</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>channels_cnt_active</strong></td>
<td valign="top"><a href="#int_comparison_exp">Int_comparison_exp</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>channels_cnt_open</strong></td>
<td valign="top"><a href="#int_comparison_exp">Int_comparison_exp</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>channels_percent_active</strong></td>
<td valign="top"><a href="#numeric_comparison_exp">numeric_comparison_exp</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>source</strong></td>
<td valign="top"><a href="#string_comparison_exp">String_comparison_exp</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>target</strong></td>
<td valign="top"><a href="#string_comparison_exp">String_comparison_exp</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>timeframe</strong></td>
<td valign="top"><a href="#int_comparison_exp">Int_comparison_exp</a></td>
<td></td>
</tr>
</tbody>
</table>

### zones_graphs_max_order_by

<table>
<thead>
<tr>
<th colspan="2" align="left">Field</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>channels_cnt_active</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>channels_cnt_open</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>channels_percent_active</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>source</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>target</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>timeframe</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
</tbody>
</table>

### zones_graphs_min_order_by

<table>
<thead>
<tr>
<th colspan="2" align="left">Field</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>channels_cnt_active</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>channels_cnt_open</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>channels_percent_active</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>source</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>target</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>timeframe</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
</tbody>
</table>

### zones_graphs_order_by

<table>
<thead>
<tr>
<th colspan="2" align="left">Field</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>channels_cnt_active</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>channels_cnt_open</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>channels_percent_active</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>source</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>target</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>timeframe</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
</tbody>
</table>

### zones_graphs_pk_columns_input

<table>
<thead>
<tr>
<th colspan="2" align="left">Field</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>source</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>target</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>timeframe</strong></td>
<td valign="top"><a href="#int">Int</a>!</td>
<td></td>
</tr>
</tbody>
</table>

### zones_graphs_stddev_order_by

<table>
<thead>
<tr>
<th colspan="2" align="left">Field</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>channels_cnt_active</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>channels_cnt_open</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>channels_percent_active</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>timeframe</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
</tbody>
</table>

### zones_graphs_stddev_pop_order_by

<table>
<thead>
<tr>
<th colspan="2" align="left">Field</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>channels_cnt_active</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>channels_cnt_open</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>channels_percent_active</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>timeframe</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
</tbody>
</table>

### zones_graphs_stddev_samp_order_by

<table>
<thead>
<tr>
<th colspan="2" align="left">Field</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>channels_cnt_active</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>channels_cnt_open</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>channels_percent_active</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>timeframe</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
</tbody>
</table>

### zones_graphs_sum_order_by

<table>
<thead>
<tr>
<th colspan="2" align="left">Field</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>channels_cnt_active</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>channels_cnt_open</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>channels_percent_active</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>timeframe</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
</tbody>
</table>

### zones_graphs_var_pop_order_by

<table>
<thead>
<tr>
<th colspan="2" align="left">Field</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>channels_cnt_active</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>channels_cnt_open</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>channels_percent_active</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>timeframe</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
</tbody>
</table>

### zones_graphs_var_samp_order_by

<table>
<thead>
<tr>
<th colspan="2" align="left">Field</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>channels_cnt_active</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>channels_cnt_open</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>channels_percent_active</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>timeframe</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
</tbody>
</table>

### zones_graphs_variance_order_by

<table>
<thead>
<tr>
<th colspan="2" align="left">Field</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>channels_cnt_active</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>channels_cnt_open</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>channels_percent_active</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>timeframe</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
</tbody>
</table>

### zones_stats_aggregate_order_by

<table>
<thead>
<tr>
<th colspan="2" align="left">Field</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>avg</strong></td>
<td valign="top"><a href="#zones_stats_avg_order_by">zones_stats_avg_order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>count</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>max</strong></td>
<td valign="top"><a href="#zones_stats_max_order_by">zones_stats_max_order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>min</strong></td>
<td valign="top"><a href="#zones_stats_min_order_by">zones_stats_min_order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>stddev</strong></td>
<td valign="top"><a href="#zones_stats_stddev_order_by">zones_stats_stddev_order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>stddev_pop</strong></td>
<td valign="top"><a href="#zones_stats_stddev_pop_order_by">zones_stats_stddev_pop_order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>stddev_samp</strong></td>
<td valign="top"><a href="#zones_stats_stddev_samp_order_by">zones_stats_stddev_samp_order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>sum</strong></td>
<td valign="top"><a href="#zones_stats_sum_order_by">zones_stats_sum_order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>var_pop</strong></td>
<td valign="top"><a href="#zones_stats_var_pop_order_by">zones_stats_var_pop_order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>var_samp</strong></td>
<td valign="top"><a href="#zones_stats_var_samp_order_by">zones_stats_var_samp_order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>variance</strong></td>
<td valign="top"><a href="#zones_stats_variance_order_by">zones_stats_variance_order_by</a></td>
<td></td>
</tr>
</tbody>
</table>

### zones_stats_avg_order_by

<table>
<thead>
<tr>
<th colspan="2" align="left">Field</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>channels_cnt_active_period</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>channels_cnt_active_period_diff</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>channels_cnt_open</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>channels_num</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>channels_percent_active_period</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>channels_percent_active_period_diff</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_percent</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_failed</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_failed_diff</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_in</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_in_diff</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_in_failed</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_in_rating</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_in_rating_diff</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_in_weight</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_out</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_out_diff</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_out_failed</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_out_rating</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_out_rating_diff</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_out_weight</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>relations_cnt_open</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>timeframe</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_active_addresses</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_active_addresses_diff</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_active_addresses_rating</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_active_addresses_rating_diff</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_active_addresses_weight</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_coin_turnover_amount</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_coin_turnover_amount_diff</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_ibc_txs</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_ibc_txs_diff</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_ibc_txs_rating</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_ibc_txs_rating_diff</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_ibc_txs_weight</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_txs</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_txs_diff</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_txs_rating</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_txs_rating_diff</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_txs_weight</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
</tbody>
</table>

### zones_stats_bool_exp

<table>
<thead>
<tr>
<th colspan="2" align="left">Field</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>_and</strong></td>
<td valign="top">[<a href="#zones_stats_bool_exp">zones_stats_bool_exp</a>]</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>_not</strong></td>
<td valign="top"><a href="#zones_stats_bool_exp">zones_stats_bool_exp</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>_or</strong></td>
<td valign="top">[<a href="#zones_stats_bool_exp">zones_stats_bool_exp</a>]</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>channels_cnt_active_period</strong></td>
<td valign="top"><a href="#int_comparison_exp">Int_comparison_exp</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>channels_cnt_active_period_diff</strong></td>
<td valign="top"><a href="#int_comparison_exp">Int_comparison_exp</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>channels_cnt_open</strong></td>
<td valign="top"><a href="#int_comparison_exp">Int_comparison_exp</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>channels_num</strong></td>
<td valign="top"><a href="#int_comparison_exp">Int_comparison_exp</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>channels_percent_active_period</strong></td>
<td valign="top"><a href="#int_comparison_exp">Int_comparison_exp</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>channels_percent_active_period_diff</strong></td>
<td valign="top"><a href="#int_comparison_exp">Int_comparison_exp</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>chart</strong></td>
<td valign="top"><a href="#jsonb_comparison_exp">jsonb_comparison_exp</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_percent</strong></td>
<td valign="top"><a href="#numeric_comparison_exp">numeric_comparison_exp</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_failed</strong></td>
<td valign="top"><a href="#int_comparison_exp">Int_comparison_exp</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_failed_diff</strong></td>
<td valign="top"><a href="#int_comparison_exp">Int_comparison_exp</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_in</strong></td>
<td valign="top"><a href="#int_comparison_exp">Int_comparison_exp</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_in_diff</strong></td>
<td valign="top"><a href="#int_comparison_exp">Int_comparison_exp</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_in_failed</strong></td>
<td valign="top"><a href="#int_comparison_exp">Int_comparison_exp</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_in_rating</strong></td>
<td valign="top"><a href="#int_comparison_exp">Int_comparison_exp</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_in_rating_diff</strong></td>
<td valign="top"><a href="#int_comparison_exp">Int_comparison_exp</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_in_weight</strong></td>
<td valign="top"><a href="#numeric_comparison_exp">numeric_comparison_exp</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_out</strong></td>
<td valign="top"><a href="#int_comparison_exp">Int_comparison_exp</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_out_diff</strong></td>
<td valign="top"><a href="#int_comparison_exp">Int_comparison_exp</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_out_failed</strong></td>
<td valign="top"><a href="#int_comparison_exp">Int_comparison_exp</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_out_rating</strong></td>
<td valign="top"><a href="#int_comparison_exp">Int_comparison_exp</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_out_rating_diff</strong></td>
<td valign="top"><a href="#int_comparison_exp">Int_comparison_exp</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_out_weight</strong></td>
<td valign="top"><a href="#numeric_comparison_exp">numeric_comparison_exp</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>relations_cnt_open</strong></td>
<td valign="top"><a href="#int_comparison_exp">Int_comparison_exp</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>timeframe</strong></td>
<td valign="top"><a href="#int_comparison_exp">Int_comparison_exp</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_active_addresses</strong></td>
<td valign="top"><a href="#int_comparison_exp">Int_comparison_exp</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_active_addresses_diff</strong></td>
<td valign="top"><a href="#int_comparison_exp">Int_comparison_exp</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_active_addresses_rating</strong></td>
<td valign="top"><a href="#int_comparison_exp">Int_comparison_exp</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_active_addresses_rating_diff</strong></td>
<td valign="top"><a href="#int_comparison_exp">Int_comparison_exp</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_active_addresses_weight</strong></td>
<td valign="top"><a href="#numeric_comparison_exp">numeric_comparison_exp</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_coin_turnover_amount</strong></td>
<td valign="top"><a href="#numeric_comparison_exp">numeric_comparison_exp</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_coin_turnover_amount_diff</strong></td>
<td valign="top"><a href="#numeric_comparison_exp">numeric_comparison_exp</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_ibc_txs</strong></td>
<td valign="top"><a href="#int_comparison_exp">Int_comparison_exp</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_ibc_txs_diff</strong></td>
<td valign="top"><a href="#int_comparison_exp">Int_comparison_exp</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_ibc_txs_rating</strong></td>
<td valign="top"><a href="#int_comparison_exp">Int_comparison_exp</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_ibc_txs_rating_diff</strong></td>
<td valign="top"><a href="#int_comparison_exp">Int_comparison_exp</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_ibc_txs_weight</strong></td>
<td valign="top"><a href="#numeric_comparison_exp">numeric_comparison_exp</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_txs</strong></td>
<td valign="top"><a href="#int_comparison_exp">Int_comparison_exp</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_txs_diff</strong></td>
<td valign="top"><a href="#int_comparison_exp">Int_comparison_exp</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_txs_rating</strong></td>
<td valign="top"><a href="#int_comparison_exp">Int_comparison_exp</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_txs_rating_diff</strong></td>
<td valign="top"><a href="#int_comparison_exp">Int_comparison_exp</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_txs_weight</strong></td>
<td valign="top"><a href="#numeric_comparison_exp">numeric_comparison_exp</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>zone</strong></td>
<td valign="top"><a href="#string_comparison_exp">String_comparison_exp</a></td>
<td></td>
</tr>
</tbody>
</table>

### zones_stats_max_order_by

<table>
<thead>
<tr>
<th colspan="2" align="left">Field</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>channels_cnt_active_period</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>channels_cnt_active_period_diff</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>channels_cnt_open</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>channels_num</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>channels_percent_active_period</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>channels_percent_active_period_diff</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_percent</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_failed</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_failed_diff</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_in</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_in_diff</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_in_failed</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_in_rating</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_in_rating_diff</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_in_weight</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_out</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_out_diff</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_out_failed</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_out_rating</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_out_rating_diff</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_out_weight</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>relations_cnt_open</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>timeframe</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_active_addresses</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_active_addresses_diff</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_active_addresses_rating</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_active_addresses_rating_diff</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_active_addresses_weight</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_coin_turnover_amount</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_coin_turnover_amount_diff</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_ibc_txs</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_ibc_txs_diff</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_ibc_txs_rating</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_ibc_txs_rating_diff</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_ibc_txs_weight</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_txs</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_txs_diff</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_txs_rating</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_txs_rating_diff</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_txs_weight</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>zone</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
</tbody>
</table>

### zones_stats_min_order_by

<table>
<thead>
<tr>
<th colspan="2" align="left">Field</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>channels_cnt_active_period</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>channels_cnt_active_period_diff</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>channels_cnt_open</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>channels_num</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>channels_percent_active_period</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>channels_percent_active_period_diff</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_percent</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_failed</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_failed_diff</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_in</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_in_diff</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_in_failed</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_in_rating</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_in_rating_diff</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_in_weight</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_out</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_out_diff</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_out_failed</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_out_rating</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_out_rating_diff</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_out_weight</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>relations_cnt_open</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>timeframe</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_active_addresses</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_active_addresses_diff</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_active_addresses_rating</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_active_addresses_rating_diff</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_active_addresses_weight</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_coin_turnover_amount</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_coin_turnover_amount_diff</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_ibc_txs</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_ibc_txs_diff</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_ibc_txs_rating</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_ibc_txs_rating_diff</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_ibc_txs_weight</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_txs</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_txs_diff</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_txs_rating</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_txs_rating_diff</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_txs_weight</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>zone</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
</tbody>
</table>

### zones_stats_order_by

<table>
<thead>
<tr>
<th colspan="2" align="left">Field</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>channels_cnt_active_period</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>channels_cnt_active_period_diff</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>channels_cnt_open</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>channels_num</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>channels_percent_active_period</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>channels_percent_active_period_diff</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>chart</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_percent</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_failed</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_failed_diff</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_in</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_in_diff</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_in_failed</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_in_rating</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_in_rating_diff</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_in_weight</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_out</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_out_diff</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_out_failed</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_out_rating</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_out_rating_diff</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_out_weight</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>relations_cnt_open</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>timeframe</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_active_addresses</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_active_addresses_diff</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_active_addresses_rating</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_active_addresses_rating_diff</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_active_addresses_weight</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_coin_turnover_amount</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_coin_turnover_amount_diff</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_ibc_txs</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_ibc_txs_diff</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_ibc_txs_rating</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_ibc_txs_rating_diff</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_ibc_txs_weight</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_txs</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_txs_diff</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_txs_rating</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_txs_rating_diff</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_txs_weight</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>zone</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
</tbody>
</table>

### zones_stats_pk_columns_input

<table>
<thead>
<tr>
<th colspan="2" align="left">Field</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>timeframe</strong></td>
<td valign="top"><a href="#int">Int</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>zone</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
</tbody>
</table>

### zones_stats_stddev_order_by

<table>
<thead>
<tr>
<th colspan="2" align="left">Field</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>channels_cnt_active_period</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>channels_cnt_active_period_diff</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>channels_cnt_open</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>channels_num</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>channels_percent_active_period</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>channels_percent_active_period_diff</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_percent</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_failed</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_failed_diff</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_in</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_in_diff</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_in_failed</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_in_rating</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_in_rating_diff</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_in_weight</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_out</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_out_diff</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_out_failed</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_out_rating</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_out_rating_diff</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_out_weight</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>relations_cnt_open</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>timeframe</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_active_addresses</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_active_addresses_diff</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_active_addresses_rating</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_active_addresses_rating_diff</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_active_addresses_weight</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_coin_turnover_amount</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_coin_turnover_amount_diff</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_ibc_txs</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_ibc_txs_diff</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_ibc_txs_rating</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_ibc_txs_rating_diff</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_ibc_txs_weight</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_txs</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_txs_diff</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_txs_rating</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_txs_rating_diff</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_txs_weight</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
</tbody>
</table>

### zones_stats_stddev_pop_order_by

<table>
<thead>
<tr>
<th colspan="2" align="left">Field</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>channels_cnt_active_period</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>channels_cnt_active_period_diff</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>channels_cnt_open</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>channels_num</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>channels_percent_active_period</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>channels_percent_active_period_diff</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_percent</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_failed</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_failed_diff</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_in</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_in_diff</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_in_failed</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_in_rating</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_in_rating_diff</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_in_weight</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_out</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_out_diff</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_out_failed</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_out_rating</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_out_rating_diff</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_out_weight</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>relations_cnt_open</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>timeframe</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_active_addresses</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_active_addresses_diff</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_active_addresses_rating</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_active_addresses_rating_diff</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_active_addresses_weight</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_coin_turnover_amount</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_coin_turnover_amount_diff</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_ibc_txs</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_ibc_txs_diff</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_ibc_txs_rating</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_ibc_txs_rating_diff</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_ibc_txs_weight</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_txs</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_txs_diff</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_txs_rating</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_txs_rating_diff</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_txs_weight</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
</tbody>
</table>

### zones_stats_stddev_samp_order_by

<table>
<thead>
<tr>
<th colspan="2" align="left">Field</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>channels_cnt_active_period</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>channels_cnt_active_period_diff</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>channels_cnt_open</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>channels_num</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>channels_percent_active_period</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>channels_percent_active_period_diff</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_percent</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_failed</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_failed_diff</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_in</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_in_diff</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_in_failed</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_in_rating</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_in_rating_diff</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_in_weight</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_out</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_out_diff</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_out_failed</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_out_rating</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_out_rating_diff</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_out_weight</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>relations_cnt_open</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>timeframe</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_active_addresses</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_active_addresses_diff</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_active_addresses_rating</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_active_addresses_rating_diff</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_active_addresses_weight</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_coin_turnover_amount</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_coin_turnover_amount_diff</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_ibc_txs</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_ibc_txs_diff</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_ibc_txs_rating</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_ibc_txs_rating_diff</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_ibc_txs_weight</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_txs</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_txs_diff</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_txs_rating</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_txs_rating_diff</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_txs_weight</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
</tbody>
</table>

### zones_stats_sum_order_by

<table>
<thead>
<tr>
<th colspan="2" align="left">Field</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>channels_cnt_active_period</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>channels_cnt_active_period_diff</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>channels_cnt_open</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>channels_num</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>channels_percent_active_period</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>channels_percent_active_period_diff</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_percent</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_failed</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_failed_diff</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_in</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_in_diff</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_in_failed</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_in_rating</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_in_rating_diff</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_in_weight</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_out</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_out_diff</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_out_failed</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_out_rating</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_out_rating_diff</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_out_weight</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>relations_cnt_open</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>timeframe</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_active_addresses</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_active_addresses_diff</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_active_addresses_rating</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_active_addresses_rating_diff</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_active_addresses_weight</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_coin_turnover_amount</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_coin_turnover_amount_diff</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_ibc_txs</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_ibc_txs_diff</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_ibc_txs_rating</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_ibc_txs_rating_diff</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_ibc_txs_weight</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_txs</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_txs_diff</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_txs_rating</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_txs_rating_diff</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_txs_weight</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
</tbody>
</table>

### zones_stats_var_pop_order_by

<table>
<thead>
<tr>
<th colspan="2" align="left">Field</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>channels_cnt_active_period</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>channels_cnt_active_period_diff</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>channels_cnt_open</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>channels_num</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>channels_percent_active_period</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>channels_percent_active_period_diff</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_percent</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_failed</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_failed_diff</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_in</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_in_diff</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_in_failed</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_in_rating</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_in_rating_diff</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_in_weight</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_out</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_out_diff</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_out_failed</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_out_rating</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_out_rating_diff</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_out_weight</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>relations_cnt_open</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>timeframe</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_active_addresses</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_active_addresses_diff</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_active_addresses_rating</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_active_addresses_rating_diff</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_active_addresses_weight</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_coin_turnover_amount</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_coin_turnover_amount_diff</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_ibc_txs</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_ibc_txs_diff</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_ibc_txs_rating</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_ibc_txs_rating_diff</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_ibc_txs_weight</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_txs</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_txs_diff</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_txs_rating</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_txs_rating_diff</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_txs_weight</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
</tbody>
</table>

### zones_stats_var_samp_order_by

<table>
<thead>
<tr>
<th colspan="2" align="left">Field</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>channels_cnt_active_period</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>channels_cnt_active_period_diff</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>channels_cnt_open</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>channels_num</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>channels_percent_active_period</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>channels_percent_active_period_diff</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_percent</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_failed</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_failed_diff</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_in</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_in_diff</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_in_failed</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_in_rating</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_in_rating_diff</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_in_weight</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_out</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_out_diff</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_out_failed</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_out_rating</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_out_rating_diff</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_out_weight</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>relations_cnt_open</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>timeframe</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_active_addresses</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_active_addresses_diff</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_active_addresses_rating</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_active_addresses_rating_diff</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_active_addresses_weight</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_coin_turnover_amount</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_coin_turnover_amount_diff</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_ibc_txs</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_ibc_txs_diff</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_ibc_txs_rating</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_ibc_txs_rating_diff</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_ibc_txs_weight</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_txs</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_txs_diff</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_txs_rating</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_txs_rating_diff</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_txs_weight</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
</tbody>
</table>

### zones_stats_variance_order_by

<table>
<thead>
<tr>
<th colspan="2" align="left">Field</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>channels_cnt_active_period</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>channels_cnt_active_period_diff</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>channels_cnt_open</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>channels_num</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>channels_percent_active_period</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>channels_percent_active_period_diff</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_percent</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_failed</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_failed_diff</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_in</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_in_diff</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_in_failed</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_in_rating</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_in_rating_diff</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_in_weight</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_out</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_out_diff</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_out_failed</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_out_rating</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_out_rating_diff</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_tx_out_weight</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>relations_cnt_open</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>timeframe</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_active_addresses</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_active_addresses_diff</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_active_addresses_rating</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_active_addresses_rating_diff</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_active_addresses_weight</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_coin_turnover_amount</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_coin_turnover_amount_diff</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_ibc_txs</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_ibc_txs_diff</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_ibc_txs_rating</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_ibc_txs_rating_diff</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_ibc_txs_weight</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_txs</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_txs_diff</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_txs_rating</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_txs_rating_diff</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_txs_weight</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
</tbody>
</table>

## Enums

### blocks_log_select_column

<table>
<thead>
<th align="left">Value</th>
<th align="left">Description</th>
</thead>
<tbody>
<tr>
<td valign="top"><strong>last_processed_block</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>last_updated_at</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>zone</strong></td>
<td></td>
</tr>
</tbody>
</table>

### channels_stats_select_column

<table>
<thead>
<th align="left">Value</th>
<th align="left">Description</th>
</thead>
<tbody>
<tr>
<td valign="top"><strong>channel_id</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>client_id</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>connection_id</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>ibc_tx_1d</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>ibc_tx_1d_diff</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>ibc_tx_1d_failed</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>ibc_tx_1d_failed_diff</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>ibc_tx_30d</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>ibc_tx_30d_diff</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>ibc_tx_30d_failed</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>ibc_tx_30d_failed_diff</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>ibc_tx_7d</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>ibc_tx_7d_diff</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>ibc_tx_7d_failed</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>ibc_tx_7d_failed_diff</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>is_opened</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>zone</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>zone_counerparty</strong></td>
<td></td>
</tr>
</tbody>
</table>

### headers_select_column

<table>
<thead>
<th align="left">Value</th>
<th align="left">Description</th>
</thead>
<tbody>
<tr>
<td valign="top"><strong>channels_cnt_active_period</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>channels_cnt_active_period_diff</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>channels_cnt_all</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>channels_cnt_open</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>channels_cnt_period</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>channels_percent_active_period</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>channels_percent_active_period_diff</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>chart</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>relations_cnt_open</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>timeframe</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>top_zone_pair</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>zones_cnt_all</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>zones_cnt_period</strong></td>
<td></td>
</tr>
</tbody>
</table>

### order_by

<table>
<thead>
<th align="left">Value</th>
<th align="left">Description</th>
</thead>
<tbody>
<tr>
<td valign="top"><strong>asc</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>asc_nulls_first</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>asc_nulls_last</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>desc</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>desc_nulls_first</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>desc_nulls_last</strong></td>
<td></td>
</tr>
</tbody>
</table>

### zone_nodes_select_column

<table>
<thead>
<th align="left">Value</th>
<th align="left">Description</th>
</thead>
<tbody>
<tr>
<td valign="top"><strong>is_alive</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>last_checked_at</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>rpc_addr</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>zone</strong></td>
<td></td>
</tr>
</tbody>
</table>

### zones_graphs_select_column

<table>
<thead>
<th align="left">Value</th>
<th align="left">Description</th>
</thead>
<tbody>
<tr>
<td valign="top"><strong>channels_cnt_active</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>channels_cnt_open</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>channels_percent_active</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>source</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>target</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>timeframe</strong></td>
<td></td>
</tr>
</tbody>
</table>

### zones_stats_select_column

<table>
<thead>
<th align="left">Value</th>
<th align="left">Description</th>
</thead>
<tbody>
<tr>
<td valign="top"><strong>channels_cnt_active_period</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>channels_cnt_active_period_diff</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>channels_cnt_open</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>channels_num</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>channels_percent_active_period</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>channels_percent_active_period_diff</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>chart</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>ibc_percent</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>ibc_tx_failed</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>ibc_tx_failed_diff</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>ibc_tx_in</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>ibc_tx_in_diff</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>ibc_tx_in_failed</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>ibc_tx_in_rating</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>ibc_tx_in_rating_diff</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>ibc_tx_in_weight</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>ibc_tx_out</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>ibc_tx_out_diff</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>ibc_tx_out_failed</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>ibc_tx_out_rating</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>ibc_tx_out_rating_diff</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>ibc_tx_out_weight</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>relations_cnt_open</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>timeframe</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>total_active_addresses</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>total_active_addresses_diff</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>total_active_addresses_rating</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>total_active_addresses_rating_diff</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>total_active_addresses_weight</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>total_coin_turnover_amount</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>total_coin_turnover_amount_diff</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>total_ibc_txs</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>total_ibc_txs_diff</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>total_ibc_txs_rating</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>total_ibc_txs_rating_diff</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>total_ibc_txs_weight</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>total_txs</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>total_txs_diff</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>total_txs_rating</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>total_txs_rating_diff</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>total_txs_weight</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>zone</strong></td>
<td></td>
</tr>
</tbody>
</table>

## Scalars

### Boolean

The `Boolean` scalar type represents `true` or `false`.

### Float

The `Float` scalar type represents signed double-precision fractional values as specified by [IEEE 754](https://en.wikipedia.org/wiki/IEEE_floating_point).

### Int

The `Int` scalar type represents non-fractional signed whole numeric values. Int can represent values between -(2^31) and 2^31 - 1.

### String

The `String` scalar type represents textual data, represented as UTF-8 character sequences. The String type is most often used by GraphQL to represent free-form human-readable text.

### jsonb

### numeric

### timestamp

