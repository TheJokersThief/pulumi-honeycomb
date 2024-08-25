// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "./utilities";

/**
 * ## # Resource: honeycomb.Column
 *
 * Provides a Honeycomb Column resource.
 * This can be used to create, update, and delete columns in a dataset.
 *
 * > **Note**: deleting a column is a destructive and irreversible operation which also removes the data in the column.
 *
 * > **Note**: prior to version 0.13.0 of the provider, columns were *not* deleted on destroy but left in place and only removed from state.
 *
 * ## Example Usage
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as honeycomb from "@pulumi/honeycomb";
 *
 * const config = new pulumi.Config();
 * const dataset = config.require("dataset");
 * const durationMs = new honeycomb.Column("durationMs", {
 *     type: "float",
 *     description: "Duration of the trace",
 *     dataset: dataset,
 * });
 * ```
 *
 * ## Import
 *
 * Columns can be imported using a combination of the dataset name and their name, e.g.
 *
 * ```sh
 * $ pulumi import honeycomb:index/column:Column my_column my-dataset/duration_ms
 * ```
 */
export class Column extends pulumi.CustomResource {
    /**
     * Get an existing Column resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: ColumnState, opts?: pulumi.CustomResourceOptions): Column {
        return new Column(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'honeycomb:index/column:Column';

    /**
     * Returns true if the given object is an instance of Column.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is Column {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === Column.__pulumiType;
    }

    /**
     * ISO8601 formatted time the column was created
     */
    public /*out*/ readonly createdAt!: pulumi.Output<string>;
    /**
     * The dataset this column is added to.
     */
    public readonly dataset!: pulumi.Output<string>;
    /**
     * A description that is shown in the UI.
     */
    public readonly description!: pulumi.Output<string | undefined>;
    /**
     * Whether this column should be hidden in the query builder and sample data. Defaults to false.
     */
    public readonly hidden!: pulumi.Output<boolean | undefined>;
    /**
     * Please use `name` instead. The name of the column. Must be unique per dataset. Conficts with `name`.
     *
     * @deprecated Please set `name` instead.
     */
    public readonly keyName!: pulumi.Output<string>;
    /**
     * ISO8601 formatted time the column was last written to (received event data)
     */
    public /*out*/ readonly lastWrittenAt!: pulumi.Output<string>;
    /**
     * The name of the column. Must be unique per dataset.
     */
    public readonly name!: pulumi.Output<string>;
    /**
     * The type of the column, allowed values are `string`, `float`, `integer` and `boolean`. Defaults to `string`.
     */
    public readonly type!: pulumi.Output<string | undefined>;
    /**
     * ISO8601 formatted time the column was updated
     */
    public /*out*/ readonly updatedAt!: pulumi.Output<string>;

    /**
     * Create a Column resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: ColumnArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: ColumnArgs | ColumnState, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (opts.id) {
            const state = argsOrState as ColumnState | undefined;
            resourceInputs["createdAt"] = state ? state.createdAt : undefined;
            resourceInputs["dataset"] = state ? state.dataset : undefined;
            resourceInputs["description"] = state ? state.description : undefined;
            resourceInputs["hidden"] = state ? state.hidden : undefined;
            resourceInputs["keyName"] = state ? state.keyName : undefined;
            resourceInputs["lastWrittenAt"] = state ? state.lastWrittenAt : undefined;
            resourceInputs["name"] = state ? state.name : undefined;
            resourceInputs["type"] = state ? state.type : undefined;
            resourceInputs["updatedAt"] = state ? state.updatedAt : undefined;
        } else {
            const args = argsOrState as ColumnArgs | undefined;
            if ((!args || args.dataset === undefined) && !opts.urn) {
                throw new Error("Missing required property 'dataset'");
            }
            resourceInputs["dataset"] = args ? args.dataset : undefined;
            resourceInputs["description"] = args ? args.description : undefined;
            resourceInputs["hidden"] = args ? args.hidden : undefined;
            resourceInputs["keyName"] = args ? args.keyName : undefined;
            resourceInputs["name"] = args ? args.name : undefined;
            resourceInputs["type"] = args ? args.type : undefined;
            resourceInputs["createdAt"] = undefined /*out*/;
            resourceInputs["lastWrittenAt"] = undefined /*out*/;
            resourceInputs["updatedAt"] = undefined /*out*/;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        super(Column.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering Column resources.
 */
export interface ColumnState {
    /**
     * ISO8601 formatted time the column was created
     */
    createdAt?: pulumi.Input<string>;
    /**
     * The dataset this column is added to.
     */
    dataset?: pulumi.Input<string>;
    /**
     * A description that is shown in the UI.
     */
    description?: pulumi.Input<string>;
    /**
     * Whether this column should be hidden in the query builder and sample data. Defaults to false.
     */
    hidden?: pulumi.Input<boolean>;
    /**
     * Please use `name` instead. The name of the column. Must be unique per dataset. Conficts with `name`.
     *
     * @deprecated Please set `name` instead.
     */
    keyName?: pulumi.Input<string>;
    /**
     * ISO8601 formatted time the column was last written to (received event data)
     */
    lastWrittenAt?: pulumi.Input<string>;
    /**
     * The name of the column. Must be unique per dataset.
     */
    name?: pulumi.Input<string>;
    /**
     * The type of the column, allowed values are `string`, `float`, `integer` and `boolean`. Defaults to `string`.
     */
    type?: pulumi.Input<string>;
    /**
     * ISO8601 formatted time the column was updated
     */
    updatedAt?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a Column resource.
 */
export interface ColumnArgs {
    /**
     * The dataset this column is added to.
     */
    dataset: pulumi.Input<string>;
    /**
     * A description that is shown in the UI.
     */
    description?: pulumi.Input<string>;
    /**
     * Whether this column should be hidden in the query builder and sample data. Defaults to false.
     */
    hidden?: pulumi.Input<boolean>;
    /**
     * Please use `name` instead. The name of the column. Must be unique per dataset. Conficts with `name`.
     *
     * @deprecated Please set `name` instead.
     */
    keyName?: pulumi.Input<string>;
    /**
     * The name of the column. Must be unique per dataset.
     */
    name?: pulumi.Input<string>;
    /**
     * The type of the column, allowed values are `string`, `float`, `integer` and `boolean`. Defaults to `string`.
     */
    type?: pulumi.Input<string>;
}
