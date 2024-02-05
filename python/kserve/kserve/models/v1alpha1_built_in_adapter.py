# Copyright 2023 The KServe Authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# coding: utf-8

"""
    KServe

    Python SDK for KServe

    The version of the OpenAPI document: v0.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Any, ClassVar, Dict, List, Optional
from pydantic import BaseModel, StrictInt, StrictStr
from pydantic import Field
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class V1alpha1BuiltInAdapter(BaseModel):
    """
    V1alpha1BuiltInAdapter
    """ # noqa: E501
    env: Optional[List[V1EnvVar]] = Field(default=None, description="Environment variables used to control other aspects of the built-in adapter's behaviour (uncommon)")
    mem_buffer_bytes: Optional[StrictInt] = Field(default=None, description="Fixed memory overhead to subtract from runtime container's memory allocation to determine model capacity", alias="memBufferBytes")
    model_loading_timeout_millis: Optional[StrictInt] = Field(default=None, description="Timeout for model loading operations in milliseconds", alias="modelLoadingTimeoutMillis")
    runtime_management_port: Optional[StrictInt] = Field(default=None, description="Port which the runtime server listens for model management requests", alias="runtimeManagementPort")
    server_type: Optional[StrictStr] = Field(default=None, description="ServerType must be one of the supported built-in types such as \"triton\" or \"mlserver\", and the runtime's container must have the same name", alias="serverType")
    __properties: ClassVar[List[str]] = ["env", "memBufferBytes", "modelLoadingTimeoutMillis", "runtimeManagementPort", "serverType"]

    model_config = {
        "populate_by_name": True,
        "validate_assignment": True,
        "protected_namespaces": (),
    }


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of V1alpha1BuiltInAdapter from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        _dict = self.model_dump(
            by_alias=True,
            exclude={
            },
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of each item in env (list)
        _items = []
        if self.env:
            for _item in self.env:
                if _item:
                    _items.append(_item.to_dict())
            _dict['env'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of V1alpha1BuiltInAdapter from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "env": [V1EnvVar.from_dict(_item) for _item in obj.get("env")] if obj.get("env") is not None else None,
            "memBufferBytes": obj.get("memBufferBytes"),
            "modelLoadingTimeoutMillis": obj.get("modelLoadingTimeoutMillis"),
            "runtimeManagementPort": obj.get("runtimeManagementPort"),
            "serverType": obj.get("serverType")
        })
        return _obj


