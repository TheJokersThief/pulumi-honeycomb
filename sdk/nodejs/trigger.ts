// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "./types/input";
import * as outputs from "./types/output";
import * as utilities from "./utilities";

/**
 * ## # Resource: honeycomb.Trigger
 *
 * Creates a trigger. For more information about triggers, check out [Alert with Triggers](https://docs.honeycomb.io/working-with-your-data/triggers/).
 *
 * ## Example Usage
 *
 * ### Basic Example
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as honeycomb from "@pulumi/honeycomb";
 * import * as honeycomb from "@thejokersthief/pulumi-honeycomb";
 *
 * const config = new pulumi.Config();
 * const dataset = config.require("dataset");
 * const exampleGetQuerySpecification = honeycomb.GetQuerySpecification({
 *     calculations: [{
 *         op: "AVG",
 *         column: "duration_ms",
 *     }],
 *     filters: [{
 *         column: "trace.parent_id",
 *         op: "does-not-exist",
 *     }],
 *     timeRange: 1800,
 * });
 * const exampleTrigger = new honeycomb.Trigger("exampleTrigger", {
 *     description: "Average duration of all requests for the last 10 minutes.",
 *     queryJson: exampleGetQuerySpecification.then(exampleGetQuerySpecification => exampleGetQuerySpecification.json),
 *     dataset: dataset,
 *     frequency: 600,
 *     alertType: "on_change",
 *     threshold: {
 *         op: ">",
 *         value: 1000,
 *     },
 *     recipients: [
 *         {
 *             type: "email",
 *             target: "hello@example.com",
 *         },
 *         {
 *             type: "marker",
 *             target: "Trigger - requests are slow",
 *         },
 *     ],
 * });
 * ```
 *
 * ## Import
 *
 * Triggers can be imported using a combination of the dataset name and their ID, e.g.
 *
 * ```sh
 * $ pulumi import honeycomb:index/trigger:Trigger my_trigger my-dataset/AeZzSoWws9G
 * ```
 * You can find the ID in the URL bar when visiting the trigger from the UI.
 */
export class Trigger extends pulumi.CustomResource {
    /**
     * Get an existing Trigger resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: TriggerState, opts?: pulumi.CustomResourceOptions): Trigger {
        return new Trigger(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'honeycomb:index/trigger:Trigger';

    /**
     * Returns true if the given object is an instance of Trigger.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is Trigger {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === Trigger.__pulumiType;
    }

    /**
     * The frequency for the alert to trigger. (`onChange` is the default behavior, `onTrue` can also be selected)
     */
    public readonly alertType!: pulumi.Output<string>;
    /**
     * The dataset this trigger is associated with.
     */
    public readonly dataset!: pulumi.Output<string>;
    /**
     * Description of the trigger.
     */
    public readonly description!: pulumi.Output<string>;
    /**
     * The state of the trigger. If true, the trigger will not be run. Defaults to false.
     */
    public readonly disabled!: pulumi.Output<boolean>;
    /**
     * A configuration block (described below) that determines when the trigger is run.
     * When the time is within the scheduled window the trigger will be run at the specified frequency.
     * Outside of the window, the trigger will not be run.
     * If no schedule is specified, the trigger will be run at the specified frequency at all times.
     */
    public readonly evaluationSchedule!: pulumi.Output<outputs.TriggerEvaluationSchedule | undefined>;
    /**
     * The interval (in seconds) in which to check the results of the query’s calculation against the threshold.
     * This value must be divisible by 60, between 60 and 86400 (between 1 minute and 1 day), and not be more than 4 times the query's duration (see note below).
     * Defaults to 900 (15 minutes).
     */
    public readonly frequency!: pulumi.Output<number>;
    /**
     * Name of the trigger.
     */
    public readonly name!: pulumi.Output<string>;
    /**
     * The ID of the Query that the Trigger will execute. Conflicts with `queryJson`.
     */
    public readonly queryId!: pulumi.Output<string | undefined>;
    /**
     * The Query Specfication JSON for the Trigger to execute.
     * Providing the Query Specification as JSON -- as opposed to a Query ID -- enables additional validation during the validate and plan stages.
     * Conflicts with `queryId`.
     */
    public readonly queryJson!: pulumi.Output<string | undefined>;
    /**
     * Zero or more configuration blocks (described below) with the recipients to notify when the trigger fires.
     *
     * One of `queryId` or `queryJson` are required.
     *
     * > **NOTE** The query used in a Trigger must follow a strict subset: the query must contain *exactly one* calcuation and may only contain `calculation`, `filter`, `filterCombination` and `breakdowns` fields.
     * The query's duration cannot be more than four times the trigger frequency (i.e. `duration <= frequency*4`).
     * See [A Caveat on Time](https://docs.honeycomb.io/working-with-your-data/query-specification/#a-caveat-on-time)) for more information on specifying a query's duration.
     * For example: if using the default query `timeRange` of `7200` the lowest `frequency` for a trigger is `1800`.
     */
    public readonly recipients!: pulumi.Output<outputs.TriggerRecipient[] | undefined>;
    /**
     * A configuration block (described below) describing the threshold of the trigger.
     */
    public readonly threshold!: pulumi.Output<outputs.TriggerThreshold | undefined>;

    /**
     * Create a Trigger resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: TriggerArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: TriggerArgs | TriggerState, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (opts.id) {
            const state = argsOrState as TriggerState | undefined;
            resourceInputs["alertType"] = state ? state.alertType : undefined;
            resourceInputs["dataset"] = state ? state.dataset : undefined;
            resourceInputs["description"] = state ? state.description : undefined;
            resourceInputs["disabled"] = state ? state.disabled : undefined;
            resourceInputs["evaluationSchedule"] = state ? state.evaluationSchedule : undefined;
            resourceInputs["frequency"] = state ? state.frequency : undefined;
            resourceInputs["name"] = state ? state.name : undefined;
            resourceInputs["queryId"] = state ? state.queryId : undefined;
            resourceInputs["queryJson"] = state ? state.queryJson : undefined;
            resourceInputs["recipients"] = state ? state.recipients : undefined;
            resourceInputs["threshold"] = state ? state.threshold : undefined;
        } else {
            const args = argsOrState as TriggerArgs | undefined;
            if ((!args || args.dataset === undefined) && !opts.urn) {
                throw new Error("Missing required property 'dataset'");
            }
            resourceInputs["alertType"] = args ? args.alertType : undefined;
            resourceInputs["dataset"] = args ? args.dataset : undefined;
            resourceInputs["description"] = args ? args.description : undefined;
            resourceInputs["disabled"] = args ? args.disabled : undefined;
            resourceInputs["evaluationSchedule"] = args ? args.evaluationSchedule : undefined;
            resourceInputs["frequency"] = args ? args.frequency : undefined;
            resourceInputs["name"] = args ? args.name : undefined;
            resourceInputs["queryId"] = args ? args.queryId : undefined;
            resourceInputs["queryJson"] = args ? args.queryJson : undefined;
            resourceInputs["recipients"] = args ? args.recipients : undefined;
            resourceInputs["threshold"] = args ? args.threshold : undefined;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        super(Trigger.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering Trigger resources.
 */
export interface TriggerState {
    /**
     * The frequency for the alert to trigger. (`onChange` is the default behavior, `onTrue` can also be selected)
     */
    alertType?: pulumi.Input<string>;
    /**
     * The dataset this trigger is associated with.
     */
    dataset?: pulumi.Input<string>;
    /**
     * Description of the trigger.
     */
    description?: pulumi.Input<string>;
    /**
     * The state of the trigger. If true, the trigger will not be run. Defaults to false.
     */
    disabled?: pulumi.Input<boolean>;
    /**
     * A configuration block (described below) that determines when the trigger is run.
     * When the time is within the scheduled window the trigger will be run at the specified frequency.
     * Outside of the window, the trigger will not be run.
     * If no schedule is specified, the trigger will be run at the specified frequency at all times.
     */
    evaluationSchedule?: pulumi.Input<inputs.TriggerEvaluationSchedule>;
    /**
     * The interval (in seconds) in which to check the results of the query’s calculation against the threshold.
     * This value must be divisible by 60, between 60 and 86400 (between 1 minute and 1 day), and not be more than 4 times the query's duration (see note below).
     * Defaults to 900 (15 minutes).
     */
    frequency?: pulumi.Input<number>;
    /**
     * Name of the trigger.
     */
    name?: pulumi.Input<string>;
    /**
     * The ID of the Query that the Trigger will execute. Conflicts with `queryJson`.
     */
    queryId?: pulumi.Input<string>;
    /**
     * The Query Specfication JSON for the Trigger to execute.
     * Providing the Query Specification as JSON -- as opposed to a Query ID -- enables additional validation during the validate and plan stages.
     * Conflicts with `queryId`.
     */
    queryJson?: pulumi.Input<string>;
    /**
     * Zero or more configuration blocks (described below) with the recipients to notify when the trigger fires.
     *
     * One of `queryId` or `queryJson` are required.
     *
     * > **NOTE** The query used in a Trigger must follow a strict subset: the query must contain *exactly one* calcuation and may only contain `calculation`, `filter`, `filterCombination` and `breakdowns` fields.
     * The query's duration cannot be more than four times the trigger frequency (i.e. `duration <= frequency*4`).
     * See [A Caveat on Time](https://docs.honeycomb.io/working-with-your-data/query-specification/#a-caveat-on-time)) for more information on specifying a query's duration.
     * For example: if using the default query `timeRange` of `7200` the lowest `frequency` for a trigger is `1800`.
     */
    recipients?: pulumi.Input<pulumi.Input<inputs.TriggerRecipient>[]>;
    /**
     * A configuration block (described below) describing the threshold of the trigger.
     */
    threshold?: pulumi.Input<inputs.TriggerThreshold>;
}

/**
 * The set of arguments for constructing a Trigger resource.
 */
export interface TriggerArgs {
    /**
     * The frequency for the alert to trigger. (`onChange` is the default behavior, `onTrue` can also be selected)
     */
    alertType?: pulumi.Input<string>;
    /**
     * The dataset this trigger is associated with.
     */
    dataset: pulumi.Input<string>;
    /**
     * Description of the trigger.
     */
    description?: pulumi.Input<string>;
    /**
     * The state of the trigger. If true, the trigger will not be run. Defaults to false.
     */
    disabled?: pulumi.Input<boolean>;
    /**
     * A configuration block (described below) that determines when the trigger is run.
     * When the time is within the scheduled window the trigger will be run at the specified frequency.
     * Outside of the window, the trigger will not be run.
     * If no schedule is specified, the trigger will be run at the specified frequency at all times.
     */
    evaluationSchedule?: pulumi.Input<inputs.TriggerEvaluationSchedule>;
    /**
     * The interval (in seconds) in which to check the results of the query’s calculation against the threshold.
     * This value must be divisible by 60, between 60 and 86400 (between 1 minute and 1 day), and not be more than 4 times the query's duration (see note below).
     * Defaults to 900 (15 minutes).
     */
    frequency?: pulumi.Input<number>;
    /**
     * Name of the trigger.
     */
    name?: pulumi.Input<string>;
    /**
     * The ID of the Query that the Trigger will execute. Conflicts with `queryJson`.
     */
    queryId?: pulumi.Input<string>;
    /**
     * The Query Specfication JSON for the Trigger to execute.
     * Providing the Query Specification as JSON -- as opposed to a Query ID -- enables additional validation during the validate and plan stages.
     * Conflicts with `queryId`.
     */
    queryJson?: pulumi.Input<string>;
    /**
     * Zero or more configuration blocks (described below) with the recipients to notify when the trigger fires.
     *
     * One of `queryId` or `queryJson` are required.
     *
     * > **NOTE** The query used in a Trigger must follow a strict subset: the query must contain *exactly one* calcuation and may only contain `calculation`, `filter`, `filterCombination` and `breakdowns` fields.
     * The query's duration cannot be more than four times the trigger frequency (i.e. `duration <= frequency*4`).
     * See [A Caveat on Time](https://docs.honeycomb.io/working-with-your-data/query-specification/#a-caveat-on-time)) for more information on specifying a query's duration.
     * For example: if using the default query `timeRange` of `7200` the lowest `frequency` for a trigger is `1800`.
     */
    recipients?: pulumi.Input<pulumi.Input<inputs.TriggerRecipient>[]>;
    /**
     * A configuration block (described below) describing the threshold of the trigger.
     */
    threshold?: pulumi.Input<inputs.TriggerThreshold>;
}
