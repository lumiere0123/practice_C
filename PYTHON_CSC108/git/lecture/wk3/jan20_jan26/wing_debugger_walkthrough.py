def print_time(minutes):
    print("Duration was", minutes, "minutes")
    
def convert_to_minutes(num_hours):
    # skipping docstring so it all fits in the screen. Don't do that!
    
    minutes = 60 * num_hours
    print_time(minutes)
    return minutes

lecture_hours = 3
lecture_minutes = convert_to_minutes(lecture_hours)
print(lecture_minutes)

#Quick intro into Wing's debugger
#You can watch video 4.5 on Coursera

#Set a breakpoint in line 7. To do this click on the gray area next
#to the line number. A red dot should appear. That's your breakpoint.
#If you click on this dot again, you can remove your breakpoint.
#Make sure you have the breakpoint set before you continue.

#Press the red bug icon. Once you do that execution will continue till
#it encounters the breakpoint. But it doesn't execute that line!

#Make sure you see the Stack Data window below. You have a stack frame
#convert_to_minutes(). That's the name of the function we are in.
#There's a separate frame for each function.
#If you look under locals, you can see we have a variable 
#num_hours (the function's parameter) which refers to value 3.

#----------------------------------------------
#Let's start using the Step Over button (or F6)
#----------------------------------------------
# If you press Step Over once, you see a new variable minutes got created
# in the convert_to_minutes() stack frame.

# If you press it one more time, you'll see that the call to function
# print_time(minutes) executed. You can see the output in the Debug I/O
# window (that's the tab next to the Python Shell).

# Notice that we didn't delve into function print_time. Step over 
# executes a line at a time, skipping the internals of a function 
# if this line contains a function call. 

# Now if you press Step Over one more time, you'll see that a <return value>
# appears in the stack frame.

# Press Step Over one more time and you'll see that the stack frame
# for function convert_to_minutes() dissapeared. Stack frames disappear
# when we exit a function. We are now in the global stack frame (called
# <module>(). We can see that a variable lecture_minutes was created
# which refers to value 180. This is due to the convert_to_minutes() function
# call.

#Press step-over one last time and you can see the value 180 in the Debug I/O
#window. 

#You can now press the red square button to stop debugging.

#----------------------------------------------
#Let's start using the Step Out button (or F7)
#----------------------------------------------

#We will now repeat this proces but we'll use the Step-Out button.
#We start by pressing the bug icon so we reach the breakpoint.
#Again we are in the convert_to_minutes() stack frame.

#If you press Step Out, you can see that we executed the entire 
#convert_to_minutes function including its return statement.
#You can see that the convert_to_minutes() stack frame vanished
#and the variable lecture_minutes which refers to value 180 was created.

#Step over is useful when we don't care about the internals of a function
#but just want to see the value it returns.

#You can press Step-Over one more time and you'll see that 180 is printed
#on Debug I/O and our debugging process completed (we reached the end of our 
#code)

#----------------------------------------------
#Let's start using the Step Into button (or F5)
#----------------------------------------------

#We'll finish this walk-through by using the Step Into button.
#Again press the bug icon. We are now inside the convert_to_minutes()
#stack frame.

#Press the Step-Into button. You can see that a new local variable, minutes,
#got created in the convert_to_minutes() stack frame.

#If you press the Step-Into button again, you can see that we are
#now inside the print_time() stack frame. So step-into allows us to go 
#inside a function body during a function call.
#Notice that we haven't yet executed the first instruction of the body of
#this function. So the stack frame of print_time() only contains a local
#variable called minutes (the function's parameter).
#This variable is different than the variable minutes which lives inside
# the convert_to_minutes stack frame. They just refer to the same value
# in our example.

#You can use the drop down menu next to the stack frame name to switch 
#between frames and see  how many exist at a given time. Right now there 
#are 3: the global frame, the convert_to_minutes() and the print_time().

#Press step-into one more time. The string "Duration was 180 minutes" is 
#printed on the Debug I/O window. 
#See how the return value of print_time() is None. This is because there is
#no explicit return statement.

#Once we press Step-Into one more time, the print_time() stack frame will
#disappear as we exit this function. 
#Now we are back to the convert_to_minutes() stack frame and a new variable
#minutes just got created.

#You can continue this process till you reach the end of your program
#or stop debugging.
