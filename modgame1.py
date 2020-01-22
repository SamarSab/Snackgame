import turtle
import time
import random

delay=0.1

# Score
score=0
high_score=0

m={1: "Setting" , 2: "Start" , 3: "Exit" }
print(m)

ch=int(input("Enter Your Choice:"))
if  ch==1 :
  print("------------SETTINGS------------")
  se={1: "Background color  (def. white)" ,2: "Snack color ( def. black)" ,3: "Food color (def. red)", 4: "Text color ( def.  black)", 5: "Return to main menu"}
  print(se)
  co=int(input("Enter Your Choice:"))
  if co==1 :
      bg=input("Enter the color for background(all letters in smallcase)")
  elif co==2 :
      sc=input("Enter the color of snake (all letters in smallcase)")
  elif  co==3 :
      fc=input("Enter the color of food (all letters in smallcase)")
  elif co==4 :
       tc=input("Enter the color of text (all letters in smallcase)")

if ch==2 :
# Set up the screen
  wn=turtle.Screen()
  wn.title("Snake Game by Bhavy, Anuj, Abhinav and Prabhjot")
  if co==1 :
     wn.bgcolor(bg)
  else:
     wn.bgcolor("white")
  wn.setup(width=600, height=600)
  wn.tracer(0) # Turns off the screen updates

  # Snake head
  head=turtle.Turtle()
  head.speed(0)
  head.shape("square")
  if co==2 :
    head.color(sc)
  else:
    head.color("black")
  head.penup()
  head.goto(0,1)
  head.direction="stop"

  # Snake food
  food=turtle.Turtle()
  food.speed(0)
  food.shape("circle")
  if co==3 :
    food.color(fc)
  else:
    food.color("red")
  food.penup()
  food.goto(0,100)

  segments=[]

  # Pen
  pen=turtle.Turtle()
  pen.speed(0)
  pen.shape("square")
  if co==4 :
    pen.color(tc)
  else: 
    pen.color("black")
  pen.penup()
  pen.hideturtle()
  pen.goto(0, 260)
  pen.write("Score: 0  High Score: 0", align="center", font=("Courier", 24, "normal"))

  # Functions
  def go_up():
      if head.direction != "down" :
          head.direction="up"

  def go_down():
      if head.direction != "up" :
          head.direction="down"

  def go_left():
      if head.direction != "right" :
          head.direction="left"

  def go_right():
      if head.direction != "left" :
          head.direction="right"

  def move():
      if head.direction == "up" :
          y=head.ycor()
          head.sety(y + 20)

      if head.direction == "down" :
          y=head.ycor()
          head.sety(y - 20)

      if head.direction == "left" :
          x=head.xcor()
          head.setx(x - 20)

      if head.direction == "right" :
          x=head.xcor()
          head.setx(x + 20)

  # Keyboard bindings
  wn.listen()
  wn.onkeypress(go_up, "8")
  wn.onkeypress(go_down, "2")
  wn.onkeypress(go_left, "4")
  wn.onkeypress(go_right, "6")

  # Main game loop
  while True:
      wn.update()
  
      # Check for a collision with the border
      if head.xcor()>290 or head.xcor()<-290 or head.ycor()>290 or head.ycor()<-290 :
          time.sleep(1)
          head.goto(0,0)
          head.direction="stop"
  
          # Hide the segments
          for segment in segments:
              segment.goto(1000, 1000)
          
          # Clear the segments list
          segments.clear()
  
          # Reset the score
          score=0
  
          # Reset the delay
          delay=0.1
  
          pen.clear()
          pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal")) 
  
  
      # Check for a collision with the food
      if head.distance(food) < 20 :
          # Move the food to a random spot
          x=random.randint(-290, 290)
          y=random.randint(-290, 290)
          food.goto(x,y)
  
          # Add a segment
          new_segment=turtle.Turtle()
          new_segment.speed(0)
          new_segment.shape("square")
          new_segment.color("grey")
          new_segment.penup()
          segments.append(new_segment)
  
          # Shorten the delay
          delay -= 0.001
  
          # Increase the score
          score +=1
  
          if score > high_score :
              high_score=score
        
          pen.clear()
          pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal")) 
  
      # Move the end segments first in reverse order
      for index in range(len(segments)-1, 0, -1):
          x=segments[index-1].xcor()
          y=segments[index-1].ycor()
          segments[index].goto(x, y)
  
      # Move segment 0 to where the head is
      if len(segments) > 0 :
          x=head.xcor()
          y=head.ycor()
          segments[0].goto(x,y)
  
      move()    
  
      # Check for head collision with the body segments
      for segment in segments:
          if segment.distance(head) < 20 :
              time.sleep(9)
              head.goto(0,0)
              head.direction="stop"
          
              # Hide the segments
              for segment in segments:
                  segment.goto(1000, 1000)
          
              # Clear the segments list
              segments.clear()
  
              # Reset the score
              score=0
  
              # Reset the delay
              delay=0.1
          
              # Update the score display
              pen.clear()
              pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))
  
      time.sleep(delay)
  
  wn.mainloop()
  
if ch==3 :
   exit()


