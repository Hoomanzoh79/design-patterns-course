from abc import ABC, abstractmethod

class SmartDevice(ABC):
    """
    abstract element of the object structure, 
    defines an accept method that takes a visitor 
    """

    @abstractmethod
    def accept(self, visitor:'DeviceVisitor') -> str:
        raise NotImplementedError

class SmartLight(SmartDevice):
    """
    concrete element of the object structure
    """

    def __init__(self,name:str,brightness:int):
        self.name = name
        self.brightness = brightness = 50

    def accept(self, visitor:'DeviceVisitor') -> str:
        return visitor.visit_smart_light(self)
    
    def set_brightness(self, brightness:int):
        self.brightness = max(0, min(brightness, 100))  
    
class SmartThermostat(SmartDevice):
    """
    concrete element of the object structure
    """

    def __init__(self,name:str):
        self.name = name
        self.temperature = 20.0

    def accept(self, visitor:'DeviceVisitor') -> str:
        return visitor.visit_smart_thermostat(self)
    
    def set_temperature(self, temperature:float):
        self.temperature = max(10.0, min(temperature, 30.0))

class SmartLock(SmartDevice):
    """
    concrete element of the object structure
    """

    def __init__(self,name:str):
        self.name = name
        self.is_locked = True

    def accept(self, visitor:'DeviceVisitor') -> str:
        return visitor.visit_smart_lock(self)

class DeviceVisitor(ABC):
    """
    abstract visitor, declares a visit method 
    for each concrete element in the object structure
    """

    @abstractmethod
    def visit_smart_light(self, light:SmartLight) -> str:
        raise NotImplementedError

    @abstractmethod
    def visit_smart_thermostat(self, thermostat:SmartThermostat) -> str:
        raise NotImplementedError

    @abstractmethod
    def visit_smart_lock(self, lock:SmartLock) -> str:
        raise NotImplementedError

class StatusVisitor(DeviceVisitor):
    """
    concrete visitor, implements the visit methods to perform status reporting
    """

    def visit_smart_light(self, light:SmartLight) -> str:
        return f"{light.name} brightness is {light.brightness}%"

    def visit_smart_thermostat(self, thermostat:SmartThermostat) -> str:
        return f"{thermostat.name} temperature is {thermostat.temperature}°C"

    def visit_smart_lock(self, lock:SmartLock) -> str:
        return f"{lock.name} is {'locked' if lock.is_locked else 'unlocked'}"

class AutomationVisitor(DeviceVisitor):
    """
    concrete visitor, implements the visit methods to perform automation actions
    """

    def __init__(self, time_of_day:str,outside_temperature:float):
        self.time_of_day = time_of_day
        self.outside_temperature = outside_temperature

    def visit_smart_light(self, light:SmartLight) -> str:
        if self.time_of_day == "evening":
            light.set_brightness(80)
            return f"{light.name} brightness set to 80% for evening"
        elif self.time_of_day == "night":
            light.set_brightness(30)
            return f"{light.name} brightness set to 30% for night"
        else:
            light.set_brightness(100)
            return f"{light.name} brightness set to 100% for daytime"
    
    def visit_smart_thermostat(self, thermostat:SmartThermostat) -> str:
        if self.outside_temperature < 15.0:
            thermostat.set_temperature(22.0)
            return f"{thermostat.name} temperature set to 22°C for cold weather"
        elif self.outside_temperature > 25.0:
            thermostat.set_temperature(18.0)
            return f"{thermostat.name} temperature set to 18°C for hot weather"
        else:
            thermostat.set_temperature(20.0)
            return f"{thermostat.name} temperature set to 20°C for mild weather"
        
    def visit_smart_lock(self, lock:SmartLock) -> str:
        if self.time_of_day == "night":
            lock.is_locked = True
            return f"{lock.name} locked for night"
        else:
            lock.is_locked = False
            return f"{lock.name} unlocked for daytime"

class SmartHome:
    """
    object structure, contains a collection of elements (smart devices)
    """

    def __init__(self):
        self.devices = []

    def add_device(self, device:SmartDevice):
        self.devices.append(device)

    def apply_visitor(self, visitor:DeviceVisitor) -> list[str]:
        return [device.accept(visitor) for device in self.devices]

if __name__ == '__main__':
    home = SmartHome()
    home.add_device(SmartLight("Living Room Light", 50))
    home.add_device(SmartThermostat("Main Thermostat"))
    home.add_device(SmartLock("Front Door Lock"))

    status_visitor = StatusVisitor()
    print("Device Status:")
    for status in home.apply_visitor(status_visitor):
        print(status)

    automation_visitor = AutomationVisitor(time_of_day="evening", outside_temperature=10.0)
    print("\nApplying Automation:")
    for result in home.apply_visitor(automation_visitor):
        print(result)
