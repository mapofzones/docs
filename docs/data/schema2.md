# Schema Types

<details>
  <summary><strong>Table of Contents</strong></summary>

  * [Query](#query)
  * [Mutation](#mutation)
  * [Objects](#objects)
    * [active_addresses](#active_addresses)
    * [active_addresses_aggregate](#active_addresses_aggregate)
    * [active_addresses_aggregate_fields](#active_addresses_aggregate_fields)
    * [active_addresses_avg_fields](#active_addresses_avg_fields)
    * [active_addresses_max_fields](#active_addresses_max_fields)
    * [active_addresses_min_fields](#active_addresses_min_fields)
    * [active_addresses_mutation_response](#active_addresses_mutation_response)
    * [active_addresses_stddev_fields](#active_addresses_stddev_fields)
    * [active_addresses_stddev_pop_fields](#active_addresses_stddev_pop_fields)
    * [active_addresses_stddev_samp_fields](#active_addresses_stddev_samp_fields)
    * [active_addresses_sum_fields](#active_addresses_sum_fields)
    * [active_addresses_var_pop_fields](#active_addresses_var_pop_fields)
    * [active_addresses_var_samp_fields](#active_addresses_var_samp_fields)
    * [active_addresses_variance_fields](#active_addresses_variance_fields)
    * [blocks_log](#blocks_log)
    * [blocks_log_aggregate](#blocks_log_aggregate)
    * [blocks_log_aggregate_fields](#blocks_log_aggregate_fields)
    * [blocks_log_avg_fields](#blocks_log_avg_fields)
    * [blocks_log_max_fields](#blocks_log_max_fields)
    * [blocks_log_min_fields](#blocks_log_min_fields)
    * [blocks_log_mutation_response](#blocks_log_mutation_response)
    * [blocks_log_stddev_fields](#blocks_log_stddev_fields)
    * [blocks_log_stddev_pop_fields](#blocks_log_stddev_pop_fields)
    * [blocks_log_stddev_samp_fields](#blocks_log_stddev_samp_fields)
    * [blocks_log_sum_fields](#blocks_log_sum_fields)
    * [blocks_log_var_pop_fields](#blocks_log_var_pop_fields)
    * [blocks_log_var_samp_fields](#blocks_log_var_samp_fields)
    * [blocks_log_variance_fields](#blocks_log_variance_fields)
    * [headers](#headers)
    * [headers_aggregate](#headers_aggregate)
    * [headers_aggregate_fields](#headers_aggregate_fields)
    * [headers_avg_fields](#headers_avg_fields)
    * [headers_max_fields](#headers_max_fields)
    * [headers_min_fields](#headers_min_fields)
    * [headers_mutation_response](#headers_mutation_response)
    * [headers_stddev_fields](#headers_stddev_fields)
    * [headers_stddev_pop_fields](#headers_stddev_pop_fields)
    * [headers_stddev_samp_fields](#headers_stddev_samp_fields)
    * [headers_sum_fields](#headers_sum_fields)
    * [headers_var_pop_fields](#headers_var_pop_fields)
    * [headers_var_samp_fields](#headers_var_samp_fields)
    * [headers_variance_fields](#headers_variance_fields)
    * [ibc_channel_zone](#ibc_channel_zone)
    * [ibc_channel_zone_aggregate](#ibc_channel_zone_aggregate)
    * [ibc_channel_zone_aggregate_fields](#ibc_channel_zone_aggregate_fields)
    * [ibc_channel_zone_max_fields](#ibc_channel_zone_max_fields)
    * [ibc_channel_zone_min_fields](#ibc_channel_zone_min_fields)
    * [ibc_channel_zone_mutation_response](#ibc_channel_zone_mutation_response)
    * [ibc_channels](#ibc_channels)
    * [ibc_channels_aggregate](#ibc_channels_aggregate)
    * [ibc_channels_aggregate_fields](#ibc_channels_aggregate_fields)
    * [ibc_channels_max_fields](#ibc_channels_max_fields)
    * [ibc_channels_min_fields](#ibc_channels_min_fields)
    * [ibc_channels_mutation_response](#ibc_channels_mutation_response)
    * [ibc_clients](#ibc_clients)
    * [ibc_clients_aggregate](#ibc_clients_aggregate)
    * [ibc_clients_aggregate_fields](#ibc_clients_aggregate_fields)
    * [ibc_clients_max_fields](#ibc_clients_max_fields)
    * [ibc_clients_min_fields](#ibc_clients_min_fields)
    * [ibc_clients_mutation_response](#ibc_clients_mutation_response)
    * [ibc_connections](#ibc_connections)
    * [ibc_connections_aggregate](#ibc_connections_aggregate)
    * [ibc_connections_aggregate_fields](#ibc_connections_aggregate_fields)
    * [ibc_connections_max_fields](#ibc_connections_max_fields)
    * [ibc_connections_min_fields](#ibc_connections_min_fields)
    * [ibc_connections_mutation_response](#ibc_connections_mutation_response)
    * [ibc_transfer_hourly_stats](#ibc_transfer_hourly_stats)
    * [ibc_transfer_hourly_stats_aggregate](#ibc_transfer_hourly_stats_aggregate)
    * [ibc_transfer_hourly_stats_aggregate_fields](#ibc_transfer_hourly_stats_aggregate_fields)
    * [ibc_transfer_hourly_stats_avg_fields](#ibc_transfer_hourly_stats_avg_fields)
    * [ibc_transfer_hourly_stats_max_fields](#ibc_transfer_hourly_stats_max_fields)
    * [ibc_transfer_hourly_stats_min_fields](#ibc_transfer_hourly_stats_min_fields)
    * [ibc_transfer_hourly_stats_mutation_response](#ibc_transfer_hourly_stats_mutation_response)
    * [ibc_transfer_hourly_stats_stddev_fields](#ibc_transfer_hourly_stats_stddev_fields)
    * [ibc_transfer_hourly_stats_stddev_pop_fields](#ibc_transfer_hourly_stats_stddev_pop_fields)
    * [ibc_transfer_hourly_stats_stddev_samp_fields](#ibc_transfer_hourly_stats_stddev_samp_fields)
    * [ibc_transfer_hourly_stats_sum_fields](#ibc_transfer_hourly_stats_sum_fields)
    * [ibc_transfer_hourly_stats_var_pop_fields](#ibc_transfer_hourly_stats_var_pop_fields)
    * [ibc_transfer_hourly_stats_var_samp_fields](#ibc_transfer_hourly_stats_var_samp_fields)
    * [ibc_transfer_hourly_stats_variance_fields](#ibc_transfer_hourly_stats_variance_fields)
    * [periods](#periods)
    * [periods_aggregate](#periods_aggregate)
    * [periods_aggregate_fields](#periods_aggregate_fields)
    * [periods_avg_fields](#periods_avg_fields)
    * [periods_max_fields](#periods_max_fields)
    * [periods_min_fields](#periods_min_fields)
    * [periods_mutation_response](#periods_mutation_response)
    * [periods_stddev_fields](#periods_stddev_fields)
    * [periods_stddev_pop_fields](#periods_stddev_pop_fields)
    * [periods_stddev_samp_fields](#periods_stddev_samp_fields)
    * [periods_sum_fields](#periods_sum_fields)
    * [periods_var_pop_fields](#periods_var_pop_fields)
    * [periods_var_samp_fields](#periods_var_samp_fields)
    * [periods_variance_fields](#periods_variance_fields)
    * [subscription_root](#subscription_root)
    * [total_tx_hourly_stats](#total_tx_hourly_stats)
    * [total_tx_hourly_stats_aggregate](#total_tx_hourly_stats_aggregate)
    * [total_tx_hourly_stats_aggregate_fields](#total_tx_hourly_stats_aggregate_fields)
    * [total_tx_hourly_stats_avg_fields](#total_tx_hourly_stats_avg_fields)
    * [total_tx_hourly_stats_max_fields](#total_tx_hourly_stats_max_fields)
    * [total_tx_hourly_stats_min_fields](#total_tx_hourly_stats_min_fields)
    * [total_tx_hourly_stats_mutation_response](#total_tx_hourly_stats_mutation_response)
    * [total_tx_hourly_stats_stddev_fields](#total_tx_hourly_stats_stddev_fields)
    * [total_tx_hourly_stats_stddev_pop_fields](#total_tx_hourly_stats_stddev_pop_fields)
    * [total_tx_hourly_stats_stddev_samp_fields](#total_tx_hourly_stats_stddev_samp_fields)
    * [total_tx_hourly_stats_sum_fields](#total_tx_hourly_stats_sum_fields)
    * [total_tx_hourly_stats_var_pop_fields](#total_tx_hourly_stats_var_pop_fields)
    * [total_tx_hourly_stats_var_samp_fields](#total_tx_hourly_stats_var_samp_fields)
    * [total_tx_hourly_stats_variance_fields](#total_tx_hourly_stats_variance_fields)
    * [zone_nodes](#zone_nodes)
    * [zone_nodes_aggregate](#zone_nodes_aggregate)
    * [zone_nodes_aggregate_fields](#zone_nodes_aggregate_fields)
    * [zone_nodes_max_fields](#zone_nodes_max_fields)
    * [zone_nodes_min_fields](#zone_nodes_min_fields)
    * [zone_nodes_mutation_response](#zone_nodes_mutation_response)
    * [zones](#zones)
    * [zones_aggregate](#zones_aggregate)
    * [zones_aggregate_fields](#zones_aggregate_fields)
    * [zones_graphs](#zones_graphs)
    * [zones_graphs_aggregate](#zones_graphs_aggregate)
    * [zones_graphs_aggregate_fields](#zones_graphs_aggregate_fields)
    * [zones_graphs_avg_fields](#zones_graphs_avg_fields)
    * [zones_graphs_max_fields](#zones_graphs_max_fields)
    * [zones_graphs_min_fields](#zones_graphs_min_fields)
    * [zones_graphs_mutation_response](#zones_graphs_mutation_response)
    * [zones_graphs_stddev_fields](#zones_graphs_stddev_fields)
    * [zones_graphs_stddev_pop_fields](#zones_graphs_stddev_pop_fields)
    * [zones_graphs_stddev_samp_fields](#zones_graphs_stddev_samp_fields)
    * [zones_graphs_sum_fields](#zones_graphs_sum_fields)
    * [zones_graphs_var_pop_fields](#zones_graphs_var_pop_fields)
    * [zones_graphs_var_samp_fields](#zones_graphs_var_samp_fields)
    * [zones_graphs_variance_fields](#zones_graphs_variance_fields)
    * [zones_max_fields](#zones_max_fields)
    * [zones_min_fields](#zones_min_fields)
    * [zones_mutation_response](#zones_mutation_response)
    * [zones_stats](#zones_stats)
    * [zones_stats_aggregate](#zones_stats_aggregate)
    * [zones_stats_aggregate_fields](#zones_stats_aggregate_fields)
    * [zones_stats_avg_fields](#zones_stats_avg_fields)
    * [zones_stats_max_fields](#zones_stats_max_fields)
    * [zones_stats_min_fields](#zones_stats_min_fields)
    * [zones_stats_mutation_response](#zones_stats_mutation_response)
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
    * [active_addresses_aggregate_order_by](#active_addresses_aggregate_order_by)
    * [active_addresses_arr_rel_insert_input](#active_addresses_arr_rel_insert_input)
    * [active_addresses_avg_order_by](#active_addresses_avg_order_by)
    * [active_addresses_bool_exp](#active_addresses_bool_exp)
    * [active_addresses_inc_input](#active_addresses_inc_input)
    * [active_addresses_insert_input](#active_addresses_insert_input)
    * [active_addresses_max_order_by](#active_addresses_max_order_by)
    * [active_addresses_min_order_by](#active_addresses_min_order_by)
    * [active_addresses_obj_rel_insert_input](#active_addresses_obj_rel_insert_input)
    * [active_addresses_on_conflict](#active_addresses_on_conflict)
    * [active_addresses_order_by](#active_addresses_order_by)
    * [active_addresses_pk_columns_input](#active_addresses_pk_columns_input)
    * [active_addresses_set_input](#active_addresses_set_input)
    * [active_addresses_stddev_order_by](#active_addresses_stddev_order_by)
    * [active_addresses_stddev_pop_order_by](#active_addresses_stddev_pop_order_by)
    * [active_addresses_stddev_samp_order_by](#active_addresses_stddev_samp_order_by)
    * [active_addresses_sum_order_by](#active_addresses_sum_order_by)
    * [active_addresses_var_pop_order_by](#active_addresses_var_pop_order_by)
    * [active_addresses_var_samp_order_by](#active_addresses_var_samp_order_by)
    * [active_addresses_variance_order_by](#active_addresses_variance_order_by)
    * [bigint_comparison_exp](#bigint_comparison_exp)
    * [blocks_log_aggregate_order_by](#blocks_log_aggregate_order_by)
    * [blocks_log_arr_rel_insert_input](#blocks_log_arr_rel_insert_input)
    * [blocks_log_avg_order_by](#blocks_log_avg_order_by)
    * [blocks_log_bool_exp](#blocks_log_bool_exp)
    * [blocks_log_inc_input](#blocks_log_inc_input)
    * [blocks_log_insert_input](#blocks_log_insert_input)
    * [blocks_log_max_order_by](#blocks_log_max_order_by)
    * [blocks_log_min_order_by](#blocks_log_min_order_by)
    * [blocks_log_obj_rel_insert_input](#blocks_log_obj_rel_insert_input)
    * [blocks_log_on_conflict](#blocks_log_on_conflict)
    * [blocks_log_order_by](#blocks_log_order_by)
    * [blocks_log_pk_columns_input](#blocks_log_pk_columns_input)
    * [blocks_log_set_input](#blocks_log_set_input)
    * [blocks_log_stddev_order_by](#blocks_log_stddev_order_by)
    * [blocks_log_stddev_pop_order_by](#blocks_log_stddev_pop_order_by)
    * [blocks_log_stddev_samp_order_by](#blocks_log_stddev_samp_order_by)
    * [blocks_log_sum_order_by](#blocks_log_sum_order_by)
    * [blocks_log_var_pop_order_by](#blocks_log_var_pop_order_by)
    * [blocks_log_var_samp_order_by](#blocks_log_var_samp_order_by)
    * [blocks_log_variance_order_by](#blocks_log_variance_order_by)
    * [headers_aggregate_order_by](#headers_aggregate_order_by)
    * [headers_append_input](#headers_append_input)
    * [headers_arr_rel_insert_input](#headers_arr_rel_insert_input)
    * [headers_avg_order_by](#headers_avg_order_by)
    * [headers_bool_exp](#headers_bool_exp)
    * [headers_delete_at_path_input](#headers_delete_at_path_input)
    * [headers_delete_elem_input](#headers_delete_elem_input)
    * [headers_delete_key_input](#headers_delete_key_input)
    * [headers_inc_input](#headers_inc_input)
    * [headers_insert_input](#headers_insert_input)
    * [headers_max_order_by](#headers_max_order_by)
    * [headers_min_order_by](#headers_min_order_by)
    * [headers_obj_rel_insert_input](#headers_obj_rel_insert_input)
    * [headers_on_conflict](#headers_on_conflict)
    * [headers_order_by](#headers_order_by)
    * [headers_pk_columns_input](#headers_pk_columns_input)
    * [headers_prepend_input](#headers_prepend_input)
    * [headers_set_input](#headers_set_input)
    * [headers_stddev_order_by](#headers_stddev_order_by)
    * [headers_stddev_pop_order_by](#headers_stddev_pop_order_by)
    * [headers_stddev_samp_order_by](#headers_stddev_samp_order_by)
    * [headers_sum_order_by](#headers_sum_order_by)
    * [headers_var_pop_order_by](#headers_var_pop_order_by)
    * [headers_var_samp_order_by](#headers_var_samp_order_by)
    * [headers_variance_order_by](#headers_variance_order_by)
    * [ibc_channel_zone_aggregate_order_by](#ibc_channel_zone_aggregate_order_by)
    * [ibc_channel_zone_arr_rel_insert_input](#ibc_channel_zone_arr_rel_insert_input)
    * [ibc_channel_zone_bool_exp](#ibc_channel_zone_bool_exp)
    * [ibc_channel_zone_insert_input](#ibc_channel_zone_insert_input)
    * [ibc_channel_zone_max_order_by](#ibc_channel_zone_max_order_by)
    * [ibc_channel_zone_min_order_by](#ibc_channel_zone_min_order_by)
    * [ibc_channel_zone_obj_rel_insert_input](#ibc_channel_zone_obj_rel_insert_input)
    * [ibc_channel_zone_on_conflict](#ibc_channel_zone_on_conflict)
    * [ibc_channel_zone_order_by](#ibc_channel_zone_order_by)
    * [ibc_channel_zone_pk_columns_input](#ibc_channel_zone_pk_columns_input)
    * [ibc_channel_zone_set_input](#ibc_channel_zone_set_input)
    * [ibc_channels_aggregate_order_by](#ibc_channels_aggregate_order_by)
    * [ibc_channels_arr_rel_insert_input](#ibc_channels_arr_rel_insert_input)
    * [ibc_channels_bool_exp](#ibc_channels_bool_exp)
    * [ibc_channels_insert_input](#ibc_channels_insert_input)
    * [ibc_channels_max_order_by](#ibc_channels_max_order_by)
    * [ibc_channels_min_order_by](#ibc_channels_min_order_by)
    * [ibc_channels_obj_rel_insert_input](#ibc_channels_obj_rel_insert_input)
    * [ibc_channels_on_conflict](#ibc_channels_on_conflict)
    * [ibc_channels_order_by](#ibc_channels_order_by)
    * [ibc_channels_pk_columns_input](#ibc_channels_pk_columns_input)
    * [ibc_channels_set_input](#ibc_channels_set_input)
    * [ibc_clients_aggregate_order_by](#ibc_clients_aggregate_order_by)
    * [ibc_clients_arr_rel_insert_input](#ibc_clients_arr_rel_insert_input)
    * [ibc_clients_bool_exp](#ibc_clients_bool_exp)
    * [ibc_clients_insert_input](#ibc_clients_insert_input)
    * [ibc_clients_max_order_by](#ibc_clients_max_order_by)
    * [ibc_clients_min_order_by](#ibc_clients_min_order_by)
    * [ibc_clients_obj_rel_insert_input](#ibc_clients_obj_rel_insert_input)
    * [ibc_clients_on_conflict](#ibc_clients_on_conflict)
    * [ibc_clients_order_by](#ibc_clients_order_by)
    * [ibc_clients_pk_columns_input](#ibc_clients_pk_columns_input)
    * [ibc_clients_set_input](#ibc_clients_set_input)
    * [ibc_connections_aggregate_order_by](#ibc_connections_aggregate_order_by)
    * [ibc_connections_arr_rel_insert_input](#ibc_connections_arr_rel_insert_input)
    * [ibc_connections_bool_exp](#ibc_connections_bool_exp)
    * [ibc_connections_insert_input](#ibc_connections_insert_input)
    * [ibc_connections_max_order_by](#ibc_connections_max_order_by)
    * [ibc_connections_min_order_by](#ibc_connections_min_order_by)
    * [ibc_connections_obj_rel_insert_input](#ibc_connections_obj_rel_insert_input)
    * [ibc_connections_on_conflict](#ibc_connections_on_conflict)
    * [ibc_connections_order_by](#ibc_connections_order_by)
    * [ibc_connections_pk_columns_input](#ibc_connections_pk_columns_input)
    * [ibc_connections_set_input](#ibc_connections_set_input)
    * [ibc_transfer_hourly_stats_aggregate_order_by](#ibc_transfer_hourly_stats_aggregate_order_by)
    * [ibc_transfer_hourly_stats_arr_rel_insert_input](#ibc_transfer_hourly_stats_arr_rel_insert_input)
    * [ibc_transfer_hourly_stats_avg_order_by](#ibc_transfer_hourly_stats_avg_order_by)
    * [ibc_transfer_hourly_stats_bool_exp](#ibc_transfer_hourly_stats_bool_exp)
    * [ibc_transfer_hourly_stats_inc_input](#ibc_transfer_hourly_stats_inc_input)
    * [ibc_transfer_hourly_stats_insert_input](#ibc_transfer_hourly_stats_insert_input)
    * [ibc_transfer_hourly_stats_max_order_by](#ibc_transfer_hourly_stats_max_order_by)
    * [ibc_transfer_hourly_stats_min_order_by](#ibc_transfer_hourly_stats_min_order_by)
    * [ibc_transfer_hourly_stats_obj_rel_insert_input](#ibc_transfer_hourly_stats_obj_rel_insert_input)
    * [ibc_transfer_hourly_stats_on_conflict](#ibc_transfer_hourly_stats_on_conflict)
    * [ibc_transfer_hourly_stats_order_by](#ibc_transfer_hourly_stats_order_by)
    * [ibc_transfer_hourly_stats_pk_columns_input](#ibc_transfer_hourly_stats_pk_columns_input)
    * [ibc_transfer_hourly_stats_set_input](#ibc_transfer_hourly_stats_set_input)
    * [ibc_transfer_hourly_stats_stddev_order_by](#ibc_transfer_hourly_stats_stddev_order_by)
    * [ibc_transfer_hourly_stats_stddev_pop_order_by](#ibc_transfer_hourly_stats_stddev_pop_order_by)
    * [ibc_transfer_hourly_stats_stddev_samp_order_by](#ibc_transfer_hourly_stats_stddev_samp_order_by)
    * [ibc_transfer_hourly_stats_sum_order_by](#ibc_transfer_hourly_stats_sum_order_by)
    * [ibc_transfer_hourly_stats_var_pop_order_by](#ibc_transfer_hourly_stats_var_pop_order_by)
    * [ibc_transfer_hourly_stats_var_samp_order_by](#ibc_transfer_hourly_stats_var_samp_order_by)
    * [ibc_transfer_hourly_stats_variance_order_by](#ibc_transfer_hourly_stats_variance_order_by)
    * [jsonb_comparison_exp](#jsonb_comparison_exp)
    * [numeric_comparison_exp](#numeric_comparison_exp)
    * [periods_aggregate_order_by](#periods_aggregate_order_by)
    * [periods_arr_rel_insert_input](#periods_arr_rel_insert_input)
    * [periods_avg_order_by](#periods_avg_order_by)
    * [periods_bool_exp](#periods_bool_exp)
    * [periods_inc_input](#periods_inc_input)
    * [periods_insert_input](#periods_insert_input)
    * [periods_max_order_by](#periods_max_order_by)
    * [periods_min_order_by](#periods_min_order_by)
    * [periods_obj_rel_insert_input](#periods_obj_rel_insert_input)
    * [periods_on_conflict](#periods_on_conflict)
    * [periods_order_by](#periods_order_by)
    * [periods_pk_columns_input](#periods_pk_columns_input)
    * [periods_set_input](#periods_set_input)
    * [periods_stddev_order_by](#periods_stddev_order_by)
    * [periods_stddev_pop_order_by](#periods_stddev_pop_order_by)
    * [periods_stddev_samp_order_by](#periods_stddev_samp_order_by)
    * [periods_sum_order_by](#periods_sum_order_by)
    * [periods_var_pop_order_by](#periods_var_pop_order_by)
    * [periods_var_samp_order_by](#periods_var_samp_order_by)
    * [periods_variance_order_by](#periods_variance_order_by)
    * [timestamp_comparison_exp](#timestamp_comparison_exp)
    * [total_tx_hourly_stats_aggregate_order_by](#total_tx_hourly_stats_aggregate_order_by)
    * [total_tx_hourly_stats_arr_rel_insert_input](#total_tx_hourly_stats_arr_rel_insert_input)
    * [total_tx_hourly_stats_avg_order_by](#total_tx_hourly_stats_avg_order_by)
    * [total_tx_hourly_stats_bool_exp](#total_tx_hourly_stats_bool_exp)
    * [total_tx_hourly_stats_inc_input](#total_tx_hourly_stats_inc_input)
    * [total_tx_hourly_stats_insert_input](#total_tx_hourly_stats_insert_input)
    * [total_tx_hourly_stats_max_order_by](#total_tx_hourly_stats_max_order_by)
    * [total_tx_hourly_stats_min_order_by](#total_tx_hourly_stats_min_order_by)
    * [total_tx_hourly_stats_obj_rel_insert_input](#total_tx_hourly_stats_obj_rel_insert_input)
    * [total_tx_hourly_stats_on_conflict](#total_tx_hourly_stats_on_conflict)
    * [total_tx_hourly_stats_order_by](#total_tx_hourly_stats_order_by)
    * [total_tx_hourly_stats_pk_columns_input](#total_tx_hourly_stats_pk_columns_input)
    * [total_tx_hourly_stats_set_input](#total_tx_hourly_stats_set_input)
    * [total_tx_hourly_stats_stddev_order_by](#total_tx_hourly_stats_stddev_order_by)
    * [total_tx_hourly_stats_stddev_pop_order_by](#total_tx_hourly_stats_stddev_pop_order_by)
    * [total_tx_hourly_stats_stddev_samp_order_by](#total_tx_hourly_stats_stddev_samp_order_by)
    * [total_tx_hourly_stats_sum_order_by](#total_tx_hourly_stats_sum_order_by)
    * [total_tx_hourly_stats_var_pop_order_by](#total_tx_hourly_stats_var_pop_order_by)
    * [total_tx_hourly_stats_var_samp_order_by](#total_tx_hourly_stats_var_samp_order_by)
    * [total_tx_hourly_stats_variance_order_by](#total_tx_hourly_stats_variance_order_by)
    * [zone_nodes_aggregate_order_by](#zone_nodes_aggregate_order_by)
    * [zone_nodes_arr_rel_insert_input](#zone_nodes_arr_rel_insert_input)
    * [zone_nodes_bool_exp](#zone_nodes_bool_exp)
    * [zone_nodes_insert_input](#zone_nodes_insert_input)
    * [zone_nodes_max_order_by](#zone_nodes_max_order_by)
    * [zone_nodes_min_order_by](#zone_nodes_min_order_by)
    * [zone_nodes_obj_rel_insert_input](#zone_nodes_obj_rel_insert_input)
    * [zone_nodes_on_conflict](#zone_nodes_on_conflict)
    * [zone_nodes_order_by](#zone_nodes_order_by)
    * [zone_nodes_pk_columns_input](#zone_nodes_pk_columns_input)
    * [zone_nodes_set_input](#zone_nodes_set_input)
    * [zones_aggregate_order_by](#zones_aggregate_order_by)
    * [zones_arr_rel_insert_input](#zones_arr_rel_insert_input)
    * [zones_bool_exp](#zones_bool_exp)
    * [zones_graphs_aggregate_order_by](#zones_graphs_aggregate_order_by)
    * [zones_graphs_arr_rel_insert_input](#zones_graphs_arr_rel_insert_input)
    * [zones_graphs_avg_order_by](#zones_graphs_avg_order_by)
    * [zones_graphs_bool_exp](#zones_graphs_bool_exp)
    * [zones_graphs_inc_input](#zones_graphs_inc_input)
    * [zones_graphs_insert_input](#zones_graphs_insert_input)
    * [zones_graphs_max_order_by](#zones_graphs_max_order_by)
    * [zones_graphs_min_order_by](#zones_graphs_min_order_by)
    * [zones_graphs_obj_rel_insert_input](#zones_graphs_obj_rel_insert_input)
    * [zones_graphs_on_conflict](#zones_graphs_on_conflict)
    * [zones_graphs_order_by](#zones_graphs_order_by)
    * [zones_graphs_pk_columns_input](#zones_graphs_pk_columns_input)
    * [zones_graphs_set_input](#zones_graphs_set_input)
    * [zones_graphs_stddev_order_by](#zones_graphs_stddev_order_by)
    * [zones_graphs_stddev_pop_order_by](#zones_graphs_stddev_pop_order_by)
    * [zones_graphs_stddev_samp_order_by](#zones_graphs_stddev_samp_order_by)
    * [zones_graphs_sum_order_by](#zones_graphs_sum_order_by)
    * [zones_graphs_var_pop_order_by](#zones_graphs_var_pop_order_by)
    * [zones_graphs_var_samp_order_by](#zones_graphs_var_samp_order_by)
    * [zones_graphs_variance_order_by](#zones_graphs_variance_order_by)
    * [zones_insert_input](#zones_insert_input)
    * [zones_max_order_by](#zones_max_order_by)
    * [zones_min_order_by](#zones_min_order_by)
    * [zones_obj_rel_insert_input](#zones_obj_rel_insert_input)
    * [zones_on_conflict](#zones_on_conflict)
    * [zones_order_by](#zones_order_by)
    * [zones_pk_columns_input](#zones_pk_columns_input)
    * [zones_set_input](#zones_set_input)
    * [zones_stats_aggregate_order_by](#zones_stats_aggregate_order_by)
    * [zones_stats_append_input](#zones_stats_append_input)
    * [zones_stats_arr_rel_insert_input](#zones_stats_arr_rel_insert_input)
    * [zones_stats_avg_order_by](#zones_stats_avg_order_by)
    * [zones_stats_bool_exp](#zones_stats_bool_exp)
    * [zones_stats_delete_at_path_input](#zones_stats_delete_at_path_input)
    * [zones_stats_delete_elem_input](#zones_stats_delete_elem_input)
    * [zones_stats_delete_key_input](#zones_stats_delete_key_input)
    * [zones_stats_inc_input](#zones_stats_inc_input)
    * [zones_stats_insert_input](#zones_stats_insert_input)
    * [zones_stats_max_order_by](#zones_stats_max_order_by)
    * [zones_stats_min_order_by](#zones_stats_min_order_by)
    * [zones_stats_obj_rel_insert_input](#zones_stats_obj_rel_insert_input)
    * [zones_stats_on_conflict](#zones_stats_on_conflict)
    * [zones_stats_order_by](#zones_stats_order_by)
    * [zones_stats_pk_columns_input](#zones_stats_pk_columns_input)
    * [zones_stats_prepend_input](#zones_stats_prepend_input)
    * [zones_stats_set_input](#zones_stats_set_input)
    * [zones_stats_stddev_order_by](#zones_stats_stddev_order_by)
    * [zones_stats_stddev_pop_order_by](#zones_stats_stddev_pop_order_by)
    * [zones_stats_stddev_samp_order_by](#zones_stats_stddev_samp_order_by)
    * [zones_stats_sum_order_by](#zones_stats_sum_order_by)
    * [zones_stats_var_pop_order_by](#zones_stats_var_pop_order_by)
    * [zones_stats_var_samp_order_by](#zones_stats_var_samp_order_by)
    * [zones_stats_variance_order_by](#zones_stats_variance_order_by)
  * [Enums](#enums)
    * [active_addresses_constraint](#active_addresses_constraint)
    * [active_addresses_select_column](#active_addresses_select_column)
    * [active_addresses_update_column](#active_addresses_update_column)
    * [blocks_log_constraint](#blocks_log_constraint)
    * [blocks_log_select_column](#blocks_log_select_column)
    * [blocks_log_update_column](#blocks_log_update_column)
    * [headers_constraint](#headers_constraint)
    * [headers_select_column](#headers_select_column)
    * [headers_update_column](#headers_update_column)
    * [ibc_channel_zone_constraint](#ibc_channel_zone_constraint)
    * [ibc_channel_zone_select_column](#ibc_channel_zone_select_column)
    * [ibc_channel_zone_update_column](#ibc_channel_zone_update_column)
    * [ibc_channels_constraint](#ibc_channels_constraint)
    * [ibc_channels_select_column](#ibc_channels_select_column)
    * [ibc_channels_update_column](#ibc_channels_update_column)
    * [ibc_clients_constraint](#ibc_clients_constraint)
    * [ibc_clients_select_column](#ibc_clients_select_column)
    * [ibc_clients_update_column](#ibc_clients_update_column)
    * [ibc_connections_constraint](#ibc_connections_constraint)
    * [ibc_connections_select_column](#ibc_connections_select_column)
    * [ibc_connections_update_column](#ibc_connections_update_column)
    * [ibc_transfer_hourly_stats_constraint](#ibc_transfer_hourly_stats_constraint)
    * [ibc_transfer_hourly_stats_select_column](#ibc_transfer_hourly_stats_select_column)
    * [ibc_transfer_hourly_stats_update_column](#ibc_transfer_hourly_stats_update_column)
    * [order_by](#order_by)
    * [periods_constraint](#periods_constraint)
    * [periods_select_column](#periods_select_column)
    * [periods_update_column](#periods_update_column)
    * [total_tx_hourly_stats_constraint](#total_tx_hourly_stats_constraint)
    * [total_tx_hourly_stats_select_column](#total_tx_hourly_stats_select_column)
    * [total_tx_hourly_stats_update_column](#total_tx_hourly_stats_update_column)
    * [zone_nodes_constraint](#zone_nodes_constraint)
    * [zone_nodes_select_column](#zone_nodes_select_column)
    * [zone_nodes_update_column](#zone_nodes_update_column)
    * [zones_constraint](#zones_constraint)
    * [zones_graphs_constraint](#zones_graphs_constraint)
    * [zones_graphs_select_column](#zones_graphs_select_column)
    * [zones_graphs_update_column](#zones_graphs_update_column)
    * [zones_select_column](#zones_select_column)
    * [zones_stats_constraint](#zones_stats_constraint)
    * [zones_stats_select_column](#zones_stats_select_column)
    * [zones_stats_update_column](#zones_stats_update_column)
    * [zones_update_column](#zones_update_column)
  * [Scalars](#scalars)
    * [Boolean](#boolean)
    * [Float](#float)
    * [Int](#int)
    * [String](#string)
    * [bigint](#bigint)
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
<td colspan="2" valign="top"><strong>active_addresses</strong></td>
<td valign="top">[<a href="#active_addresses">active_addresses</a>!]!</td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">distinct_on</td>
<td valign="top">[<a href="#active_addresses_select_column">active_addresses_select_column</a>!]</td>
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
<td valign="top">[<a href="#active_addresses_order_by">active_addresses_order_by</a>!]</td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">where</td>
<td valign="top"><a href="#active_addresses_bool_exp">active_addresses_bool_exp</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>active_addresses_aggregate</strong></td>
<td valign="top"><a href="#active_addresses_aggregate">active_addresses_aggregate</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">distinct_on</td>
<td valign="top">[<a href="#active_addresses_select_column">active_addresses_select_column</a>!]</td>
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
<td valign="top">[<a href="#active_addresses_order_by">active_addresses_order_by</a>!]</td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">where</td>
<td valign="top"><a href="#active_addresses_bool_exp">active_addresses_bool_exp</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>active_addresses_by_pk</strong></td>
<td valign="top"><a href="#active_addresses">active_addresses</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">address</td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">hour</td>
<td valign="top"><a href="#timestamp">timestamp</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">period</td>
<td valign="top"><a href="#int">Int</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">zone</td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
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
<td colspan="2" valign="top"><strong>blocks_log_aggregate</strong></td>
<td valign="top"><a href="#blocks_log_aggregate">blocks_log_aggregate</a>!</td>
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
<td colspan="2" valign="top"><strong>ibc_channel_zone</strong></td>
<td valign="top">[<a href="#ibc_channel_zone">ibc_channel_zone</a>!]!</td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">distinct_on</td>
<td valign="top">[<a href="#ibc_channel_zone_select_column">ibc_channel_zone_select_column</a>!]</td>
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
<td valign="top">[<a href="#ibc_channel_zone_order_by">ibc_channel_zone_order_by</a>!]</td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">where</td>
<td valign="top"><a href="#ibc_channel_zone_bool_exp">ibc_channel_zone_bool_exp</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_channel_zone_aggregate</strong></td>
<td valign="top"><a href="#ibc_channel_zone_aggregate">ibc_channel_zone_aggregate</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">distinct_on</td>
<td valign="top">[<a href="#ibc_channel_zone_select_column">ibc_channel_zone_select_column</a>!]</td>
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
<td valign="top">[<a href="#ibc_channel_zone_order_by">ibc_channel_zone_order_by</a>!]</td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">where</td>
<td valign="top"><a href="#ibc_channel_zone_bool_exp">ibc_channel_zone_bool_exp</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_channel_zone_by_pk</strong></td>
<td valign="top"><a href="#ibc_channel_zone">ibc_channel_zone</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">chanel_id</td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">zone</td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_channels</strong></td>
<td valign="top">[<a href="#ibc_channels">ibc_channels</a>!]!</td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">distinct_on</td>
<td valign="top">[<a href="#ibc_channels_select_column">ibc_channels_select_column</a>!]</td>
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
<td valign="top">[<a href="#ibc_channels_order_by">ibc_channels_order_by</a>!]</td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">where</td>
<td valign="top"><a href="#ibc_channels_bool_exp">ibc_channels_bool_exp</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_channels_aggregate</strong></td>
<td valign="top"><a href="#ibc_channels_aggregate">ibc_channels_aggregate</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">distinct_on</td>
<td valign="top">[<a href="#ibc_channels_select_column">ibc_channels_select_column</a>!]</td>
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
<td valign="top">[<a href="#ibc_channels_order_by">ibc_channels_order_by</a>!]</td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">where</td>
<td valign="top"><a href="#ibc_channels_bool_exp">ibc_channels_bool_exp</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_channels_by_pk</strong></td>
<td valign="top"><a href="#ibc_channels">ibc_channels</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">channel_id</td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">zone</td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_clients</strong></td>
<td valign="top">[<a href="#ibc_clients">ibc_clients</a>!]!</td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">distinct_on</td>
<td valign="top">[<a href="#ibc_clients_select_column">ibc_clients_select_column</a>!]</td>
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
<td valign="top">[<a href="#ibc_clients_order_by">ibc_clients_order_by</a>!]</td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">where</td>
<td valign="top"><a href="#ibc_clients_bool_exp">ibc_clients_bool_exp</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_clients_aggregate</strong></td>
<td valign="top"><a href="#ibc_clients_aggregate">ibc_clients_aggregate</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">distinct_on</td>
<td valign="top">[<a href="#ibc_clients_select_column">ibc_clients_select_column</a>!]</td>
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
<td valign="top">[<a href="#ibc_clients_order_by">ibc_clients_order_by</a>!]</td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">where</td>
<td valign="top"><a href="#ibc_clients_bool_exp">ibc_clients_bool_exp</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_clients_by_pk</strong></td>
<td valign="top"><a href="#ibc_clients">ibc_clients</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">client_id</td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">zone</td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_connections</strong></td>
<td valign="top">[<a href="#ibc_connections">ibc_connections</a>!]!</td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">distinct_on</td>
<td valign="top">[<a href="#ibc_connections_select_column">ibc_connections_select_column</a>!]</td>
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
<td valign="top">[<a href="#ibc_connections_order_by">ibc_connections_order_by</a>!]</td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">where</td>
<td valign="top"><a href="#ibc_connections_bool_exp">ibc_connections_bool_exp</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_connections_aggregate</strong></td>
<td valign="top"><a href="#ibc_connections_aggregate">ibc_connections_aggregate</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">distinct_on</td>
<td valign="top">[<a href="#ibc_connections_select_column">ibc_connections_select_column</a>!]</td>
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
<td valign="top">[<a href="#ibc_connections_order_by">ibc_connections_order_by</a>!]</td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">where</td>
<td valign="top"><a href="#ibc_connections_bool_exp">ibc_connections_bool_exp</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_connections_by_pk</strong></td>
<td valign="top"><a href="#ibc_connections">ibc_connections</a></td>
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
<td colspan="2" valign="top"><strong>ibc_transfer_hourly_stats</strong></td>
<td valign="top">[<a href="#ibc_transfer_hourly_stats">ibc_transfer_hourly_stats</a>!]!</td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">distinct_on</td>
<td valign="top">[<a href="#ibc_transfer_hourly_stats_select_column">ibc_transfer_hourly_stats_select_column</a>!]</td>
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
<td valign="top">[<a href="#ibc_transfer_hourly_stats_order_by">ibc_transfer_hourly_stats_order_by</a>!]</td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">where</td>
<td valign="top"><a href="#ibc_transfer_hourly_stats_bool_exp">ibc_transfer_hourly_stats_bool_exp</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_transfer_hourly_stats_aggregate</strong></td>
<td valign="top"><a href="#ibc_transfer_hourly_stats_aggregate">ibc_transfer_hourly_stats_aggregate</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">distinct_on</td>
<td valign="top">[<a href="#ibc_transfer_hourly_stats_select_column">ibc_transfer_hourly_stats_select_column</a>!]</td>
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
<td valign="top">[<a href="#ibc_transfer_hourly_stats_order_by">ibc_transfer_hourly_stats_order_by</a>!]</td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">where</td>
<td valign="top"><a href="#ibc_transfer_hourly_stats_bool_exp">ibc_transfer_hourly_stats_bool_exp</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_transfer_hourly_stats_by_pk</strong></td>
<td valign="top"><a href="#ibc_transfer_hourly_stats">ibc_transfer_hourly_stats</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">hour</td>
<td valign="top"><a href="#timestamp">timestamp</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">period</td>
<td valign="top"><a href="#int">Int</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">zone</td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">zone_dest</td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">zone_src</td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>periods</strong></td>
<td valign="top">[<a href="#periods">periods</a>!]!</td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">distinct_on</td>
<td valign="top">[<a href="#periods_select_column">periods_select_column</a>!]</td>
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
<td valign="top">[<a href="#periods_order_by">periods_order_by</a>!]</td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">where</td>
<td valign="top"><a href="#periods_bool_exp">periods_bool_exp</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>periods_aggregate</strong></td>
<td valign="top"><a href="#periods_aggregate">periods_aggregate</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">distinct_on</td>
<td valign="top">[<a href="#periods_select_column">periods_select_column</a>!]</td>
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
<td valign="top">[<a href="#periods_order_by">periods_order_by</a>!]</td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">where</td>
<td valign="top"><a href="#periods_bool_exp">periods_bool_exp</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>periods_by_pk</strong></td>
<td valign="top"><a href="#periods">periods</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">period_in_hours</td>
<td valign="top"><a href="#int">Int</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_tx_hourly_stats</strong></td>
<td valign="top">[<a href="#total_tx_hourly_stats">total_tx_hourly_stats</a>!]!</td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">distinct_on</td>
<td valign="top">[<a href="#total_tx_hourly_stats_select_column">total_tx_hourly_stats_select_column</a>!]</td>
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
<td valign="top">[<a href="#total_tx_hourly_stats_order_by">total_tx_hourly_stats_order_by</a>!]</td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">where</td>
<td valign="top"><a href="#total_tx_hourly_stats_bool_exp">total_tx_hourly_stats_bool_exp</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_tx_hourly_stats_aggregate</strong></td>
<td valign="top"><a href="#total_tx_hourly_stats_aggregate">total_tx_hourly_stats_aggregate</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">distinct_on</td>
<td valign="top">[<a href="#total_tx_hourly_stats_select_column">total_tx_hourly_stats_select_column</a>!]</td>
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
<td valign="top">[<a href="#total_tx_hourly_stats_order_by">total_tx_hourly_stats_order_by</a>!]</td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">where</td>
<td valign="top"><a href="#total_tx_hourly_stats_bool_exp">total_tx_hourly_stats_bool_exp</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_tx_hourly_stats_by_pk</strong></td>
<td valign="top"><a href="#total_tx_hourly_stats">total_tx_hourly_stats</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">hour</td>
<td valign="top"><a href="#timestamp">timestamp</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">period</td>
<td valign="top"><a href="#int">Int</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">zone</td>
<td valign="top"><a href="#string">String</a>!</td>
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
<td colspan="2" align="right" valign="top">zone</td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>zones</strong></td>
<td valign="top">[<a href="#zones">zones</a>!]!</td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">distinct_on</td>
<td valign="top">[<a href="#zones_select_column">zones_select_column</a>!]</td>
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
<td valign="top">[<a href="#zones_order_by">zones_order_by</a>!]</td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">where</td>
<td valign="top"><a href="#zones_bool_exp">zones_bool_exp</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>zones_aggregate</strong></td>
<td valign="top"><a href="#zones_aggregate">zones_aggregate</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">distinct_on</td>
<td valign="top">[<a href="#zones_select_column">zones_select_column</a>!]</td>
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
<td valign="top">[<a href="#zones_order_by">zones_order_by</a>!]</td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">where</td>
<td valign="top"><a href="#zones_bool_exp">zones_bool_exp</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>zones_by_pk</strong></td>
<td valign="top"><a href="#zones">zones</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">chain_id</td>
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

## Mutation (mutation_root)
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
<td colspan="2" valign="top"><strong>delete_active_addresses</strong></td>
<td valign="top"><a href="#active_addresses_mutation_response">active_addresses_mutation_response</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">where</td>
<td valign="top"><a href="#active_addresses_bool_exp">active_addresses_bool_exp</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>delete_active_addresses_by_pk</strong></td>
<td valign="top"><a href="#active_addresses">active_addresses</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">address</td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">hour</td>
<td valign="top"><a href="#timestamp">timestamp</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">period</td>
<td valign="top"><a href="#int">Int</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">zone</td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>delete_blocks_log</strong></td>
<td valign="top"><a href="#blocks_log_mutation_response">blocks_log_mutation_response</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">where</td>
<td valign="top"><a href="#blocks_log_bool_exp">blocks_log_bool_exp</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>delete_blocks_log_by_pk</strong></td>
<td valign="top"><a href="#blocks_log">blocks_log</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">zone</td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>delete_headers</strong></td>
<td valign="top"><a href="#headers_mutation_response">headers_mutation_response</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">where</td>
<td valign="top"><a href="#headers_bool_exp">headers_bool_exp</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>delete_headers_by_pk</strong></td>
<td valign="top"><a href="#headers">headers</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">timeframe</td>
<td valign="top"><a href="#int">Int</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>delete_ibc_channel_zone</strong></td>
<td valign="top"><a href="#ibc_channel_zone_mutation_response">ibc_channel_zone_mutation_response</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">where</td>
<td valign="top"><a href="#ibc_channel_zone_bool_exp">ibc_channel_zone_bool_exp</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>delete_ibc_channel_zone_by_pk</strong></td>
<td valign="top"><a href="#ibc_channel_zone">ibc_channel_zone</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">chanel_id</td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">zone</td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>delete_ibc_channels</strong></td>
<td valign="top"><a href="#ibc_channels_mutation_response">ibc_channels_mutation_response</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">where</td>
<td valign="top"><a href="#ibc_channels_bool_exp">ibc_channels_bool_exp</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>delete_ibc_channels_by_pk</strong></td>
<td valign="top"><a href="#ibc_channels">ibc_channels</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">channel_id</td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">zone</td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>delete_ibc_clients</strong></td>
<td valign="top"><a href="#ibc_clients_mutation_response">ibc_clients_mutation_response</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">where</td>
<td valign="top"><a href="#ibc_clients_bool_exp">ibc_clients_bool_exp</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>delete_ibc_clients_by_pk</strong></td>
<td valign="top"><a href="#ibc_clients">ibc_clients</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">client_id</td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">zone</td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>delete_ibc_connections</strong></td>
<td valign="top"><a href="#ibc_connections_mutation_response">ibc_connections_mutation_response</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">where</td>
<td valign="top"><a href="#ibc_connections_bool_exp">ibc_connections_bool_exp</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>delete_ibc_connections_by_pk</strong></td>
<td valign="top"><a href="#ibc_connections">ibc_connections</a></td>
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
<td colspan="2" valign="top"><strong>delete_ibc_transfer_hourly_stats</strong></td>
<td valign="top"><a href="#ibc_transfer_hourly_stats_mutation_response">ibc_transfer_hourly_stats_mutation_response</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">where</td>
<td valign="top"><a href="#ibc_transfer_hourly_stats_bool_exp">ibc_transfer_hourly_stats_bool_exp</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>delete_ibc_transfer_hourly_stats_by_pk</strong></td>
<td valign="top"><a href="#ibc_transfer_hourly_stats">ibc_transfer_hourly_stats</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">hour</td>
<td valign="top"><a href="#timestamp">timestamp</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">period</td>
<td valign="top"><a href="#int">Int</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">zone</td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">zone_dest</td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">zone_src</td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>delete_periods</strong></td>
<td valign="top"><a href="#periods_mutation_response">periods_mutation_response</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">where</td>
<td valign="top"><a href="#periods_bool_exp">periods_bool_exp</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>delete_periods_by_pk</strong></td>
<td valign="top"><a href="#periods">periods</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">period_in_hours</td>
<td valign="top"><a href="#int">Int</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>delete_total_tx_hourly_stats</strong></td>
<td valign="top"><a href="#total_tx_hourly_stats_mutation_response">total_tx_hourly_stats_mutation_response</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">where</td>
<td valign="top"><a href="#total_tx_hourly_stats_bool_exp">total_tx_hourly_stats_bool_exp</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>delete_total_tx_hourly_stats_by_pk</strong></td>
<td valign="top"><a href="#total_tx_hourly_stats">total_tx_hourly_stats</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">hour</td>
<td valign="top"><a href="#timestamp">timestamp</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">period</td>
<td valign="top"><a href="#int">Int</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">zone</td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>delete_zone_nodes</strong></td>
<td valign="top"><a href="#zone_nodes_mutation_response">zone_nodes_mutation_response</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">where</td>
<td valign="top"><a href="#zone_nodes_bool_exp">zone_nodes_bool_exp</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>delete_zone_nodes_by_pk</strong></td>
<td valign="top"><a href="#zone_nodes">zone_nodes</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">rpc_addr</td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">zone</td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>delete_zones</strong></td>
<td valign="top"><a href="#zones_mutation_response">zones_mutation_response</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">where</td>
<td valign="top"><a href="#zones_bool_exp">zones_bool_exp</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>delete_zones_by_pk</strong></td>
<td valign="top"><a href="#zones">zones</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">chain_id</td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>delete_zones_graphs</strong></td>
<td valign="top"><a href="#zones_graphs_mutation_response">zones_graphs_mutation_response</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">where</td>
<td valign="top"><a href="#zones_graphs_bool_exp">zones_graphs_bool_exp</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>delete_zones_graphs_by_pk</strong></td>
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
<td colspan="2" valign="top"><strong>delete_zones_stats</strong></td>
<td valign="top"><a href="#zones_stats_mutation_response">zones_stats_mutation_response</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">where</td>
<td valign="top"><a href="#zones_stats_bool_exp">zones_stats_bool_exp</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>delete_zones_stats_by_pk</strong></td>
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
<tr>
<td colspan="2" valign="top"><strong>insert_active_addresses</strong></td>
<td valign="top"><a href="#active_addresses_mutation_response">active_addresses_mutation_response</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">objects</td>
<td valign="top">[<a href="#active_addresses_insert_input">active_addresses_insert_input</a>!]!</td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">on_conflict</td>
<td valign="top"><a href="#active_addresses_on_conflict">active_addresses_on_conflict</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>insert_active_addresses_one</strong></td>
<td valign="top"><a href="#active_addresses">active_addresses</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">object</td>
<td valign="top"><a href="#active_addresses_insert_input">active_addresses_insert_input</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">on_conflict</td>
<td valign="top"><a href="#active_addresses_on_conflict">active_addresses_on_conflict</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>insert_blocks_log</strong></td>
<td valign="top"><a href="#blocks_log_mutation_response">blocks_log_mutation_response</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">objects</td>
<td valign="top">[<a href="#blocks_log_insert_input">blocks_log_insert_input</a>!]!</td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">on_conflict</td>
<td valign="top"><a href="#blocks_log_on_conflict">blocks_log_on_conflict</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>insert_blocks_log_one</strong></td>
<td valign="top"><a href="#blocks_log">blocks_log</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">object</td>
<td valign="top"><a href="#blocks_log_insert_input">blocks_log_insert_input</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">on_conflict</td>
<td valign="top"><a href="#blocks_log_on_conflict">blocks_log_on_conflict</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>insert_headers</strong></td>
<td valign="top"><a href="#headers_mutation_response">headers_mutation_response</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">objects</td>
<td valign="top">[<a href="#headers_insert_input">headers_insert_input</a>!]!</td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">on_conflict</td>
<td valign="top"><a href="#headers_on_conflict">headers_on_conflict</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>insert_headers_one</strong></td>
<td valign="top"><a href="#headers">headers</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">object</td>
<td valign="top"><a href="#headers_insert_input">headers_insert_input</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">on_conflict</td>
<td valign="top"><a href="#headers_on_conflict">headers_on_conflict</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>insert_ibc_channel_zone</strong></td>
<td valign="top"><a href="#ibc_channel_zone_mutation_response">ibc_channel_zone_mutation_response</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">objects</td>
<td valign="top">[<a href="#ibc_channel_zone_insert_input">ibc_channel_zone_insert_input</a>!]!</td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">on_conflict</td>
<td valign="top"><a href="#ibc_channel_zone_on_conflict">ibc_channel_zone_on_conflict</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>insert_ibc_channel_zone_one</strong></td>
<td valign="top"><a href="#ibc_channel_zone">ibc_channel_zone</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">object</td>
<td valign="top"><a href="#ibc_channel_zone_insert_input">ibc_channel_zone_insert_input</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">on_conflict</td>
<td valign="top"><a href="#ibc_channel_zone_on_conflict">ibc_channel_zone_on_conflict</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>insert_ibc_channels</strong></td>
<td valign="top"><a href="#ibc_channels_mutation_response">ibc_channels_mutation_response</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">objects</td>
<td valign="top">[<a href="#ibc_channels_insert_input">ibc_channels_insert_input</a>!]!</td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">on_conflict</td>
<td valign="top"><a href="#ibc_channels_on_conflict">ibc_channels_on_conflict</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>insert_ibc_channels_one</strong></td>
<td valign="top"><a href="#ibc_channels">ibc_channels</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">object</td>
<td valign="top"><a href="#ibc_channels_insert_input">ibc_channels_insert_input</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">on_conflict</td>
<td valign="top"><a href="#ibc_channels_on_conflict">ibc_channels_on_conflict</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>insert_ibc_clients</strong></td>
<td valign="top"><a href="#ibc_clients_mutation_response">ibc_clients_mutation_response</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">objects</td>
<td valign="top">[<a href="#ibc_clients_insert_input">ibc_clients_insert_input</a>!]!</td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">on_conflict</td>
<td valign="top"><a href="#ibc_clients_on_conflict">ibc_clients_on_conflict</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>insert_ibc_clients_one</strong></td>
<td valign="top"><a href="#ibc_clients">ibc_clients</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">object</td>
<td valign="top"><a href="#ibc_clients_insert_input">ibc_clients_insert_input</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">on_conflict</td>
<td valign="top"><a href="#ibc_clients_on_conflict">ibc_clients_on_conflict</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>insert_ibc_connections</strong></td>
<td valign="top"><a href="#ibc_connections_mutation_response">ibc_connections_mutation_response</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">objects</td>
<td valign="top">[<a href="#ibc_connections_insert_input">ibc_connections_insert_input</a>!]!</td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">on_conflict</td>
<td valign="top"><a href="#ibc_connections_on_conflict">ibc_connections_on_conflict</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>insert_ibc_connections_one</strong></td>
<td valign="top"><a href="#ibc_connections">ibc_connections</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">object</td>
<td valign="top"><a href="#ibc_connections_insert_input">ibc_connections_insert_input</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">on_conflict</td>
<td valign="top"><a href="#ibc_connections_on_conflict">ibc_connections_on_conflict</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>insert_ibc_transfer_hourly_stats</strong></td>
<td valign="top"><a href="#ibc_transfer_hourly_stats_mutation_response">ibc_transfer_hourly_stats_mutation_response</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">objects</td>
<td valign="top">[<a href="#ibc_transfer_hourly_stats_insert_input">ibc_transfer_hourly_stats_insert_input</a>!]!</td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">on_conflict</td>
<td valign="top"><a href="#ibc_transfer_hourly_stats_on_conflict">ibc_transfer_hourly_stats_on_conflict</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>insert_ibc_transfer_hourly_stats_one</strong></td>
<td valign="top"><a href="#ibc_transfer_hourly_stats">ibc_transfer_hourly_stats</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">object</td>
<td valign="top"><a href="#ibc_transfer_hourly_stats_insert_input">ibc_transfer_hourly_stats_insert_input</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">on_conflict</td>
<td valign="top"><a href="#ibc_transfer_hourly_stats_on_conflict">ibc_transfer_hourly_stats_on_conflict</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>insert_periods</strong></td>
<td valign="top"><a href="#periods_mutation_response">periods_mutation_response</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">objects</td>
<td valign="top">[<a href="#periods_insert_input">periods_insert_input</a>!]!</td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">on_conflict</td>
<td valign="top"><a href="#periods_on_conflict">periods_on_conflict</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>insert_periods_one</strong></td>
<td valign="top"><a href="#periods">periods</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">object</td>
<td valign="top"><a href="#periods_insert_input">periods_insert_input</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">on_conflict</td>
<td valign="top"><a href="#periods_on_conflict">periods_on_conflict</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>insert_total_tx_hourly_stats</strong></td>
<td valign="top"><a href="#total_tx_hourly_stats_mutation_response">total_tx_hourly_stats_mutation_response</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">objects</td>
<td valign="top">[<a href="#total_tx_hourly_stats_insert_input">total_tx_hourly_stats_insert_input</a>!]!</td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">on_conflict</td>
<td valign="top"><a href="#total_tx_hourly_stats_on_conflict">total_tx_hourly_stats_on_conflict</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>insert_total_tx_hourly_stats_one</strong></td>
<td valign="top"><a href="#total_tx_hourly_stats">total_tx_hourly_stats</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">object</td>
<td valign="top"><a href="#total_tx_hourly_stats_insert_input">total_tx_hourly_stats_insert_input</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">on_conflict</td>
<td valign="top"><a href="#total_tx_hourly_stats_on_conflict">total_tx_hourly_stats_on_conflict</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>insert_zone_nodes</strong></td>
<td valign="top"><a href="#zone_nodes_mutation_response">zone_nodes_mutation_response</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">objects</td>
<td valign="top">[<a href="#zone_nodes_insert_input">zone_nodes_insert_input</a>!]!</td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">on_conflict</td>
<td valign="top"><a href="#zone_nodes_on_conflict">zone_nodes_on_conflict</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>insert_zone_nodes_one</strong></td>
<td valign="top"><a href="#zone_nodes">zone_nodes</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">object</td>
<td valign="top"><a href="#zone_nodes_insert_input">zone_nodes_insert_input</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">on_conflict</td>
<td valign="top"><a href="#zone_nodes_on_conflict">zone_nodes_on_conflict</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>insert_zones</strong></td>
<td valign="top"><a href="#zones_mutation_response">zones_mutation_response</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">objects</td>
<td valign="top">[<a href="#zones_insert_input">zones_insert_input</a>!]!</td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">on_conflict</td>
<td valign="top"><a href="#zones_on_conflict">zones_on_conflict</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>insert_zones_graphs</strong></td>
<td valign="top"><a href="#zones_graphs_mutation_response">zones_graphs_mutation_response</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">objects</td>
<td valign="top">[<a href="#zones_graphs_insert_input">zones_graphs_insert_input</a>!]!</td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">on_conflict</td>
<td valign="top"><a href="#zones_graphs_on_conflict">zones_graphs_on_conflict</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>insert_zones_graphs_one</strong></td>
<td valign="top"><a href="#zones_graphs">zones_graphs</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">object</td>
<td valign="top"><a href="#zones_graphs_insert_input">zones_graphs_insert_input</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">on_conflict</td>
<td valign="top"><a href="#zones_graphs_on_conflict">zones_graphs_on_conflict</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>insert_zones_one</strong></td>
<td valign="top"><a href="#zones">zones</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">object</td>
<td valign="top"><a href="#zones_insert_input">zones_insert_input</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">on_conflict</td>
<td valign="top"><a href="#zones_on_conflict">zones_on_conflict</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>insert_zones_stats</strong></td>
<td valign="top"><a href="#zones_stats_mutation_response">zones_stats_mutation_response</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">objects</td>
<td valign="top">[<a href="#zones_stats_insert_input">zones_stats_insert_input</a>!]!</td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">on_conflict</td>
<td valign="top"><a href="#zones_stats_on_conflict">zones_stats_on_conflict</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>insert_zones_stats_one</strong></td>
<td valign="top"><a href="#zones_stats">zones_stats</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">object</td>
<td valign="top"><a href="#zones_stats_insert_input">zones_stats_insert_input</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">on_conflict</td>
<td valign="top"><a href="#zones_stats_on_conflict">zones_stats_on_conflict</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>update_active_addresses</strong></td>
<td valign="top"><a href="#active_addresses_mutation_response">active_addresses_mutation_response</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">_inc</td>
<td valign="top"><a href="#active_addresses_inc_input">active_addresses_inc_input</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">_set</td>
<td valign="top"><a href="#active_addresses_set_input">active_addresses_set_input</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">where</td>
<td valign="top"><a href="#active_addresses_bool_exp">active_addresses_bool_exp</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>update_active_addresses_by_pk</strong></td>
<td valign="top"><a href="#active_addresses">active_addresses</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">_inc</td>
<td valign="top"><a href="#active_addresses_inc_input">active_addresses_inc_input</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">_set</td>
<td valign="top"><a href="#active_addresses_set_input">active_addresses_set_input</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">pk_columns</td>
<td valign="top"><a href="#active_addresses_pk_columns_input">active_addresses_pk_columns_input</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>update_blocks_log</strong></td>
<td valign="top"><a href="#blocks_log_mutation_response">blocks_log_mutation_response</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">_inc</td>
<td valign="top"><a href="#blocks_log_inc_input">blocks_log_inc_input</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">_set</td>
<td valign="top"><a href="#blocks_log_set_input">blocks_log_set_input</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">where</td>
<td valign="top"><a href="#blocks_log_bool_exp">blocks_log_bool_exp</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>update_blocks_log_by_pk</strong></td>
<td valign="top"><a href="#blocks_log">blocks_log</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">_inc</td>
<td valign="top"><a href="#blocks_log_inc_input">blocks_log_inc_input</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">_set</td>
<td valign="top"><a href="#blocks_log_set_input">blocks_log_set_input</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">pk_columns</td>
<td valign="top"><a href="#blocks_log_pk_columns_input">blocks_log_pk_columns_input</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>update_headers</strong></td>
<td valign="top"><a href="#headers_mutation_response">headers_mutation_response</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">_append</td>
<td valign="top"><a href="#headers_append_input">headers_append_input</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">_delete_at_path</td>
<td valign="top"><a href="#headers_delete_at_path_input">headers_delete_at_path_input</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">_delete_elem</td>
<td valign="top"><a href="#headers_delete_elem_input">headers_delete_elem_input</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">_delete_key</td>
<td valign="top"><a href="#headers_delete_key_input">headers_delete_key_input</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">_inc</td>
<td valign="top"><a href="#headers_inc_input">headers_inc_input</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">_prepend</td>
<td valign="top"><a href="#headers_prepend_input">headers_prepend_input</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">_set</td>
<td valign="top"><a href="#headers_set_input">headers_set_input</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">where</td>
<td valign="top"><a href="#headers_bool_exp">headers_bool_exp</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>update_headers_by_pk</strong></td>
<td valign="top"><a href="#headers">headers</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">_append</td>
<td valign="top"><a href="#headers_append_input">headers_append_input</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">_delete_at_path</td>
<td valign="top"><a href="#headers_delete_at_path_input">headers_delete_at_path_input</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">_delete_elem</td>
<td valign="top"><a href="#headers_delete_elem_input">headers_delete_elem_input</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">_delete_key</td>
<td valign="top"><a href="#headers_delete_key_input">headers_delete_key_input</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">_inc</td>
<td valign="top"><a href="#headers_inc_input">headers_inc_input</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">_prepend</td>
<td valign="top"><a href="#headers_prepend_input">headers_prepend_input</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">_set</td>
<td valign="top"><a href="#headers_set_input">headers_set_input</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">pk_columns</td>
<td valign="top"><a href="#headers_pk_columns_input">headers_pk_columns_input</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>update_ibc_channel_zone</strong></td>
<td valign="top"><a href="#ibc_channel_zone_mutation_response">ibc_channel_zone_mutation_response</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">_set</td>
<td valign="top"><a href="#ibc_channel_zone_set_input">ibc_channel_zone_set_input</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">where</td>
<td valign="top"><a href="#ibc_channel_zone_bool_exp">ibc_channel_zone_bool_exp</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>update_ibc_channel_zone_by_pk</strong></td>
<td valign="top"><a href="#ibc_channel_zone">ibc_channel_zone</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">_set</td>
<td valign="top"><a href="#ibc_channel_zone_set_input">ibc_channel_zone_set_input</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">pk_columns</td>
<td valign="top"><a href="#ibc_channel_zone_pk_columns_input">ibc_channel_zone_pk_columns_input</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>update_ibc_channels</strong></td>
<td valign="top"><a href="#ibc_channels_mutation_response">ibc_channels_mutation_response</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">_set</td>
<td valign="top"><a href="#ibc_channels_set_input">ibc_channels_set_input</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">where</td>
<td valign="top"><a href="#ibc_channels_bool_exp">ibc_channels_bool_exp</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>update_ibc_channels_by_pk</strong></td>
<td valign="top"><a href="#ibc_channels">ibc_channels</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">_set</td>
<td valign="top"><a href="#ibc_channels_set_input">ibc_channels_set_input</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">pk_columns</td>
<td valign="top"><a href="#ibc_channels_pk_columns_input">ibc_channels_pk_columns_input</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>update_ibc_clients</strong></td>
<td valign="top"><a href="#ibc_clients_mutation_response">ibc_clients_mutation_response</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">_set</td>
<td valign="top"><a href="#ibc_clients_set_input">ibc_clients_set_input</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">where</td>
<td valign="top"><a href="#ibc_clients_bool_exp">ibc_clients_bool_exp</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>update_ibc_clients_by_pk</strong></td>
<td valign="top"><a href="#ibc_clients">ibc_clients</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">_set</td>
<td valign="top"><a href="#ibc_clients_set_input">ibc_clients_set_input</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">pk_columns</td>
<td valign="top"><a href="#ibc_clients_pk_columns_input">ibc_clients_pk_columns_input</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>update_ibc_connections</strong></td>
<td valign="top"><a href="#ibc_connections_mutation_response">ibc_connections_mutation_response</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">_set</td>
<td valign="top"><a href="#ibc_connections_set_input">ibc_connections_set_input</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">where</td>
<td valign="top"><a href="#ibc_connections_bool_exp">ibc_connections_bool_exp</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>update_ibc_connections_by_pk</strong></td>
<td valign="top"><a href="#ibc_connections">ibc_connections</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">_set</td>
<td valign="top"><a href="#ibc_connections_set_input">ibc_connections_set_input</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">pk_columns</td>
<td valign="top"><a href="#ibc_connections_pk_columns_input">ibc_connections_pk_columns_input</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>update_ibc_transfer_hourly_stats</strong></td>
<td valign="top"><a href="#ibc_transfer_hourly_stats_mutation_response">ibc_transfer_hourly_stats_mutation_response</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">_inc</td>
<td valign="top"><a href="#ibc_transfer_hourly_stats_inc_input">ibc_transfer_hourly_stats_inc_input</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">_set</td>
<td valign="top"><a href="#ibc_transfer_hourly_stats_set_input">ibc_transfer_hourly_stats_set_input</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">where</td>
<td valign="top"><a href="#ibc_transfer_hourly_stats_bool_exp">ibc_transfer_hourly_stats_bool_exp</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>update_ibc_transfer_hourly_stats_by_pk</strong></td>
<td valign="top"><a href="#ibc_transfer_hourly_stats">ibc_transfer_hourly_stats</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">_inc</td>
<td valign="top"><a href="#ibc_transfer_hourly_stats_inc_input">ibc_transfer_hourly_stats_inc_input</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">_set</td>
<td valign="top"><a href="#ibc_transfer_hourly_stats_set_input">ibc_transfer_hourly_stats_set_input</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">pk_columns</td>
<td valign="top"><a href="#ibc_transfer_hourly_stats_pk_columns_input">ibc_transfer_hourly_stats_pk_columns_input</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>update_periods</strong></td>
<td valign="top"><a href="#periods_mutation_response">periods_mutation_response</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">_inc</td>
<td valign="top"><a href="#periods_inc_input">periods_inc_input</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">_set</td>
<td valign="top"><a href="#periods_set_input">periods_set_input</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">where</td>
<td valign="top"><a href="#periods_bool_exp">periods_bool_exp</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>update_periods_by_pk</strong></td>
<td valign="top"><a href="#periods">periods</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">_inc</td>
<td valign="top"><a href="#periods_inc_input">periods_inc_input</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">_set</td>
<td valign="top"><a href="#periods_set_input">periods_set_input</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">pk_columns</td>
<td valign="top"><a href="#periods_pk_columns_input">periods_pk_columns_input</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>update_total_tx_hourly_stats</strong></td>
<td valign="top"><a href="#total_tx_hourly_stats_mutation_response">total_tx_hourly_stats_mutation_response</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">_inc</td>
<td valign="top"><a href="#total_tx_hourly_stats_inc_input">total_tx_hourly_stats_inc_input</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">_set</td>
<td valign="top"><a href="#total_tx_hourly_stats_set_input">total_tx_hourly_stats_set_input</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">where</td>
<td valign="top"><a href="#total_tx_hourly_stats_bool_exp">total_tx_hourly_stats_bool_exp</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>update_total_tx_hourly_stats_by_pk</strong></td>
<td valign="top"><a href="#total_tx_hourly_stats">total_tx_hourly_stats</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">_inc</td>
<td valign="top"><a href="#total_tx_hourly_stats_inc_input">total_tx_hourly_stats_inc_input</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">_set</td>
<td valign="top"><a href="#total_tx_hourly_stats_set_input">total_tx_hourly_stats_set_input</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">pk_columns</td>
<td valign="top"><a href="#total_tx_hourly_stats_pk_columns_input">total_tx_hourly_stats_pk_columns_input</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>update_zone_nodes</strong></td>
<td valign="top"><a href="#zone_nodes_mutation_response">zone_nodes_mutation_response</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">_set</td>
<td valign="top"><a href="#zone_nodes_set_input">zone_nodes_set_input</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">where</td>
<td valign="top"><a href="#zone_nodes_bool_exp">zone_nodes_bool_exp</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>update_zone_nodes_by_pk</strong></td>
<td valign="top"><a href="#zone_nodes">zone_nodes</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">_set</td>
<td valign="top"><a href="#zone_nodes_set_input">zone_nodes_set_input</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">pk_columns</td>
<td valign="top"><a href="#zone_nodes_pk_columns_input">zone_nodes_pk_columns_input</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>update_zones</strong></td>
<td valign="top"><a href="#zones_mutation_response">zones_mutation_response</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">_set</td>
<td valign="top"><a href="#zones_set_input">zones_set_input</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">where</td>
<td valign="top"><a href="#zones_bool_exp">zones_bool_exp</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>update_zones_by_pk</strong></td>
<td valign="top"><a href="#zones">zones</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">_set</td>
<td valign="top"><a href="#zones_set_input">zones_set_input</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">pk_columns</td>
<td valign="top"><a href="#zones_pk_columns_input">zones_pk_columns_input</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>update_zones_graphs</strong></td>
<td valign="top"><a href="#zones_graphs_mutation_response">zones_graphs_mutation_response</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">_inc</td>
<td valign="top"><a href="#zones_graphs_inc_input">zones_graphs_inc_input</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">_set</td>
<td valign="top"><a href="#zones_graphs_set_input">zones_graphs_set_input</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">where</td>
<td valign="top"><a href="#zones_graphs_bool_exp">zones_graphs_bool_exp</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>update_zones_graphs_by_pk</strong></td>
<td valign="top"><a href="#zones_graphs">zones_graphs</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">_inc</td>
<td valign="top"><a href="#zones_graphs_inc_input">zones_graphs_inc_input</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">_set</td>
<td valign="top"><a href="#zones_graphs_set_input">zones_graphs_set_input</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">pk_columns</td>
<td valign="top"><a href="#zones_graphs_pk_columns_input">zones_graphs_pk_columns_input</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>update_zones_stats</strong></td>
<td valign="top"><a href="#zones_stats_mutation_response">zones_stats_mutation_response</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">_append</td>
<td valign="top"><a href="#zones_stats_append_input">zones_stats_append_input</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">_delete_at_path</td>
<td valign="top"><a href="#zones_stats_delete_at_path_input">zones_stats_delete_at_path_input</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">_delete_elem</td>
<td valign="top"><a href="#zones_stats_delete_elem_input">zones_stats_delete_elem_input</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">_delete_key</td>
<td valign="top"><a href="#zones_stats_delete_key_input">zones_stats_delete_key_input</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">_inc</td>
<td valign="top"><a href="#zones_stats_inc_input">zones_stats_inc_input</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">_prepend</td>
<td valign="top"><a href="#zones_stats_prepend_input">zones_stats_prepend_input</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">_set</td>
<td valign="top"><a href="#zones_stats_set_input">zones_stats_set_input</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">where</td>
<td valign="top"><a href="#zones_stats_bool_exp">zones_stats_bool_exp</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>update_zones_stats_by_pk</strong></td>
<td valign="top"><a href="#zones_stats">zones_stats</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">_append</td>
<td valign="top"><a href="#zones_stats_append_input">zones_stats_append_input</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">_delete_at_path</td>
<td valign="top"><a href="#zones_stats_delete_at_path_input">zones_stats_delete_at_path_input</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">_delete_elem</td>
<td valign="top"><a href="#zones_stats_delete_elem_input">zones_stats_delete_elem_input</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">_delete_key</td>
<td valign="top"><a href="#zones_stats_delete_key_input">zones_stats_delete_key_input</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">_inc</td>
<td valign="top"><a href="#zones_stats_inc_input">zones_stats_inc_input</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">_prepend</td>
<td valign="top"><a href="#zones_stats_prepend_input">zones_stats_prepend_input</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">_set</td>
<td valign="top"><a href="#zones_stats_set_input">zones_stats_set_input</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">pk_columns</td>
<td valign="top"><a href="#zones_stats_pk_columns_input">zones_stats_pk_columns_input</a>!</td>
<td></td>
</tr>
</tbody>
</table>

## Objects

### active_addresses

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
<td colspan="2" valign="top"><strong>address</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>hour</strong></td>
<td valign="top"><a href="#timestamp">timestamp</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>period</strong></td>
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

### active_addresses_aggregate

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
<td valign="top"><a href="#active_addresses_aggregate_fields">active_addresses_aggregate_fields</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>nodes</strong></td>
<td valign="top">[<a href="#active_addresses">active_addresses</a>!]!</td>
<td></td>
</tr>
</tbody>
</table>

### active_addresses_aggregate_fields

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
<td valign="top"><a href="#active_addresses_avg_fields">active_addresses_avg_fields</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>count</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">columns</td>
<td valign="top">[<a href="#active_addresses_select_column">active_addresses_select_column</a>!]</td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">distinct</td>
<td valign="top"><a href="#boolean">Boolean</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>max</strong></td>
<td valign="top"><a href="#active_addresses_max_fields">active_addresses_max_fields</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>min</strong></td>
<td valign="top"><a href="#active_addresses_min_fields">active_addresses_min_fields</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>stddev</strong></td>
<td valign="top"><a href="#active_addresses_stddev_fields">active_addresses_stddev_fields</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>stddev_pop</strong></td>
<td valign="top"><a href="#active_addresses_stddev_pop_fields">active_addresses_stddev_pop_fields</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>stddev_samp</strong></td>
<td valign="top"><a href="#active_addresses_stddev_samp_fields">active_addresses_stddev_samp_fields</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>sum</strong></td>
<td valign="top"><a href="#active_addresses_sum_fields">active_addresses_sum_fields</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>var_pop</strong></td>
<td valign="top"><a href="#active_addresses_var_pop_fields">active_addresses_var_pop_fields</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>var_samp</strong></td>
<td valign="top"><a href="#active_addresses_var_samp_fields">active_addresses_var_samp_fields</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>variance</strong></td>
<td valign="top"><a href="#active_addresses_variance_fields">active_addresses_variance_fields</a></td>
<td></td>
</tr>
</tbody>
</table>

### active_addresses_avg_fields

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
<td colspan="2" valign="top"><strong>period</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
</tbody>
</table>

### active_addresses_max_fields

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
<td colspan="2" valign="top"><strong>address</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>hour</strong></td>
<td valign="top"><a href="#timestamp">timestamp</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>period</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>zone</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td></td>
</tr>
</tbody>
</table>

### active_addresses_min_fields

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
<td colspan="2" valign="top"><strong>address</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>hour</strong></td>
<td valign="top"><a href="#timestamp">timestamp</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>period</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>zone</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td></td>
</tr>
</tbody>
</table>

### active_addresses_mutation_response

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
<td colspan="2" valign="top"><strong>affected_rows</strong></td>
<td valign="top"><a href="#int">Int</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>returning</strong></td>
<td valign="top">[<a href="#active_addresses">active_addresses</a>!]!</td>
<td></td>
</tr>
</tbody>
</table>

### active_addresses_stddev_fields

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
<td colspan="2" valign="top"><strong>period</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
</tbody>
</table>

### active_addresses_stddev_pop_fields

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
<td colspan="2" valign="top"><strong>period</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
</tbody>
</table>

### active_addresses_stddev_samp_fields

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
<td colspan="2" valign="top"><strong>period</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
</tbody>
</table>

### active_addresses_sum_fields

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
<td colspan="2" valign="top"><strong>period</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td></td>
</tr>
</tbody>
</table>

### active_addresses_var_pop_fields

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
<td colspan="2" valign="top"><strong>period</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
</tbody>
</table>

### active_addresses_var_samp_fields

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
<td colspan="2" valign="top"><strong>period</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
</tbody>
</table>

### active_addresses_variance_fields

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
<td colspan="2" valign="top"><strong>period</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
</tbody>
</table>

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

### blocks_log_aggregate

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
<td valign="top"><a href="#blocks_log_aggregate_fields">blocks_log_aggregate_fields</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>nodes</strong></td>
<td valign="top">[<a href="#blocks_log">blocks_log</a>!]!</td>
<td></td>
</tr>
</tbody>
</table>

### blocks_log_aggregate_fields

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
<td valign="top"><a href="#blocks_log_avg_fields">blocks_log_avg_fields</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>count</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">columns</td>
<td valign="top">[<a href="#blocks_log_select_column">blocks_log_select_column</a>!]</td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">distinct</td>
<td valign="top"><a href="#boolean">Boolean</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>max</strong></td>
<td valign="top"><a href="#blocks_log_max_fields">blocks_log_max_fields</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>min</strong></td>
<td valign="top"><a href="#blocks_log_min_fields">blocks_log_min_fields</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>stddev</strong></td>
<td valign="top"><a href="#blocks_log_stddev_fields">blocks_log_stddev_fields</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>stddev_pop</strong></td>
<td valign="top"><a href="#blocks_log_stddev_pop_fields">blocks_log_stddev_pop_fields</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>stddev_samp</strong></td>
<td valign="top"><a href="#blocks_log_stddev_samp_fields">blocks_log_stddev_samp_fields</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>sum</strong></td>
<td valign="top"><a href="#blocks_log_sum_fields">blocks_log_sum_fields</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>var_pop</strong></td>
<td valign="top"><a href="#blocks_log_var_pop_fields">blocks_log_var_pop_fields</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>var_samp</strong></td>
<td valign="top"><a href="#blocks_log_var_samp_fields">blocks_log_var_samp_fields</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>variance</strong></td>
<td valign="top"><a href="#blocks_log_variance_fields">blocks_log_variance_fields</a></td>
<td></td>
</tr>
</tbody>
</table>

### blocks_log_avg_fields

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
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
</tbody>
</table>

### blocks_log_max_fields

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
<td valign="top"><a href="#int">Int</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>last_updated_at</strong></td>
<td valign="top"><a href="#timestamp">timestamp</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>zone</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td></td>
</tr>
</tbody>
</table>

### blocks_log_min_fields

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
<td valign="top"><a href="#int">Int</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>last_updated_at</strong></td>
<td valign="top"><a href="#timestamp">timestamp</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>zone</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td></td>
</tr>
</tbody>
</table>

### blocks_log_mutation_response

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
<td colspan="2" valign="top"><strong>affected_rows</strong></td>
<td valign="top"><a href="#int">Int</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>returning</strong></td>
<td valign="top">[<a href="#blocks_log">blocks_log</a>!]!</td>
<td></td>
</tr>
</tbody>
</table>

### blocks_log_stddev_fields

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
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
</tbody>
</table>

### blocks_log_stddev_pop_fields

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
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
</tbody>
</table>

### blocks_log_stddev_samp_fields

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
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
</tbody>
</table>

### blocks_log_sum_fields

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
<td valign="top"><a href="#int">Int</a></td>
<td></td>
</tr>
</tbody>
</table>

### blocks_log_var_pop_fields

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
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
</tbody>
</table>

### blocks_log_var_samp_fields

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
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
</tbody>
</table>

### blocks_log_variance_fields

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
<td colspan="2" valign="top"><strong>channels_cnt_all</strong></td>
<td valign="top"><a href="#int">Int</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>channels_cnt_period</strong></td>
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
<td colspan="2" valign="top"><strong>channels_cnt_all</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>channels_cnt_period</strong></td>
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
<td colspan="2" valign="top"><strong>channels_cnt_all</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>channels_cnt_period</strong></td>
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
<td colspan="2" valign="top"><strong>channels_cnt_all</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>channels_cnt_period</strong></td>
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

### headers_mutation_response

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
<td colspan="2" valign="top"><strong>affected_rows</strong></td>
<td valign="top"><a href="#int">Int</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>returning</strong></td>
<td valign="top">[<a href="#headers">headers</a>!]!</td>
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
<td colspan="2" valign="top"><strong>channels_cnt_all</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>channels_cnt_period</strong></td>
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
<td colspan="2" valign="top"><strong>channels_cnt_all</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>channels_cnt_period</strong></td>
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
<td colspan="2" valign="top"><strong>channels_cnt_all</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>channels_cnt_period</strong></td>
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
<td colspan="2" valign="top"><strong>channels_cnt_all</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>channels_cnt_period</strong></td>
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
<td colspan="2" valign="top"><strong>channels_cnt_all</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>channels_cnt_period</strong></td>
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
<td colspan="2" valign="top"><strong>channels_cnt_all</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>channels_cnt_period</strong></td>
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
<td colspan="2" valign="top"><strong>channels_cnt_all</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>channels_cnt_period</strong></td>
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

### ibc_channel_zone

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
<td colspan="2" valign="top"><strong>added_at</strong></td>
<td valign="top"><a href="#timestamp">timestamp</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>chain_id</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>chanel_id</strong></td>
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

### ibc_channel_zone_aggregate

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
<td valign="top"><a href="#ibc_channel_zone_aggregate_fields">ibc_channel_zone_aggregate_fields</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>nodes</strong></td>
<td valign="top">[<a href="#ibc_channel_zone">ibc_channel_zone</a>!]!</td>
<td></td>
</tr>
</tbody>
</table>

### ibc_channel_zone_aggregate_fields

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
<td valign="top">[<a href="#ibc_channel_zone_select_column">ibc_channel_zone_select_column</a>!]</td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">distinct</td>
<td valign="top"><a href="#boolean">Boolean</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>max</strong></td>
<td valign="top"><a href="#ibc_channel_zone_max_fields">ibc_channel_zone_max_fields</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>min</strong></td>
<td valign="top"><a href="#ibc_channel_zone_min_fields">ibc_channel_zone_min_fields</a></td>
<td></td>
</tr>
</tbody>
</table>

### ibc_channel_zone_max_fields

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
<td colspan="2" valign="top"><strong>added_at</strong></td>
<td valign="top"><a href="#timestamp">timestamp</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>chain_id</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>chanel_id</strong></td>
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

### ibc_channel_zone_min_fields

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
<td colspan="2" valign="top"><strong>added_at</strong></td>
<td valign="top"><a href="#timestamp">timestamp</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>chain_id</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>chanel_id</strong></td>
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

### ibc_channel_zone_mutation_response

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
<td colspan="2" valign="top"><strong>affected_rows</strong></td>
<td valign="top"><a href="#int">Int</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>returning</strong></td>
<td valign="top">[<a href="#ibc_channel_zone">ibc_channel_zone</a>!]!</td>
<td></td>
</tr>
</tbody>
</table>

### ibc_channels

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
<td colspan="2" valign="top"><strong>added_at</strong></td>
<td valign="top"><a href="#timestamp">timestamp</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>channel_id</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>connection_id</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
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
</tbody>
</table>

### ibc_channels_aggregate

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
<td valign="top"><a href="#ibc_channels_aggregate_fields">ibc_channels_aggregate_fields</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>nodes</strong></td>
<td valign="top">[<a href="#ibc_channels">ibc_channels</a>!]!</td>
<td></td>
</tr>
</tbody>
</table>

### ibc_channels_aggregate_fields

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
<td valign="top">[<a href="#ibc_channels_select_column">ibc_channels_select_column</a>!]</td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">distinct</td>
<td valign="top"><a href="#boolean">Boolean</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>max</strong></td>
<td valign="top"><a href="#ibc_channels_max_fields">ibc_channels_max_fields</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>min</strong></td>
<td valign="top"><a href="#ibc_channels_min_fields">ibc_channels_min_fields</a></td>
<td></td>
</tr>
</tbody>
</table>

### ibc_channels_max_fields

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
<td colspan="2" valign="top"><strong>added_at</strong></td>
<td valign="top"><a href="#timestamp">timestamp</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>channel_id</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>connection_id</strong></td>
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

### ibc_channels_min_fields

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
<td colspan="2" valign="top"><strong>added_at</strong></td>
<td valign="top"><a href="#timestamp">timestamp</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>channel_id</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>connection_id</strong></td>
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

### ibc_channels_mutation_response

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
<td colspan="2" valign="top"><strong>affected_rows</strong></td>
<td valign="top"><a href="#int">Int</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>returning</strong></td>
<td valign="top">[<a href="#ibc_channels">ibc_channels</a>!]!</td>
<td></td>
</tr>
</tbody>
</table>

### ibc_clients

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
<td colspan="2" valign="top"><strong>added_at</strong></td>
<td valign="top"><a href="#timestamp">timestamp</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>chain_id</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>client_id</strong></td>
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

### ibc_clients_aggregate

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
<td valign="top"><a href="#ibc_clients_aggregate_fields">ibc_clients_aggregate_fields</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>nodes</strong></td>
<td valign="top">[<a href="#ibc_clients">ibc_clients</a>!]!</td>
<td></td>
</tr>
</tbody>
</table>

### ibc_clients_aggregate_fields

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
<td valign="top">[<a href="#ibc_clients_select_column">ibc_clients_select_column</a>!]</td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">distinct</td>
<td valign="top"><a href="#boolean">Boolean</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>max</strong></td>
<td valign="top"><a href="#ibc_clients_max_fields">ibc_clients_max_fields</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>min</strong></td>
<td valign="top"><a href="#ibc_clients_min_fields">ibc_clients_min_fields</a></td>
<td></td>
</tr>
</tbody>
</table>

### ibc_clients_max_fields

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
<td colspan="2" valign="top"><strong>added_at</strong></td>
<td valign="top"><a href="#timestamp">timestamp</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>chain_id</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>client_id</strong></td>
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

### ibc_clients_min_fields

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
<td colspan="2" valign="top"><strong>added_at</strong></td>
<td valign="top"><a href="#timestamp">timestamp</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>chain_id</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>client_id</strong></td>
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

### ibc_clients_mutation_response

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
<td colspan="2" valign="top"><strong>affected_rows</strong></td>
<td valign="top"><a href="#int">Int</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>returning</strong></td>
<td valign="top">[<a href="#ibc_clients">ibc_clients</a>!]!</td>
<td></td>
</tr>
</tbody>
</table>

### ibc_connections

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
<td colspan="2" valign="top"><strong>added_at</strong></td>
<td valign="top"><a href="#timestamp">timestamp</a>!</td>
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

### ibc_connections_aggregate

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
<td valign="top"><a href="#ibc_connections_aggregate_fields">ibc_connections_aggregate_fields</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>nodes</strong></td>
<td valign="top">[<a href="#ibc_connections">ibc_connections</a>!]!</td>
<td></td>
</tr>
</tbody>
</table>

### ibc_connections_aggregate_fields

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
<td valign="top">[<a href="#ibc_connections_select_column">ibc_connections_select_column</a>!]</td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">distinct</td>
<td valign="top"><a href="#boolean">Boolean</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>max</strong></td>
<td valign="top"><a href="#ibc_connections_max_fields">ibc_connections_max_fields</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>min</strong></td>
<td valign="top"><a href="#ibc_connections_min_fields">ibc_connections_min_fields</a></td>
<td></td>
</tr>
</tbody>
</table>

### ibc_connections_max_fields

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
<td colspan="2" valign="top"><strong>added_at</strong></td>
<td valign="top"><a href="#timestamp">timestamp</a></td>
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
<td colspan="2" valign="top"><strong>zone</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td></td>
</tr>
</tbody>
</table>

### ibc_connections_min_fields

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
<td colspan="2" valign="top"><strong>added_at</strong></td>
<td valign="top"><a href="#timestamp">timestamp</a></td>
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
<td colspan="2" valign="top"><strong>zone</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td></td>
</tr>
</tbody>
</table>

### ibc_connections_mutation_response

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
<td colspan="2" valign="top"><strong>affected_rows</strong></td>
<td valign="top"><a href="#int">Int</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>returning</strong></td>
<td valign="top">[<a href="#ibc_connections">ibc_connections</a>!]!</td>
<td></td>
</tr>
</tbody>
</table>

### ibc_transfer_hourly_stats

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
<td colspan="2" valign="top"><strong>hour</strong></td>
<td valign="top"><a href="#timestamp">timestamp</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>period</strong></td>
<td valign="top"><a href="#int">Int</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>txs_cnt</strong></td>
<td valign="top"><a href="#int">Int</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>zone</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>zone_dest</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>zone_src</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
</tbody>
</table>

### ibc_transfer_hourly_stats_aggregate

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
<td valign="top"><a href="#ibc_transfer_hourly_stats_aggregate_fields">ibc_transfer_hourly_stats_aggregate_fields</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>nodes</strong></td>
<td valign="top">[<a href="#ibc_transfer_hourly_stats">ibc_transfer_hourly_stats</a>!]!</td>
<td></td>
</tr>
</tbody>
</table>

### ibc_transfer_hourly_stats_aggregate_fields

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
<td valign="top"><a href="#ibc_transfer_hourly_stats_avg_fields">ibc_transfer_hourly_stats_avg_fields</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>count</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">columns</td>
<td valign="top">[<a href="#ibc_transfer_hourly_stats_select_column">ibc_transfer_hourly_stats_select_column</a>!]</td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">distinct</td>
<td valign="top"><a href="#boolean">Boolean</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>max</strong></td>
<td valign="top"><a href="#ibc_transfer_hourly_stats_max_fields">ibc_transfer_hourly_stats_max_fields</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>min</strong></td>
<td valign="top"><a href="#ibc_transfer_hourly_stats_min_fields">ibc_transfer_hourly_stats_min_fields</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>stddev</strong></td>
<td valign="top"><a href="#ibc_transfer_hourly_stats_stddev_fields">ibc_transfer_hourly_stats_stddev_fields</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>stddev_pop</strong></td>
<td valign="top"><a href="#ibc_transfer_hourly_stats_stddev_pop_fields">ibc_transfer_hourly_stats_stddev_pop_fields</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>stddev_samp</strong></td>
<td valign="top"><a href="#ibc_transfer_hourly_stats_stddev_samp_fields">ibc_transfer_hourly_stats_stddev_samp_fields</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>sum</strong></td>
<td valign="top"><a href="#ibc_transfer_hourly_stats_sum_fields">ibc_transfer_hourly_stats_sum_fields</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>var_pop</strong></td>
<td valign="top"><a href="#ibc_transfer_hourly_stats_var_pop_fields">ibc_transfer_hourly_stats_var_pop_fields</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>var_samp</strong></td>
<td valign="top"><a href="#ibc_transfer_hourly_stats_var_samp_fields">ibc_transfer_hourly_stats_var_samp_fields</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>variance</strong></td>
<td valign="top"><a href="#ibc_transfer_hourly_stats_variance_fields">ibc_transfer_hourly_stats_variance_fields</a></td>
<td></td>
</tr>
</tbody>
</table>

### ibc_transfer_hourly_stats_avg_fields

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
<td colspan="2" valign="top"><strong>period</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>txs_cnt</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
</tbody>
</table>

### ibc_transfer_hourly_stats_max_fields

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
<td colspan="2" valign="top"><strong>hour</strong></td>
<td valign="top"><a href="#timestamp">timestamp</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>period</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>txs_cnt</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>zone</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>zone_dest</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>zone_src</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td></td>
</tr>
</tbody>
</table>

### ibc_transfer_hourly_stats_min_fields

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
<td colspan="2" valign="top"><strong>hour</strong></td>
<td valign="top"><a href="#timestamp">timestamp</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>period</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>txs_cnt</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>zone</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>zone_dest</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>zone_src</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td></td>
</tr>
</tbody>
</table>

### ibc_transfer_hourly_stats_mutation_response

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
<td colspan="2" valign="top"><strong>affected_rows</strong></td>
<td valign="top"><a href="#int">Int</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>returning</strong></td>
<td valign="top">[<a href="#ibc_transfer_hourly_stats">ibc_transfer_hourly_stats</a>!]!</td>
<td></td>
</tr>
</tbody>
</table>

### ibc_transfer_hourly_stats_stddev_fields

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
<td colspan="2" valign="top"><strong>period</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>txs_cnt</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
</tbody>
</table>

### ibc_transfer_hourly_stats_stddev_pop_fields

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
<td colspan="2" valign="top"><strong>period</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>txs_cnt</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
</tbody>
</table>

### ibc_transfer_hourly_stats_stddev_samp_fields

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
<td colspan="2" valign="top"><strong>period</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>txs_cnt</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
</tbody>
</table>

### ibc_transfer_hourly_stats_sum_fields

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
<td colspan="2" valign="top"><strong>period</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>txs_cnt</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td></td>
</tr>
</tbody>
</table>

### ibc_transfer_hourly_stats_var_pop_fields

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
<td colspan="2" valign="top"><strong>period</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>txs_cnt</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
</tbody>
</table>

### ibc_transfer_hourly_stats_var_samp_fields

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
<td colspan="2" valign="top"><strong>period</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>txs_cnt</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
</tbody>
</table>

### ibc_transfer_hourly_stats_variance_fields

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
<td colspan="2" valign="top"><strong>period</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>txs_cnt</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
</tbody>
</table>

### periods

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
<td colspan="2" valign="top"><strong>period_in_hours</strong></td>
<td valign="top"><a href="#int">Int</a>!</td>
<td></td>
</tr>
</tbody>
</table>

### periods_aggregate

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
<td valign="top"><a href="#periods_aggregate_fields">periods_aggregate_fields</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>nodes</strong></td>
<td valign="top">[<a href="#periods">periods</a>!]!</td>
<td></td>
</tr>
</tbody>
</table>

### periods_aggregate_fields

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
<td valign="top"><a href="#periods_avg_fields">periods_avg_fields</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>count</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">columns</td>
<td valign="top">[<a href="#periods_select_column">periods_select_column</a>!]</td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">distinct</td>
<td valign="top"><a href="#boolean">Boolean</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>max</strong></td>
<td valign="top"><a href="#periods_max_fields">periods_max_fields</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>min</strong></td>
<td valign="top"><a href="#periods_min_fields">periods_min_fields</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>stddev</strong></td>
<td valign="top"><a href="#periods_stddev_fields">periods_stddev_fields</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>stddev_pop</strong></td>
<td valign="top"><a href="#periods_stddev_pop_fields">periods_stddev_pop_fields</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>stddev_samp</strong></td>
<td valign="top"><a href="#periods_stddev_samp_fields">periods_stddev_samp_fields</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>sum</strong></td>
<td valign="top"><a href="#periods_sum_fields">periods_sum_fields</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>var_pop</strong></td>
<td valign="top"><a href="#periods_var_pop_fields">periods_var_pop_fields</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>var_samp</strong></td>
<td valign="top"><a href="#periods_var_samp_fields">periods_var_samp_fields</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>variance</strong></td>
<td valign="top"><a href="#periods_variance_fields">periods_variance_fields</a></td>
<td></td>
</tr>
</tbody>
</table>

### periods_avg_fields

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
<td colspan="2" valign="top"><strong>period_in_hours</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
</tbody>
</table>

### periods_max_fields

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
<td colspan="2" valign="top"><strong>period_in_hours</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td></td>
</tr>
</tbody>
</table>

### periods_min_fields

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
<td colspan="2" valign="top"><strong>period_in_hours</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td></td>
</tr>
</tbody>
</table>

### periods_mutation_response

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
<td colspan="2" valign="top"><strong>affected_rows</strong></td>
<td valign="top"><a href="#int">Int</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>returning</strong></td>
<td valign="top">[<a href="#periods">periods</a>!]!</td>
<td></td>
</tr>
</tbody>
</table>

### periods_stddev_fields

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
<td colspan="2" valign="top"><strong>period_in_hours</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
</tbody>
</table>

### periods_stddev_pop_fields

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
<td colspan="2" valign="top"><strong>period_in_hours</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
</tbody>
</table>

### periods_stddev_samp_fields

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
<td colspan="2" valign="top"><strong>period_in_hours</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
</tbody>
</table>

### periods_sum_fields

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
<td colspan="2" valign="top"><strong>period_in_hours</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td></td>
</tr>
</tbody>
</table>

### periods_var_pop_fields

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
<td colspan="2" valign="top"><strong>period_in_hours</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
</tbody>
</table>

### periods_var_samp_fields

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
<td colspan="2" valign="top"><strong>period_in_hours</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
</tbody>
</table>

### periods_variance_fields

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
<td colspan="2" valign="top"><strong>period_in_hours</strong></td>
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
<td colspan="2" valign="top"><strong>active_addresses</strong></td>
<td valign="top">[<a href="#active_addresses">active_addresses</a>!]!</td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">distinct_on</td>
<td valign="top">[<a href="#active_addresses_select_column">active_addresses_select_column</a>!]</td>
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
<td valign="top">[<a href="#active_addresses_order_by">active_addresses_order_by</a>!]</td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">where</td>
<td valign="top"><a href="#active_addresses_bool_exp">active_addresses_bool_exp</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>active_addresses_aggregate</strong></td>
<td valign="top"><a href="#active_addresses_aggregate">active_addresses_aggregate</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">distinct_on</td>
<td valign="top">[<a href="#active_addresses_select_column">active_addresses_select_column</a>!]</td>
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
<td valign="top">[<a href="#active_addresses_order_by">active_addresses_order_by</a>!]</td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">where</td>
<td valign="top"><a href="#active_addresses_bool_exp">active_addresses_bool_exp</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>active_addresses_by_pk</strong></td>
<td valign="top"><a href="#active_addresses">active_addresses</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">address</td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">hour</td>
<td valign="top"><a href="#timestamp">timestamp</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">period</td>
<td valign="top"><a href="#int">Int</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">zone</td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
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
<td colspan="2" valign="top"><strong>blocks_log_aggregate</strong></td>
<td valign="top"><a href="#blocks_log_aggregate">blocks_log_aggregate</a>!</td>
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
<td colspan="2" valign="top"><strong>ibc_channel_zone</strong></td>
<td valign="top">[<a href="#ibc_channel_zone">ibc_channel_zone</a>!]!</td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">distinct_on</td>
<td valign="top">[<a href="#ibc_channel_zone_select_column">ibc_channel_zone_select_column</a>!]</td>
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
<td valign="top">[<a href="#ibc_channel_zone_order_by">ibc_channel_zone_order_by</a>!]</td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">where</td>
<td valign="top"><a href="#ibc_channel_zone_bool_exp">ibc_channel_zone_bool_exp</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_channel_zone_aggregate</strong></td>
<td valign="top"><a href="#ibc_channel_zone_aggregate">ibc_channel_zone_aggregate</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">distinct_on</td>
<td valign="top">[<a href="#ibc_channel_zone_select_column">ibc_channel_zone_select_column</a>!]</td>
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
<td valign="top">[<a href="#ibc_channel_zone_order_by">ibc_channel_zone_order_by</a>!]</td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">where</td>
<td valign="top"><a href="#ibc_channel_zone_bool_exp">ibc_channel_zone_bool_exp</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_channel_zone_by_pk</strong></td>
<td valign="top"><a href="#ibc_channel_zone">ibc_channel_zone</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">chanel_id</td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">zone</td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_channels</strong></td>
<td valign="top">[<a href="#ibc_channels">ibc_channels</a>!]!</td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">distinct_on</td>
<td valign="top">[<a href="#ibc_channels_select_column">ibc_channels_select_column</a>!]</td>
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
<td valign="top">[<a href="#ibc_channels_order_by">ibc_channels_order_by</a>!]</td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">where</td>
<td valign="top"><a href="#ibc_channels_bool_exp">ibc_channels_bool_exp</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_channels_aggregate</strong></td>
<td valign="top"><a href="#ibc_channels_aggregate">ibc_channels_aggregate</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">distinct_on</td>
<td valign="top">[<a href="#ibc_channels_select_column">ibc_channels_select_column</a>!]</td>
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
<td valign="top">[<a href="#ibc_channels_order_by">ibc_channels_order_by</a>!]</td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">where</td>
<td valign="top"><a href="#ibc_channels_bool_exp">ibc_channels_bool_exp</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_channels_by_pk</strong></td>
<td valign="top"><a href="#ibc_channels">ibc_channels</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">channel_id</td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">zone</td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_clients</strong></td>
<td valign="top">[<a href="#ibc_clients">ibc_clients</a>!]!</td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">distinct_on</td>
<td valign="top">[<a href="#ibc_clients_select_column">ibc_clients_select_column</a>!]</td>
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
<td valign="top">[<a href="#ibc_clients_order_by">ibc_clients_order_by</a>!]</td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">where</td>
<td valign="top"><a href="#ibc_clients_bool_exp">ibc_clients_bool_exp</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_clients_aggregate</strong></td>
<td valign="top"><a href="#ibc_clients_aggregate">ibc_clients_aggregate</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">distinct_on</td>
<td valign="top">[<a href="#ibc_clients_select_column">ibc_clients_select_column</a>!]</td>
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
<td valign="top">[<a href="#ibc_clients_order_by">ibc_clients_order_by</a>!]</td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">where</td>
<td valign="top"><a href="#ibc_clients_bool_exp">ibc_clients_bool_exp</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_clients_by_pk</strong></td>
<td valign="top"><a href="#ibc_clients">ibc_clients</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">client_id</td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">zone</td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_connections</strong></td>
<td valign="top">[<a href="#ibc_connections">ibc_connections</a>!]!</td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">distinct_on</td>
<td valign="top">[<a href="#ibc_connections_select_column">ibc_connections_select_column</a>!]</td>
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
<td valign="top">[<a href="#ibc_connections_order_by">ibc_connections_order_by</a>!]</td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">where</td>
<td valign="top"><a href="#ibc_connections_bool_exp">ibc_connections_bool_exp</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_connections_aggregate</strong></td>
<td valign="top"><a href="#ibc_connections_aggregate">ibc_connections_aggregate</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">distinct_on</td>
<td valign="top">[<a href="#ibc_connections_select_column">ibc_connections_select_column</a>!]</td>
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
<td valign="top">[<a href="#ibc_connections_order_by">ibc_connections_order_by</a>!]</td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">where</td>
<td valign="top"><a href="#ibc_connections_bool_exp">ibc_connections_bool_exp</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_connections_by_pk</strong></td>
<td valign="top"><a href="#ibc_connections">ibc_connections</a></td>
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
<td colspan="2" valign="top"><strong>ibc_transfer_hourly_stats</strong></td>
<td valign="top">[<a href="#ibc_transfer_hourly_stats">ibc_transfer_hourly_stats</a>!]!</td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">distinct_on</td>
<td valign="top">[<a href="#ibc_transfer_hourly_stats_select_column">ibc_transfer_hourly_stats_select_column</a>!]</td>
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
<td valign="top">[<a href="#ibc_transfer_hourly_stats_order_by">ibc_transfer_hourly_stats_order_by</a>!]</td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">where</td>
<td valign="top"><a href="#ibc_transfer_hourly_stats_bool_exp">ibc_transfer_hourly_stats_bool_exp</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_transfer_hourly_stats_aggregate</strong></td>
<td valign="top"><a href="#ibc_transfer_hourly_stats_aggregate">ibc_transfer_hourly_stats_aggregate</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">distinct_on</td>
<td valign="top">[<a href="#ibc_transfer_hourly_stats_select_column">ibc_transfer_hourly_stats_select_column</a>!]</td>
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
<td valign="top">[<a href="#ibc_transfer_hourly_stats_order_by">ibc_transfer_hourly_stats_order_by</a>!]</td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">where</td>
<td valign="top"><a href="#ibc_transfer_hourly_stats_bool_exp">ibc_transfer_hourly_stats_bool_exp</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_transfer_hourly_stats_by_pk</strong></td>
<td valign="top"><a href="#ibc_transfer_hourly_stats">ibc_transfer_hourly_stats</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">hour</td>
<td valign="top"><a href="#timestamp">timestamp</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">period</td>
<td valign="top"><a href="#int">Int</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">zone</td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">zone_dest</td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">zone_src</td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>periods</strong></td>
<td valign="top">[<a href="#periods">periods</a>!]!</td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">distinct_on</td>
<td valign="top">[<a href="#periods_select_column">periods_select_column</a>!]</td>
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
<td valign="top">[<a href="#periods_order_by">periods_order_by</a>!]</td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">where</td>
<td valign="top"><a href="#periods_bool_exp">periods_bool_exp</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>periods_aggregate</strong></td>
<td valign="top"><a href="#periods_aggregate">periods_aggregate</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">distinct_on</td>
<td valign="top">[<a href="#periods_select_column">periods_select_column</a>!]</td>
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
<td valign="top">[<a href="#periods_order_by">periods_order_by</a>!]</td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">where</td>
<td valign="top"><a href="#periods_bool_exp">periods_bool_exp</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>periods_by_pk</strong></td>
<td valign="top"><a href="#periods">periods</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">period_in_hours</td>
<td valign="top"><a href="#int">Int</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_tx_hourly_stats</strong></td>
<td valign="top">[<a href="#total_tx_hourly_stats">total_tx_hourly_stats</a>!]!</td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">distinct_on</td>
<td valign="top">[<a href="#total_tx_hourly_stats_select_column">total_tx_hourly_stats_select_column</a>!]</td>
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
<td valign="top">[<a href="#total_tx_hourly_stats_order_by">total_tx_hourly_stats_order_by</a>!]</td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">where</td>
<td valign="top"><a href="#total_tx_hourly_stats_bool_exp">total_tx_hourly_stats_bool_exp</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_tx_hourly_stats_aggregate</strong></td>
<td valign="top"><a href="#total_tx_hourly_stats_aggregate">total_tx_hourly_stats_aggregate</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">distinct_on</td>
<td valign="top">[<a href="#total_tx_hourly_stats_select_column">total_tx_hourly_stats_select_column</a>!]</td>
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
<td valign="top">[<a href="#total_tx_hourly_stats_order_by">total_tx_hourly_stats_order_by</a>!]</td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">where</td>
<td valign="top"><a href="#total_tx_hourly_stats_bool_exp">total_tx_hourly_stats_bool_exp</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_tx_hourly_stats_by_pk</strong></td>
<td valign="top"><a href="#total_tx_hourly_stats">total_tx_hourly_stats</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">hour</td>
<td valign="top"><a href="#timestamp">timestamp</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">period</td>
<td valign="top"><a href="#int">Int</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">zone</td>
<td valign="top"><a href="#string">String</a>!</td>
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
<td colspan="2" align="right" valign="top">zone</td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>zones</strong></td>
<td valign="top">[<a href="#zones">zones</a>!]!</td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">distinct_on</td>
<td valign="top">[<a href="#zones_select_column">zones_select_column</a>!]</td>
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
<td valign="top">[<a href="#zones_order_by">zones_order_by</a>!]</td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">where</td>
<td valign="top"><a href="#zones_bool_exp">zones_bool_exp</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>zones_aggregate</strong></td>
<td valign="top"><a href="#zones_aggregate">zones_aggregate</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">distinct_on</td>
<td valign="top">[<a href="#zones_select_column">zones_select_column</a>!]</td>
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
<td valign="top">[<a href="#zones_order_by">zones_order_by</a>!]</td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">where</td>
<td valign="top"><a href="#zones_bool_exp">zones_bool_exp</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>zones_by_pk</strong></td>
<td valign="top"><a href="#zones">zones</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">chain_id</td>
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

### total_tx_hourly_stats

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
<td colspan="2" valign="top"><strong>hour</strong></td>
<td valign="top"><a href="#timestamp">timestamp</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>period</strong></td>
<td valign="top"><a href="#int">Int</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_coin_turnover_amount</strong></td>
<td valign="top"><a href="#bigint">bigint</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>txs_cnt</strong></td>
<td valign="top"><a href="#int">Int</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>txs_w_ibc_xfer_cnt</strong></td>
<td valign="top"><a href="#int">Int</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>txs_w_ibc_xfer_fail_cnt</strong></td>
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

### total_tx_hourly_stats_aggregate

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
<td valign="top"><a href="#total_tx_hourly_stats_aggregate_fields">total_tx_hourly_stats_aggregate_fields</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>nodes</strong></td>
<td valign="top">[<a href="#total_tx_hourly_stats">total_tx_hourly_stats</a>!]!</td>
<td></td>
</tr>
</tbody>
</table>

### total_tx_hourly_stats_aggregate_fields

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
<td valign="top"><a href="#total_tx_hourly_stats_avg_fields">total_tx_hourly_stats_avg_fields</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>count</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">columns</td>
<td valign="top">[<a href="#total_tx_hourly_stats_select_column">total_tx_hourly_stats_select_column</a>!]</td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">distinct</td>
<td valign="top"><a href="#boolean">Boolean</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>max</strong></td>
<td valign="top"><a href="#total_tx_hourly_stats_max_fields">total_tx_hourly_stats_max_fields</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>min</strong></td>
<td valign="top"><a href="#total_tx_hourly_stats_min_fields">total_tx_hourly_stats_min_fields</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>stddev</strong></td>
<td valign="top"><a href="#total_tx_hourly_stats_stddev_fields">total_tx_hourly_stats_stddev_fields</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>stddev_pop</strong></td>
<td valign="top"><a href="#total_tx_hourly_stats_stddev_pop_fields">total_tx_hourly_stats_stddev_pop_fields</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>stddev_samp</strong></td>
<td valign="top"><a href="#total_tx_hourly_stats_stddev_samp_fields">total_tx_hourly_stats_stddev_samp_fields</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>sum</strong></td>
<td valign="top"><a href="#total_tx_hourly_stats_sum_fields">total_tx_hourly_stats_sum_fields</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>var_pop</strong></td>
<td valign="top"><a href="#total_tx_hourly_stats_var_pop_fields">total_tx_hourly_stats_var_pop_fields</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>var_samp</strong></td>
<td valign="top"><a href="#total_tx_hourly_stats_var_samp_fields">total_tx_hourly_stats_var_samp_fields</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>variance</strong></td>
<td valign="top"><a href="#total_tx_hourly_stats_variance_fields">total_tx_hourly_stats_variance_fields</a></td>
<td></td>
</tr>
</tbody>
</table>

### total_tx_hourly_stats_avg_fields

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
<td colspan="2" valign="top"><strong>period</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_coin_turnover_amount</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>txs_cnt</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>txs_w_ibc_xfer_cnt</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>txs_w_ibc_xfer_fail_cnt</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
</tbody>
</table>

### total_tx_hourly_stats_max_fields

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
<td colspan="2" valign="top"><strong>hour</strong></td>
<td valign="top"><a href="#timestamp">timestamp</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>period</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_coin_turnover_amount</strong></td>
<td valign="top"><a href="#bigint">bigint</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>txs_cnt</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>txs_w_ibc_xfer_cnt</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>txs_w_ibc_xfer_fail_cnt</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>zone</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td></td>
</tr>
</tbody>
</table>

### total_tx_hourly_stats_min_fields

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
<td colspan="2" valign="top"><strong>hour</strong></td>
<td valign="top"><a href="#timestamp">timestamp</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>period</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_coin_turnover_amount</strong></td>
<td valign="top"><a href="#bigint">bigint</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>txs_cnt</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>txs_w_ibc_xfer_cnt</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>txs_w_ibc_xfer_fail_cnt</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>zone</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td></td>
</tr>
</tbody>
</table>

### total_tx_hourly_stats_mutation_response

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
<td colspan="2" valign="top"><strong>affected_rows</strong></td>
<td valign="top"><a href="#int">Int</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>returning</strong></td>
<td valign="top">[<a href="#total_tx_hourly_stats">total_tx_hourly_stats</a>!]!</td>
<td></td>
</tr>
</tbody>
</table>

### total_tx_hourly_stats_stddev_fields

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
<td colspan="2" valign="top"><strong>period</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_coin_turnover_amount</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>txs_cnt</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>txs_w_ibc_xfer_cnt</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>txs_w_ibc_xfer_fail_cnt</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
</tbody>
</table>

### total_tx_hourly_stats_stddev_pop_fields

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
<td colspan="2" valign="top"><strong>period</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_coin_turnover_amount</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>txs_cnt</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>txs_w_ibc_xfer_cnt</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>txs_w_ibc_xfer_fail_cnt</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
</tbody>
</table>

### total_tx_hourly_stats_stddev_samp_fields

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
<td colspan="2" valign="top"><strong>period</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_coin_turnover_amount</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>txs_cnt</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>txs_w_ibc_xfer_cnt</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>txs_w_ibc_xfer_fail_cnt</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
</tbody>
</table>

### total_tx_hourly_stats_sum_fields

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
<td colspan="2" valign="top"><strong>period</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_coin_turnover_amount</strong></td>
<td valign="top"><a href="#bigint">bigint</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>txs_cnt</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>txs_w_ibc_xfer_cnt</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>txs_w_ibc_xfer_fail_cnt</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td></td>
</tr>
</tbody>
</table>

### total_tx_hourly_stats_var_pop_fields

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
<td colspan="2" valign="top"><strong>period</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_coin_turnover_amount</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>txs_cnt</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>txs_w_ibc_xfer_cnt</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>txs_w_ibc_xfer_fail_cnt</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
</tbody>
</table>

### total_tx_hourly_stats_var_samp_fields

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
<td colspan="2" valign="top"><strong>period</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_coin_turnover_amount</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>txs_cnt</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>txs_w_ibc_xfer_cnt</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>txs_w_ibc_xfer_fail_cnt</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
</tbody>
</table>

### total_tx_hourly_stats_variance_fields

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
<td colspan="2" valign="top"><strong>period</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_coin_turnover_amount</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>txs_cnt</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>txs_w_ibc_xfer_cnt</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>txs_w_ibc_xfer_fail_cnt</strong></td>
<td valign="top"><a href="#float">Float</a></td>
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

### zone_nodes_mutation_response

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
<td colspan="2" valign="top"><strong>affected_rows</strong></td>
<td valign="top"><a href="#int">Int</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>returning</strong></td>
<td valign="top">[<a href="#zone_nodes">zone_nodes</a>!]!</td>
<td></td>
</tr>
</tbody>
</table>

### zones

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
<td colspan="2" valign="top"><strong>added_at</strong></td>
<td valign="top"><a href="#timestamp">timestamp</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>chain_id</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>description</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>is_caught_up</strong></td>
<td valign="top"><a href="#boolean">Boolean</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>is_enabled</strong></td>
<td valign="top"><a href="#boolean">Boolean</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>name</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>updated_at</strong></td>
<td valign="top"><a href="#timestamp">timestamp</a>!</td>
<td></td>
</tr>
</tbody>
</table>

### zones_aggregate

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
<td valign="top"><a href="#zones_aggregate_fields">zones_aggregate_fields</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>nodes</strong></td>
<td valign="top">[<a href="#zones">zones</a>!]!</td>
<td></td>
</tr>
</tbody>
</table>

### zones_aggregate_fields

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
<td valign="top">[<a href="#zones_select_column">zones_select_column</a>!]</td>
<td></td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">distinct</td>
<td valign="top"><a href="#boolean">Boolean</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>max</strong></td>
<td valign="top"><a href="#zones_max_fields">zones_max_fields</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>min</strong></td>
<td valign="top"><a href="#zones_min_fields">zones_min_fields</a></td>
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

### zones_graphs_mutation_response

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
<td colspan="2" valign="top"><strong>affected_rows</strong></td>
<td valign="top"><a href="#int">Int</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>returning</strong></td>
<td valign="top">[<a href="#zones_graphs">zones_graphs</a>!]!</td>
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
<td colspan="2" valign="top"><strong>timeframe</strong></td>
<td valign="top"><a href="#float">Float</a></td>
<td></td>
</tr>
</tbody>
</table>

### zones_max_fields

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
<td colspan="2" valign="top"><strong>added_at</strong></td>
<td valign="top"><a href="#timestamp">timestamp</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>chain_id</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>description</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>name</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>updated_at</strong></td>
<td valign="top"><a href="#timestamp">timestamp</a></td>
<td></td>
</tr>
</tbody>
</table>

### zones_min_fields

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
<td colspan="2" valign="top"><strong>added_at</strong></td>
<td valign="top"><a href="#timestamp">timestamp</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>chain_id</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>description</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>name</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>updated_at</strong></td>
<td valign="top"><a href="#timestamp">timestamp</a></td>
<td></td>
</tr>
</tbody>
</table>

### zones_mutation_response

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
<td colspan="2" valign="top"><strong>affected_rows</strong></td>
<td valign="top"><a href="#int">Int</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>returning</strong></td>
<td valign="top">[<a href="#zones">zones</a>!]!</td>
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
<td colspan="2" valign="top"><strong>channels_num</strong></td>
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
<td valign="top"><a href="#int">Int</a>!</td>
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
<td colspan="2" valign="top"><strong>channels_num</strong></td>
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
<td colspan="2" valign="top"><strong>channels_num</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_percent</strong></td>
<td valign="top"><a href="#int">Int</a></td>
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
<td colspan="2" valign="top"><strong>channels_num</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_percent</strong></td>
<td valign="top"><a href="#int">Int</a></td>
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

### zones_stats_mutation_response

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
<td colspan="2" valign="top"><strong>affected_rows</strong></td>
<td valign="top"><a href="#int">Int</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>returning</strong></td>
<td valign="top">[<a href="#zones_stats">zones_stats</a>!]!</td>
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
<td colspan="2" valign="top"><strong>channels_num</strong></td>
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
<td colspan="2" valign="top"><strong>channels_num</strong></td>
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
<td colspan="2" valign="top"><strong>channels_num</strong></td>
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
<td colspan="2" valign="top"><strong>channels_num</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_percent</strong></td>
<td valign="top"><a href="#int">Int</a></td>
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
<td colspan="2" valign="top"><strong>channels_num</strong></td>
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
<td colspan="2" valign="top"><strong>channels_num</strong></td>
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
<td colspan="2" valign="top"><strong>channels_num</strong></td>
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

### active_addresses_aggregate_order_by

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
<td valign="top"><a href="#active_addresses_avg_order_by">active_addresses_avg_order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>count</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>max</strong></td>
<td valign="top"><a href="#active_addresses_max_order_by">active_addresses_max_order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>min</strong></td>
<td valign="top"><a href="#active_addresses_min_order_by">active_addresses_min_order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>stddev</strong></td>
<td valign="top"><a href="#active_addresses_stddev_order_by">active_addresses_stddev_order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>stddev_pop</strong></td>
<td valign="top"><a href="#active_addresses_stddev_pop_order_by">active_addresses_stddev_pop_order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>stddev_samp</strong></td>
<td valign="top"><a href="#active_addresses_stddev_samp_order_by">active_addresses_stddev_samp_order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>sum</strong></td>
<td valign="top"><a href="#active_addresses_sum_order_by">active_addresses_sum_order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>var_pop</strong></td>
<td valign="top"><a href="#active_addresses_var_pop_order_by">active_addresses_var_pop_order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>var_samp</strong></td>
<td valign="top"><a href="#active_addresses_var_samp_order_by">active_addresses_var_samp_order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>variance</strong></td>
<td valign="top"><a href="#active_addresses_variance_order_by">active_addresses_variance_order_by</a></td>
<td></td>
</tr>
</tbody>
</table>

### active_addresses_arr_rel_insert_input

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
<td colspan="2" valign="top"><strong>data</strong></td>
<td valign="top">[<a href="#active_addresses_insert_input">active_addresses_insert_input</a>!]!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>on_conflict</strong></td>
<td valign="top"><a href="#active_addresses_on_conflict">active_addresses_on_conflict</a></td>
<td></td>
</tr>
</tbody>
</table>

### active_addresses_avg_order_by

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
<td colspan="2" valign="top"><strong>period</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
</tbody>
</table>

### active_addresses_bool_exp

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
<td valign="top">[<a href="#active_addresses_bool_exp">active_addresses_bool_exp</a>]</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>_not</strong></td>
<td valign="top"><a href="#active_addresses_bool_exp">active_addresses_bool_exp</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>_or</strong></td>
<td valign="top">[<a href="#active_addresses_bool_exp">active_addresses_bool_exp</a>]</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>address</strong></td>
<td valign="top"><a href="#string_comparison_exp">String_comparison_exp</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>hour</strong></td>
<td valign="top"><a href="#timestamp_comparison_exp">timestamp_comparison_exp</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>period</strong></td>
<td valign="top"><a href="#int_comparison_exp">Int_comparison_exp</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>zone</strong></td>
<td valign="top"><a href="#string_comparison_exp">String_comparison_exp</a></td>
<td></td>
</tr>
</tbody>
</table>

### active_addresses_inc_input

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
<td colspan="2" valign="top"><strong>period</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td></td>
</tr>
</tbody>
</table>

### active_addresses_insert_input

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
<td colspan="2" valign="top"><strong>address</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>hour</strong></td>
<td valign="top"><a href="#timestamp">timestamp</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>period</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>zone</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td></td>
</tr>
</tbody>
</table>

### active_addresses_max_order_by

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
<td colspan="2" valign="top"><strong>address</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>hour</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>period</strong></td>
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

### active_addresses_min_order_by

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
<td colspan="2" valign="top"><strong>address</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>hour</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>period</strong></td>
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

### active_addresses_obj_rel_insert_input

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
<td colspan="2" valign="top"><strong>data</strong></td>
<td valign="top"><a href="#active_addresses_insert_input">active_addresses_insert_input</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>on_conflict</strong></td>
<td valign="top"><a href="#active_addresses_on_conflict">active_addresses_on_conflict</a></td>
<td></td>
</tr>
</tbody>
</table>

### active_addresses_on_conflict

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
<td colspan="2" valign="top"><strong>constraint</strong></td>
<td valign="top"><a href="#active_addresses_constraint">active_addresses_constraint</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>update_columns</strong></td>
<td valign="top">[<a href="#active_addresses_update_column">active_addresses_update_column</a>!]!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>where</strong></td>
<td valign="top"><a href="#active_addresses_bool_exp">active_addresses_bool_exp</a></td>
<td></td>
</tr>
</tbody>
</table>

### active_addresses_order_by

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
<td colspan="2" valign="top"><strong>address</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>hour</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>period</strong></td>
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

### active_addresses_pk_columns_input

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
<td colspan="2" valign="top"><strong>address</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>hour</strong></td>
<td valign="top"><a href="#timestamp">timestamp</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>period</strong></td>
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

### active_addresses_set_input

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
<td colspan="2" valign="top"><strong>address</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>hour</strong></td>
<td valign="top"><a href="#timestamp">timestamp</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>period</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>zone</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td></td>
</tr>
</tbody>
</table>

### active_addresses_stddev_order_by

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
<td colspan="2" valign="top"><strong>period</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
</tbody>
</table>

### active_addresses_stddev_pop_order_by

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
<td colspan="2" valign="top"><strong>period</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
</tbody>
</table>

### active_addresses_stddev_samp_order_by

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
<td colspan="2" valign="top"><strong>period</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
</tbody>
</table>

### active_addresses_sum_order_by

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
<td colspan="2" valign="top"><strong>period</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
</tbody>
</table>

### active_addresses_var_pop_order_by

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
<td colspan="2" valign="top"><strong>period</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
</tbody>
</table>

### active_addresses_var_samp_order_by

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
<td colspan="2" valign="top"><strong>period</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
</tbody>
</table>

### active_addresses_variance_order_by

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
<td colspan="2" valign="top"><strong>period</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
</tbody>
</table>

### bigint_comparison_exp

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
<td valign="top"><a href="#bigint">bigint</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>_gt</strong></td>
<td valign="top"><a href="#bigint">bigint</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>_gte</strong></td>
<td valign="top"><a href="#bigint">bigint</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>_in</strong></td>
<td valign="top">[<a href="#bigint">bigint</a>!]</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>_is_null</strong></td>
<td valign="top"><a href="#boolean">Boolean</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>_lt</strong></td>
<td valign="top"><a href="#bigint">bigint</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>_lte</strong></td>
<td valign="top"><a href="#bigint">bigint</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>_neq</strong></td>
<td valign="top"><a href="#bigint">bigint</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>_nin</strong></td>
<td valign="top">[<a href="#bigint">bigint</a>!]</td>
<td></td>
</tr>
</tbody>
</table>

### blocks_log_aggregate_order_by

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
<td valign="top"><a href="#blocks_log_avg_order_by">blocks_log_avg_order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>count</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>max</strong></td>
<td valign="top"><a href="#blocks_log_max_order_by">blocks_log_max_order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>min</strong></td>
<td valign="top"><a href="#blocks_log_min_order_by">blocks_log_min_order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>stddev</strong></td>
<td valign="top"><a href="#blocks_log_stddev_order_by">blocks_log_stddev_order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>stddev_pop</strong></td>
<td valign="top"><a href="#blocks_log_stddev_pop_order_by">blocks_log_stddev_pop_order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>stddev_samp</strong></td>
<td valign="top"><a href="#blocks_log_stddev_samp_order_by">blocks_log_stddev_samp_order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>sum</strong></td>
<td valign="top"><a href="#blocks_log_sum_order_by">blocks_log_sum_order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>var_pop</strong></td>
<td valign="top"><a href="#blocks_log_var_pop_order_by">blocks_log_var_pop_order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>var_samp</strong></td>
<td valign="top"><a href="#blocks_log_var_samp_order_by">blocks_log_var_samp_order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>variance</strong></td>
<td valign="top"><a href="#blocks_log_variance_order_by">blocks_log_variance_order_by</a></td>
<td></td>
</tr>
</tbody>
</table>

### blocks_log_arr_rel_insert_input

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
<td colspan="2" valign="top"><strong>data</strong></td>
<td valign="top">[<a href="#blocks_log_insert_input">blocks_log_insert_input</a>!]!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>on_conflict</strong></td>
<td valign="top"><a href="#blocks_log_on_conflict">blocks_log_on_conflict</a></td>
<td></td>
</tr>
</tbody>
</table>

### blocks_log_avg_order_by

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

### blocks_log_inc_input

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
<td valign="top"><a href="#int">Int</a></td>
<td></td>
</tr>
</tbody>
</table>

### blocks_log_insert_input

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
<td valign="top"><a href="#int">Int</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>last_updated_at</strong></td>
<td valign="top"><a href="#timestamp">timestamp</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>zone</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td></td>
</tr>
</tbody>
</table>

### blocks_log_max_order_by

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

### blocks_log_min_order_by

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

### blocks_log_obj_rel_insert_input

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
<td colspan="2" valign="top"><strong>data</strong></td>
<td valign="top"><a href="#blocks_log_insert_input">blocks_log_insert_input</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>on_conflict</strong></td>
<td valign="top"><a href="#blocks_log_on_conflict">blocks_log_on_conflict</a></td>
<td></td>
</tr>
</tbody>
</table>

### blocks_log_on_conflict

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
<td colspan="2" valign="top"><strong>constraint</strong></td>
<td valign="top"><a href="#blocks_log_constraint">blocks_log_constraint</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>update_columns</strong></td>
<td valign="top">[<a href="#blocks_log_update_column">blocks_log_update_column</a>!]!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>where</strong></td>
<td valign="top"><a href="#blocks_log_bool_exp">blocks_log_bool_exp</a></td>
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

### blocks_log_set_input

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
<td valign="top"><a href="#int">Int</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>last_updated_at</strong></td>
<td valign="top"><a href="#timestamp">timestamp</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>zone</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td></td>
</tr>
</tbody>
</table>

### blocks_log_stddev_order_by

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
</tbody>
</table>

### blocks_log_stddev_pop_order_by

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
</tbody>
</table>

### blocks_log_stddev_samp_order_by

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
</tbody>
</table>

### blocks_log_sum_order_by

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
</tbody>
</table>

### blocks_log_var_pop_order_by

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
</tbody>
</table>

### blocks_log_var_samp_order_by

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
</tbody>
</table>

### blocks_log_variance_order_by

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

### headers_append_input

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
<td colspan="2" valign="top"><strong>chart</strong></td>
<td valign="top"><a href="#jsonb">jsonb</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>top_zone_pair</strong></td>
<td valign="top"><a href="#jsonb">jsonb</a></td>
<td></td>
</tr>
</tbody>
</table>

### headers_arr_rel_insert_input

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
<td colspan="2" valign="top"><strong>data</strong></td>
<td valign="top">[<a href="#headers_insert_input">headers_insert_input</a>!]!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>on_conflict</strong></td>
<td valign="top"><a href="#headers_on_conflict">headers_on_conflict</a></td>
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
<td colspan="2" valign="top"><strong>channels_cnt_all</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>channels_cnt_period</strong></td>
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
<td colspan="2" valign="top"><strong>channels_cnt_all</strong></td>
<td valign="top"><a href="#int_comparison_exp">Int_comparison_exp</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>channels_cnt_period</strong></td>
<td valign="top"><a href="#int_comparison_exp">Int_comparison_exp</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>chart</strong></td>
<td valign="top"><a href="#jsonb_comparison_exp">jsonb_comparison_exp</a></td>
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

### headers_delete_at_path_input

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
<td colspan="2" valign="top"><strong>chart</strong></td>
<td valign="top">[<a href="#string">String</a>]</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>top_zone_pair</strong></td>
<td valign="top">[<a href="#string">String</a>]</td>
<td></td>
</tr>
</tbody>
</table>

### headers_delete_elem_input

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
<td colspan="2" valign="top"><strong>chart</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>top_zone_pair</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td></td>
</tr>
</tbody>
</table>

### headers_delete_key_input

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
<td colspan="2" valign="top"><strong>chart</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>top_zone_pair</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td></td>
</tr>
</tbody>
</table>

### headers_inc_input

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
<td colspan="2" valign="top"><strong>channels_cnt_all</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>channels_cnt_period</strong></td>
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

### headers_insert_input

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
<td colspan="2" valign="top"><strong>channels_cnt_all</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>channels_cnt_period</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>chart</strong></td>
<td valign="top"><a href="#jsonb">jsonb</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>timeframe</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>top_zone_pair</strong></td>
<td valign="top"><a href="#jsonb">jsonb</a></td>
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
<td colspan="2" valign="top"><strong>channels_cnt_all</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>channels_cnt_period</strong></td>
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
<td colspan="2" valign="top"><strong>channels_cnt_all</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>channels_cnt_period</strong></td>
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

### headers_obj_rel_insert_input

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
<td colspan="2" valign="top"><strong>data</strong></td>
<td valign="top"><a href="#headers_insert_input">headers_insert_input</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>on_conflict</strong></td>
<td valign="top"><a href="#headers_on_conflict">headers_on_conflict</a></td>
<td></td>
</tr>
</tbody>
</table>

### headers_on_conflict

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
<td colspan="2" valign="top"><strong>constraint</strong></td>
<td valign="top"><a href="#headers_constraint">headers_constraint</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>update_columns</strong></td>
<td valign="top">[<a href="#headers_update_column">headers_update_column</a>!]!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>where</strong></td>
<td valign="top"><a href="#headers_bool_exp">headers_bool_exp</a></td>
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
<td colspan="2" valign="top"><strong>channels_cnt_all</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>channels_cnt_period</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>chart</strong></td>
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

### headers_prepend_input

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
<td colspan="2" valign="top"><strong>chart</strong></td>
<td valign="top"><a href="#jsonb">jsonb</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>top_zone_pair</strong></td>
<td valign="top"><a href="#jsonb">jsonb</a></td>
<td></td>
</tr>
</tbody>
</table>

### headers_set_input

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
<td colspan="2" valign="top"><strong>channels_cnt_all</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>channels_cnt_period</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>chart</strong></td>
<td valign="top"><a href="#jsonb">jsonb</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>timeframe</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>top_zone_pair</strong></td>
<td valign="top"><a href="#jsonb">jsonb</a></td>
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
<td colspan="2" valign="top"><strong>channels_cnt_all</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>channels_cnt_period</strong></td>
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
<td colspan="2" valign="top"><strong>channels_cnt_all</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>channels_cnt_period</strong></td>
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
<td colspan="2" valign="top"><strong>channels_cnt_all</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>channels_cnt_period</strong></td>
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
<td colspan="2" valign="top"><strong>channels_cnt_all</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>channels_cnt_period</strong></td>
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
<td colspan="2" valign="top"><strong>channels_cnt_all</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>channels_cnt_period</strong></td>
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
<td colspan="2" valign="top"><strong>channels_cnt_all</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>channels_cnt_period</strong></td>
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
<td colspan="2" valign="top"><strong>channels_cnt_all</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>channels_cnt_period</strong></td>
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

### ibc_channel_zone_aggregate_order_by

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
<td valign="top"><a href="#ibc_channel_zone_max_order_by">ibc_channel_zone_max_order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>min</strong></td>
<td valign="top"><a href="#ibc_channel_zone_min_order_by">ibc_channel_zone_min_order_by</a></td>
<td></td>
</tr>
</tbody>
</table>

### ibc_channel_zone_arr_rel_insert_input

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
<td colspan="2" valign="top"><strong>data</strong></td>
<td valign="top">[<a href="#ibc_channel_zone_insert_input">ibc_channel_zone_insert_input</a>!]!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>on_conflict</strong></td>
<td valign="top"><a href="#ibc_channel_zone_on_conflict">ibc_channel_zone_on_conflict</a></td>
<td></td>
</tr>
</tbody>
</table>

### ibc_channel_zone_bool_exp

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
<td valign="top">[<a href="#ibc_channel_zone_bool_exp">ibc_channel_zone_bool_exp</a>]</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>_not</strong></td>
<td valign="top"><a href="#ibc_channel_zone_bool_exp">ibc_channel_zone_bool_exp</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>_or</strong></td>
<td valign="top">[<a href="#ibc_channel_zone_bool_exp">ibc_channel_zone_bool_exp</a>]</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>added_at</strong></td>
<td valign="top"><a href="#timestamp_comparison_exp">timestamp_comparison_exp</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>chain_id</strong></td>
<td valign="top"><a href="#string_comparison_exp">String_comparison_exp</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>chanel_id</strong></td>
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

### ibc_channel_zone_insert_input

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
<td colspan="2" valign="top"><strong>added_at</strong></td>
<td valign="top"><a href="#timestamp">timestamp</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>chain_id</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>chanel_id</strong></td>
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

### ibc_channel_zone_max_order_by

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
<td colspan="2" valign="top"><strong>added_at</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>chain_id</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>chanel_id</strong></td>
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

### ibc_channel_zone_min_order_by

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
<td colspan="2" valign="top"><strong>added_at</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>chain_id</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>chanel_id</strong></td>
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

### ibc_channel_zone_obj_rel_insert_input

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
<td colspan="2" valign="top"><strong>data</strong></td>
<td valign="top"><a href="#ibc_channel_zone_insert_input">ibc_channel_zone_insert_input</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>on_conflict</strong></td>
<td valign="top"><a href="#ibc_channel_zone_on_conflict">ibc_channel_zone_on_conflict</a></td>
<td></td>
</tr>
</tbody>
</table>

### ibc_channel_zone_on_conflict

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
<td colspan="2" valign="top"><strong>constraint</strong></td>
<td valign="top"><a href="#ibc_channel_zone_constraint">ibc_channel_zone_constraint</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>update_columns</strong></td>
<td valign="top">[<a href="#ibc_channel_zone_update_column">ibc_channel_zone_update_column</a>!]!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>where</strong></td>
<td valign="top"><a href="#ibc_channel_zone_bool_exp">ibc_channel_zone_bool_exp</a></td>
<td></td>
</tr>
</tbody>
</table>

### ibc_channel_zone_order_by

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
<td colspan="2" valign="top"><strong>added_at</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>chain_id</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>chanel_id</strong></td>
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

### ibc_channel_zone_pk_columns_input

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
<td colspan="2" valign="top"><strong>chanel_id</strong></td>
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

### ibc_channel_zone_set_input

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
<td colspan="2" valign="top"><strong>added_at</strong></td>
<td valign="top"><a href="#timestamp">timestamp</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>chain_id</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>chanel_id</strong></td>
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

### ibc_channels_aggregate_order_by

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
<td valign="top"><a href="#ibc_channels_max_order_by">ibc_channels_max_order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>min</strong></td>
<td valign="top"><a href="#ibc_channels_min_order_by">ibc_channels_min_order_by</a></td>
<td></td>
</tr>
</tbody>
</table>

### ibc_channels_arr_rel_insert_input

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
<td colspan="2" valign="top"><strong>data</strong></td>
<td valign="top">[<a href="#ibc_channels_insert_input">ibc_channels_insert_input</a>!]!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>on_conflict</strong></td>
<td valign="top"><a href="#ibc_channels_on_conflict">ibc_channels_on_conflict</a></td>
<td></td>
</tr>
</tbody>
</table>

### ibc_channels_bool_exp

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
<td valign="top">[<a href="#ibc_channels_bool_exp">ibc_channels_bool_exp</a>]</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>_not</strong></td>
<td valign="top"><a href="#ibc_channels_bool_exp">ibc_channels_bool_exp</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>_or</strong></td>
<td valign="top">[<a href="#ibc_channels_bool_exp">ibc_channels_bool_exp</a>]</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>added_at</strong></td>
<td valign="top"><a href="#timestamp_comparison_exp">timestamp_comparison_exp</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>channel_id</strong></td>
<td valign="top"><a href="#string_comparison_exp">String_comparison_exp</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>connection_id</strong></td>
<td valign="top"><a href="#string_comparison_exp">String_comparison_exp</a></td>
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
</tbody>
</table>

### ibc_channels_insert_input

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
<td colspan="2" valign="top"><strong>added_at</strong></td>
<td valign="top"><a href="#timestamp">timestamp</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>channel_id</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>connection_id</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>is_opened</strong></td>
<td valign="top"><a href="#boolean">Boolean</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>zone</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td></td>
</tr>
</tbody>
</table>

### ibc_channels_max_order_by

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
<td colspan="2" valign="top"><strong>added_at</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>channel_id</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>connection_id</strong></td>
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

### ibc_channels_min_order_by

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
<td colspan="2" valign="top"><strong>added_at</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>channel_id</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>connection_id</strong></td>
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

### ibc_channels_obj_rel_insert_input

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
<td colspan="2" valign="top"><strong>data</strong></td>
<td valign="top"><a href="#ibc_channels_insert_input">ibc_channels_insert_input</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>on_conflict</strong></td>
<td valign="top"><a href="#ibc_channels_on_conflict">ibc_channels_on_conflict</a></td>
<td></td>
</tr>
</tbody>
</table>

### ibc_channels_on_conflict

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
<td colspan="2" valign="top"><strong>constraint</strong></td>
<td valign="top"><a href="#ibc_channels_constraint">ibc_channels_constraint</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>update_columns</strong></td>
<td valign="top">[<a href="#ibc_channels_update_column">ibc_channels_update_column</a>!]!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>where</strong></td>
<td valign="top"><a href="#ibc_channels_bool_exp">ibc_channels_bool_exp</a></td>
<td></td>
</tr>
</tbody>
</table>

### ibc_channels_order_by

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
<td colspan="2" valign="top"><strong>added_at</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>channel_id</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>connection_id</strong></td>
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
</tbody>
</table>

### ibc_channels_pk_columns_input

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
<td colspan="2" valign="top"><strong>zone</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
</tbody>
</table>

### ibc_channels_set_input

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
<td colspan="2" valign="top"><strong>added_at</strong></td>
<td valign="top"><a href="#timestamp">timestamp</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>channel_id</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>connection_id</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>is_opened</strong></td>
<td valign="top"><a href="#boolean">Boolean</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>zone</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td></td>
</tr>
</tbody>
</table>

### ibc_clients_aggregate_order_by

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
<td valign="top"><a href="#ibc_clients_max_order_by">ibc_clients_max_order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>min</strong></td>
<td valign="top"><a href="#ibc_clients_min_order_by">ibc_clients_min_order_by</a></td>
<td></td>
</tr>
</tbody>
</table>

### ibc_clients_arr_rel_insert_input

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
<td colspan="2" valign="top"><strong>data</strong></td>
<td valign="top">[<a href="#ibc_clients_insert_input">ibc_clients_insert_input</a>!]!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>on_conflict</strong></td>
<td valign="top"><a href="#ibc_clients_on_conflict">ibc_clients_on_conflict</a></td>
<td></td>
</tr>
</tbody>
</table>

### ibc_clients_bool_exp

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
<td valign="top">[<a href="#ibc_clients_bool_exp">ibc_clients_bool_exp</a>]</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>_not</strong></td>
<td valign="top"><a href="#ibc_clients_bool_exp">ibc_clients_bool_exp</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>_or</strong></td>
<td valign="top">[<a href="#ibc_clients_bool_exp">ibc_clients_bool_exp</a>]</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>added_at</strong></td>
<td valign="top"><a href="#timestamp_comparison_exp">timestamp_comparison_exp</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>chain_id</strong></td>
<td valign="top"><a href="#string_comparison_exp">String_comparison_exp</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>client_id</strong></td>
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

### ibc_clients_insert_input

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
<td colspan="2" valign="top"><strong>added_at</strong></td>
<td valign="top"><a href="#timestamp">timestamp</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>chain_id</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>client_id</strong></td>
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

### ibc_clients_max_order_by

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
<td colspan="2" valign="top"><strong>added_at</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>chain_id</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>client_id</strong></td>
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

### ibc_clients_min_order_by

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
<td colspan="2" valign="top"><strong>added_at</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>chain_id</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>client_id</strong></td>
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

### ibc_clients_obj_rel_insert_input

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
<td colspan="2" valign="top"><strong>data</strong></td>
<td valign="top"><a href="#ibc_clients_insert_input">ibc_clients_insert_input</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>on_conflict</strong></td>
<td valign="top"><a href="#ibc_clients_on_conflict">ibc_clients_on_conflict</a></td>
<td></td>
</tr>
</tbody>
</table>

### ibc_clients_on_conflict

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
<td colspan="2" valign="top"><strong>constraint</strong></td>
<td valign="top"><a href="#ibc_clients_constraint">ibc_clients_constraint</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>update_columns</strong></td>
<td valign="top">[<a href="#ibc_clients_update_column">ibc_clients_update_column</a>!]!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>where</strong></td>
<td valign="top"><a href="#ibc_clients_bool_exp">ibc_clients_bool_exp</a></td>
<td></td>
</tr>
</tbody>
</table>

### ibc_clients_order_by

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
<td colspan="2" valign="top"><strong>added_at</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>chain_id</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>client_id</strong></td>
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

### ibc_clients_pk_columns_input

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
<td colspan="2" valign="top"><strong>client_id</strong></td>
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

### ibc_clients_set_input

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
<td colspan="2" valign="top"><strong>added_at</strong></td>
<td valign="top"><a href="#timestamp">timestamp</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>chain_id</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>client_id</strong></td>
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

### ibc_connections_aggregate_order_by

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
<td valign="top"><a href="#ibc_connections_max_order_by">ibc_connections_max_order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>min</strong></td>
<td valign="top"><a href="#ibc_connections_min_order_by">ibc_connections_min_order_by</a></td>
<td></td>
</tr>
</tbody>
</table>

### ibc_connections_arr_rel_insert_input

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
<td colspan="2" valign="top"><strong>data</strong></td>
<td valign="top">[<a href="#ibc_connections_insert_input">ibc_connections_insert_input</a>!]!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>on_conflict</strong></td>
<td valign="top"><a href="#ibc_connections_on_conflict">ibc_connections_on_conflict</a></td>
<td></td>
</tr>
</tbody>
</table>

### ibc_connections_bool_exp

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
<td valign="top">[<a href="#ibc_connections_bool_exp">ibc_connections_bool_exp</a>]</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>_not</strong></td>
<td valign="top"><a href="#ibc_connections_bool_exp">ibc_connections_bool_exp</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>_or</strong></td>
<td valign="top">[<a href="#ibc_connections_bool_exp">ibc_connections_bool_exp</a>]</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>added_at</strong></td>
<td valign="top"><a href="#timestamp_comparison_exp">timestamp_comparison_exp</a></td>
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
<td colspan="2" valign="top"><strong>zone</strong></td>
<td valign="top"><a href="#string_comparison_exp">String_comparison_exp</a></td>
<td></td>
</tr>
</tbody>
</table>

### ibc_connections_insert_input

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
<td colspan="2" valign="top"><strong>added_at</strong></td>
<td valign="top"><a href="#timestamp">timestamp</a></td>
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
<td colspan="2" valign="top"><strong>zone</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td></td>
</tr>
</tbody>
</table>

### ibc_connections_max_order_by

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
<td colspan="2" valign="top"><strong>added_at</strong></td>
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
<td colspan="2" valign="top"><strong>zone</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
</tbody>
</table>

### ibc_connections_min_order_by

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
<td colspan="2" valign="top"><strong>added_at</strong></td>
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
<td colspan="2" valign="top"><strong>zone</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
</tbody>
</table>

### ibc_connections_obj_rel_insert_input

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
<td colspan="2" valign="top"><strong>data</strong></td>
<td valign="top"><a href="#ibc_connections_insert_input">ibc_connections_insert_input</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>on_conflict</strong></td>
<td valign="top"><a href="#ibc_connections_on_conflict">ibc_connections_on_conflict</a></td>
<td></td>
</tr>
</tbody>
</table>

### ibc_connections_on_conflict

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
<td colspan="2" valign="top"><strong>constraint</strong></td>
<td valign="top"><a href="#ibc_connections_constraint">ibc_connections_constraint</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>update_columns</strong></td>
<td valign="top">[<a href="#ibc_connections_update_column">ibc_connections_update_column</a>!]!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>where</strong></td>
<td valign="top"><a href="#ibc_connections_bool_exp">ibc_connections_bool_exp</a></td>
<td></td>
</tr>
</tbody>
</table>

### ibc_connections_order_by

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
<td colspan="2" valign="top"><strong>added_at</strong></td>
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
<td colspan="2" valign="top"><strong>zone</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
</tbody>
</table>

### ibc_connections_pk_columns_input

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

### ibc_connections_set_input

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
<td colspan="2" valign="top"><strong>added_at</strong></td>
<td valign="top"><a href="#timestamp">timestamp</a></td>
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
<td colspan="2" valign="top"><strong>zone</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td></td>
</tr>
</tbody>
</table>

### ibc_transfer_hourly_stats_aggregate_order_by

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
<td valign="top"><a href="#ibc_transfer_hourly_stats_avg_order_by">ibc_transfer_hourly_stats_avg_order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>count</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>max</strong></td>
<td valign="top"><a href="#ibc_transfer_hourly_stats_max_order_by">ibc_transfer_hourly_stats_max_order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>min</strong></td>
<td valign="top"><a href="#ibc_transfer_hourly_stats_min_order_by">ibc_transfer_hourly_stats_min_order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>stddev</strong></td>
<td valign="top"><a href="#ibc_transfer_hourly_stats_stddev_order_by">ibc_transfer_hourly_stats_stddev_order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>stddev_pop</strong></td>
<td valign="top"><a href="#ibc_transfer_hourly_stats_stddev_pop_order_by">ibc_transfer_hourly_stats_stddev_pop_order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>stddev_samp</strong></td>
<td valign="top"><a href="#ibc_transfer_hourly_stats_stddev_samp_order_by">ibc_transfer_hourly_stats_stddev_samp_order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>sum</strong></td>
<td valign="top"><a href="#ibc_transfer_hourly_stats_sum_order_by">ibc_transfer_hourly_stats_sum_order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>var_pop</strong></td>
<td valign="top"><a href="#ibc_transfer_hourly_stats_var_pop_order_by">ibc_transfer_hourly_stats_var_pop_order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>var_samp</strong></td>
<td valign="top"><a href="#ibc_transfer_hourly_stats_var_samp_order_by">ibc_transfer_hourly_stats_var_samp_order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>variance</strong></td>
<td valign="top"><a href="#ibc_transfer_hourly_stats_variance_order_by">ibc_transfer_hourly_stats_variance_order_by</a></td>
<td></td>
</tr>
</tbody>
</table>

### ibc_transfer_hourly_stats_arr_rel_insert_input

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
<td colspan="2" valign="top"><strong>data</strong></td>
<td valign="top">[<a href="#ibc_transfer_hourly_stats_insert_input">ibc_transfer_hourly_stats_insert_input</a>!]!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>on_conflict</strong></td>
<td valign="top"><a href="#ibc_transfer_hourly_stats_on_conflict">ibc_transfer_hourly_stats_on_conflict</a></td>
<td></td>
</tr>
</tbody>
</table>

### ibc_transfer_hourly_stats_avg_order_by

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
<td colspan="2" valign="top"><strong>period</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>txs_cnt</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
</tbody>
</table>

### ibc_transfer_hourly_stats_bool_exp

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
<td valign="top">[<a href="#ibc_transfer_hourly_stats_bool_exp">ibc_transfer_hourly_stats_bool_exp</a>]</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>_not</strong></td>
<td valign="top"><a href="#ibc_transfer_hourly_stats_bool_exp">ibc_transfer_hourly_stats_bool_exp</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>_or</strong></td>
<td valign="top">[<a href="#ibc_transfer_hourly_stats_bool_exp">ibc_transfer_hourly_stats_bool_exp</a>]</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>hour</strong></td>
<td valign="top"><a href="#timestamp_comparison_exp">timestamp_comparison_exp</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>period</strong></td>
<td valign="top"><a href="#int_comparison_exp">Int_comparison_exp</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>txs_cnt</strong></td>
<td valign="top"><a href="#int_comparison_exp">Int_comparison_exp</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>zone</strong></td>
<td valign="top"><a href="#string_comparison_exp">String_comparison_exp</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>zone_dest</strong></td>
<td valign="top"><a href="#string_comparison_exp">String_comparison_exp</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>zone_src</strong></td>
<td valign="top"><a href="#string_comparison_exp">String_comparison_exp</a></td>
<td></td>
</tr>
</tbody>
</table>

### ibc_transfer_hourly_stats_inc_input

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
<td colspan="2" valign="top"><strong>period</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>txs_cnt</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td></td>
</tr>
</tbody>
</table>

### ibc_transfer_hourly_stats_insert_input

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
<td colspan="2" valign="top"><strong>hour</strong></td>
<td valign="top"><a href="#timestamp">timestamp</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>period</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>txs_cnt</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>zone</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>zone_dest</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>zone_src</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td></td>
</tr>
</tbody>
</table>

### ibc_transfer_hourly_stats_max_order_by

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
<td colspan="2" valign="top"><strong>hour</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>period</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>txs_cnt</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>zone</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>zone_dest</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>zone_src</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
</tbody>
</table>

### ibc_transfer_hourly_stats_min_order_by

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
<td colspan="2" valign="top"><strong>hour</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>period</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>txs_cnt</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>zone</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>zone_dest</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>zone_src</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
</tbody>
</table>

### ibc_transfer_hourly_stats_obj_rel_insert_input

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
<td colspan="2" valign="top"><strong>data</strong></td>
<td valign="top"><a href="#ibc_transfer_hourly_stats_insert_input">ibc_transfer_hourly_stats_insert_input</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>on_conflict</strong></td>
<td valign="top"><a href="#ibc_transfer_hourly_stats_on_conflict">ibc_transfer_hourly_stats_on_conflict</a></td>
<td></td>
</tr>
</tbody>
</table>

### ibc_transfer_hourly_stats_on_conflict

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
<td colspan="2" valign="top"><strong>constraint</strong></td>
<td valign="top"><a href="#ibc_transfer_hourly_stats_constraint">ibc_transfer_hourly_stats_constraint</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>update_columns</strong></td>
<td valign="top">[<a href="#ibc_transfer_hourly_stats_update_column">ibc_transfer_hourly_stats_update_column</a>!]!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>where</strong></td>
<td valign="top"><a href="#ibc_transfer_hourly_stats_bool_exp">ibc_transfer_hourly_stats_bool_exp</a></td>
<td></td>
</tr>
</tbody>
</table>

### ibc_transfer_hourly_stats_order_by

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
<td colspan="2" valign="top"><strong>hour</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>period</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>txs_cnt</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>zone</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>zone_dest</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>zone_src</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
</tbody>
</table>

### ibc_transfer_hourly_stats_pk_columns_input

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
<td colspan="2" valign="top"><strong>hour</strong></td>
<td valign="top"><a href="#timestamp">timestamp</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>period</strong></td>
<td valign="top"><a href="#int">Int</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>zone</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>zone_dest</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>zone_src</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
</tbody>
</table>

### ibc_transfer_hourly_stats_set_input

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
<td colspan="2" valign="top"><strong>hour</strong></td>
<td valign="top"><a href="#timestamp">timestamp</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>period</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>txs_cnt</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>zone</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>zone_dest</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>zone_src</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td></td>
</tr>
</tbody>
</table>

### ibc_transfer_hourly_stats_stddev_order_by

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
<td colspan="2" valign="top"><strong>period</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>txs_cnt</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
</tbody>
</table>

### ibc_transfer_hourly_stats_stddev_pop_order_by

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
<td colspan="2" valign="top"><strong>period</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>txs_cnt</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
</tbody>
</table>

### ibc_transfer_hourly_stats_stddev_samp_order_by

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
<td colspan="2" valign="top"><strong>period</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>txs_cnt</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
</tbody>
</table>

### ibc_transfer_hourly_stats_sum_order_by

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
<td colspan="2" valign="top"><strong>period</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>txs_cnt</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
</tbody>
</table>

### ibc_transfer_hourly_stats_var_pop_order_by

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
<td colspan="2" valign="top"><strong>period</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>txs_cnt</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
</tbody>
</table>

### ibc_transfer_hourly_stats_var_samp_order_by

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
<td colspan="2" valign="top"><strong>period</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>txs_cnt</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
</tbody>
</table>

### ibc_transfer_hourly_stats_variance_order_by

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
<td colspan="2" valign="top"><strong>period</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>txs_cnt</strong></td>
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

### periods_aggregate_order_by

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
<td valign="top"><a href="#periods_avg_order_by">periods_avg_order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>count</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>max</strong></td>
<td valign="top"><a href="#periods_max_order_by">periods_max_order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>min</strong></td>
<td valign="top"><a href="#periods_min_order_by">periods_min_order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>stddev</strong></td>
<td valign="top"><a href="#periods_stddev_order_by">periods_stddev_order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>stddev_pop</strong></td>
<td valign="top"><a href="#periods_stddev_pop_order_by">periods_stddev_pop_order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>stddev_samp</strong></td>
<td valign="top"><a href="#periods_stddev_samp_order_by">periods_stddev_samp_order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>sum</strong></td>
<td valign="top"><a href="#periods_sum_order_by">periods_sum_order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>var_pop</strong></td>
<td valign="top"><a href="#periods_var_pop_order_by">periods_var_pop_order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>var_samp</strong></td>
<td valign="top"><a href="#periods_var_samp_order_by">periods_var_samp_order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>variance</strong></td>
<td valign="top"><a href="#periods_variance_order_by">periods_variance_order_by</a></td>
<td></td>
</tr>
</tbody>
</table>

### periods_arr_rel_insert_input

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
<td colspan="2" valign="top"><strong>data</strong></td>
<td valign="top">[<a href="#periods_insert_input">periods_insert_input</a>!]!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>on_conflict</strong></td>
<td valign="top"><a href="#periods_on_conflict">periods_on_conflict</a></td>
<td></td>
</tr>
</tbody>
</table>

### periods_avg_order_by

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
<td colspan="2" valign="top"><strong>period_in_hours</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
</tbody>
</table>

### periods_bool_exp

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
<td valign="top">[<a href="#periods_bool_exp">periods_bool_exp</a>]</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>_not</strong></td>
<td valign="top"><a href="#periods_bool_exp">periods_bool_exp</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>_or</strong></td>
<td valign="top">[<a href="#periods_bool_exp">periods_bool_exp</a>]</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>period_in_hours</strong></td>
<td valign="top"><a href="#int_comparison_exp">Int_comparison_exp</a></td>
<td></td>
</tr>
</tbody>
</table>

### periods_inc_input

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
<td colspan="2" valign="top"><strong>period_in_hours</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td></td>
</tr>
</tbody>
</table>

### periods_insert_input

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
<td colspan="2" valign="top"><strong>period_in_hours</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td></td>
</tr>
</tbody>
</table>

### periods_max_order_by

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
<td colspan="2" valign="top"><strong>period_in_hours</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
</tbody>
</table>

### periods_min_order_by

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
<td colspan="2" valign="top"><strong>period_in_hours</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
</tbody>
</table>

### periods_obj_rel_insert_input

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
<td colspan="2" valign="top"><strong>data</strong></td>
<td valign="top"><a href="#periods_insert_input">periods_insert_input</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>on_conflict</strong></td>
<td valign="top"><a href="#periods_on_conflict">periods_on_conflict</a></td>
<td></td>
</tr>
</tbody>
</table>

### periods_on_conflict

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
<td colspan="2" valign="top"><strong>constraint</strong></td>
<td valign="top"><a href="#periods_constraint">periods_constraint</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>update_columns</strong></td>
<td valign="top">[<a href="#periods_update_column">periods_update_column</a>!]!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>where</strong></td>
<td valign="top"><a href="#periods_bool_exp">periods_bool_exp</a></td>
<td></td>
</tr>
</tbody>
</table>

### periods_order_by

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
<td colspan="2" valign="top"><strong>period_in_hours</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
</tbody>
</table>

### periods_pk_columns_input

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
<td colspan="2" valign="top"><strong>period_in_hours</strong></td>
<td valign="top"><a href="#int">Int</a>!</td>
<td></td>
</tr>
</tbody>
</table>

### periods_set_input

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
<td colspan="2" valign="top"><strong>period_in_hours</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td></td>
</tr>
</tbody>
</table>

### periods_stddev_order_by

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
<td colspan="2" valign="top"><strong>period_in_hours</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
</tbody>
</table>

### periods_stddev_pop_order_by

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
<td colspan="2" valign="top"><strong>period_in_hours</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
</tbody>
</table>

### periods_stddev_samp_order_by

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
<td colspan="2" valign="top"><strong>period_in_hours</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
</tbody>
</table>

### periods_sum_order_by

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
<td colspan="2" valign="top"><strong>period_in_hours</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
</tbody>
</table>

### periods_var_pop_order_by

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
<td colspan="2" valign="top"><strong>period_in_hours</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
</tbody>
</table>

### periods_var_samp_order_by

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
<td colspan="2" valign="top"><strong>period_in_hours</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
</tbody>
</table>

### periods_variance_order_by

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
<td colspan="2" valign="top"><strong>period_in_hours</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
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

### total_tx_hourly_stats_aggregate_order_by

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
<td valign="top"><a href="#total_tx_hourly_stats_avg_order_by">total_tx_hourly_stats_avg_order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>count</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>max</strong></td>
<td valign="top"><a href="#total_tx_hourly_stats_max_order_by">total_tx_hourly_stats_max_order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>min</strong></td>
<td valign="top"><a href="#total_tx_hourly_stats_min_order_by">total_tx_hourly_stats_min_order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>stddev</strong></td>
<td valign="top"><a href="#total_tx_hourly_stats_stddev_order_by">total_tx_hourly_stats_stddev_order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>stddev_pop</strong></td>
<td valign="top"><a href="#total_tx_hourly_stats_stddev_pop_order_by">total_tx_hourly_stats_stddev_pop_order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>stddev_samp</strong></td>
<td valign="top"><a href="#total_tx_hourly_stats_stddev_samp_order_by">total_tx_hourly_stats_stddev_samp_order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>sum</strong></td>
<td valign="top"><a href="#total_tx_hourly_stats_sum_order_by">total_tx_hourly_stats_sum_order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>var_pop</strong></td>
<td valign="top"><a href="#total_tx_hourly_stats_var_pop_order_by">total_tx_hourly_stats_var_pop_order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>var_samp</strong></td>
<td valign="top"><a href="#total_tx_hourly_stats_var_samp_order_by">total_tx_hourly_stats_var_samp_order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>variance</strong></td>
<td valign="top"><a href="#total_tx_hourly_stats_variance_order_by">total_tx_hourly_stats_variance_order_by</a></td>
<td></td>
</tr>
</tbody>
</table>

### total_tx_hourly_stats_arr_rel_insert_input

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
<td colspan="2" valign="top"><strong>data</strong></td>
<td valign="top">[<a href="#total_tx_hourly_stats_insert_input">total_tx_hourly_stats_insert_input</a>!]!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>on_conflict</strong></td>
<td valign="top"><a href="#total_tx_hourly_stats_on_conflict">total_tx_hourly_stats_on_conflict</a></td>
<td></td>
</tr>
</tbody>
</table>

### total_tx_hourly_stats_avg_order_by

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
<td colspan="2" valign="top"><strong>period</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_coin_turnover_amount</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>txs_cnt</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>txs_w_ibc_xfer_cnt</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>txs_w_ibc_xfer_fail_cnt</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
</tbody>
</table>

### total_tx_hourly_stats_bool_exp

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
<td valign="top">[<a href="#total_tx_hourly_stats_bool_exp">total_tx_hourly_stats_bool_exp</a>]</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>_not</strong></td>
<td valign="top"><a href="#total_tx_hourly_stats_bool_exp">total_tx_hourly_stats_bool_exp</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>_or</strong></td>
<td valign="top">[<a href="#total_tx_hourly_stats_bool_exp">total_tx_hourly_stats_bool_exp</a>]</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>hour</strong></td>
<td valign="top"><a href="#timestamp_comparison_exp">timestamp_comparison_exp</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>period</strong></td>
<td valign="top"><a href="#int_comparison_exp">Int_comparison_exp</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_coin_turnover_amount</strong></td>
<td valign="top"><a href="#bigint_comparison_exp">bigint_comparison_exp</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>txs_cnt</strong></td>
<td valign="top"><a href="#int_comparison_exp">Int_comparison_exp</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>txs_w_ibc_xfer_cnt</strong></td>
<td valign="top"><a href="#int_comparison_exp">Int_comparison_exp</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>txs_w_ibc_xfer_fail_cnt</strong></td>
<td valign="top"><a href="#int_comparison_exp">Int_comparison_exp</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>zone</strong></td>
<td valign="top"><a href="#string_comparison_exp">String_comparison_exp</a></td>
<td></td>
</tr>
</tbody>
</table>

### total_tx_hourly_stats_inc_input

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
<td colspan="2" valign="top"><strong>period</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_coin_turnover_amount</strong></td>
<td valign="top"><a href="#bigint">bigint</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>txs_cnt</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>txs_w_ibc_xfer_cnt</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>txs_w_ibc_xfer_fail_cnt</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td></td>
</tr>
</tbody>
</table>

### total_tx_hourly_stats_insert_input

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
<td colspan="2" valign="top"><strong>hour</strong></td>
<td valign="top"><a href="#timestamp">timestamp</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>period</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_coin_turnover_amount</strong></td>
<td valign="top"><a href="#bigint">bigint</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>txs_cnt</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>txs_w_ibc_xfer_cnt</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>txs_w_ibc_xfer_fail_cnt</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>zone</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td></td>
</tr>
</tbody>
</table>

### total_tx_hourly_stats_max_order_by

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
<td colspan="2" valign="top"><strong>hour</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>period</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_coin_turnover_amount</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>txs_cnt</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>txs_w_ibc_xfer_cnt</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>txs_w_ibc_xfer_fail_cnt</strong></td>
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

### total_tx_hourly_stats_min_order_by

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
<td colspan="2" valign="top"><strong>hour</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>period</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_coin_turnover_amount</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>txs_cnt</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>txs_w_ibc_xfer_cnt</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>txs_w_ibc_xfer_fail_cnt</strong></td>
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

### total_tx_hourly_stats_obj_rel_insert_input

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
<td colspan="2" valign="top"><strong>data</strong></td>
<td valign="top"><a href="#total_tx_hourly_stats_insert_input">total_tx_hourly_stats_insert_input</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>on_conflict</strong></td>
<td valign="top"><a href="#total_tx_hourly_stats_on_conflict">total_tx_hourly_stats_on_conflict</a></td>
<td></td>
</tr>
</tbody>
</table>

### total_tx_hourly_stats_on_conflict

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
<td colspan="2" valign="top"><strong>constraint</strong></td>
<td valign="top"><a href="#total_tx_hourly_stats_constraint">total_tx_hourly_stats_constraint</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>update_columns</strong></td>
<td valign="top">[<a href="#total_tx_hourly_stats_update_column">total_tx_hourly_stats_update_column</a>!]!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>where</strong></td>
<td valign="top"><a href="#total_tx_hourly_stats_bool_exp">total_tx_hourly_stats_bool_exp</a></td>
<td></td>
</tr>
</tbody>
</table>

### total_tx_hourly_stats_order_by

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
<td colspan="2" valign="top"><strong>hour</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>period</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_coin_turnover_amount</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>txs_cnt</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>txs_w_ibc_xfer_cnt</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>txs_w_ibc_xfer_fail_cnt</strong></td>
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

### total_tx_hourly_stats_pk_columns_input

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
<td colspan="2" valign="top"><strong>hour</strong></td>
<td valign="top"><a href="#timestamp">timestamp</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>period</strong></td>
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

### total_tx_hourly_stats_set_input

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
<td colspan="2" valign="top"><strong>hour</strong></td>
<td valign="top"><a href="#timestamp">timestamp</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>period</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_coin_turnover_amount</strong></td>
<td valign="top"><a href="#bigint">bigint</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>txs_cnt</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>txs_w_ibc_xfer_cnt</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>txs_w_ibc_xfer_fail_cnt</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>zone</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td></td>
</tr>
</tbody>
</table>

### total_tx_hourly_stats_stddev_order_by

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
<td colspan="2" valign="top"><strong>period</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_coin_turnover_amount</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>txs_cnt</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>txs_w_ibc_xfer_cnt</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>txs_w_ibc_xfer_fail_cnt</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
</tbody>
</table>

### total_tx_hourly_stats_stddev_pop_order_by

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
<td colspan="2" valign="top"><strong>period</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_coin_turnover_amount</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>txs_cnt</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>txs_w_ibc_xfer_cnt</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>txs_w_ibc_xfer_fail_cnt</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
</tbody>
</table>

### total_tx_hourly_stats_stddev_samp_order_by

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
<td colspan="2" valign="top"><strong>period</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_coin_turnover_amount</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>txs_cnt</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>txs_w_ibc_xfer_cnt</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>txs_w_ibc_xfer_fail_cnt</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
</tbody>
</table>

### total_tx_hourly_stats_sum_order_by

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
<td colspan="2" valign="top"><strong>period</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_coin_turnover_amount</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>txs_cnt</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>txs_w_ibc_xfer_cnt</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>txs_w_ibc_xfer_fail_cnt</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
</tbody>
</table>

### total_tx_hourly_stats_var_pop_order_by

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
<td colspan="2" valign="top"><strong>period</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_coin_turnover_amount</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>txs_cnt</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>txs_w_ibc_xfer_cnt</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>txs_w_ibc_xfer_fail_cnt</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
</tbody>
</table>

### total_tx_hourly_stats_var_samp_order_by

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
<td colspan="2" valign="top"><strong>period</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_coin_turnover_amount</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>txs_cnt</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>txs_w_ibc_xfer_cnt</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>txs_w_ibc_xfer_fail_cnt</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
</tbody>
</table>

### total_tx_hourly_stats_variance_order_by

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
<td colspan="2" valign="top"><strong>period</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>total_coin_turnover_amount</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>txs_cnt</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>txs_w_ibc_xfer_cnt</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>txs_w_ibc_xfer_fail_cnt</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
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

### zone_nodes_arr_rel_insert_input

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
<td colspan="2" valign="top"><strong>data</strong></td>
<td valign="top">[<a href="#zone_nodes_insert_input">zone_nodes_insert_input</a>!]!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>on_conflict</strong></td>
<td valign="top"><a href="#zone_nodes_on_conflict">zone_nodes_on_conflict</a></td>
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

### zone_nodes_insert_input

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
<td valign="top"><a href="#boolean">Boolean</a></td>
<td></td>
</tr>
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

### zone_nodes_obj_rel_insert_input

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
<td colspan="2" valign="top"><strong>data</strong></td>
<td valign="top"><a href="#zone_nodes_insert_input">zone_nodes_insert_input</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>on_conflict</strong></td>
<td valign="top"><a href="#zone_nodes_on_conflict">zone_nodes_on_conflict</a></td>
<td></td>
</tr>
</tbody>
</table>

### zone_nodes_on_conflict

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
<td colspan="2" valign="top"><strong>constraint</strong></td>
<td valign="top"><a href="#zone_nodes_constraint">zone_nodes_constraint</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>update_columns</strong></td>
<td valign="top">[<a href="#zone_nodes_update_column">zone_nodes_update_column</a>!]!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>where</strong></td>
<td valign="top"><a href="#zone_nodes_bool_exp">zone_nodes_bool_exp</a></td>
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
<tr>
<td colspan="2" valign="top"><strong>zone</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
</tbody>
</table>

### zone_nodes_set_input

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
<td valign="top"><a href="#boolean">Boolean</a></td>
<td></td>
</tr>
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

### zones_aggregate_order_by

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
<td valign="top"><a href="#zones_max_order_by">zones_max_order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>min</strong></td>
<td valign="top"><a href="#zones_min_order_by">zones_min_order_by</a></td>
<td></td>
</tr>
</tbody>
</table>

### zones_arr_rel_insert_input

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
<td colspan="2" valign="top"><strong>data</strong></td>
<td valign="top">[<a href="#zones_insert_input">zones_insert_input</a>!]!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>on_conflict</strong></td>
<td valign="top"><a href="#zones_on_conflict">zones_on_conflict</a></td>
<td></td>
</tr>
</tbody>
</table>

### zones_bool_exp

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
<td valign="top">[<a href="#zones_bool_exp">zones_bool_exp</a>]</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>_not</strong></td>
<td valign="top"><a href="#zones_bool_exp">zones_bool_exp</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>_or</strong></td>
<td valign="top">[<a href="#zones_bool_exp">zones_bool_exp</a>]</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>added_at</strong></td>
<td valign="top"><a href="#timestamp_comparison_exp">timestamp_comparison_exp</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>chain_id</strong></td>
<td valign="top"><a href="#string_comparison_exp">String_comparison_exp</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>description</strong></td>
<td valign="top"><a href="#string_comparison_exp">String_comparison_exp</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>is_caught_up</strong></td>
<td valign="top"><a href="#boolean_comparison_exp">Boolean_comparison_exp</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>is_enabled</strong></td>
<td valign="top"><a href="#boolean_comparison_exp">Boolean_comparison_exp</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>name</strong></td>
<td valign="top"><a href="#string_comparison_exp">String_comparison_exp</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>updated_at</strong></td>
<td valign="top"><a href="#timestamp_comparison_exp">timestamp_comparison_exp</a></td>
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

### zones_graphs_arr_rel_insert_input

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
<td colspan="2" valign="top"><strong>data</strong></td>
<td valign="top">[<a href="#zones_graphs_insert_input">zones_graphs_insert_input</a>!]!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>on_conflict</strong></td>
<td valign="top"><a href="#zones_graphs_on_conflict">zones_graphs_on_conflict</a></td>
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

### zones_graphs_inc_input

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
<td valign="top"><a href="#int">Int</a></td>
<td></td>
</tr>
</tbody>
</table>

### zones_graphs_insert_input

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

### zones_graphs_obj_rel_insert_input

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
<td colspan="2" valign="top"><strong>data</strong></td>
<td valign="top"><a href="#zones_graphs_insert_input">zones_graphs_insert_input</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>on_conflict</strong></td>
<td valign="top"><a href="#zones_graphs_on_conflict">zones_graphs_on_conflict</a></td>
<td></td>
</tr>
</tbody>
</table>

### zones_graphs_on_conflict

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
<td colspan="2" valign="top"><strong>constraint</strong></td>
<td valign="top"><a href="#zones_graphs_constraint">zones_graphs_constraint</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>update_columns</strong></td>
<td valign="top">[<a href="#zones_graphs_update_column">zones_graphs_update_column</a>!]!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>where</strong></td>
<td valign="top"><a href="#zones_graphs_bool_exp">zones_graphs_bool_exp</a></td>
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

### zones_graphs_set_input

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
<td colspan="2" valign="top"><strong>timeframe</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
</tbody>
</table>

### zones_insert_input

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
<td colspan="2" valign="top"><strong>added_at</strong></td>
<td valign="top"><a href="#timestamp">timestamp</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>chain_id</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>description</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>is_caught_up</strong></td>
<td valign="top"><a href="#boolean">Boolean</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>is_enabled</strong></td>
<td valign="top"><a href="#boolean">Boolean</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>name</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>updated_at</strong></td>
<td valign="top"><a href="#timestamp">timestamp</a></td>
<td></td>
</tr>
</tbody>
</table>

### zones_max_order_by

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
<td colspan="2" valign="top"><strong>added_at</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>chain_id</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>description</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>name</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>updated_at</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
</tbody>
</table>

### zones_min_order_by

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
<td colspan="2" valign="top"><strong>added_at</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>chain_id</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>description</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>name</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>updated_at</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
</tbody>
</table>

### zones_obj_rel_insert_input

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
<td colspan="2" valign="top"><strong>data</strong></td>
<td valign="top"><a href="#zones_insert_input">zones_insert_input</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>on_conflict</strong></td>
<td valign="top"><a href="#zones_on_conflict">zones_on_conflict</a></td>
<td></td>
</tr>
</tbody>
</table>

### zones_on_conflict

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
<td colspan="2" valign="top"><strong>constraint</strong></td>
<td valign="top"><a href="#zones_constraint">zones_constraint</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>update_columns</strong></td>
<td valign="top">[<a href="#zones_update_column">zones_update_column</a>!]!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>where</strong></td>
<td valign="top"><a href="#zones_bool_exp">zones_bool_exp</a></td>
<td></td>
</tr>
</tbody>
</table>

### zones_order_by

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
<td colspan="2" valign="top"><strong>added_at</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>chain_id</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>description</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>is_caught_up</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>is_enabled</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>name</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>updated_at</strong></td>
<td valign="top"><a href="#order_by">order_by</a></td>
<td></td>
</tr>
</tbody>
</table>

### zones_pk_columns_input

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
<td colspan="2" valign="top"><strong>chain_id</strong></td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
</tbody>
</table>

### zones_set_input

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
<td colspan="2" valign="top"><strong>added_at</strong></td>
<td valign="top"><a href="#timestamp">timestamp</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>chain_id</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>description</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>is_caught_up</strong></td>
<td valign="top"><a href="#boolean">Boolean</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>is_enabled</strong></td>
<td valign="top"><a href="#boolean">Boolean</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>name</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>updated_at</strong></td>
<td valign="top"><a href="#timestamp">timestamp</a></td>
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

### zones_stats_append_input

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
<td colspan="2" valign="top"><strong>chart</strong></td>
<td valign="top"><a href="#jsonb">jsonb</a></td>
<td></td>
</tr>
</tbody>
</table>

### zones_stats_arr_rel_insert_input

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
<td colspan="2" valign="top"><strong>data</strong></td>
<td valign="top">[<a href="#zones_stats_insert_input">zones_stats_insert_input</a>!]!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>on_conflict</strong></td>
<td valign="top"><a href="#zones_stats_on_conflict">zones_stats_on_conflict</a></td>
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
<td colspan="2" valign="top"><strong>channels_num</strong></td>
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
<td colspan="2" valign="top"><strong>channels_num</strong></td>
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
<td valign="top"><a href="#int_comparison_exp">Int_comparison_exp</a></td>
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

### zones_stats_delete_at_path_input

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
<td colspan="2" valign="top"><strong>chart</strong></td>
<td valign="top">[<a href="#string">String</a>]</td>
<td></td>
</tr>
</tbody>
</table>

### zones_stats_delete_elem_input

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
<td colspan="2" valign="top"><strong>chart</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td></td>
</tr>
</tbody>
</table>

### zones_stats_delete_key_input

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
<td colspan="2" valign="top"><strong>chart</strong></td>
<td valign="top"><a href="#string">String</a></td>
<td></td>
</tr>
</tbody>
</table>

### zones_stats_inc_input

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
<td colspan="2" valign="top"><strong>channels_num</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_percent</strong></td>
<td valign="top"><a href="#int">Int</a></td>
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

### zones_stats_insert_input

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
<td colspan="2" valign="top"><strong>channels_num</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>chart</strong></td>
<td valign="top"><a href="#jsonb">jsonb</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_percent</strong></td>
<td valign="top"><a href="#int">Int</a></td>
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
<td colspan="2" valign="top"><strong>channels_num</strong></td>
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
<td colspan="2" valign="top"><strong>channels_num</strong></td>
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

### zones_stats_obj_rel_insert_input

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
<td colspan="2" valign="top"><strong>data</strong></td>
<td valign="top"><a href="#zones_stats_insert_input">zones_stats_insert_input</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>on_conflict</strong></td>
<td valign="top"><a href="#zones_stats_on_conflict">zones_stats_on_conflict</a></td>
<td></td>
</tr>
</tbody>
</table>

### zones_stats_on_conflict

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
<td colspan="2" valign="top"><strong>constraint</strong></td>
<td valign="top"><a href="#zones_stats_constraint">zones_stats_constraint</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>update_columns</strong></td>
<td valign="top">[<a href="#zones_stats_update_column">zones_stats_update_column</a>!]!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>where</strong></td>
<td valign="top"><a href="#zones_stats_bool_exp">zones_stats_bool_exp</a></td>
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
<td colspan="2" valign="top"><strong>channels_num</strong></td>
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

### zones_stats_prepend_input

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
<td colspan="2" valign="top"><strong>chart</strong></td>
<td valign="top"><a href="#jsonb">jsonb</a></td>
<td></td>
</tr>
</tbody>
</table>

### zones_stats_set_input

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
<td colspan="2" valign="top"><strong>channels_num</strong></td>
<td valign="top"><a href="#int">Int</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>chart</strong></td>
<td valign="top"><a href="#jsonb">jsonb</a></td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>ibc_percent</strong></td>
<td valign="top"><a href="#int">Int</a></td>
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
<td colspan="2" valign="top"><strong>channels_num</strong></td>
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
<td colspan="2" valign="top"><strong>channels_num</strong></td>
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
<td colspan="2" valign="top"><strong>channels_num</strong></td>
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
<td colspan="2" valign="top"><strong>channels_num</strong></td>
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
<td colspan="2" valign="top"><strong>channels_num</strong></td>
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
<td colspan="2" valign="top"><strong>channels_num</strong></td>
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
<td colspan="2" valign="top"><strong>channels_num</strong></td>
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

### active_addresses_constraint

<table>
<thead>
<th align="left">Value</th>
<th align="left">Description</th>
</thead>
<tbody>
<tr>
<td valign="top"><strong>active_addresses_pkey</strong></td>
<td></td>
</tr>
</tbody>
</table>

### active_addresses_select_column

<table>
<thead>
<th align="left">Value</th>
<th align="left">Description</th>
</thead>
<tbody>
<tr>
<td valign="top"><strong>address</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>hour</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>period</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>zone</strong></td>
<td></td>
</tr>
</tbody>
</table>

### active_addresses_update_column

<table>
<thead>
<th align="left">Value</th>
<th align="left">Description</th>
</thead>
<tbody>
<tr>
<td valign="top"><strong>address</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>hour</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>period</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>zone</strong></td>
<td></td>
</tr>
</tbody>
</table>

### blocks_log_constraint

<table>
<thead>
<th align="left">Value</th>
<th align="left">Description</th>
</thead>
<tbody>
<tr>
<td valign="top"><strong>blocks_log_hub_pkey</strong></td>
<td></td>
</tr>
</tbody>
</table>

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

### blocks_log_update_column

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

### headers_constraint

<table>
<thead>
<th align="left">Value</th>
<th align="left">Description</th>
</thead>
<tbody>
<tr>
<td valign="top"><strong>headers_pkey</strong></td>
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
<td valign="top"><strong>channels_cnt_all</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>channels_cnt_period</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>chart</strong></td>
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

### headers_update_column

<table>
<thead>
<th align="left">Value</th>
<th align="left">Description</th>
</thead>
<tbody>
<tr>
<td valign="top"><strong>channels_cnt_all</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>channels_cnt_period</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>chart</strong></td>
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

### ibc_channel_zone_constraint

<table>
<thead>
<th align="left">Value</th>
<th align="left">Description</th>
</thead>
<tbody>
<tr>
<td valign="top"><strong>ibc_channel_zone_pkey</strong></td>
<td></td>
</tr>
</tbody>
</table>

### ibc_channel_zone_select_column

<table>
<thead>
<th align="left">Value</th>
<th align="left">Description</th>
</thead>
<tbody>
<tr>
<td valign="top"><strong>added_at</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>chain_id</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>chanel_id</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>zone</strong></td>
<td></td>
</tr>
</tbody>
</table>

### ibc_channel_zone_update_column

<table>
<thead>
<th align="left">Value</th>
<th align="left">Description</th>
</thead>
<tbody>
<tr>
<td valign="top"><strong>added_at</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>chain_id</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>chanel_id</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>zone</strong></td>
<td></td>
</tr>
</tbody>
</table>

### ibc_channels_constraint

<table>
<thead>
<th align="left">Value</th>
<th align="left">Description</th>
</thead>
<tbody>
<tr>
<td valign="top"><strong>channels_pkey</strong></td>
<td></td>
</tr>
</tbody>
</table>

### ibc_channels_select_column

<table>
<thead>
<th align="left">Value</th>
<th align="left">Description</th>
</thead>
<tbody>
<tr>
<td valign="top"><strong>added_at</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>channel_id</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>connection_id</strong></td>
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
</tbody>
</table>

### ibc_channels_update_column

<table>
<thead>
<th align="left">Value</th>
<th align="left">Description</th>
</thead>
<tbody>
<tr>
<td valign="top"><strong>added_at</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>channel_id</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>connection_id</strong></td>
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
</tbody>
</table>

### ibc_clients_constraint

<table>
<thead>
<th align="left">Value</th>
<th align="left">Description</th>
</thead>
<tbody>
<tr>
<td valign="top"><strong>ibc_clients_pkey</strong></td>
<td></td>
</tr>
</tbody>
</table>

### ibc_clients_select_column

<table>
<thead>
<th align="left">Value</th>
<th align="left">Description</th>
</thead>
<tbody>
<tr>
<td valign="top"><strong>added_at</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>chain_id</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>client_id</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>zone</strong></td>
<td></td>
</tr>
</tbody>
</table>

### ibc_clients_update_column

<table>
<thead>
<th align="left">Value</th>
<th align="left">Description</th>
</thead>
<tbody>
<tr>
<td valign="top"><strong>added_at</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>chain_id</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>client_id</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>zone</strong></td>
<td></td>
</tr>
</tbody>
</table>

### ibc_connections_constraint

<table>
<thead>
<th align="left">Value</th>
<th align="left">Description</th>
</thead>
<tbody>
<tr>
<td valign="top"><strong>connections_pkey</strong></td>
<td></td>
</tr>
</tbody>
</table>

### ibc_connections_select_column

<table>
<thead>
<th align="left">Value</th>
<th align="left">Description</th>
</thead>
<tbody>
<tr>
<td valign="top"><strong>added_at</strong></td>
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
<td valign="top"><strong>zone</strong></td>
<td></td>
</tr>
</tbody>
</table>

### ibc_connections_update_column

<table>
<thead>
<th align="left">Value</th>
<th align="left">Description</th>
</thead>
<tbody>
<tr>
<td valign="top"><strong>added_at</strong></td>
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
<td valign="top"><strong>zone</strong></td>
<td></td>
</tr>
</tbody>
</table>

### ibc_transfer_hourly_stats_constraint

<table>
<thead>
<th align="left">Value</th>
<th align="left">Description</th>
</thead>
<tbody>
<tr>
<td valign="top"><strong>ibc_transfer_hourly_stats_pkey</strong></td>
<td></td>
</tr>
</tbody>
</table>

### ibc_transfer_hourly_stats_select_column

<table>
<thead>
<th align="left">Value</th>
<th align="left">Description</th>
</thead>
<tbody>
<tr>
<td valign="top"><strong>hour</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>period</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>txs_cnt</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>zone</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>zone_dest</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>zone_src</strong></td>
<td></td>
</tr>
</tbody>
</table>

### ibc_transfer_hourly_stats_update_column

<table>
<thead>
<th align="left">Value</th>
<th align="left">Description</th>
</thead>
<tbody>
<tr>
<td valign="top"><strong>hour</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>period</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>txs_cnt</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>zone</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>zone_dest</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>zone_src</strong></td>
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

### periods_constraint

<table>
<thead>
<th align="left">Value</th>
<th align="left">Description</th>
</thead>
<tbody>
<tr>
<td valign="top"><strong>periods_pkey</strong></td>
<td></td>
</tr>
</tbody>
</table>

### periods_select_column

<table>
<thead>
<th align="left">Value</th>
<th align="left">Description</th>
</thead>
<tbody>
<tr>
<td valign="top"><strong>period_in_hours</strong></td>
<td></td>
</tr>
</tbody>
</table>

### periods_update_column

<table>
<thead>
<th align="left">Value</th>
<th align="left">Description</th>
</thead>
<tbody>
<tr>
<td valign="top"><strong>period_in_hours</strong></td>
<td></td>
</tr>
</tbody>
</table>

### total_tx_hourly_stats_constraint

<table>
<thead>
<th align="left">Value</th>
<th align="left">Description</th>
</thead>
<tbody>
<tr>
<td valign="top"><strong>total_tx_hourly_stats_pkey</strong></td>
<td></td>
</tr>
</tbody>
</table>

### total_tx_hourly_stats_select_column

<table>
<thead>
<th align="left">Value</th>
<th align="left">Description</th>
</thead>
<tbody>
<tr>
<td valign="top"><strong>hour</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>period</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>total_coin_turnover_amount</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>txs_cnt</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>txs_w_ibc_xfer_cnt</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>txs_w_ibc_xfer_fail_cnt</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>zone</strong></td>
<td></td>
</tr>
</tbody>
</table>

### total_tx_hourly_stats_update_column

<table>
<thead>
<th align="left">Value</th>
<th align="left">Description</th>
</thead>
<tbody>
<tr>
<td valign="top"><strong>hour</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>period</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>total_coin_turnover_amount</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>txs_cnt</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>txs_w_ibc_xfer_cnt</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>txs_w_ibc_xfer_fail_cnt</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>zone</strong></td>
<td></td>
</tr>
</tbody>
</table>

### zone_nodes_constraint

<table>
<thead>
<th align="left">Value</th>
<th align="left">Description</th>
</thead>
<tbody>
<tr>
<td valign="top"><strong>zone_nodes_pkey</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>zone_nodes_rpc_addr_key</strong></td>
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

### zone_nodes_update_column

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

### zones_constraint

<table>
<thead>
<th align="left">Value</th>
<th align="left">Description</th>
</thead>
<tbody>
<tr>
<td valign="top"><strong>zones_pkey</strong></td>
<td></td>
</tr>
</tbody>
</table>

### zones_graphs_constraint

<table>
<thead>
<th align="left">Value</th>
<th align="left">Description</th>
</thead>
<tbody>
<tr>
<td valign="top"><strong>zones_graphs_pkey</strong></td>
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

### zones_graphs_update_column

<table>
<thead>
<th align="left">Value</th>
<th align="left">Description</th>
</thead>
<tbody>
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

### zones_select_column

<table>
<thead>
<th align="left">Value</th>
<th align="left">Description</th>
</thead>
<tbody>
<tr>
<td valign="top"><strong>added_at</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>chain_id</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>description</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>is_caught_up</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>is_enabled</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>name</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>updated_at</strong></td>
<td></td>
</tr>
</tbody>
</table>

### zones_stats_constraint

<table>
<thead>
<th align="left">Value</th>
<th align="left">Description</th>
</thead>
<tbody>
<tr>
<td valign="top"><strong>zones_stats_pkey</strong></td>
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
<td valign="top"><strong>channels_num</strong></td>
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

### zones_stats_update_column

<table>
<thead>
<th align="left">Value</th>
<th align="left">Description</th>
</thead>
<tbody>
<tr>
<td valign="top"><strong>channels_num</strong></td>
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

### zones_update_column

<table>
<thead>
<th align="left">Value</th>
<th align="left">Description</th>
</thead>
<tbody>
<tr>
<td valign="top"><strong>added_at</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>chain_id</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>description</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>is_caught_up</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>is_enabled</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>name</strong></td>
<td></td>
</tr>
<tr>
<td valign="top"><strong>updated_at</strong></td>
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

### bigint

### jsonb

### numeric

### timestamp

