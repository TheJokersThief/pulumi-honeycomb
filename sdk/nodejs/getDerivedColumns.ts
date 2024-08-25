// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "./utilities";

/**
 * ## # Data Source: honeycomb.GetDerivedColumns
 *
 * The `honeycomb.GetDerivedColumns` data source allows the derived columns of a dataset to be retrieved.
 *
 * ## Example Usage
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as honeycomb from "@pulumi/honeycomb";
 *
 * const config = new pulumi.Config();
 * const dataset = config.require("dataset");
 * const all = honeycomb.GetDerivedColumns({
 *     dataset: dataset,
 * });
 * const foo = honeycomb.GetDerivedColumns({
 *     dataset: dataset,
 *     startsWith: "foo_",
 * });
 * ```
 */
export function getDerivedColumns(args: GetDerivedColumnsArgs, opts?: pulumi.InvokeOptions): Promise<GetDerivedColumnsResult> {

    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invoke("honeycomb:index/getDerivedColumns:GetDerivedColumns", {
        "dataset": args.dataset,
        "startsWith": args.startsWith,
    }, opts);
}

/**
 * A collection of arguments for invoking GetDerivedColumns.
 */
export interface GetDerivedColumnsArgs {
    /**
     * The dataset to retrieve the columns list from. Use `__all__` for Environment-wide derived columns.
     */
    dataset: string;
    /**
     * Only return derived columns starting with the given value.
     */
    startsWith?: string;
}

/**
 * A collection of values returned by GetDerivedColumns.
 */
export interface GetDerivedColumnsResult {
    readonly dataset: string;
    readonly id: string;
    /**
     * a list of all the derived column names found in the dataset
     */
    readonly names: string[];
    readonly startsWith?: string;
}
/**
 * ## # Data Source: honeycomb.GetDerivedColumns
 *
 * The `honeycomb.GetDerivedColumns` data source allows the derived columns of a dataset to be retrieved.
 *
 * ## Example Usage
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as honeycomb from "@pulumi/honeycomb";
 *
 * const config = new pulumi.Config();
 * const dataset = config.require("dataset");
 * const all = honeycomb.GetDerivedColumns({
 *     dataset: dataset,
 * });
 * const foo = honeycomb.GetDerivedColumns({
 *     dataset: dataset,
 *     startsWith: "foo_",
 * });
 * ```
 */
export function getDerivedColumnsOutput(args: GetDerivedColumnsOutputArgs, opts?: pulumi.InvokeOptions): pulumi.Output<GetDerivedColumnsResult> {
    return pulumi.output(args).apply((a: any) => getDerivedColumns(a, opts))
}

/**
 * A collection of arguments for invoking GetDerivedColumns.
 */
export interface GetDerivedColumnsOutputArgs {
    /**
     * The dataset to retrieve the columns list from. Use `__all__` for Environment-wide derived columns.
     */
    dataset: pulumi.Input<string>;
    /**
     * Only return derived columns starting with the given value.
     */
    startsWith?: pulumi.Input<string>;
}
