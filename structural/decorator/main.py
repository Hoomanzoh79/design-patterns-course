class WrittenText:
    """
    Component (base object).

    Inheritance adds behavior at class definition time.
    Decorators add behavior at runtime by wrapping objects.
    Decorator Pattern

    Purpose:
    - Add behavior dynamically.
    - Favor composition over inheritance.

    Key idea:
    - Inheritance = extend classes.
    - Decorator = wrap objects.

    Benefit:
    - Avoid subclass explosion.
    - Combine features at runtime.
    Note : python decorators are using the same idea as this
    """

    def __init__(self, text: str):
        self._text = text

    def render(self) -> str:
        return self._text


class ItalicText(WrittenText):
    """
    Decorator.

    Wraps another WrittenText object and adds italic formatting
    without modifying the original object.
    """

    def __init__(self, wrapped: WrittenText):
        self._wrapped = wrapped

    def render(self) -> str:
        return f"<i>{self._wrapped.render()}</i>"


class BoldText(WrittenText):
    """
    Decorator.

    Decorators can be stacked to compose behavior:
    BoldText(ItalicText(WrittenText("hello")))
    """

    def __init__(self, wrapped: WrittenText):
        self._wrapped = wrapped

    def render(self) -> str:
        return f"<b>{self._wrapped.render()}</b>"


if __name__ == "__main__":
    print(BoldText(ItalicText(WrittenText("example for decorator design pattern"))).render())
