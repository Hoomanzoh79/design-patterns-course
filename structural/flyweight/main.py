import random
import sys
from dataclasses import dataclass


@dataclass
class TreeType:
    """
    FLYWEIGHT
    ---------
    Stores the INTRINSIC (shared, context-independent) state of a tree:
    name, texture, model, wind_sound. Many Tree (context) objects can
    point to the SAME TreeType instance, so this data is created only
    once per unique (name, texture, model) combo, no matter how many
    trees use it.

    - Immutable / treated as read-only after creation
    - Shared across many contexts
    - Holds data that does NOT depend on a tree's position
    """
    name: str
    texture: str
    model: str
    wind_sound: str

    def display(self, x: int, y: int):
        print(f"Rendering {self.name} at ({x},{y}), Texture: {self.texture}, Model: {self.model}")


class TreeTypeFactory:
    """
    FLYWEIGHT FACTORY
    -----------------
    Creates and manages the pool ("cache") of TreeType (flyweight)
    objects. Guarantees that identical TreeTypes are created only ONCE
    and reused afterwards, keyed by (name, texture, model).

    - Owns the flyweight pool/cache
    - get_xxx() -> returns existing flyweight or creates + caches a new one
    - Client code never calls TreeType(...) directly
    """
    _tree_types: dict[str, TreeType] = {}

    @classmethod
    def get_tree_type(cls, name: str, texture: str, model: str, wind_sound: str) -> TreeType:
        key = f"{name}-{texture}-{model}"

        if key not in cls._tree_types:
            cls._tree_types[key] = TreeType(name, texture, model, wind_sound)
            print(f"Creating tree type: {key}")
        else:
            print(f"Reusing tree type:  {key}")
        return cls._tree_types[key]

    @classmethod
    def total_types_created(cls) -> int:
        return len(cls._tree_types)

    @classmethod
    def all_types(cls) -> list[TreeType]:
        return list(cls._tree_types.values())


@dataclass
class Tree:
    """
    CONTEXT
    -------
    - Holds extrinsic state that varies per object (x, y)
    - Holds a *reference* to a flyweight, never a copy
    - Many contexts can share one flyweight instance
    """
    x: int
    y: int
    tree_type: TreeType

    def display(self):
        self.tree_type.display(self.x, self.y)


class Forest:
    """
    CLIENT-SIDE COLLECTION
    -----------------------
    Holds many Tree (context) objects and always asks TreeTypeFactory
    for a flyweight instead of constructing TreeType objects itself.
    """
    def __init__(self):
        self.trees: list[Tree] = []

    def plant_tree(self, x: int, y: int, name: str, texture: str, model: str, wind_sound: str):
        tree_type = TreeTypeFactory.get_tree_type(name, texture, model, wind_sound)
        tree = Tree(x, y, tree_type)
        self.trees.append(tree)

    def plant_random_trees(self, count: int):
        tree_specs = [
            ("Tree 1", "tree1_texture.png", "tree1_model.obj", "tree1_wind_sound.mp3"),
            ("Tree 2", "tree2_texture.png", "tree2_model.obj", "tree2_wind_sound.mp3"),
            ("Tree 3", "tree3_texture.png", "tree3_model.obj", "tree3_wind_sound.mp3"),
        ]
        for _ in range(count):
            x, y = random.randint(0, 100), random.randint(0, 100)
            spec = random.choice(tree_specs)
            self.plant_tree(x, y, *spec)

    def display(self):
        for tree in self.trees[:5]:
            tree.display()
        remaining = max(0, len(self.trees) - 5)
        if remaining:
            print(f"... and {remaining} more trees ...")


if __name__ == "__main__":
    forest = Forest()
    forest.plant_random_trees(1000)
    print("\n--- Sample of planted trees ---")
    forest.display()

    unique_types = TreeTypeFactory.total_types_created()
    print(f"\nTotal trees planted      : {len(forest.trees)}")
    print(f"Unique TreeTypes created : {unique_types}")

    sample_type = TreeTypeFactory.all_types()[0]
    size_tree_type_shell = sys.getsizeof(sample_type)
    size_tree_type_strings = sum(
        sys.getsizeof(getattr(sample_type, f)) for f in ("name", "texture", "model", "wind_sound")
    )
    full_tree_type_size = size_tree_type_shell + size_tree_type_strings
    size_tree = sys.getsizeof(forest.trees[0])

    # WITH the flyweight pattern:
    mem_with_flyweight = (unique_types * full_tree_type_size) + (len(forest.trees) * size_tree)
    # WITHOUT the flyweight pattern:
    mem_without_flyweight = len(forest.trees) * (full_tree_type_size + size_tree)
    saved = mem_without_flyweight - mem_with_flyweight
    pct_saved = (saved / mem_without_flyweight) * 100

    print("\n--- Memory comparison (approximate, via sys.getsizeof) ---")
    print(f"Size of one TreeType (incl. strings) : {full_tree_type_size:,} bytes")
    print(f"Size of one Tree (context)           : {size_tree:,} bytes")
    print(f"Memory WITH flyweight pattern         : {mem_with_flyweight:,} bytes")
    print(f"Memory WITHOUT flyweight pattern      : {mem_without_flyweight:,} bytes")
    print(f"Memory saved                          : {saved:,} bytes ({pct_saved:.2f}%)")
