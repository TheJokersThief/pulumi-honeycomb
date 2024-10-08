// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package honeycomb

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
	"github.com/thejokersthief/pulumi-honeycomb/sdk/go/honeycomb/internal"
)

// ## # Data Source: GetDatasets
//
// The Datasets data source retrieves the Environment's Datasets.
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
//			_, err := honeycomb.GetDatasets(ctx, nil, nil)
//			if err != nil {
//				return err
//			}
//			_, err = honeycomb.GetDatasets(ctx, &honeycomb.GetDatasetsArgs{
//				DetailFilter: honeycomb.GetDatasetsDetailFilter{
//					Name:       "name",
//					ValueRegex: pulumi.StringRef("foo_*"),
//				},
//			}, nil)
//			if err != nil {
//				return err
//			}
//			return nil
//		})
//	}
//
// ```
func GetDatasets(ctx *pulumi.Context, args *GetDatasetsArgs, opts ...pulumi.InvokeOption) (*GetDatasetsResult, error) {
	opts = internal.PkgInvokeDefaultOpts(opts)
	var rv GetDatasetsResult
	err := ctx.Invoke("honeycomb:index/getDatasets:GetDatasets", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

// A collection of arguments for invoking GetDatasets.
type GetDatasetsArgs struct {
	// a block to further filter results as described below. `name` must be set when providing a filter. Conflicts with `startsWith`.
	DetailFilter *GetDatasetsDetailFilter `pulumi:"detailFilter"`
	// Deprecated: use `detailFilter` instead. Only return datasets whose name starts with the given value.
	//
	// Deprecated: Use the `detailFilter` block instead.
	StartsWith *string `pulumi:"startsWith"`
}

// A collection of values returned by GetDatasets.
type GetDatasetsResult struct {
	DetailFilter *GetDatasetsDetailFilter `pulumi:"detailFilter"`
	Id           string                   `pulumi:"id"`
	// a list of all the dataset names.
	Names []string `pulumi:"names"`
	// a list of all the dataset slugs.
	Slugs []string `pulumi:"slugs"`
	// Deprecated: Use the `detailFilter` block instead.
	StartsWith *string `pulumi:"startsWith"`
}

func GetDatasetsOutput(ctx *pulumi.Context, args GetDatasetsOutputArgs, opts ...pulumi.InvokeOption) GetDatasetsResultOutput {
	return pulumi.ToOutputWithContext(context.Background(), args).
		ApplyT(func(v interface{}) (GetDatasetsResult, error) {
			args := v.(GetDatasetsArgs)
			r, err := GetDatasets(ctx, &args, opts...)
			var s GetDatasetsResult
			if r != nil {
				s = *r
			}
			return s, err
		}).(GetDatasetsResultOutput)
}

// A collection of arguments for invoking GetDatasets.
type GetDatasetsOutputArgs struct {
	// a block to further filter results as described below. `name` must be set when providing a filter. Conflicts with `startsWith`.
	DetailFilter GetDatasetsDetailFilterPtrInput `pulumi:"detailFilter"`
	// Deprecated: use `detailFilter` instead. Only return datasets whose name starts with the given value.
	//
	// Deprecated: Use the `detailFilter` block instead.
	StartsWith pulumi.StringPtrInput `pulumi:"startsWith"`
}

func (GetDatasetsOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*GetDatasetsArgs)(nil)).Elem()
}

// A collection of values returned by GetDatasets.
type GetDatasetsResultOutput struct{ *pulumi.OutputState }

func (GetDatasetsResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*GetDatasetsResult)(nil)).Elem()
}

func (o GetDatasetsResultOutput) ToGetDatasetsResultOutput() GetDatasetsResultOutput {
	return o
}

func (o GetDatasetsResultOutput) ToGetDatasetsResultOutputWithContext(ctx context.Context) GetDatasetsResultOutput {
	return o
}

func (o GetDatasetsResultOutput) DetailFilter() GetDatasetsDetailFilterPtrOutput {
	return o.ApplyT(func(v GetDatasetsResult) *GetDatasetsDetailFilter { return v.DetailFilter }).(GetDatasetsDetailFilterPtrOutput)
}

func (o GetDatasetsResultOutput) Id() pulumi.StringOutput {
	return o.ApplyT(func(v GetDatasetsResult) string { return v.Id }).(pulumi.StringOutput)
}

// a list of all the dataset names.
func (o GetDatasetsResultOutput) Names() pulumi.StringArrayOutput {
	return o.ApplyT(func(v GetDatasetsResult) []string { return v.Names }).(pulumi.StringArrayOutput)
}

// a list of all the dataset slugs.
func (o GetDatasetsResultOutput) Slugs() pulumi.StringArrayOutput {
	return o.ApplyT(func(v GetDatasetsResult) []string { return v.Slugs }).(pulumi.StringArrayOutput)
}

// Deprecated: Use the `detailFilter` block instead.
func (o GetDatasetsResultOutput) StartsWith() pulumi.StringPtrOutput {
	return o.ApplyT(func(v GetDatasetsResult) *string { return v.StartsWith }).(pulumi.StringPtrOutput)
}

func init() {
	pulumi.RegisterOutputType(GetDatasetsResultOutput{})
}
