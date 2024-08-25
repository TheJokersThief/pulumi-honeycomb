# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = ['DatasetArgs', 'Dataset']

@pulumi.input_type
class DatasetArgs:
    def __init__(__self__, *,
                 description: Optional[pulumi.Input[str]] = None,
                 expand_json_depth: Optional[pulumi.Input[int]] = None,
                 name: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a Dataset resource.
        :param pulumi.Input[str] description: A longer description for dataset.
        :param pulumi.Input[int] expand_json_depth: The maximum unpacking depth of nested JSON fields.
        :param pulumi.Input[str] name: The name of the dataset.
        """
        if description is not None:
            pulumi.set(__self__, "description", description)
        if expand_json_depth is not None:
            pulumi.set(__self__, "expand_json_depth", expand_json_depth)
        if name is not None:
            pulumi.set(__self__, "name", name)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        A longer description for dataset.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter(name="expandJsonDepth")
    def expand_json_depth(self) -> Optional[pulumi.Input[int]]:
        """
        The maximum unpacking depth of nested JSON fields.
        """
        return pulumi.get(self, "expand_json_depth")

    @expand_json_depth.setter
    def expand_json_depth(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "expand_json_depth", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the dataset.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)


@pulumi.input_type
class _DatasetState:
    def __init__(__self__, *,
                 created_at: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 expand_json_depth: Optional[pulumi.Input[int]] = None,
                 last_written_at: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 slug: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering Dataset resources.
        :param pulumi.Input[str] created_at: ISO8601 formatted time the column was created
        :param pulumi.Input[str] description: A longer description for dataset.
        :param pulumi.Input[int] expand_json_depth: The maximum unpacking depth of nested JSON fields.
        :param pulumi.Input[str] last_written_at: ISO8601 formatted time the column was last written to (received event data)
        :param pulumi.Input[str] name: The name of the dataset.
        :param pulumi.Input[str] slug: The slug of the dataset.
        """
        if created_at is not None:
            pulumi.set(__self__, "created_at", created_at)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if expand_json_depth is not None:
            pulumi.set(__self__, "expand_json_depth", expand_json_depth)
        if last_written_at is not None:
            pulumi.set(__self__, "last_written_at", last_written_at)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if slug is not None:
            pulumi.set(__self__, "slug", slug)

    @property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> Optional[pulumi.Input[str]]:
        """
        ISO8601 formatted time the column was created
        """
        return pulumi.get(self, "created_at")

    @created_at.setter
    def created_at(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "created_at", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        A longer description for dataset.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter(name="expandJsonDepth")
    def expand_json_depth(self) -> Optional[pulumi.Input[int]]:
        """
        The maximum unpacking depth of nested JSON fields.
        """
        return pulumi.get(self, "expand_json_depth")

    @expand_json_depth.setter
    def expand_json_depth(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "expand_json_depth", value)

    @property
    @pulumi.getter(name="lastWrittenAt")
    def last_written_at(self) -> Optional[pulumi.Input[str]]:
        """
        ISO8601 formatted time the column was last written to (received event data)
        """
        return pulumi.get(self, "last_written_at")

    @last_written_at.setter
    def last_written_at(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "last_written_at", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the dataset.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def slug(self) -> Optional[pulumi.Input[str]]:
        """
        The slug of the dataset.
        """
        return pulumi.get(self, "slug")

    @slug.setter
    def slug(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "slug", value)


class Dataset(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 expand_json_depth: Optional[pulumi.Input[int]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        ## # Resource: Dataset

        Creates a dataset.

        > **Note** If this dataset already exists, creating this resource is a no-op.

        > **Note** Destroying or replacing this resource will not delete the created dataset. It's not possible to delete a dataset using the API.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_honeycomb as honeycomb

        my_dataset = honeycomb.Dataset("myDataset", description="buzzing with data")
        ```

        ## Import

        Datasets can be imported by their slug, e.g.

        ```sh
        $ pulumi import honeycomb:index/dataset:Dataset my_dataset my-dataset
        ```

        You can find the slug in the URL bar when visiting the Dataset from the UI.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] description: A longer description for dataset.
        :param pulumi.Input[int] expand_json_depth: The maximum unpacking depth of nested JSON fields.
        :param pulumi.Input[str] name: The name of the dataset.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: Optional[DatasetArgs] = None,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        ## # Resource: Dataset

        Creates a dataset.

        > **Note** If this dataset already exists, creating this resource is a no-op.

        > **Note** Destroying or replacing this resource will not delete the created dataset. It's not possible to delete a dataset using the API.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_honeycomb as honeycomb

        my_dataset = honeycomb.Dataset("myDataset", description="buzzing with data")
        ```

        ## Import

        Datasets can be imported by their slug, e.g.

        ```sh
        $ pulumi import honeycomb:index/dataset:Dataset my_dataset my-dataset
        ```

        You can find the slug in the URL bar when visiting the Dataset from the UI.

        :param str resource_name: The name of the resource.
        :param DatasetArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(DatasetArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 expand_json_depth: Optional[pulumi.Input[int]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = DatasetArgs.__new__(DatasetArgs)

            __props__.__dict__["description"] = description
            __props__.__dict__["expand_json_depth"] = expand_json_depth
            __props__.__dict__["name"] = name
            __props__.__dict__["created_at"] = None
            __props__.__dict__["last_written_at"] = None
            __props__.__dict__["slug"] = None
        super(Dataset, __self__).__init__(
            'honeycomb:index/dataset:Dataset',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            created_at: Optional[pulumi.Input[str]] = None,
            description: Optional[pulumi.Input[str]] = None,
            expand_json_depth: Optional[pulumi.Input[int]] = None,
            last_written_at: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            slug: Optional[pulumi.Input[str]] = None) -> 'Dataset':
        """
        Get an existing Dataset resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] created_at: ISO8601 formatted time the column was created
        :param pulumi.Input[str] description: A longer description for dataset.
        :param pulumi.Input[int] expand_json_depth: The maximum unpacking depth of nested JSON fields.
        :param pulumi.Input[str] last_written_at: ISO8601 formatted time the column was last written to (received event data)
        :param pulumi.Input[str] name: The name of the dataset.
        :param pulumi.Input[str] slug: The slug of the dataset.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _DatasetState.__new__(_DatasetState)

        __props__.__dict__["created_at"] = created_at
        __props__.__dict__["description"] = description
        __props__.__dict__["expand_json_depth"] = expand_json_depth
        __props__.__dict__["last_written_at"] = last_written_at
        __props__.__dict__["name"] = name
        __props__.__dict__["slug"] = slug
        return Dataset(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> pulumi.Output[str]:
        """
        ISO8601 formatted time the column was created
        """
        return pulumi.get(self, "created_at")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        A longer description for dataset.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="expandJsonDepth")
    def expand_json_depth(self) -> pulumi.Output[Optional[int]]:
        """
        The maximum unpacking depth of nested JSON fields.
        """
        return pulumi.get(self, "expand_json_depth")

    @property
    @pulumi.getter(name="lastWrittenAt")
    def last_written_at(self) -> pulumi.Output[str]:
        """
        ISO8601 formatted time the column was last written to (received event data)
        """
        return pulumi.get(self, "last_written_at")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the dataset.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def slug(self) -> pulumi.Output[str]:
        """
        The slug of the dataset.
        """
        return pulumi.get(self, "slug")

