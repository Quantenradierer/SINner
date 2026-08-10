from typing import Self, Iterator

from pydantic import BaseModel, Field

from npc_creator.game_mechanics.sr6.object_type import ObjectType


class GearCollection(BaseModel):
    objects: list["ModifiableObject"] = Field(default_factory=list["ModifiableObject"])

    def __contains__(self, item: "Gear") -> bool:
        return item in self.objects

    def filter(self, object_type: ObjectType) -> Self:
        return self.__class__(
            objects=[g for g in self.objects if g.type == object_type]
        )

    def append(self, gear: "ModifiableObject") -> None:
        self.objects.append(gear)

    def __bool__(self) -> bool:
        return bool(self.objects)

    def __len__(self) -> int:
        return len(self.objects)

    def __getitem__(self, index: int) -> "ModifiableObject":
        return self.objects[index]

    def __iter__(
        self,
    ) -> Iterator[
        "ModifiableObject"
    ]:  # pyright: ignore [reportIncompatibleMethodOverride]
        return iter(self.objects)


from npc_creator.game_mechanics.sr6.modifiable_object import ModifiableObject
