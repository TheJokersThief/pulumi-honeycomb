# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities
from . import outputs
from ._inputs import *

__all__ = [
    'GetRecipientsResult',
    'AwaitableGetRecipientsResult',
    'get_recipients',
    'get_recipients_output',
]

@pulumi.output_type
class GetRecipientsResult:
    """
    A collection of values returned by GetRecipients.
    """
    def __init__(__self__, detail_filter=None, id=None, ids=None, type=None):
        if detail_filter and not isinstance(detail_filter, dict):
            raise TypeError("Expected argument 'detail_filter' to be a dict")
        pulumi.set(__self__, "detail_filter", detail_filter)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if ids and not isinstance(ids, list):
            raise TypeError("Expected argument 'ids' to be a list")
        pulumi.set(__self__, "ids", ids)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter(name="detailFilter")
    def detail_filter(self) -> Optional['outputs.GetRecipientsDetailFilterResult']:
        return pulumi.get(self, "detail_filter")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def ids(self) -> Sequence[str]:
        """
        A list of all the recipient IDs found.
        """
        return pulumi.get(self, "ids")

    @property
    @pulumi.getter
    def type(self) -> Optional[str]:
        return pulumi.get(self, "type")


class AwaitableGetRecipientsResult(GetRecipientsResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetRecipientsResult(
            detail_filter=self.detail_filter,
            id=self.id,
            ids=self.ids,
            type=self.type)


def get_recipients(detail_filter: Optional[Union['GetRecipientsDetailFilterArgs', 'GetRecipientsDetailFilterArgsDict']] = None,
                   type: Optional[str] = None,
                   opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetRecipientsResult:
    """
    ## # Data Source: get_recipients

    `get_recipients` data source provides recipient IDs of recipients matching a set of criteria.

    ## Example Usage

    ### Get all recipients
    ```python
    import pulumi
    import pulumi_honeycomb as honeycomb

    all = honeycomb.get_recipients()
    ```

    ### Get all email recipients matching a specific domain
    ```python
    import pulumi
    import pulumi_honeycomb as honeycomb

    example_dot_com = honeycomb.get_recipients(detail_filter={
            "name": "address",
            "value_regex": ".*@example.com",
        },
        type="email")
    ```


    :param Union['GetRecipientsDetailFilterArgs', 'GetRecipientsDetailFilterArgsDict'] detail_filter: a block to further filter recipients as described below. `name` must be set when providing a filter.
    :param str type: The type of recipient, allowed types are `email`, `pagerduty`, `msteams`, `slack` and `webhook`.
    """
    __args__ = dict()
    __args__['detailFilter'] = detail_filter
    __args__['type'] = type
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('honeycomb:index/getRecipients:GetRecipients', __args__, opts=opts, typ=GetRecipientsResult).value

    return AwaitableGetRecipientsResult(
        detail_filter=pulumi.get(__ret__, 'detail_filter'),
        id=pulumi.get(__ret__, 'id'),
        ids=pulumi.get(__ret__, 'ids'),
        type=pulumi.get(__ret__, 'type'))


@_utilities.lift_output_func(get_recipients)
def get_recipients_output(detail_filter: Optional[pulumi.Input[Optional[Union['GetRecipientsDetailFilterArgs', 'GetRecipientsDetailFilterArgsDict']]]] = None,
                          type: Optional[pulumi.Input[Optional[str]]] = None,
                          opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetRecipientsResult]:
    """
    ## # Data Source: get_recipients

    `get_recipients` data source provides recipient IDs of recipients matching a set of criteria.

    ## Example Usage

    ### Get all recipients
    ```python
    import pulumi
    import pulumi_honeycomb as honeycomb

    all = honeycomb.get_recipients()
    ```

    ### Get all email recipients matching a specific domain
    ```python
    import pulumi
    import pulumi_honeycomb as honeycomb

    example_dot_com = honeycomb.get_recipients(detail_filter={
            "name": "address",
            "value_regex": ".*@example.com",
        },
        type="email")
    ```


    :param Union['GetRecipientsDetailFilterArgs', 'GetRecipientsDetailFilterArgsDict'] detail_filter: a block to further filter recipients as described below. `name` must be set when providing a filter.
    :param str type: The type of recipient, allowed types are `email`, `pagerduty`, `msteams`, `slack` and `webhook`.
    """
    ...
