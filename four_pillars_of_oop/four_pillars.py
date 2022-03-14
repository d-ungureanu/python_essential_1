class Device:
    def __init__(self, brand_n, model_n):
        self.brand_name = brand_n
        self.model_name = model_n

    def __str__(self):
        return f"Device brand: {self.get_brand_name()}\nDevice model: {self.get_model_name()}"

    def set_brand_name(self, brand_n):
        self.brand_name = brand_n

    def get_brand_name(self):
        return self.brand_name

    def set_model_name(self, model_n):
        self.model_name = model_n

    def get_model_name(self):
        return self.model_name

    def power_check(self):
        print("Check if the devices needs a charger or to be connected to mains.")


class MobileDevice(Device):
    def __init__(self, brand_n, model_n, screen_s):
        super().__init__(brand_n, model_n)
        self.screen_size = screen_s

    def __str__(self):
        return f"Device brand: {self.get_brand_name()}\nDevice model: {self.get_model_name()}\nScreen size: {self.get_screen_size()}"

    def set_screen_size(self, screen_s):
        self.screen_size = screen_s

    def get_screen_size(self):
        return self.screen_size

    def power_check(self):
        print("This device needs a charger.")


class SmartWatch(MobileDevice):
    def __init__(self, brand_n, model_n, screen_s, mem_s):
        super().__init__(brand_n, model_n, screen_s)
        self.memory_size = mem_s

    def __str__(self):
        return f"Device brand: {self.get_brand_name()}\nDevice model: {self.get_model_name()}\nScreen size: {self.get_screen_size()}\nMemory size: {self.get_memory_size()}"

    def set_memory_size(self, mem_s):
        self.memory_size = mem_s

    def get_memory_size(self):
        return self.memory_size

    def power_check(self):
        print("This device has wireless charging.")


device = Device("Generic Brand", "Generic Model")
print(device)
device.power_check()
print("__________________________________________________________")

note_ten = MobileDevice("Samsung", "Note 10", 6)
print(note_ten)
note_ten.power_check()
print("__________________________________________________________")

apple_watch = SmartWatch("Apple", "series 5", 2.5, 64)
print(apple_watch)
apple_watch.power_check()
