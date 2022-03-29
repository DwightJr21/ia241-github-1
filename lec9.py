class car:
    
    maker = 'toyota'
    
    def report_maker(self):
        
        return self.maker
        
my_car = car()

print(my_car.maker)
print(my_car.report_maker())