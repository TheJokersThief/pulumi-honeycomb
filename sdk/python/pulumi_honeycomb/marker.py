# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = ['MarkerArgs', 'Marker']

@pulumi.input_type
class MarkerArgs:
    def __init__(__self__, *,
                 dataset: pulumi.Input[str],
                 message: Optional[pulumi.Input[str]] = None,
                 type: Optional[pulumi.Input[str]] = None,
                 url: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a Marker resource.
        :param pulumi.Input[str] dataset: The dataset this marker is placed on. Use `__all__` for Environment-wide markers.
        :param pulumi.Input[str] message: The message on the marker.
        :param pulumi.Input[str] type: The type of the marker, Honeycomb.io can display markers in different colors depending on their type.
        :param pulumi.Input[str] url: A target for the Marker. If you click on the Marker text, it will take you to this URL.
        """
        pulumi.set(__self__, "dataset", dataset)
        if message is not None:
            pulumi.set(__self__, "message", message)
        if type is not None:
            pulumi.set(__self__, "type", type)
        if url is not None:
            pulumi.set(__self__, "url", url)

    @property
    @pulumi.getter
    def dataset(self) -> pulumi.Input[str]:
        """
        The dataset this marker is placed on. Use `__all__` for Environment-wide markers.
        """
        return pulumi.get(self, "dataset")

    @dataset.setter
    def dataset(self, value: pulumi.Input[str]):
        pulumi.set(self, "dataset", value)

    @property
    @pulumi.getter
    def message(self) -> Optional[pulumi.Input[str]]:
        """
        The message on the marker.
        """
        return pulumi.get(self, "message")

    @message.setter
    def message(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "message", value)

    @property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[str]]:
        """
        The type of the marker, Honeycomb.io can display markers in different colors depending on their type.
        """
        return pulumi.get(self, "type")

    @type.setter
    def type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "type", value)

    @property
    @pulumi.getter
    def url(self) -> Optional[pulumi.Input[str]]:
        """
        A target for the Marker. If you click on the Marker text, it will take you to this URL.
        """
        return pulumi.get(self, "url")

    @url.setter
    def url(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "url", value)


@pulumi.input_type
class _MarkerState:
    def __init__(__self__, *,
                 dataset: Optional[pulumi.Input[str]] = None,
                 message: Optional[pulumi.Input[str]] = None,
                 type: Optional[pulumi.Input[str]] = None,
                 url: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering Marker resources.
        :param pulumi.Input[str] dataset: The dataset this marker is placed on. Use `__all__` for Environment-wide markers.
        :param pulumi.Input[str] message: The message on the marker.
        :param pulumi.Input[str] type: The type of the marker, Honeycomb.io can display markers in different colors depending on their type.
        :param pulumi.Input[str] url: A target for the Marker. If you click on the Marker text, it will take you to this URL.
        """
        if dataset is not None:
            pulumi.set(__self__, "dataset", dataset)
        if message is not None:
            pulumi.set(__self__, "message", message)
        if type is not None:
            pulumi.set(__self__, "type", type)
        if url is not None:
            pulumi.set(__self__, "url", url)

    @property
    @pulumi.getter
    def dataset(self) -> Optional[pulumi.Input[str]]:
        """
        The dataset this marker is placed on. Use `__all__` for Environment-wide markers.
        """
        return pulumi.get(self, "dataset")

    @dataset.setter
    def dataset(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "dataset", value)

    @property
    @pulumi.getter
    def message(self) -> Optional[pulumi.Input[str]]:
        """
        The message on the marker.
        """
        return pulumi.get(self, "message")

    @message.setter
    def message(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "message", value)

    @property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[str]]:
        """
        The type of the marker, Honeycomb.io can display markers in different colors depending on their type.
        """
        return pulumi.get(self, "type")

    @type.setter
    def type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "type", value)

    @property
    @pulumi.getter
    def url(self) -> Optional[pulumi.Input[str]]:
        """
        A target for the Marker. If you click on the Marker text, it will take you to this URL.
        """
        return pulumi.get(self, "url")

    @url.setter
    def url(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "url", value)


class Marker(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 dataset: Optional[pulumi.Input[str]] = None,
                 message: Optional[pulumi.Input[str]] = None,
                 type: Optional[pulumi.Input[str]] = None,
                 url: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        ## # Resource: Marker

        Creates a marker. For more information about markers, check out [Annotate the timeline with Markers](https://docs.honeycomb.io/working-with-your-data/customizing-your-query/markers/).

        > **Note** Destroying or replacing this resource will not delete the previously created marker. This is intentional to preserve the markers. At this time, it is not possible to remove markers using this provider.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_honeycomb as honeycomb

        config = pulumi.Config()
        dataset = config.require("dataset")
        app_version = config.require("appVersion")
        marker = honeycomb.Marker("marker",
            message=f"deploy {app_version}",
            type="deploy",
            url="http://www.example.com/",
            dataset=dataset)
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] dataset: The dataset this marker is placed on. Use `__all__` for Environment-wide markers.
        :param pulumi.Input[str] message: The message on the marker.
        :param pulumi.Input[str] type: The type of the marker, Honeycomb.io can display markers in different colors depending on their type.
        :param pulumi.Input[str] url: A target for the Marker. If you click on the Marker text, it will take you to this URL.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: MarkerArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        ## # Resource: Marker

        Creates a marker. For more information about markers, check out [Annotate the timeline with Markers](https://docs.honeycomb.io/working-with-your-data/customizing-your-query/markers/).

        > **Note** Destroying or replacing this resource will not delete the previously created marker. This is intentional to preserve the markers. At this time, it is not possible to remove markers using this provider.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_honeycomb as honeycomb

        config = pulumi.Config()
        dataset = config.require("dataset")
        app_version = config.require("appVersion")
        marker = honeycomb.Marker("marker",
            message=f"deploy {app_version}",
            type="deploy",
            url="http://www.example.com/",
            dataset=dataset)
        ```

        :param str resource_name: The name of the resource.
        :param MarkerArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(MarkerArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 dataset: Optional[pulumi.Input[str]] = None,
                 message: Optional[pulumi.Input[str]] = None,
                 type: Optional[pulumi.Input[str]] = None,
                 url: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = MarkerArgs.__new__(MarkerArgs)

            if dataset is None and not opts.urn:
                raise TypeError("Missing required property 'dataset'")
            __props__.__dict__["dataset"] = dataset
            __props__.__dict__["message"] = message
            __props__.__dict__["type"] = type
            __props__.__dict__["url"] = url
        super(Marker, __self__).__init__(
            'honeycomb:index/marker:Marker',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            dataset: Optional[pulumi.Input[str]] = None,
            message: Optional[pulumi.Input[str]] = None,
            type: Optional[pulumi.Input[str]] = None,
            url: Optional[pulumi.Input[str]] = None) -> 'Marker':
        """
        Get an existing Marker resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] dataset: The dataset this marker is placed on. Use `__all__` for Environment-wide markers.
        :param pulumi.Input[str] message: The message on the marker.
        :param pulumi.Input[str] type: The type of the marker, Honeycomb.io can display markers in different colors depending on their type.
        :param pulumi.Input[str] url: A target for the Marker. If you click on the Marker text, it will take you to this URL.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _MarkerState.__new__(_MarkerState)

        __props__.__dict__["dataset"] = dataset
        __props__.__dict__["message"] = message
        __props__.__dict__["type"] = type
        __props__.__dict__["url"] = url
        return Marker(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def dataset(self) -> pulumi.Output[str]:
        """
        The dataset this marker is placed on. Use `__all__` for Environment-wide markers.
        """
        return pulumi.get(self, "dataset")

    @property
    @pulumi.getter
    def message(self) -> pulumi.Output[Optional[str]]:
        """
        The message on the marker.
        """
        return pulumi.get(self, "message")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[Optional[str]]:
        """
        The type of the marker, Honeycomb.io can display markers in different colors depending on their type.
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter
    def url(self) -> pulumi.Output[Optional[str]]:
        """
        A target for the Marker. If you click on the Marker text, it will take you to this URL.
        """
        return pulumi.get(self, "url")

