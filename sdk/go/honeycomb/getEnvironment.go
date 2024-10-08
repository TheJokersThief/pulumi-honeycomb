// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package honeycomb

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
	"github.com/thejokersthief/pulumi-honeycomb/sdk/go/honeycomb/internal"
)

// ## # Data Source: Environment
//
// The `Environment` data source retrieves the details of a single Environment.
// If you want to retrieve multiple Environments, use the `GetEnvironments` data source instead.
//
// > **NOTE** This data source requires the provider be configured with a Management Key with `environments:read` in the configured scopes.
//
// ## Example Usage
//
// ```go
// package main
//
// import (
//
//	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
//	"github.com/thejokersthief/pulumi-honeycomb/sdk/go/honeycomb"
//
// )
//
//	func main() {
//		pulumi.Run(func(ctx *pulumi.Context) error {
//			_, err := honeycomb.GetEnvironment(ctx, &honeycomb.LookupEnvironmentArgs{
//				Id: "hcaen_01j1d7t02zf7wgw7q89z3t60vf",
//			}, nil)
//			if err != nil {
//				return err
//			}
//			return nil
//		})
//	}
//
// ```
func LookupEnvironment(ctx *pulumi.Context, args *LookupEnvironmentArgs, opts ...pulumi.InvokeOption) (*LookupEnvironmentResult, error) {
	opts = internal.PkgInvokeDefaultOpts(opts)
	var rv LookupEnvironmentResult
	err := ctx.Invoke("honeycomb:index/getEnvironment:GetEnvironment", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

// A collection of arguments for invoking GetEnvironment.
type LookupEnvironmentArgs struct {
	// The ID of the Environment
	Id string `pulumi:"id"`
}

// A collection of values returned by GetEnvironment.
type LookupEnvironmentResult struct {
	// the Environment's color.
	Color string `pulumi:"color"`
	// the current state of the Environment's deletion protection status.
	DeleteProtected bool `pulumi:"deleteProtected"`
	// the Environment's description.
	Description string `pulumi:"description"`
	Id          string `pulumi:"id"`
	// the Environment's name.
	Name string `pulumi:"name"`
	// the Environment's slug.
	Slug string `pulumi:"slug"`
}

func LookupEnvironmentOutput(ctx *pulumi.Context, args LookupEnvironmentOutputArgs, opts ...pulumi.InvokeOption) LookupEnvironmentResultOutput {
	return pulumi.ToOutputWithContext(context.Background(), args).
		ApplyT(func(v interface{}) (LookupEnvironmentResult, error) {
			args := v.(LookupEnvironmentArgs)
			r, err := LookupEnvironment(ctx, &args, opts...)
			var s LookupEnvironmentResult
			if r != nil {
				s = *r
			}
			return s, err
		}).(LookupEnvironmentResultOutput)
}

// A collection of arguments for invoking GetEnvironment.
type LookupEnvironmentOutputArgs struct {
	// The ID of the Environment
	Id pulumi.StringInput `pulumi:"id"`
}

func (LookupEnvironmentOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupEnvironmentArgs)(nil)).Elem()
}

// A collection of values returned by GetEnvironment.
type LookupEnvironmentResultOutput struct{ *pulumi.OutputState }

func (LookupEnvironmentResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupEnvironmentResult)(nil)).Elem()
}

func (o LookupEnvironmentResultOutput) ToLookupEnvironmentResultOutput() LookupEnvironmentResultOutput {
	return o
}

func (o LookupEnvironmentResultOutput) ToLookupEnvironmentResultOutputWithContext(ctx context.Context) LookupEnvironmentResultOutput {
	return o
}

// the Environment's color.
func (o LookupEnvironmentResultOutput) Color() pulumi.StringOutput {
	return o.ApplyT(func(v LookupEnvironmentResult) string { return v.Color }).(pulumi.StringOutput)
}

// the current state of the Environment's deletion protection status.
func (o LookupEnvironmentResultOutput) DeleteProtected() pulumi.BoolOutput {
	return o.ApplyT(func(v LookupEnvironmentResult) bool { return v.DeleteProtected }).(pulumi.BoolOutput)
}

// the Environment's description.
func (o LookupEnvironmentResultOutput) Description() pulumi.StringOutput {
	return o.ApplyT(func(v LookupEnvironmentResult) string { return v.Description }).(pulumi.StringOutput)
}

func (o LookupEnvironmentResultOutput) Id() pulumi.StringOutput {
	return o.ApplyT(func(v LookupEnvironmentResult) string { return v.Id }).(pulumi.StringOutput)
}

// the Environment's name.
func (o LookupEnvironmentResultOutput) Name() pulumi.StringOutput {
	return o.ApplyT(func(v LookupEnvironmentResult) string { return v.Name }).(pulumi.StringOutput)
}

// the Environment's slug.
func (o LookupEnvironmentResultOutput) Slug() pulumi.StringOutput {
	return o.ApplyT(func(v LookupEnvironmentResult) string { return v.Slug }).(pulumi.StringOutput)
}

func init() {
	pulumi.RegisterOutputType(LookupEnvironmentResultOutput{})
}
