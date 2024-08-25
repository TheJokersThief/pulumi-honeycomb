// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package honeycomb

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
	"github.com/thejokersthief/pulumi-honeycomb/sdk/go/honeycomb/internal"
)

// The provider type for the honeycombio package. By default, resources use package-wide configuration
// settings, however an explicit `Provider` instance may be created and passed during resource
// construction to achieve fine-grained programmatic control over provider settings. See the
// [documentation](https://www.pulumi.com/docs/reference/programming-model/#providers) for more information.
type Provider struct {
	pulumi.ProviderResourceState

	// The Honeycomb API key to use. It can also be set via the `HONEYCOMB_API_KEY` or `HONEYCOMBIO_APIKEY` environment
	// variables.
	ApiKey pulumi.StringPtrOutput `pulumi:"apiKey"`
	// The ID portion of the Honeycomb Management API key to use. It can also be set via the `HONEYCOMB_KEY_ID` environment
	// variable.
	ApiKeyId pulumi.StringPtrOutput `pulumi:"apiKeyId"`
	// The secret portion of the Honeycomb Management API key to use. It can also be set via the `HONEYCOMB_KEY_SECRET`
	// environment variable.
	ApiKeySecret pulumi.StringPtrOutput `pulumi:"apiKeySecret"`
	// Override the URL of the Honeycomb API. Defaults to `https://api.honeycomb.io`. It can also be set via the
	// `HONEYCOMB_API_ENDPOINT` environment variable.
	ApiUrl pulumi.StringPtrOutput `pulumi:"apiUrl"`
}

// NewProvider registers a new resource with the given unique name, arguments, and options.
func NewProvider(ctx *pulumi.Context,
	name string, args *ProviderArgs, opts ...pulumi.ResourceOption) (*Provider, error) {
	if args == nil {
		args = &ProviderArgs{}
	}

	if args.ApiKey != nil {
		args.ApiKey = pulumi.ToSecret(args.ApiKey).(pulumi.StringPtrInput)
	}
	if args.ApiKeySecret != nil {
		args.ApiKeySecret = pulumi.ToSecret(args.ApiKeySecret).(pulumi.StringPtrInput)
	}
	secrets := pulumi.AdditionalSecretOutputs([]string{
		"apiKey",
		"apiKeySecret",
	})
	opts = append(opts, secrets)
	opts = internal.PkgResourceDefaultOpts(opts)
	var resource Provider
	err := ctx.RegisterResource("pulumi:providers:honeycomb", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

type providerArgs struct {
	// The Honeycomb API key to use. It can also be set via the `HONEYCOMB_API_KEY` or `HONEYCOMBIO_APIKEY` environment
	// variables.
	ApiKey *string `pulumi:"apiKey"`
	// The ID portion of the Honeycomb Management API key to use. It can also be set via the `HONEYCOMB_KEY_ID` environment
	// variable.
	ApiKeyId *string `pulumi:"apiKeyId"`
	// The secret portion of the Honeycomb Management API key to use. It can also be set via the `HONEYCOMB_KEY_SECRET`
	// environment variable.
	ApiKeySecret *string `pulumi:"apiKeySecret"`
	// Override the URL of the Honeycomb API. Defaults to `https://api.honeycomb.io`. It can also be set via the
	// `HONEYCOMB_API_ENDPOINT` environment variable.
	ApiUrl *string `pulumi:"apiUrl"`
	// Enable the API client's debug logs. By default, a `TF_LOG` setting of debug or higher will enable this.
	Debug *bool `pulumi:"debug"`
}

// The set of arguments for constructing a Provider resource.
type ProviderArgs struct {
	// The Honeycomb API key to use. It can also be set via the `HONEYCOMB_API_KEY` or `HONEYCOMBIO_APIKEY` environment
	// variables.
	ApiKey pulumi.StringPtrInput
	// The ID portion of the Honeycomb Management API key to use. It can also be set via the `HONEYCOMB_KEY_ID` environment
	// variable.
	ApiKeyId pulumi.StringPtrInput
	// The secret portion of the Honeycomb Management API key to use. It can also be set via the `HONEYCOMB_KEY_SECRET`
	// environment variable.
	ApiKeySecret pulumi.StringPtrInput
	// Override the URL of the Honeycomb API. Defaults to `https://api.honeycomb.io`. It can also be set via the
	// `HONEYCOMB_API_ENDPOINT` environment variable.
	ApiUrl pulumi.StringPtrInput
	// Enable the API client's debug logs. By default, a `TF_LOG` setting of debug or higher will enable this.
	Debug pulumi.BoolPtrInput
}

func (ProviderArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*providerArgs)(nil)).Elem()
}

type ProviderInput interface {
	pulumi.Input

	ToProviderOutput() ProviderOutput
	ToProviderOutputWithContext(ctx context.Context) ProviderOutput
}

func (*Provider) ElementType() reflect.Type {
	return reflect.TypeOf((**Provider)(nil)).Elem()
}

func (i *Provider) ToProviderOutput() ProviderOutput {
	return i.ToProviderOutputWithContext(context.Background())
}

func (i *Provider) ToProviderOutputWithContext(ctx context.Context) ProviderOutput {
	return pulumi.ToOutputWithContext(ctx, i).(ProviderOutput)
}

type ProviderOutput struct{ *pulumi.OutputState }

func (ProviderOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**Provider)(nil)).Elem()
}

func (o ProviderOutput) ToProviderOutput() ProviderOutput {
	return o
}

func (o ProviderOutput) ToProviderOutputWithContext(ctx context.Context) ProviderOutput {
	return o
}

// The Honeycomb API key to use. It can also be set via the `HONEYCOMB_API_KEY` or `HONEYCOMBIO_APIKEY` environment
// variables.
func (o ProviderOutput) ApiKey() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *Provider) pulumi.StringPtrOutput { return v.ApiKey }).(pulumi.StringPtrOutput)
}

// The ID portion of the Honeycomb Management API key to use. It can also be set via the `HONEYCOMB_KEY_ID` environment
// variable.
func (o ProviderOutput) ApiKeyId() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *Provider) pulumi.StringPtrOutput { return v.ApiKeyId }).(pulumi.StringPtrOutput)
}

// The secret portion of the Honeycomb Management API key to use. It can also be set via the `HONEYCOMB_KEY_SECRET`
// environment variable.
func (o ProviderOutput) ApiKeySecret() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *Provider) pulumi.StringPtrOutput { return v.ApiKeySecret }).(pulumi.StringPtrOutput)
}

// Override the URL of the Honeycomb API. Defaults to `https://api.honeycomb.io`. It can also be set via the
// `HONEYCOMB_API_ENDPOINT` environment variable.
func (o ProviderOutput) ApiUrl() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *Provider) pulumi.StringPtrOutput { return v.ApiUrl }).(pulumi.StringPtrOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*ProviderInput)(nil)).Elem(), &Provider{})
	pulumi.RegisterOutputType(ProviderOutput{})
}
