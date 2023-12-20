from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.entity_model_employee import EntityModelEmployee
    from ..models.link import Link


T = TypeVar("T", bound="CollectionModelEntityModelEmployee")


@_attrs_define
class CollectionModelEntityModelEmployee:
    """
    Attributes:
        links (Union[Unset, List['Link']]):
        content (Union[Unset, List['EntityModelEmployee']]):
    """

    links: Union[Unset, List["Link"]] = UNSET
    content: Union[Unset, List["EntityModelEmployee"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        links: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.links, Unset):
            links = []
            for links_item_data in self.links:
                links_item = links_item_data.to_dict()

                links.append(links_item)

        content: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.content, Unset):
            content = []
            for content_item_data in self.content:
                content_item = content_item_data.to_dict()

                content.append(content_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if links is not UNSET:
            field_dict["links"] = links
        if content is not UNSET:
            field_dict["content"] = content

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.entity_model_employee import EntityModelEmployee
        from ..models.link import Link

        d = src_dict.copy()
        links = []
        _links = d.pop("links", UNSET)
        for links_item_data in _links or []:
            links_item = Link.from_dict(links_item_data)

            links.append(links_item)

        content = []
        _content = d.pop("content", UNSET)
        for content_item_data in _content or []:
            content_item = EntityModelEmployee.from_dict(content_item_data)

            content.append(content_item)

        collection_model_entity_model_employee = cls(
            links=links,
            content=content,
        )

        collection_model_entity_model_employee.additional_properties = d
        return collection_model_entity_model_employee

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
