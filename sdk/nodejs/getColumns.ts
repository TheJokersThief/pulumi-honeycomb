// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "./utilities";

/**
 * ## # Data Source: honeycomb.GetColumns
 *
 * The columns data source allows the columns of a dataset to be retrieved.
 *
 * ## Example Usage
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as honeycomb from "@pulumi/honeycomb";
 *
 * const config = new pulumi.Config();
 * const dataset = config.require("dataset");
 * const all = honeycomb.GetColumns({
 *     dataset: dataset,
 * });
 * const foo = honeycomb.GetColumns({
 *     dataset: dataset,
 *     startsWith: "foo_",
 * });
 * ```
 */
export function getColumns(args: GetColumnsArgs, opts?: pulumi.InvokeOptions): Promise<GetColumnsResult> {

    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invoke("honeycomb:index/getColumns:GetColumns", {
        "dataset": args.dataset,
        "startsWith": args.startsWith,
    }, opts);
}

/**
 * A collection of arguments for invoking GetColumns.
 */
export interface GetColumnsArgs {
    /**
     * The dataset to retrieve the columns list from
     */
    dataset: string;
    /**
     * Only return columns starting with the given value.
     */
    startsWith?: string;
}

/**
 * A collection of values returned by GetColumns.
 */
export interface GetColumnsResult {
    readonly dataset: string;
    /**
     * The provider-assigned unique ID for this managed resource.
     */
    readonly id: string;
    /**
     * a list of all the column names found in the dataset
     */
    readonly names: string[];
    readonly startsWith?: string;
}
/**
 * ## # Data Source: honeycomb.GetColumns
 *
 * The columns data source allows the columns of a dataset to be retrieved.
 *
 * ## Example Usage
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as honeycomb from "@pulumi/honeycomb";
 *
 * const config = new pulumi.Config();
 * const dataset = config.require("dataset");
 * const all = honeycomb.GetColumns({
 *     dataset: dataset,
 * });
 * const foo = honeycomb.GetColumns({
 *     dataset: dataset,
 *     startsWith: "foo_",
 * });
 * ```
 */
export function getColumnsOutput(args: GetColumnsOutputArgs, opts?: pulumi.InvokeOptions): pulumi.Output<GetColumnsResult> {
    return pulumi.output(args).apply((a: any) => getColumns(a, opts))
}

/**
 * A collection of arguments for invoking GetColumns.
 */
export interface GetColumnsOutputArgs {
    /**
     * The dataset to retrieve the columns list from
     */
    dataset: pulumi.Input<string>;
    /**
     * Only return columns starting with the given value.
     */
    startsWith?: pulumi.Input<string>;
}
