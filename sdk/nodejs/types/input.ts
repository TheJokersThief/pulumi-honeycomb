// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";

export interface BoardQuery {
    /**
     * Descriptive text to contextualize the Query within the Board. Supports Markdown.
     */
    caption?: pulumi.Input<string>;
    /**
     * The dataset this query is associated with.
     *
     * @deprecated Board Queries no longer require the dataset as they rely on the provided Query ID's dataset.
     */
    dataset?: pulumi.Input<string>;
    /**
     * A map of boolean toggles to manages the settings for this query's graph on the board.
     * If a value is unspecified, it is assumed to be false.
     * Currently supported toggles are:
     */
    graphSettings?: pulumi.Input<inputs.BoardQueryGraphSettings>;
    /**
     * The ID of the Query Annotation to associate with this query.
     */
    queryAnnotationId?: pulumi.Input<string>;
    /**
     * The ID of the Query to run.
     */
    queryId: pulumi.Input<string>;
    /**
     * How the query should be displayed within the board, either `graph` (the default), `table` or `combo`.
     */
    queryStyle?: pulumi.Input<string>;
}

export interface BoardQueryGraphSettings {
    /**
     * Disable the overlay of Markers on the graph.
     */
    hideMarkers?: pulumi.Input<boolean>;
    /**
     * Set the graph's Y axis to Log scale.
     */
    logScale?: pulumi.Input<boolean>;
    /**
     * Enable interpolatation between datapoints when the intervening time buckets have no matching events.
     */
    omitMissingValues?: pulumi.Input<boolean>;
    /**
     * See [Graph Settings](https://docs.honeycomb.io/working-with-your-data/graph-settings/) in the documentation for more information on any individual setting.
     */
    overlaidCharts?: pulumi.Input<boolean>;
    /**
     * Enable the display of groups as stacked colored area under their line graphs.
     */
    stackedGraphs?: pulumi.Input<boolean>;
    /**
     * Set the graph's X axis to UTC.
     */
    utcXaxis?: pulumi.Input<boolean>;
}

export interface GetQuerySpecificationCalculation {
    /**
     * The column to apply the operator to, not needed with `COUNT` or `CONCURRENCY`.
     */
    column?: string;
    /**
     * The operator to apply, see the supported list of calculation operators at [Calculation Operators](https://docs.honeycomb.io/api/query-specification/#calculation-operators).
     */
    op: string;
}

export interface GetQuerySpecificationCalculationArgs {
    /**
     * The column to apply the operator to, not needed with `COUNT` or `CONCURRENCY`.
     */
    column?: pulumi.Input<string>;
    /**
     * The operator to apply, see the supported list of calculation operators at [Calculation Operators](https://docs.honeycomb.io/api/query-specification/#calculation-operators).
     */
    op: pulumi.Input<string>;
}

export interface GetQuerySpecificationFilter {
    /**
     * The column to apply the filter to.
     */
    column: string;
    /**
     * The operator to apply, see the supported list of filter operators at [Filter Operators](https://docs.honeycomb.io/api/query-specification/#filter-operators). Not all operators require a value.
     */
    op: string;
    /**
     * The value used for the filter. Not needed if op is `exists` or `not-exists`. Mutually exclusive with the other `value_*` options.
     */
    value?: string;
    /**
     * Deprecated: use 'value' instead. The value used for the filter when the column is a boolean. Mutually exclusive with `value` and the other `value_*` options.
     *
     * * > **NOTE** Filter op `in` and `not-in` expect an array of strings as value. Use the `value` attribute and pass the values in single string separated by `,` without additional spaces (similar to the query builder in the UI). For example: the list `foo`, `bar` becomes `foo,bar`.
     *
     * @deprecated Use of attribute `valueBoolean` is discouraged and will fail to plan if using 'false'. Use of `value` is encouraged.
     */
    valueBoolean?: boolean;
    /**
     * Deprecated: use 'value' instead. The value used for the filter when the column is a float. Mutually exclusive with `value` and the other `value_*` options.
     *
     * @deprecated Use of attribute `valueFloat` is discouraged and will fail to plan if using '0'. Use of `value` is encouraged.
     */
    valueFloat?: number;
    /**
     * Deprecated: use 'value' instead. The value used for the filter when the column is an integer. Mutually exclusive with `value` and the other `value_*` options.
     *
     * @deprecated Use of attribute `valueInteger` is discouraged and will fail to plan if using '0'. Use of `value` is encouraged.
     */
    valueInteger?: number;
    /**
     * Deprecated: use 'value' instead. The value used for the filter when the column is a string. Mutually exclusive with `value` and the other `value_*` options.
     *
     * @deprecated Use of attribute `valueString` is discouraged and will fail to plan if using the empty string. Use of `value` is encouraged.
     */
    valueString?: string;
}

export interface GetQuerySpecificationFilterArgs {
    /**
     * The column to apply the filter to.
     */
    column: pulumi.Input<string>;
    /**
     * The operator to apply, see the supported list of filter operators at [Filter Operators](https://docs.honeycomb.io/api/query-specification/#filter-operators). Not all operators require a value.
     */
    op: pulumi.Input<string>;
    /**
     * The value used for the filter. Not needed if op is `exists` or `not-exists`. Mutually exclusive with the other `value_*` options.
     */
    value?: pulumi.Input<string>;
    /**
     * Deprecated: use 'value' instead. The value used for the filter when the column is a boolean. Mutually exclusive with `value` and the other `value_*` options.
     *
     * * > **NOTE** Filter op `in` and `not-in` expect an array of strings as value. Use the `value` attribute and pass the values in single string separated by `,` without additional spaces (similar to the query builder in the UI). For example: the list `foo`, `bar` becomes `foo,bar`.
     *
     * @deprecated Use of attribute `valueBoolean` is discouraged and will fail to plan if using 'false'. Use of `value` is encouraged.
     */
    valueBoolean?: pulumi.Input<boolean>;
    /**
     * Deprecated: use 'value' instead. The value used for the filter when the column is a float. Mutually exclusive with `value` and the other `value_*` options.
     *
     * @deprecated Use of attribute `valueFloat` is discouraged and will fail to plan if using '0'. Use of `value` is encouraged.
     */
    valueFloat?: pulumi.Input<number>;
    /**
     * Deprecated: use 'value' instead. The value used for the filter when the column is an integer. Mutually exclusive with `value` and the other `value_*` options.
     *
     * @deprecated Use of attribute `valueInteger` is discouraged and will fail to plan if using '0'. Use of `value` is encouraged.
     */
    valueInteger?: pulumi.Input<number>;
    /**
     * Deprecated: use 'value' instead. The value used for the filter when the column is a string. Mutually exclusive with `value` and the other `value_*` options.
     *
     * @deprecated Use of attribute `valueString` is discouraged and will fail to plan if using the empty string. Use of `value` is encouraged.
     */
    valueString?: pulumi.Input<string>;
}

export interface GetQuerySpecificationHaving {
    /**
     * The calculation operator to apply, supports all of the [Calculation Operators](https://docs.honeycomb.io/api/query-specification/#calculation-operators) with the exception of `HEATMAP`.
     */
    calculateOp: string;
    /**
     * The column to apply the `calculateOp` to, not needed with `COUNT` or `CONCURRENCY`.
     */
    column?: string;
    /**
     * The operator to apply to filter the query results. One of `=`, `!=`, `>`, `>=`, `<`, or `<=`.
     */
    op: string;
    /**
     * The value used with `op`. Currently assumed to be a number.
     *
     * > **NOTE** A having term's `column`/`calculateOp` pair must have a corresponding `calculation`. There can be multiple `having` blocks for the same `column`/`calculateOp` pair.
     */
    value: number;
}

export interface GetQuerySpecificationHavingArgs {
    /**
     * The calculation operator to apply, supports all of the [Calculation Operators](https://docs.honeycomb.io/api/query-specification/#calculation-operators) with the exception of `HEATMAP`.
     */
    calculateOp: pulumi.Input<string>;
    /**
     * The column to apply the `calculateOp` to, not needed with `COUNT` or `CONCURRENCY`.
     */
    column?: pulumi.Input<string>;
    /**
     * The operator to apply to filter the query results. One of `=`, `!=`, `>`, `>=`, `<`, or `<=`.
     */
    op: pulumi.Input<string>;
    /**
     * The value used with `op`. Currently assumed to be a number.
     *
     * > **NOTE** A having term's `column`/`calculateOp` pair must have a corresponding `calculation`. There can be multiple `having` blocks for the same `column`/`calculateOp` pair.
     */
    value: pulumi.Input<number>;
}

export interface GetQuerySpecificationOrder {
    /**
     * Either a column present in `breakdown` or a column to `op` applies to.
     */
    column?: string;
    /**
     * The calculation operator to apply, see the supported list of calculation operators at [Calculation Operators](https://docs.honeycomb.io/api/query-specification/#calculation-operators).
     */
    op?: string;
    /**
     * The sort direction, if set must be `ascending` or `descending`.
     */
    order?: string;
}

export interface GetQuerySpecificationOrderArgs {
    /**
     * Either a column present in `breakdown` or a column to `op` applies to.
     */
    column?: pulumi.Input<string>;
    /**
     * The calculation operator to apply, see the supported list of calculation operators at [Calculation Operators](https://docs.honeycomb.io/api/query-specification/#calculation-operators).
     */
    op?: pulumi.Input<string>;
    /**
     * The sort direction, if set must be `ascending` or `descending`.
     */
    order?: pulumi.Input<string>;
}

export interface GetRecipientDetailFilter {
    /**
     * The name of the detail field to filter by. Allowed values are `address`, `channel`, `name`, `integrationName`, and `url`.
     */
    name: string;
    /**
     * The value of the detail field to match on.
     */
    value?: string;
    /**
     * A regular expression string to apply to the value of the detail field to match on.
     *
     * > **Note** one of `value` or `valueRegex` is required.
     */
    valueRegex?: string;
}

export interface GetRecipientDetailFilterArgs {
    /**
     * The name of the detail field to filter by. Allowed values are `address`, `channel`, `name`, `integrationName`, and `url`.
     */
    name: pulumi.Input<string>;
    /**
     * The value of the detail field to match on.
     */
    value?: pulumi.Input<string>;
    /**
     * A regular expression string to apply to the value of the detail field to match on.
     *
     * > **Note** one of `value` or `valueRegex` is required.
     */
    valueRegex?: pulumi.Input<string>;
}

export interface GetRecipientsDetailFilter {
    /**
     * The name of the detail field to filter by. Allowed values are `address`, `channel`, `name`, `integrationName`, and `url`.
     */
    name: string;
    /**
     * The value of the detail field to match on.
     */
    value?: string;
    /**
     * A regular expression string to apply to the value of the detail field to match on.
     *
     * > **Note** one of `value` or `valueRegex` is required.
     */
    valueRegex?: string;
}

export interface GetRecipientsDetailFilterArgs {
    /**
     * The name of the detail field to filter by. Allowed values are `address`, `channel`, `name`, `integrationName`, and `url`.
     */
    name: pulumi.Input<string>;
    /**
     * The value of the detail field to match on.
     */
    value?: pulumi.Input<string>;
    /**
     * A regular expression string to apply to the value of the detail field to match on.
     *
     * > **Note** one of `value` or `valueRegex` is required.
     */
    valueRegex?: pulumi.Input<string>;
}
