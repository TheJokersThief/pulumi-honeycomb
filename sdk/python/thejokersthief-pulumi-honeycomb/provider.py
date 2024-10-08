# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = ['ProviderArgs', 'Provider']

@pulumi.input_type
class ProviderArgs:
    def __init__(__self__, *,
                 api_key: Optional[pulumi.Input[str]] = None,
                 api_key_id: Optional[pulumi.Input[str]] = None,
                 api_key_secret: Optional[pulumi.Input[str]] = None,
                 api_url: Optional[pulumi.Input[str]] = None,
                 debug: Optional[pulumi.Input[bool]] = None):
        """
        The set of arguments for constructing a Provider resource.
        :param pulumi.Input[str] api_key: The Honeycomb API key to use. It can also be set via the `HONEYCOMB_API_KEY` or `HONEYCOMBIO_APIKEY` environment
               variables.
        :param pulumi.Input[str] api_key_id: The ID portion of the Honeycomb Management API key to use. It can also be set via the `HONEYCOMB_KEY_ID` environment
               variable.
        :param pulumi.Input[str] api_key_secret: The secret portion of the Honeycomb Management API key to use. It can also be set via the `HONEYCOMB_KEY_SECRET`
               environment variable.
        :param pulumi.Input[str] api_url: Override the URL of the Honeycomb API. Defaults to `https://api.honeycomb.io`. It can also be set via the
               `HONEYCOMB_API_ENDPOINT` environment variable.
        :param pulumi.Input[bool] debug: Enable the API client's debug logs. By default, a `TF_LOG` setting of debug or higher will enable this.
        """
        if api_key is not None:
            pulumi.set(__self__, "api_key", api_key)
        if api_key_id is not None:
            pulumi.set(__self__, "api_key_id", api_key_id)
        if api_key_secret is not None:
            pulumi.set(__self__, "api_key_secret", api_key_secret)
        if api_url is not None:
            pulumi.set(__self__, "api_url", api_url)
        if debug is not None:
            pulumi.set(__self__, "debug", debug)

    @property
    @pulumi.getter(name="apiKey")
    def api_key(self) -> Optional[pulumi.Input[str]]:
        """
        The Honeycomb API key to use. It can also be set via the `HONEYCOMB_API_KEY` or `HONEYCOMBIO_APIKEY` environment
        variables.
        """
        return pulumi.get(self, "api_key")

    @api_key.setter
    def api_key(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "api_key", value)

    @property
    @pulumi.getter(name="apiKeyId")
    def api_key_id(self) -> Optional[pulumi.Input[str]]:
        """
        The ID portion of the Honeycomb Management API key to use. It can also be set via the `HONEYCOMB_KEY_ID` environment
        variable.
        """
        return pulumi.get(self, "api_key_id")

    @api_key_id.setter
    def api_key_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "api_key_id", value)

    @property
    @pulumi.getter(name="apiKeySecret")
    def api_key_secret(self) -> Optional[pulumi.Input[str]]:
        """
        The secret portion of the Honeycomb Management API key to use. It can also be set via the `HONEYCOMB_KEY_SECRET`
        environment variable.
        """
        return pulumi.get(self, "api_key_secret")

    @api_key_secret.setter
    def api_key_secret(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "api_key_secret", value)

    @property
    @pulumi.getter(name="apiUrl")
    def api_url(self) -> Optional[pulumi.Input[str]]:
        """
        Override the URL of the Honeycomb API. Defaults to `https://api.honeycomb.io`. It can also be set via the
        `HONEYCOMB_API_ENDPOINT` environment variable.
        """
        return pulumi.get(self, "api_url")

    @api_url.setter
    def api_url(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "api_url", value)

    @property
    @pulumi.getter
    def debug(self) -> Optional[pulumi.Input[bool]]:
        """
        Enable the API client's debug logs. By default, a `TF_LOG` setting of debug or higher will enable this.
        """
        return pulumi.get(self, "debug")

    @debug.setter
    def debug(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "debug", value)


class Provider(pulumi.ProviderResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 api_key: Optional[pulumi.Input[str]] = None,
                 api_key_id: Optional[pulumi.Input[str]] = None,
                 api_key_secret: Optional[pulumi.Input[str]] = None,
                 api_url: Optional[pulumi.Input[str]] = None,
                 debug: Optional[pulumi.Input[bool]] = None,
                 __props__=None):
        """
        The provider type for the honeycombio package. By default, resources use package-wide configuration
        settings, however an explicit `Provider` instance may be created and passed during resource
        construction to achieve fine-grained programmatic control over provider settings. See the
        [documentation](https://www.pulumi.com/docs/reference/programming-model/#providers) for more information.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] api_key: The Honeycomb API key to use. It can also be set via the `HONEYCOMB_API_KEY` or `HONEYCOMBIO_APIKEY` environment
               variables.
        :param pulumi.Input[str] api_key_id: The ID portion of the Honeycomb Management API key to use. It can also be set via the `HONEYCOMB_KEY_ID` environment
               variable.
        :param pulumi.Input[str] api_key_secret: The secret portion of the Honeycomb Management API key to use. It can also be set via the `HONEYCOMB_KEY_SECRET`
               environment variable.
        :param pulumi.Input[str] api_url: Override the URL of the Honeycomb API. Defaults to `https://api.honeycomb.io`. It can also be set via the
               `HONEYCOMB_API_ENDPOINT` environment variable.
        :param pulumi.Input[bool] debug: Enable the API client's debug logs. By default, a `TF_LOG` setting of debug or higher will enable this.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: Optional[ProviderArgs] = None,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        The provider type for the honeycombio package. By default, resources use package-wide configuration
        settings, however an explicit `Provider` instance may be created and passed during resource
        construction to achieve fine-grained programmatic control over provider settings. See the
        [documentation](https://www.pulumi.com/docs/reference/programming-model/#providers) for more information.

        :param str resource_name: The name of the resource.
        :param ProviderArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ProviderArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 api_key: Optional[pulumi.Input[str]] = None,
                 api_key_id: Optional[pulumi.Input[str]] = None,
                 api_key_secret: Optional[pulumi.Input[str]] = None,
                 api_url: Optional[pulumi.Input[str]] = None,
                 debug: Optional[pulumi.Input[bool]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ProviderArgs.__new__(ProviderArgs)

            __props__.__dict__["api_key"] = None if api_key is None else pulumi.Output.secret(api_key)
            __props__.__dict__["api_key_id"] = api_key_id
            __props__.__dict__["api_key_secret"] = None if api_key_secret is None else pulumi.Output.secret(api_key_secret)
            __props__.__dict__["api_url"] = api_url
            __props__.__dict__["debug"] = pulumi.Output.from_input(debug).apply(pulumi.runtime.to_json) if debug is not None else None
        secret_opts = pulumi.ResourceOptions(additional_secret_outputs=["apiKey", "apiKeySecret"])
        opts = pulumi.ResourceOptions.merge(opts, secret_opts)
        super(Provider, __self__).__init__(
            'honeycomb',
            resource_name,
            __props__,
            opts)

    @property
    @pulumi.getter(name="apiKey")
    def api_key(self) -> pulumi.Output[Optional[str]]:
        """
        The Honeycomb API key to use. It can also be set via the `HONEYCOMB_API_KEY` or `HONEYCOMBIO_APIKEY` environment
        variables.
        """
        return pulumi.get(self, "api_key")

    @property
    @pulumi.getter(name="apiKeyId")
    def api_key_id(self) -> pulumi.Output[Optional[str]]:
        """
        The ID portion of the Honeycomb Management API key to use. It can also be set via the `HONEYCOMB_KEY_ID` environment
        variable.
        """
        return pulumi.get(self, "api_key_id")

    @property
    @pulumi.getter(name="apiKeySecret")
    def api_key_secret(self) -> pulumi.Output[Optional[str]]:
        """
        The secret portion of the Honeycomb Management API key to use. It can also be set via the `HONEYCOMB_KEY_SECRET`
        environment variable.
        """
        return pulumi.get(self, "api_key_secret")

    @property
    @pulumi.getter(name="apiUrl")
    def api_url(self) -> pulumi.Output[Optional[str]]:
        """
        Override the URL of the Honeycomb API. Defaults to `https://api.honeycomb.io`. It can also be set via the
        `HONEYCOMB_API_ENDPOINT` environment variable.
        """
        return pulumi.get(self, "api_url")

