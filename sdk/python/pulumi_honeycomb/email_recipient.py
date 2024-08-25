# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = ['EmailRecipientArgs', 'EmailRecipient']

@pulumi.input_type
class EmailRecipientArgs:
    def __init__(__self__, *,
                 address: pulumi.Input[str]):
        """
        The set of arguments for constructing a EmailRecipient resource.
        :param pulumi.Input[str] address: The email address to send the notification to.
        """
        pulumi.set(__self__, "address", address)

    @property
    @pulumi.getter
    def address(self) -> pulumi.Input[str]:
        """
        The email address to send the notification to.
        """
        return pulumi.get(self, "address")

    @address.setter
    def address(self, value: pulumi.Input[str]):
        pulumi.set(self, "address", value)


@pulumi.input_type
class _EmailRecipientState:
    def __init__(__self__, *,
                 address: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering EmailRecipient resources.
        :param pulumi.Input[str] address: The email address to send the notification to.
        """
        if address is not None:
            pulumi.set(__self__, "address", address)

    @property
    @pulumi.getter
    def address(self) -> Optional[pulumi.Input[str]]:
        """
        The email address to send the notification to.
        """
        return pulumi.get(self, "address")

    @address.setter
    def address(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "address", value)


class EmailRecipient(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 address: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        ## # Resource: EmailRecipient

        `EmailRecipient` allows you to define and manage an Email recipient that can be used by Triggers or BurnAlerts notifications.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_honeycomb as honeycomb

        alerts = honeycomb.EmailRecipient("alerts", address="alerts@example.com")
        ```

        ## Import

        Email Recipients can be imported by their ID, e.g.

        ```sh
        $ pulumi import honeycomb:index/emailRecipient:EmailRecipient my_recipient nx2zsegA0dZ
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] address: The email address to send the notification to.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: EmailRecipientArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        ## # Resource: EmailRecipient

        `EmailRecipient` allows you to define and manage an Email recipient that can be used by Triggers or BurnAlerts notifications.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_honeycomb as honeycomb

        alerts = honeycomb.EmailRecipient("alerts", address="alerts@example.com")
        ```

        ## Import

        Email Recipients can be imported by their ID, e.g.

        ```sh
        $ pulumi import honeycomb:index/emailRecipient:EmailRecipient my_recipient nx2zsegA0dZ
        ```

        :param str resource_name: The name of the resource.
        :param EmailRecipientArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(EmailRecipientArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 address: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = EmailRecipientArgs.__new__(EmailRecipientArgs)

            if address is None and not opts.urn:
                raise TypeError("Missing required property 'address'")
            __props__.__dict__["address"] = address
        super(EmailRecipient, __self__).__init__(
            'honeycomb:index/emailRecipient:EmailRecipient',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            address: Optional[pulumi.Input[str]] = None) -> 'EmailRecipient':
        """
        Get an existing EmailRecipient resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] address: The email address to send the notification to.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _EmailRecipientState.__new__(_EmailRecipientState)

        __props__.__dict__["address"] = address
        return EmailRecipient(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def address(self) -> pulumi.Output[str]:
        """
        The email address to send the notification to.
        """
        return pulumi.get(self, "address")

