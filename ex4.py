cars = 100
space_in_a_car = 4.0
drivers = 30
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven

print 'There are %s cars available.' % cars
print 'There are only %s drivers available.' % drivers
print 'There will be %s empty cars today.' % cars_not_driven
print 'We can transport %s people today.' % carpool_capacity
print 'We have %s passengers to carpool today.' % passengers
print 'We need to put about %s in each car.' % average_passengers_per_car

