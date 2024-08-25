package shim

import (
	tfprovider "github.com/hashicorp/terraform-plugin-framework/provider"
	"github.com/honeycombio/terraform-provider-honeycombio/internal/provider"
)

// fix provider.Provider here to match whats in internal/provider
func Provider() tfprovider.Provider {
	return provider.New("dev")
}
