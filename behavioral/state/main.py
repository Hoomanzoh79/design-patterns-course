from abc import ABC, abstractmethod


class TrafficLight:
    """
    CONTEXT

    This is the object whose behavior changes depending on its current state

    Responsibilities:
    - Stores the current state object
    - Delegates work to the current state
    - Does NOT decide state transitions itself

    Key State Pattern idea:
        TrafficLight -> delegates -> Current State

    Instead of writing:

        if state == "RED":
            ...
        elif state == "GREEN":
            ...

    we let each state object decide what should happen
    """

    def __init__(self):
        self._state: 'TrafficLightState' | None = None

    @property
    def state(self):
        return self._state

    @state.setter
    def state(self, value):
        self._state = value
        print(
            f"Traffic light state changed to "
            f"{self._state.__class__.__name__}"
        )

    def switch(self):
        """
        Delegates the action to the current state

        The context does not know:
        - what behavior should occur
        - what the next state should be

        It simply asks the current state to handle the request
        """
        if self._state:
            self._state.handle(self)


class TrafficLightState(ABC):
    """
    STATE INTERFACE

    Defines the contract that every concrete state must implement

    The context (TrafficLight) only knows about this interface,
    not about RedLight, GreenLight, or YellowLight directly

    This allows states to be swapped at runtime
    """

    @abstractmethod
    def handle(self, traffic_light: TrafficLight):
        """
        Execute behavior associated with this state and
        optionally transition the context to another state
        """
        raise NotImplementedError

class RedLight(TrafficLightState):
    """
    CONCRETE STATE

    Represents the RED state

    Responsibilities:
    - Execute behavior specific to RED
    - Decide which state comes next

    Transition:
        Red -> Green
    """

    def handle(self, traffic_light: TrafficLight):
        print("Red light, all vehicles must stop")
        traffic_light.state = GreenLight()

class GreenLight(TrafficLightState):
    """
    CONCRETE STATE

    Represents the GREEN state

    Responsibilities:
    - Execute behavior specific to GREEN
    - Decide which state comes next

    Transition:
        Green -> Yellow
    """

    def handle(self, traffic_light: TrafficLight):
        print("Green light, all vehicles must go")
        traffic_light.state = YellowLight()

class YellowLight(TrafficLightState):
    """
    CONCRETE STATE

    Represents the YELLOW state

    Responsibilities:
    - Execute behavior specific to YELLOW
    - Decide which state comes next

    Transition:
        Yellow -> Red
    """

    def handle(self, traffic_light: TrafficLight):
        print("Yellow light, all vehicles must slow down")
        traffic_light.state = RedLight()


if __name__ == "__main__":
    """
    Execution flow:

        TrafficLight
            |
            v
        RedLight
            |
            v
        GreenLight
            |
            v
        YellowLight
            |
            v
        RedLight
            ...

    Each call to switch() delegates work to the current state,
    and that state decides the next transition
    """
    light = TrafficLight()
    light.state = RedLight()

    for _ in range(3):
        light.switch()
