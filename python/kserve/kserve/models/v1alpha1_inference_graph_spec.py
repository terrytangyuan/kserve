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
from kserve.models.v1alpha1_inference_router import V1alpha1InferenceRouter
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class V1alpha1InferenceGraphSpec(BaseModel):
    """
    InferenceGraphSpec defines the InferenceGraph spec
    """ # noqa: E501
    affinity: Optional[V1Affinity] = None
    max_replicas: Optional[StrictInt] = Field(default=None, description="Maximum number of replicas for autoscaling.", alias="maxReplicas")
    min_replicas: Optional[StrictInt] = Field(default=None, description="Minimum number of replicas, defaults to 1 but can be set to 0 to enable scale-to-zero.", alias="minReplicas")
    nodes: Dict[str, V1alpha1InferenceRouter] = Field(description="Map of InferenceGraph router nodes Each node defines the router which can be different routing types")
    resources: Optional[V1ResourceRequirements] = None
    scale_metric: Optional[StrictStr] = Field(default=None, description="ScaleMetric defines the scaling metric type watched by autoscaler possible values are concurrency, rps, cpu, memory. concurrency, rps are supported via Knative Pod Autoscaler(https://knative.dev/docs/serving/autoscaling/autoscaling-metrics).", alias="scaleMetric")
    scale_target: Optional[StrictInt] = Field(default=None, description="ScaleTarget specifies the integer target value of the metric type the Autoscaler watches for. concurrency and rps targets are supported by Knative Pod Autoscaler (https://knative.dev/docs/serving/autoscaling/autoscaling-targets/).", alias="scaleTarget")
    timeout: Optional[StrictInt] = Field(default=None, description="TimeoutSeconds specifies the number of seconds to wait before timing out a request to the component.")
    __properties: ClassVar[List[str]] = ["affinity", "maxReplicas", "minReplicas", "nodes", "resources", "scaleMetric", "scaleTarget", "timeout"]

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
        """Create an instance of V1alpha1InferenceGraphSpec from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of affinity
        if self.affinity:
            _dict['affinity'] = self.affinity.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each value in nodes (dict)
        _field_dict = {}
        if self.nodes:
            for _key in self.nodes:
                if self.nodes[_key]:
                    _field_dict[_key] = self.nodes[_key].to_dict()
            _dict['nodes'] = _field_dict
        # override the default output from pydantic by calling `to_dict()` of resources
        if self.resources:
            _dict['resources'] = self.resources.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of V1alpha1InferenceGraphSpec from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "affinity": V1Affinity.from_dict(obj.get("affinity")) if obj.get("affinity") is not None else None,
            "maxReplicas": obj.get("maxReplicas"),
            "minReplicas": obj.get("minReplicas"),
            "nodes": dict(
                (_k, V1alpha1InferenceRouter.from_dict(_v))
                for _k, _v in obj.get("nodes").items()
            )
            if obj.get("nodes") is not None
            else None,
            "resources": V1ResourceRequirements.from_dict(obj.get("resources")) if obj.get("resources") is not None else None,
            "scaleMetric": obj.get("scaleMetric"),
            "scaleTarget": obj.get("scaleTarget"),
            "timeout": obj.get("timeout")
        })
        return _obj


