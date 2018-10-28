import turtle
import time
import random

class TrackDesign:
	def __init__(self):
		self.car = turtle.Turtle()
		self.screen = turtle.Screen()
		self.team = {"Mercedes":"#00D2BE", "Ferrari":"#DC0000", "RedBull":"#00327D", "Renault":"#FFF500",
		"ForceIndia":"#F596C8", "McLaren":"#FF8700"}
		self.eraser = turtle.Turtle()
		self.time = turtle.Turtle()

	def track(self, team, i):
		self.screen.setup(500,500)
		self.screen.title("Suzuka Circuit Map")
		self.car.color(team)
		self.time.hideturtle()

		for name, color in self.team.items():
			if color == team:
				self.eraser.hideturtle()
				self.eraser.penup()
				self.eraser.color(team)
				self.eraser.goto(-150, -150)
				self.eraser.write(name,font=("TimesNewRoman",20,"bold"))
				teamname = name

		startLap = time.time()

		self.car.pensize(4)
		self.car.penup()
		self.car.speed(0)
		self.car.goto(-80,-80)
		self.car.speed(0)
		self.car.pendown()

		self.car.setheading(190)
		self.straightLine(65,1)

		# First Turn
		self.car.setheading(200)
		self.turnRight(90, 20)
		self.turnRight(90, 10)
		self.turnRight(10, 10)

		# Short Straight
		self.straightLine(30,1)

		# 'S' Curves
		# First Curve
		self.turnLeft(20,10)
		self.turnLeft(40,10)
		self.turnRight(20,30)
		self.turnRight(80,10)
		self.car.setheading(340)
		self.straightLine(15,1)

		# Second Curve
		self.turnLeft(80,10)
		self.straightLine(10,1)
		self.turnRight(60,20)
		self.straightLine(3,1)
		self.turnRight(50,10)
		self.straightLine(20,1)

		# Turn 7
		self.turnLeft(60,10)
		self.turnLeft(20,20)
		self.turnLeft(5,20)		
		self.straightLine(5,1)

		# Dunlop Curve
		self.straightLine(5,1)
		self.turnLeft(10,10)
		for i in range(50):
			self.car.left(1)
			self.straightLine(1,1)
		self.car.setheading(110)
		self.straightLine(30,1)

		# Degner Curve
		self.turnRight(40,10)	
		self.straightLine(30,1)

		# Turn 9
		self.turnRight(10, 20)
		self.car.right(80)
		self.straightLine(80, 1)

		# Hairpin
		self.turnRight(30, 10)
		self.straightLine(30, 1)
		for i in range(25):
			self.car.left(8)
			self.straightLine(1,1)
		self.turnRight(20,10)

		# Towards turn 12
		self.straightLine(20,1)
		for i in range(20):
			if i == 10:
				self.turnRight(10, 1)
			if i >= 15:
				self.straightLine(10,1)
				self.turnRight(4,1)
			if i >= 18:
				self.turnRight(5,1)	
			self.turnRight(5,1)
			self.straightLine(4,1)

		# Spoon Curve
		self.straightLine(20,1)
		self.turnLeft(90, 20)
		self.straightLine(10,1)
		self.turnLeft(70, 10)
		for i in range(11):
			self.straightLine(2,1)
			self.turnLeft(5,1)

		# Longest Straight
		self.straightLine(60,1)
		for i in range(4):
			self.turnLeft(1,5)
			self.straightLine(2,1)
		self.straightLine(130,1)

		# Turn 15
		self.turnLeft(40,3)
		self.straightLine(20,1)
		self.turnLeft(20,2)
		self.straightLine(30,1)
		self.turnLeft(20,10)
		self.straightLine(20,1)

		# Casino Triangle
		self.turnRight(80,2)
		self.straightLine(10,1)
		for i in range(4):
			self.turnLeft(20,2)
			self.straightLine(1,1)
		self.straightLine(5,1)
		self.turnRight(3,1)

		for i in range(22):
			self.turnRight(1,1)
			self.straightLine(2,1)

		# Towards Lap Completion
		self.straightLine(20,1)
		self.car.goto(-80,-80)

		# self.time.clear()
		self.time.forward(15)
		self.time.color("#000000")
		self.time.write("Lap Time: "+ str(75 + time.time() - startLap - random.random() + random.random())[:6] + " s : "+teamname,font=("TimesNewRoman",11,"bold"))
		self.screen.delay(400)

	def straightLine(self, distance, speed):
		for i in range(0,distance,speed):
			self.car.forward(speed)

	def turnLeft(self, angle, radius):
		step = 10*3.14*radius/360
		for i in range(0,angle,5):
			self.car.left(5)
			self.car.forward(step)

	def turnRight(self, angle, radius):
		step = 10*3.14*radius/360
		for i in range(0,angle,5):
			self.car.right(5)
			self.car.forward(step)

	def laps(self):
		self.time.hideturtle()
		self.time.right(90)
		self.time.penup()
		self.time.goto(-160, -180)
		for i in range(10):
			self.eraser.clear()
			self.track(self.team[list(self.team.keys())[i%6]], i)
			self.screen.delay(10)
		turtle.done()

if __name__ == '__main__':
	design = TrackDesign()
	design.laps()