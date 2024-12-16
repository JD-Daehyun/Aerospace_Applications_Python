


class Spaceship:
    def __init__(self, name, crew_capacity, speed) -> None:
         self.name = name
         self.crew_capacity = crew_capacity
         self.speed = speed

    def increase_speed(self):
         self.speed = self.speed + 10
         print(f'Speed is now at {self.speed}')
    
    def set_crew_capacity(self, capacity):
         print(f'Previous Crew Capacity {self.crew_capacity}')
         self.crew_capacity = capacity
         print(f'New Crew Capacity {self.crew_capacity}')

    def state_name(self):
         print(f'Hello, my name is {self.name}')




sp_1 = Spaceship('Daniel', 45, 400)

sp_1.increase_speed()
sp_1.set_crew_capacity(100)