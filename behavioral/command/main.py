from abc import ABC,abstractmethod

class RemoteControlCommand(ABC):
    @abstractmethod
    def execute(self,*args, **kwargs):
        raise NotImplementedError

class Device(ABC):
    @abstractmethod
    def turn_on(self,*args, **kwargs):
        raise NotImplementedError

    @abstractmethod
    def turn_off(self,*args, **kwargs):
        raise NotImplementedError

class TV(Device):
    def turn_on(self):
        print("TV is on")
    
    def turn_off(self):
        print("TV is off")

class DVDPlayer(Device):
    def turn_on(self):
        print("DVD Player is on")
    
    def turn_off(self):
        print("DVD Player is off")

class TurnOnCommand(RemoteControlCommand):
    def __init__(self,device:Device):
        self.device = device
    
    def execute(self):
        self.device.turn_on()

class TurnOffCommand(RemoteControlCommand):
    def __init__(self,device:Device):
        self.device = device
    
    def execute(self):
        self.device.turn_off()

class RemoteControl:
    def __init__(self):
        self.commands = {}
    
    def add_command(self,command_name:str,command:RemoteControlCommand):
        self.commands[command_name] = command
    
    def execute_command(self,command_name:str):
        if command_name in self.commands:
            self.commands[command_name].execute()
        else:
            raise KeyError("command not found in remote control !")

if __name__ == "__main__":
    tv = TV()
    dvd_player = DVDPlayer()
    remote_control = RemoteControl()
    remote_control.add_command("turn_on_tv",TurnOnCommand(tv))
    remote_control.add_command("turn_off_tv",TurnOffCommand(tv))
    remote_control.add_command("turn_on_dvd",TurnOnCommand(dvd_player))
    remote_control.add_command("turn_off_dvd",TurnOffCommand(dvd_player))
    for item in remote_control.commands.keys():
        print(f"------ {item} -------")
    remote_control.execute_command(input("please enter your desired command: "))
