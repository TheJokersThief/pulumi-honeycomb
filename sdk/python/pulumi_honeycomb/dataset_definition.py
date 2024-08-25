# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = ['DatasetDefinitionArgs', 'DatasetDefinition']

@pulumi.input_type
class DatasetDefinitionArgs:
    def __init__(__self__, *,
                 column: pulumi.Input[str],
                 dataset: pulumi.Input[str],
                 name: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a DatasetDefinition resource.
        :param pulumi.Input[str] column: The column to set the definition to. Must be the name of an existing Column or the alias of an existing Derived Column.
        :param pulumi.Input[str] dataset: The dataset to set the Dataset Definition for.
        :param pulumi.Input[str] name: The name of the definition being set.
        """
        pulumi.set(__self__, "column", column)
        pulumi.set(__self__, "dataset", dataset)
        if name is not None:
            pulumi.set(__self__, "name", name)

    @property
    @pulumi.getter
    def column(self) -> pulumi.Input[str]:
        """
        The column to set the definition to. Must be the name of an existing Column or the alias of an existing Derived Column.
        """
        return pulumi.get(self, "column")

    @column.setter
    def column(self, value: pulumi.Input[str]):
        pulumi.set(self, "column", value)

    @property
    @pulumi.getter
    def dataset(self) -> pulumi.Input[str]:
        """
        The dataset to set the Dataset Definition for.
        """
        return pulumi.get(self, "dataset")

    @dataset.setter
    def dataset(self, value: pulumi.Input[str]):
        pulumi.set(self, "dataset", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the definition being set.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)


@pulumi.input_type
class _DatasetDefinitionState:
    def __init__(__self__, *,
                 column: Optional[pulumi.Input[str]] = None,
                 column_type: Optional[pulumi.Input[str]] = None,
                 dataset: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering DatasetDefinition resources.
        :param pulumi.Input[str] column: The column to set the definition to. Must be the name of an existing Column or the alias of an existing Derived Column.
        :param pulumi.Input[str] column_type: The type of the column assigned to the definition. Either `column` or `derived_column`.
        :param pulumi.Input[str] dataset: The dataset to set the Dataset Definition for.
        :param pulumi.Input[str] name: The name of the definition being set.
        """
        if column is not None:
            pulumi.set(__self__, "column", column)
        if column_type is not None:
            pulumi.set(__self__, "column_type", column_type)
        if dataset is not None:
            pulumi.set(__self__, "dataset", dataset)
        if name is not None:
            pulumi.set(__self__, "name", name)

    @property
    @pulumi.getter
    def column(self) -> Optional[pulumi.Input[str]]:
        """
        The column to set the definition to. Must be the name of an existing Column or the alias of an existing Derived Column.
        """
        return pulumi.get(self, "column")

    @column.setter
    def column(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "column", value)

    @property
    @pulumi.getter(name="columnType")
    def column_type(self) -> Optional[pulumi.Input[str]]:
        """
        The type of the column assigned to the definition. Either `column` or `derived_column`.
        """
        return pulumi.get(self, "column_type")

    @column_type.setter
    def column_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "column_type", value)

    @property
    @pulumi.getter
    def dataset(self) -> Optional[pulumi.Input[str]]:
        """
        The dataset to set the Dataset Definition for.
        """
        return pulumi.get(self, "dataset")

    @dataset.setter
    def dataset(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "dataset", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the definition being set.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)


class DatasetDefinition(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 column: Optional[pulumi.Input[str]] = None,
                 dataset: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Create a DatasetDefinition resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] column: The column to set the definition to. Must be the name of an existing Column or the alias of an existing Derived Column.
        :param pulumi.Input[str] dataset: The dataset to set the Dataset Definition for.
        :param pulumi.Input[str] name: The name of the definition being set.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: DatasetDefinitionArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Create a DatasetDefinition resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param DatasetDefinitionArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(DatasetDefinitionArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 column: Optional[pulumi.Input[str]] = None,
                 dataset: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = DatasetDefinitionArgs.__new__(DatasetDefinitionArgs)

            if column is None and not opts.urn:
                raise TypeError("Missing required property 'column'")
            __props__.__dict__["column"] = column
            if dataset is None and not opts.urn:
                raise TypeError("Missing required property 'dataset'")
            __props__.__dict__["dataset"] = dataset
            __props__.__dict__["name"] = name
            __props__.__dict__["column_type"] = None
        super(DatasetDefinition, __self__).__init__(
            'honeycomb:index/datasetDefinition:DatasetDefinition',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            column: Optional[pulumi.Input[str]] = None,
            column_type: Optional[pulumi.Input[str]] = None,
            dataset: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None) -> 'DatasetDefinition':
        """
        Get an existing DatasetDefinition resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] column: The column to set the definition to. Must be the name of an existing Column or the alias of an existing Derived Column.
        :param pulumi.Input[str] column_type: The type of the column assigned to the definition. Either `column` or `derived_column`.
        :param pulumi.Input[str] dataset: The dataset to set the Dataset Definition for.
        :param pulumi.Input[str] name: The name of the definition being set.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _DatasetDefinitionState.__new__(_DatasetDefinitionState)

        __props__.__dict__["column"] = column
        __props__.__dict__["column_type"] = column_type
        __props__.__dict__["dataset"] = dataset
        __props__.__dict__["name"] = name
        return DatasetDefinition(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def column(self) -> pulumi.Output[str]:
        """
        The column to set the definition to. Must be the name of an existing Column or the alias of an existing Derived Column.
        """
        return pulumi.get(self, "column")

    @property
    @pulumi.getter(name="columnType")
    def column_type(self) -> pulumi.Output[str]:
        """
        The type of the column assigned to the definition. Either `column` or `derived_column`.
        """
        return pulumi.get(self, "column_type")

    @property
    @pulumi.getter
    def dataset(self) -> pulumi.Output[str]:
        """
        The dataset to set the Dataset Definition for.
        """
        return pulumi.get(self, "dataset")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the definition being set.
        """
        return pulumi.get(self, "name")

