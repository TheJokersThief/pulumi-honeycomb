// Copyright 2016-2024, Pulumi Corporation.
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//     http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.

package honeycomb

import (
	"path"

	// Allow embedding bridge-metadata.json in the provider.
	_ "embed"

	pfbridge "github.com/pulumi/pulumi-terraform-bridge/pf/tfbridge"
	"github.com/pulumi/pulumi-terraform-bridge/v3/pkg/tfbridge"
	"github.com/pulumi/pulumi-terraform-bridge/v3/pkg/tfbridge/tokens"

	// Replace this provider with the provider you are bridging.
	honeycomb "github.com/honeycombio/terraform-provider-honeycombio/shim"

	"github.com/thejokersthief/pulumi-honeycomb/provider/pkg/version"
)

// all of the token components used below.
const (
	// This variable controls the default name of the package in the package
	// registries for nodejs and python:
	mainPkg = "honeycomb"
	// modules:
	mainMod = "index" // the honeycomb module
)

//go:embed cmd/pulumi-resource-honeycomb/bridge-metadata.json
var metadata []byte

// Provider returns additional overlaid schema and metadata associated with the provider.
func Provider() tfbridge.ProviderInfo {
	// Create a Pulumi provider mapping
	prov := tfbridge.ProviderInfo{
		// Instantiate the Terraform provider
		//
		// The [pulumi-terraform-bridge](https://github.com/pulumi/pulumi-terraform-bridge) supports 3
		// types of Terraform providers:
		//
		// 1. Providers written with the terraform-plugin-sdk/v1:
		//
		//    If the provider you are bridging is written with the terraform-plugin-sdk/v1, then you
		//    will need to adapt the boilerplate:
		//
		//    - Change the import "shimv2" to "shimv1" and change the associated import to
		//      "github.com/pulumi/pulumi-terraform-bridge/v3/pkg/tfshim/sdk-v1".
		//
		//    You can then proceed as normal.
		//
		// 2. Providers written with terraform-plugin-sdk/v2:
		//
		//    This boilerplate is already geared towards providers written with the
		//    terraform-plugin-sdk/v2, since it is the most common provider framework used. No
		//    adaptions are needed.
		//
		// 3. Providers written with terraform-plugin-framework:
		//
		//    If the provider you are bridging is written with the terraform-plugin-framework, then
		//    you will need to adapt the boilerplate:
		//
		//    - Remove the `shimv2` import and add:
		//
		//      	pfbridge "github.com/pulumi/pulumi-terraform-bridge/pf/tfbridge"
		//
		//    - Replace `shimv2.NewProvider` with `pfbridge.ShimProvider`.
		//
		//    - In provider/cmd/pulumi-tfgen-honeycomb/main.go, replace the
		//      "github.com/pulumi/pulumi-terraform-bridge/v3/pkg/tfgen" import with
		//      "github.com/pulumi/pulumi-terraform-bridge/pf/tfgen". Remove the `version.Version`
		//      argument to `tfgen.Main`.
		//
		//    - In provider/cmd/pulumi-resource-honeycomb/main.go, replace the
		//      "github.com/pulumi/pulumi-terraform-bridge/v3/pkg/tfbridge" import with
		//      "github.com/pulumi/pulumi-terraform-bridge/pf/tfbridge". Replace the arguments to the
		//      `tfbridge.Main` so it looks like this:
		//
		//      	tfbridge.Main(context.Background(), "honeycomb", honeycomb.Provider(),
		//			tfbridge.ProviderMetadata{PulumiSchema: pulumiSchema})
		//
		//   Detailed instructions can be found at
		//   https://github.com/pulumi/pulumi-terraform-bridge/blob/master/pf/README.md#how-to-upgrade-a-bridged-provider-to-plugin-framework.
		//   After that, you can proceed as normal.
		//
		// This is where you give the bridge a handle to the upstream terraform provider. SDKv2
		// convention is to have a function at "github.com/iwahbe/terraform-provider-honeycomb/provider".New
		// which takes a version and produces a factory function. The provider you are bridging may
		// not do that. You will need to find the function (generally called in upstream's main.go)
		// that produces a:
		//
		// - *"github.com/hashicorp/terraform-plugin-sdk/v2/helper/schema".Provider (for SDKv2)
		// - *"github.com/hashicorp/terraform-plugin-sdk/v1/helper/schema".Provider (for SDKv1)
		// - "github.com/hashicorp/terraform-plugin-framework/provider".Provider (for plugin-framework)
		//
		//nolint:lll
		P: pfbridge.ShimProvider(honeycomb.Provider()),

		Name:    "honeycombio",
		Version: version.Version,
		// DisplayName is a way to be able to change the casing of the provider name when being
		// displayed on the Pulumi registry
		DisplayName: "Honeycomb",
		// Change this to your personal name (or a company name) that you would like to be shown in
		// the Pulumi Registry if this package is published there.
		Publisher: "thejokersthief",
		// LogoURL is optional but useful to help identify your package in the Pulumi Registry
		// if this package is published there.
		//
		// You may host a logo on a domain you control or add an SVG logo for your package
		// in your repository and use the raw content URL for that file as your logo URL.
		LogoURL: "",
		// PluginDownloadURL is an optional URL used to download the Provider
		// for use in Pulumi programs
		// e.g https://github.com/org/pulumi-provider-name/releases/
		PluginDownloadURL: "",
		Description:       "A Pulumi package for creating and managing honeycomb cloud resources.",
		// category/cloud tag helps with categorizing the package in the Pulumi Registry.
		// For all available categories, see `Keywords` in
		// https://www.pulumi.com/docs/guides/pulumi-packages/schema/#package.
		Keywords:   []string{"thejokersthief", "honeycomb", "category/cloud"},
		License:    "Apache-2.0",
		Homepage:   "https://www.pulumi.com",
		Repository: "https://github.com/thejokersthief/pulumi-honeycomb",
		// The GitHub Org for the provider - defaults to `terraform-providers`. Note that this should
		// match the TF provider module's require directive, not any replace directives.
		GitHubOrg:    "honeycombio",
		MetadataInfo: tfbridge.NewProviderMetadata(metadata),
		Config:       map[string]*tfbridge.SchemaInfo{
			// Add any required configuration here, or remove the example below if
			// no additional points are required.
			// "region": {
			// 	Type: tfbridge.MakeType("region", "Region"),
			// 	Default: &tfbridge.DefaultInfo{
			// 		EnvVars: []string{"AWS_REGION", "AWS_DEFAULT_REGION"},
			// 	},
			// },
		},
		JavaScript: &tfbridge.JavaScriptInfo{
			PackageName: "@thejokersthief/pulumi-honeycomb",
			// List any npm dependencies and their versions
			Dependencies: map[string]string{
				"@pulumi/pulumi": "^3.0.0",
			},
			DevDependencies: map[string]string{
				"@types/node": "^10.0.0", // so we can access strongly typed node definitions.
				"@types/mime": "^2.0.0",
			},
		},
		Python: &tfbridge.PythonInfo{
			PackageName: "thejokersthief-pulumi-honeycomb",
			// List any Python dependencies and their version ranges
			Requires: map[string]string{
				"pulumi": ">=3.0.0,<4.0.0",
			},
		},
		Golang: &tfbridge.GolangInfo{
			ImportBasePath: path.Join(
				"github.com/thejokersthief/pulumi-honeycomb/sdk/",
				tfbridge.GetModuleMajorVersion(version.Version),
				"go",
				mainPkg,
			),
			GenerateResourceContainerTypes: true,
		},
		CSharp: &tfbridge.CSharpInfo{
			PackageReferences: map[string]string{
				"Pulumi": "3.*",
			},
		},

		Resources: map[string]*tfbridge.ResourceInfo{
			// "honeycombio_board":               {Tok: tfbridge.MakeResource(mainPkg, mainMod, "Board")},
			// "honeycombio_column":             {Tok: tfbridge.MakeResource(mainPkg, mainMod, "Column")},
			"honeycombio_dataset": {Tok: tfbridge.MakeResource(mainPkg, mainMod, "Dataset")},
			// "honeycombio_dataset_definition": {Tok: tfbridge.MakeResource(mainPkg, mainMod, "DatasetDefinition")},
			// "honeycombio_derived_column":      {Tok: tfbridge.MakeResource(mainPkg, mainMod, "DerivedColumn")},
			// "honeycombio_email_recipient":     {Tok: tfbridge.MakeResource(mainPkg, mainMod, "EmailRecipient")},
			// "honeycombio_marker":              {Tok: tfbridge.MakeResource(mainPkg, mainMod, "Marker")},
			// "honeycombio_marker_setting":      {Tok: tfbridge.MakeResource(mainPkg, mainMod, "MarkerSetting")},
			// "honeycombio_pagerduty_recipient": {Tok: tfbridge.MakeResource(mainPkg, mainMod, "PagerDutyRecipient")},
			"honeycombio_query": {Tok: tfbridge.MakeResource(mainPkg, mainMod, "Query")},
			// "honeycombio_query_annotation":    {Tok: tfbridge.MakeResource(mainPkg, mainMod, "QueryAnnotation")},
			// "honeycombio_slack_recipient":     {Tok: tfbridge.MakeResource(mainPkg, mainMod, "SlackRecipient")},
			// "honeycombio_slo":                 {Tok: tfbridge.MakeResource(mainPkg, mainMod, "SLO")},
			// "honeycombio_webhook_recipient":   {Tok: tfbridge.MakeResource(mainPkg, mainMod, "WebhookRecipient")},
			"honeycombio_trigger":     {Tok: tfbridge.MakeResource(mainPkg, mainMod, "Trigger")},
			"honeycombio_burn_alert":  {Tok: tfbridge.MakeResource(mainPkg, mainMod, "BurnAlert")},
			"honeycombio_api_key":     {Tok: tfbridge.MakeResource(mainPkg, mainMod, "ApiKey")},
			"honeycombio_environment": {Tok: tfbridge.MakeResource(mainPkg, mainMod, "Environment")},
		},
		DataSources: map[string]*tfbridge.DataSourceInfo{
			"honeycombio_column":              {Tok: tfbridge.MakeDataSource(mainPkg, mainMod, "GetColumn")},
			"honeycombio_columns":             {Tok: tfbridge.MakeDataSource(mainPkg, mainMod, "GetColumns")},
			"honeycombio_datasets":            {Tok: tfbridge.MakeDataSource(mainPkg, mainMod, "GetDatasets")},
			"honeycombio_query_result":        {Tok: tfbridge.MakeDataSource(mainPkg, mainMod, "GetQueryResult")},
			"honeycombio_query_specification": {Tok: tfbridge.MakeDataSource(mainPkg, mainMod, "GetQuerySpecification")},
			"honeycombio_recipient":           {Tok: tfbridge.MakeDataSource(mainPkg, mainMod, "GetRecipient")},
			"honeycombio_recipients":          {Tok: tfbridge.MakeDataSource(mainPkg, mainMod, "GetRecipients")},
			"honeycombio_trigger_recipient":   {Tok: tfbridge.MakeDataSource(mainPkg, mainMod, "GetTriggerRecipient")},
			"honeycombio_auth_metadata":       {Tok: tfbridge.MakeDataSource(mainPkg, mainMod, "GetAuthMetadata")},
			"honeycombio_dataset":             {Tok: tfbridge.MakeDataSource(mainPkg, mainMod, "GetDataset")},
			"honeycombio_derived_column":      {Tok: tfbridge.MakeDataSource(mainPkg, mainMod, "GetDerivedColumn")},
			"honeycombio_derived_columns":     {Tok: tfbridge.MakeDataSource(mainPkg, mainMod, "GetDerivedColumns")},
			"honeycombio_environment":         {Tok: tfbridge.MakeDataSource(mainPkg, mainMod, "GetEnvironment")},
			"honeycombio_environments":        {Tok: tfbridge.MakeDataSource(mainPkg, mainMod, "GetEnvironments")},
			"honeycombio_slo":                 {Tok: tfbridge.MakeDataSource(mainPkg, mainMod, "GetSLO")},
			"honeycombio_slos":                {Tok: tfbridge.MakeDataSource(mainPkg, mainMod, "GetSLOs")},
		},
	}

	// MustComputeTokens maps all resources and datasources from the upstream provider into Pulumi.
	//
	// tokens.SingleModule puts every upstream item into your provider's main module.
	//
	// You shouldn't need to override anything, but if you do, use the [tfbridge.ProviderInfo.Resources]
	// and [tfbridge.ProviderInfo.DataSources].
	prov.MustComputeTokens(tokens.SingleModule("honeycomb_", mainMod,
		tokens.MakeStandard(mainPkg)))

	prov.MustApplyAutoAliases()
	prov.SetAutonaming(255, "-")

	return prov
}
