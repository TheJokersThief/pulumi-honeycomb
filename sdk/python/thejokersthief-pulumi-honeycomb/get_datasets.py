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
    'GetDatasetsResult',
    'AwaitableGetDatasetsResult',
    'get_datasets',
    'get_datasets_output',
]

@pulumi.output_type
class GetDatasetsResult:
    """
    A collection of values returned by GetDatasets.
    """
    def __init__(__self__, detail_filter=None, id=None, names=None, slugs=None, starts_with=None):
        if detail_filter and not isinstance(detail_filter, dict):
            raise TypeError("Expected argument 'detail_filter' to be a dict")
        pulumi.set(__self__, "detail_filter", detail_filter)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if names and not isinstance(names, list):
            raise TypeError("Expected argument 'names' to be a list")
        pulumi.set(__self__, "names", names)
        if slugs and not isinstance(slugs, list):
            raise TypeError("Expected argument 'slugs' to be a list")
        pulumi.set(__self__, "slugs", slugs)
        if starts_with and not isinstance(starts_with, str):
            raise TypeError("Expected argument 'starts_with' to be a str")
        pulumi.set(__self__, "starts_with", starts_with)

    @property
    @pulumi.getter(name="detailFilter")
    def detail_filter(self) -> Optional['outputs.GetDatasetsDetailFilterResult']:
        return pulumi.get(self, "detail_filter")

    @property
    @pulumi.getter
    def id(self) -> str:
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def names(self) -> Sequence[str]:
        """
        a list of all the dataset names.
        """
        return pulumi.get(self, "names")

    @property
    @pulumi.getter
    def slugs(self) -> Sequence[str]:
        """
        a list of all the dataset slugs.
        """
        return pulumi.get(self, "slugs")

    @property
    @pulumi.getter(name="startsWith")
    @_utilities.deprecated("""Use the `detail_filter` block instead.""")
    def starts_with(self) -> Optional[str]:
        return pulumi.get(self, "starts_with")


class AwaitableGetDatasetsResult(GetDatasetsResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetDatasetsResult(
            detail_filter=self.detail_filter,
            id=self.id,
            names=self.names,
            slugs=self.slugs,
            starts_with=self.starts_with)


def get_datasets(detail_filter: Optional[Union['GetDatasetsDetailFilterArgs', 'GetDatasetsDetailFilterArgsDict']] = None,
                 starts_with: Optional[str] = None,
                 opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetDatasetsResult:
    """
    ## # Data Source: get_datasets

    The Datasets data source retrieves the Environment's Datasets.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_honeycomb as honeycomb

    all = honeycomb.get_datasets()
    foo = honeycomb.get_datasets(detail_filter={
        "name": "name",
        "value_regex": "foo_*",
    })
    ```


    :param Union['GetDatasetsDetailFilterArgs', 'GetDatasetsDetailFilterArgsDict'] detail_filter: a block to further filter results as described below. `name` must be set when providing a filter. Conflicts with `starts_with`.
    :param str starts_with: Deprecated: use `detail_filter` instead. Only return datasets whose name starts with the given value.
    """
    __args__ = dict()
    __args__['detailFilter'] = detail_filter
    __args__['startsWith'] = starts_with
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('honeycomb:index/getDatasets:GetDatasets', __args__, opts=opts, typ=GetDatasetsResult).value

    return AwaitableGetDatasetsResult(
        detail_filter=pulumi.get(__ret__, 'detail_filter'),
        id=pulumi.get(__ret__, 'id'),
        names=pulumi.get(__ret__, 'names'),
        slugs=pulumi.get(__ret__, 'slugs'),
        starts_with=pulumi.get(__ret__, 'starts_with'))


@_utilities.lift_output_func(get_datasets)
def get_datasets_output(detail_filter: Optional[pulumi.Input[Optional[Union['GetDatasetsDetailFilterArgs', 'GetDatasetsDetailFilterArgsDict']]]] = None,
                        starts_with: Optional[pulumi.Input[Optional[str]]] = None,
                        opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetDatasetsResult]:
    """
    ## # Data Source: get_datasets

    The Datasets data source retrieves the Environment's Datasets.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_honeycomb as honeycomb

    all = honeycomb.get_datasets()
    foo = honeycomb.get_datasets(detail_filter={
        "name": "name",
        "value_regex": "foo_*",
    })
    ```


    :param Union['GetDatasetsDetailFilterArgs', 'GetDatasetsDetailFilterArgsDict'] detail_filter: a block to further filter results as described below. `name` must be set when providing a filter. Conflicts with `starts_with`.
    :param str starts_with: Deprecated: use `detail_filter` instead. Only return datasets whose name starts with the given value.
    """
    ...
