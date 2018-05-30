#!/usr/bin/env python
# -*- coding: utf-8 -*-

import roslib
import rospy

from geometry_msgs.msg import Twist
from std_msgs.msg import Float32

import sys, select, termios, tty


starting_msg = """
-------------Teleop Program for Waiter Robot--------------



Hello~ Greetings from Chee Wah :P Please choose mode:

|-------------------------------------------------------|
|                 2-D Translation Movement              |
|‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|
|  ↖   press 'q'      ↑   press 'w'       ↗   press 'e' | 
|  ←   press 'a'                          →   press 'd' | 
|  ↙   press 'z'      ↓   press 'x'       ↘   press 'c' | 
|-------------------------------------------------------|


|-------------------------------------------------------|
|                  2-D Rotation Movement                |
|‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|
|  ⟲   press 'f'                           ⟳  press 'h' | 
|-------------------------------------------------------|


|-------------------------------------------------------|
|                    Scissor Movement                   |
|‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|
|  ⤉   press 'v'                          ⤈  press 'n'  | 
|-------------------------------------------------------|


|-------------------------------------------------------|
|                  Tray Delivery Movement               |
|‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|
|  ⇞   press 'r'      ↹   press 't'       ⇟  press 'y'  | 
|-------------------------------------------------------|


Press Esc to quit program! :D



-------------Teleop Program for Waiter Robot--------------
"""


def encoder5_subscriber_callback(msg): # TODO(Loy Chee Wah): Create the soft limit of Z scissors motor
	if False: #TODO : if motor hit soft limit!
		pass
		 


def getKey():
	tty.setraw(sys.stdin.fileno())
	select.select([sys.stdin], [], [], 0)
	key = sys.stdin.read(1)
	termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)
	return key


def upward_translation():
	
	upward_translation_speed_variable = 0.00
	active_upward_translation_speed	= 0.00
	upward_translation_msg = """
-----------Upward Translation for Waiter Robot------------



|-------------------------------------------------------|
|               Upward Translation Movement             |
|‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|
|                 Speed variable = %.2f                 | 
|             Current relative speed = %.2f             |
|                                                       |
|                   Max speed = 0.50                    |
|  ⇑   press 'g'                         ⇓   press 'b'  | 
|                                                       |
|                                                       |
|                     Motor %s                     |
|         To toggle start/stop motor, press 's'         |
|           To stop motor and exit, press Esc           |
|-------------------------------------------------------|




-----------Upward Translation for Waiter Robot------------
"""
	
	import os
	twist = Twist()
	twist.linear.x = 0; twist.linear.y = 0; twist.linear.z = 0
	twist.angular.x = 0; twist.angular.y = 0; twist.angular.z = 0
	for count in range (0,10):	
		cmd_vel_publisher.publish(twist)
	while True:	
		os.system('clear')
		if active_upward_translation_speed == 0.00: #motor stopped
			motor_state = "stopped"
		else: #motor started
			motor_state = "started"		
		print upward_translation_msg %(abs(upward_translation_speed_variable), abs(active_upward_translation_speed), motor_state)
		key_respond_from_user = getKey()
		if key_respond_from_user == '\x1b': #Esc key
			twist.linear.x = 0; twist.linear.y = 0; twist.linear.z = 0
			twist.angular.x = 0; twist.angular.y = 0; twist.angular.z = 0
			for count in range (0,10):			
				cmd_vel_publisher.publish(twist)
			upward_translation_speed_variable = 0.00
			active_upward_translation_speed = 0.00
			break
		elif key_respond_from_user == 's': #start/stop motor
			if upward_translation_speed_variable != active_upward_translation_speed: #motor have stopped, now start motor
				active_upward_translation_speed = upward_translation_speed_variable
				twist.linear.x = active_upward_translation_speed; twist.linear.y = 0; twist.linear.z = 0
				twist.angular.x = 0; twist.angular.y = 0; twist.angular.z = 0
				for count in range (0,10):				
					cmd_vel_publisher.publish(twist)
			else: #motor is started, now stop motor
				active_upward_translation_speed = 0.00
				twist.linear.x = active_upward_translation_speed; twist.linear.y = 0; twist.linear.z = 0
				twist.angular.x = 0; twist.angular.y = 0; twist.angular.z = 0
				for count in range (0,10):					
					cmd_vel_publisher.publish(twist)
				
		elif key_respond_from_user == 'g': #increase speed
			if upward_translation_speed_variable < 0.50:
				upward_translation_speed_variable += 0.01
				if active_upward_translation_speed != 0.00: #motor is moving
					active_upward_translation_speed = upward_translation_speed_variable
					twist.linear.x = active_upward_translation_speed; twist.linear.y = 0; twist.linear.z = 0
					twist.angular.x = 0; twist.angular.y = 0; twist.angular.z = 0
					for count in range (0,10):					
						cmd_vel_publisher.publish(twist)
				
		elif key_respond_from_user == 'b': #decrease speed
			if upward_translation_speed_variable > 0.00:
				upward_translation_speed_variable -= 0.01
				if active_upward_translation_speed != 0.00: #motor is moving				
					active_upward_translation_speed = upward_translation_speed_variable
					twist.linear.x = active_upward_translation_speed; twist.linear.y = 0; twist.linear.z = 0
					twist.angular.x = 0; twist.angular.y = 0; twist.angular.z = 0
					for count in range (0,10):						
						cmd_vel_publisher.publish(twist)

def downward_translation():
	
	downward_translation_speed_variable = 0.00
	active_downward_translation_speed = 0.00
	downward_translation_msg = """
----------Downward Translation for Waiter Robot-----------



|-------------------------------------------------------|
|              Downward Translation Movement            |
|‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|
|                 Speed variable = %.2f                 | 
|             Current relative speed = %.2f             |
|                                                       |
|                   Max speed = 0.50                    |
|  ⇑   press 'g'                         ⇓   press 'b'  | 
|                                                       |
|                                                       |
|                     Motor %s                     |
|         To toggle start/stop motor, press 's'         |
|           To stop motor and exit, press Esc           |
|-------------------------------------------------------|




----------Downward Translation for Waiter Robot-----------
"""
	
	import os
	twist = Twist()
	twist.linear.x = 0; twist.linear.y = 0; twist.linear.z = 0
	twist.angular.x = 0; twist.angular.y = 0; twist.angular.z = 0
	for count in range (0,10):	
		cmd_vel_publisher.publish(twist)
	while True:	
		os.system('clear')
		if active_downward_translation_speed == 0.00: #motor stopped
			motor_state = "stopped"
		else: #motor started
			motor_state = "started"		
		print downward_translation_msg %(abs(downward_translation_speed_variable), abs(active_downward_translation_speed), motor_state)
		key_respond_from_user = getKey()
		if key_respond_from_user == '\x1b': #Esc key
			twist.linear.x = 0; twist.linear.y = 0; twist.linear.z = 0
			twist.angular.x = 0; twist.angular.y = 0; twist.angular.z = 0
			for count in range (0,10):			
				cmd_vel_publisher.publish(twist)
			downward_translation_speed_variable = 0.00
			active_downward_translation_speed = 0.00
			break
		elif key_respond_from_user == 's': #start/stop motor
			if downward_translation_speed_variable != active_downward_translation_speed: #motor have stopped, now start motor
				active_downward_translation_speed = downward_translation_speed_variable
				twist.linear.x = -(active_downward_translation_speed); twist.linear.y = 0; twist.linear.z = 0
				twist.angular.x = 0; twist.angular.y = 0; twist.angular.z = 0
				for count in range (0,10):				
					cmd_vel_publisher.publish(twist)
			else: #motor is started, now stop motor
				active_downward_translation_speed = 0.00
				twist.linear.x = -(active_downward_translation_speed); twist.linear.y = 0; twist.linear.z = 0
				twist.angular.x = 0; twist.angular.y = 0; twist.angular.z = 0
				for count in range (0,10):				
					cmd_vel_publisher.publish(twist)
				
		elif key_respond_from_user == 'g': #increase speed
			if downward_translation_speed_variable < 0.50:
				downward_translation_speed_variable += 0.01
				if active_downward_translation_speed != 0.00: #motor is moving
					active_downward_translation_speed = downward_translation_speed_variable
					twist.linear.x = -(active_downward_translation_speed); twist.linear.y = 0; twist.linear.z = 0
					twist.angular.x = 0; twist.angular.y = 0; twist.angular.z = 0
					for count in range (0,10):					
						cmd_vel_publisher.publish(twist)
				
		elif key_respond_from_user == 'b': #decrease speed
			if downward_translation_speed_variable > 0.00:
				downward_translation_speed_variable -= 0.01
				if active_downward_translation_speed != 0.00: #motor is moving				
					active_downward_translation_speed = downward_translation_speed_variable
					twist.linear.x = -(active_downward_translation_speed); twist.linear.y = 0; twist.linear.z = 0
					twist.angular.x = 0; twist.angular.y = 0; twist.angular.z = 0
					for count in range (0,10):					
						cmd_vel_publisher.publish(twist)

def leftward_translation():
	
	leftward_translation_speed_variable = 0.00
	active_leftward_translation_speed = 0.00
	leftward_translation_msg = """
----------Leftward Translation for Waiter Robot-----------



|-------------------------------------------------------|
|              Leftward Translation Movement            |
|‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|
|                 Speed variable = %.2f                 | 
|             Current relative speed = %.2f             |
|                                                       |
|                   Max speed = 0.50                    |
|  ⇑   press 'g'                         ⇓   press 'b'  | 
|                                                       |
|                                                       |
|                     Motor %s                     |
|         To toggle start/stop motor, press 's'         |
|           To stop motor and exit, press Esc           |
|-------------------------------------------------------|




----------Leftward Translation for Waiter Robot-----------
"""
	
	import os
	twist = Twist()
	twist.linear.x = 0; twist.linear.y = 0; twist.linear.z = 0
	twist.angular.x = 0; twist.angular.y = 0; twist.angular.z = 0
	for count in range (0,10):	
		cmd_vel_publisher.publish(twist)
	while True:	
		os.system('clear')
		if active_leftward_translation_speed == 0.00: #motor stopped
			motor_state = "stopped"
		else: #motor started
			motor_state = "started"		
		print leftward_translation_msg %(abs(leftward_translation_speed_variable), abs(active_leftward_translation_speed), motor_state)
		key_respond_from_user = getKey()
		if key_respond_from_user == '\x1b': #Esc key
			twist.linear.x = 0; twist.linear.y = 0; twist.linear.z = 0
			twist.angular.x = 0; twist.angular.y = 0; twist.angular.z = 0
			for count in range (0,10):			
				cmd_vel_publisher.publish(twist)
			leftward_translation_speed_variable = 0.00
			active_leftward_translation_speed = 0.00
			break
		elif key_respond_from_user == 's': #start/stop motor
			if leftward_translation_speed_variable != active_leftward_translation_speed: #motor have stopped, now start motor
				active_leftward_translation_speed = leftward_translation_speed_variable
				twist.linear.x = 0; twist.linear.y = -(active_leftward_translation_speed); twist.linear.z = 0
				twist.angular.x = 0; twist.angular.y = 0; twist.angular.z = 0
				for count in range (0,10):				
					cmd_vel_publisher.publish(twist)
			else: #motor is started, now stop motor
				active_leftward_translation_speed = 0.00
				twist.linear.x = 0; twist.linear.y = -(active_leftward_translation_speed); twist.linear.z = 0
				twist.angular.x = 0; twist.angular.y = 0; twist.angular.z = 0
				for count in range (0,10):				
					cmd_vel_publisher.publish(twist)
				
		elif key_respond_from_user == 'g': #increase speed
			if leftward_translation_speed_variable < 0.50:
				leftward_translation_speed_variable += 0.01
				if active_leftward_translation_speed != 0.00: #motor is moving
					active_leftward_translation_speed = leftward_translation_speed_variable
					twist.linear.x = 0; twist.linear.y = -(active_leftward_translation_speed); twist.linear.z = 0
					twist.angular.x = 0; twist.angular.y = 0; twist.angular.z = 0
					for count in range (0,10):					
						cmd_vel_publisher.publish(twist)
				
		elif key_respond_from_user == 'b': #decrease speed
			if leftward_translation_speed_variable > 0.00:
				leftward_translation_speed_variable -= 0.01
				if active_leftward_translation_speed != 0.00: #motor is moving				
					active_leftward_translation_speed = leftward_translation_speed_variable
					twist.linear.x = 0; twist.linear.y = -(active_leftward_translation_speed); twist.linear.z = 0
					twist.angular.x = 0; twist.angular.y = 0; twist.angular.z = 0
					for count in range (0,10):					
						cmd_vel_publisher.publish(twist)

def rightward_translation():
	
	rightward_translation_speed_variable = 0.00
	active_rightward_translation_speed = 0.00
	rightward_translation_msg = """
----------Rightward Translation for Waiter Robot----------



|-------------------------------------------------------|
|             Rightward Translation Movement            |
|‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|
|                 Speed variable = %.2f                 | 
|             Current relative speed = %.2f             |
|                                                       |
|                   Max speed = 0.50                    |
|  ⇑   press 'g'                         ⇓   press 'b'  | 
|                                                       |
|                                                       |
|                     Motor %s                     |
|         To toggle start/stop motor, press 's'         |
|           To stop motor and exit, press Esc           |
|-------------------------------------------------------|




----------Rightward Translation for Waiter Robot----------
"""
	
	import os
	twist = Twist()
	twist.linear.x = 0; twist.linear.y = 0; twist.linear.z = 0
	twist.angular.x = 0; twist.angular.y = 0; twist.angular.z = 0
	for count in range (0,10):	
		cmd_vel_publisher.publish(twist)
	while True:	
		os.system('clear')
		if active_rightward_translation_speed == 0.00: #motor stopped
			motor_state = "stopped"
		else: #motor started
			motor_state = "started"		
		print rightward_translation_msg %(abs(rightward_translation_speed_variable), abs(active_rightward_translation_speed), motor_state)
		key_respond_from_user = getKey()
		if key_respond_from_user == '\x1b': #Esc key
			twist.linear.x = 0; twist.linear.y = 0; twist.linear.z = 0
			twist.angular.x = 0; twist.angular.y = 0; twist.angular.z = 0
			for count in range (0,10):			
				cmd_vel_publisher.publish(twist)
			rightward_translation_speed_variable = 0.00
			active_rightward_translation_speed = 0.00
			break
		elif key_respond_from_user == 's': #start/stop motor
			if rightward_translation_speed_variable != active_rightward_translation_speed: #motor have stopped, now start motor
				active_rightward_translation_speed = rightward_translation_speed_variable
				twist.linear.x = 0; twist.linear.y = active_rightward_translation_speed; twist.linear.z = 0
				twist.angular.x = 0; twist.angular.y = 0; twist.angular.z = 0
				for count in range (0,10):				
					cmd_vel_publisher.publish(twist)
			else: #motor is started, now stop motor
				active_rightward_translation_speed = 0.00
				twist.linear.x = 0; twist.linear.y = active_rightward_translation_speed; twist.linear.z = 0
				twist.angular.x = 0; twist.angular.y = 0; twist.angular.z = 0
				for count in range (0,10):				
					cmd_vel_publisher.publish(twist)
				
		elif key_respond_from_user == 'g': #increase speed
			if rightward_translation_speed_variable < 0.50:
				rightward_translation_speed_variable += 0.01
				if active_rightward_translation_speed != 0.00: #motor is moving
					active_rightward_translation_speed = rightward_translation_speed_variable
					twist.linear.x = 0; twist.linear.y = active_rightward_translation_speed; twist.linear.z = 0
					twist.angular.x = 0; twist.angular.y = 0; twist.angular.z = 0
					for count in range (0,10):					
						cmd_vel_publisher.publish(twist)
				
		elif key_respond_from_user == 'b': #decrease speed
			if rightward_translation_speed_variable > 0.00:
				rightward_translation_speed_variable -= 0.01
				if active_rightward_translation_speed != 0.00: #motor is moving				
					active_rightward_translation_speed = rightward_translation_speed_variable
					twist.linear.x = 0; twist.linear.y = active_rightward_translation_speed; twist.linear.z = 0
					twist.angular.x = 0; twist.angular.y = 0; twist.angular.z = 0
					for count in range (0,10):					
						cmd_vel_publisher.publish(twist)

def upward_left_translation():
	
	upward_left_translation_speed_variable = 0.00
	active_upward_left_translation_speed = 0.00
	upward_left_translation_msg = """
---------Upward Left Translation for Waiter Robot---------



|-------------------------------------------------------|
|            Upward Left Translation Movement           |
|‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|
|                 Speed variable = %.2f                 | 
|             Current relative speed = %.2f             |
|                                                       |
|                   Max speed = 0.50                    |
|  ⇑   press 'g'                         ⇓   press 'b'  | 
|                                                       |
|                                                       |
|                     Motor %s                     |
|         To toggle start/stop motor, press 's'         |
|           To stop motor and exit, press Esc           |
|-------------------------------------------------------|




---------Upward Left Translation for Waiter Robot---------
"""
	
	import os
	twist = Twist()
	twist.linear.x = 0; twist.linear.y = 0; twist.linear.z = 0
	twist.angular.x = 0; twist.angular.y = 0; twist.angular.z = 0
	for count in range (0,10):	
		cmd_vel_publisher.publish(twist)
	while True:	
		os.system('clear')
		if active_upward_left_translation_speed == 0.00: #motor stopped
			motor_state = "stopped"
		else: #motor started
			motor_state = "started"		
		print upward_left_translation_msg %(abs(upward_left_translation_speed_variable), abs(active_upward_left_translation_speed), motor_state)
		key_respond_from_user = getKey()
		if key_respond_from_user == '\x1b': #Esc key
			twist.linear.x = 0; twist.linear.y = 0; twist.linear.z = 0
			twist.angular.x = 0; twist.angular.y = 0; twist.angular.z = 0
			for count in range (0,10):			
				cmd_vel_publisher.publish(twist)
			upward_left_translation_speed_variable = 0.00
			active_upward_left_translation_speed = 0.00
			break
		elif key_respond_from_user == 's': #start/stop motor
			if upward_left_translation_speed_variable != active_upward_left_translation_speed: #motor have stopped, now start motor
				active_upward_left_translation_speed = upward_left_translation_speed_variable
				twist.linear.x = active_upward_left_translation_speed; twist.linear.y = -(active_upward_left_translation_speed); twist.linear.z = 0
				twist.angular.x = 0; twist.angular.y = 0; twist.angular.z = 0
				for count in range (0,10):				
					cmd_vel_publisher.publish(twist)
			else: #motor is started, now stop motor
				active_upward_left_translation_speed = 0.00
				twist.linear.x = active_upward_left_translation_speed; twist.linear.y = -(active_upward_left_translation_speed); twist.linear.z = 0
				twist.angular.x = 0; twist.angular.y = 0; twist.angular.z = 0
				for count in range (0,10):				
					cmd_vel_publisher.publish(twist)
				
		elif key_respond_from_user == 'g': #increase speed
			if upward_left_translation_speed_variable < 0.50:
				upward_left_translation_speed_variable += 0.01
				if active_upward_left_translation_speed != 0.00: #motor is moving
					active_upward_left_translation_speed = upward_left_translation_speed_variable
					twist.linear.x = active_upward_left_translation_speed; twist.linear.y = -(active_upward_left_translation_speed); twist.linear.z = 0
					twist.angular.x = 0; twist.angular.y = 0; twist.angular.z = 0
					for count in range (0,10):					
						cmd_vel_publisher.publish(twist)
				
		elif key_respond_from_user == 'b': #decrease speed
			if upward_left_translation_speed_variable > 0.00:
				upward_left_translation_speed_variable -= 0.01
				if active_upward_left_translation_speed != 0.00: #motor is moving				
					active_upward_left_translation_speed = upward_left_translation_speed_variable
					twist.linear.x = active_upward_left_translation_speed; twist.linear.y = -(active_upward_left_translation_speed); twist.linear.z = 0
					twist.angular.x = 0; twist.angular.y = 0; twist.angular.z = 0
					for count in range (0,10):					
						cmd_vel_publisher.publish(twist)

def upward_right_translation():
	
	upward_right_translation_speed_variable = 0.00
	active_upward_right_translation_speed = 0.00
	upward_right_translation_msg = """
---------Upward Right Translation for Waiter Robot--------



|-------------------------------------------------------|
|           Upward Right Translation Movement           |
|‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|
|                 Speed variable = %.2f                 | 
|             Current relative speed = %.2f             |
|                                                       |
|                   Max speed = 0.50                    |
|  ⇑   press 'g'                         ⇓   press 'b'  | 
|                                                       |
|                                                       |
|                     Motor %s                     |
|         To toggle start/stop motor, press 's'         |
|           To stop motor and exit, press Esc           |
|-------------------------------------------------------|




---------Upward Right Translation for Waiter Robot--------
"""
	
	import os
	twist = Twist()
	twist.linear.x = 0; twist.linear.y = 0; twist.linear.z = 0
	twist.angular.x = 0; twist.angular.y = 0; twist.angular.z = 0
	for count in range (0,10):	
		cmd_vel_publisher.publish(twist)
	while True:	
		os.system('clear')
		if active_upward_right_translation_speed == 0.00: #motor stopped
			motor_state = "stopped"
		else: #motor started
			motor_state = "started"		
		print upward_right_translation_msg %(abs(upward_right_translation_speed_variable), abs(active_upward_right_translation_speed), motor_state)
		key_respond_from_user = getKey()
		if key_respond_from_user == '\x1b': #Esc key
			twist.linear.x = 0; twist.linear.y = 0; twist.linear.z = 0
			twist.angular.x = 0; twist.angular.y = 0; twist.angular.z = 0
			for count in range (0,10):
				cmd_vel_publisher.publish(twist)
			upward_right_translation_speed_variable = 0.00
			active_upward_right_translation_speed = 0.00
			break
		elif key_respond_from_user == 's': #start/stop motor
			if upward_right_translation_speed_variable != active_upward_right_translation_speed: #motor have stopped, now start motor
				active_upward_right_translation_speed = upward_right_translation_speed_variable
				twist.linear.x = active_upward_right_translation_speed; twist.linear.y = active_upward_right_translation_speed; twist.linear.z = 0
				twist.angular.x = 0; twist.angular.y = 0; twist.angular.z = 0
				for count in range (0,10):				
					cmd_vel_publisher.publish(twist)
			else: #motor is started, now stop motor
				active_upward_right_translation_speed = 0.00
				twist.linear.x = active_upward_right_translation_speed; twist.linear.y = active_upward_right_translation_speed; twist.linear.z = 0
				twist.angular.x = 0; twist.angular.y = 0; twist.angular.z = 0
				for count in range (0,10):
					cmd_vel_publisher.publish(twist)
				
		elif key_respond_from_user == 'g': #increase speed
			if upward_right_translation_speed_variable < 0.50:
				upward_right_translation_speed_variable += 0.01
				if active_upward_right_translation_speed != 0.00: #motor is moving
					active_upward_right_translation_speed = upward_right_translation_speed_variable
					twist.linear.x = active_upward_right_translation_speed; twist.linear.y = active_upward_right_translation_speed; twist.linear.z = 0
					twist.angular.x = 0; twist.angular.y = 0; twist.angular.z = 0
					for count in range (0,10):					
						cmd_vel_publisher.publish(twist)
				
		elif key_respond_from_user == 'b': #decrease speed
			if upward_right_translation_speed_variable > 0.00:
				upward_right_translation_speed_variable -= 0.01
				if active_upward_right_translation_speed != 0.00: #motor is moving				
					active_upward_right_translation_speed = upward_right_translation_speed_variable
					twist.linear.x = active_upward_right_translation_speed; twist.linear.y = active_upward_right_translation_speed; twist.linear.z = 0
					twist.angular.x = 0; twist.angular.y = 0; twist.angular.z = 0
					for count in range (0,10):					
						cmd_vel_publisher.publish(twist)

def downward_left_translation():
	
	downward_left_translation_speed_variable = 0.00
	active_downward_left_translation_speed = 0.00
	downward_left_translation_msg = """
--------Downward Left Translation for Waiter Robot--------



|-------------------------------------------------------|
|           Downward Left Translation Movement          |
|‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|
|                 Speed variable = %.2f                 | 
|             Current relative speed = %.2f             |
|                                                       |
|                   Max speed = 0.50                    |
|  ⇑   press 'g'                         ⇓   press 'b'  | 
|                                                       |
|                                                       |
|                     Motor %s                     |
|         To toggle start/stop motor, press 's'         |
|           To stop motor and exit, press Esc           |
|-------------------------------------------------------|




--------Downward Left Translation for Waiter Robot--------
"""
	
	import os
	twist = Twist()
	twist.linear.x = 0; twist.linear.y = 0; twist.linear.z = 0
	twist.angular.x = 0; twist.angular.y = 0; twist.angular.z = 0
	for count in range (0,10):	
		cmd_vel_publisher.publish(twist)
	while True:	
		os.system('clear')
		if active_downward_left_translation_speed == 0.00: #motor stopped
			motor_state = "stopped"
		else: #motor started
			motor_state = "started"		
		print downward_left_translation_msg %(abs(downward_left_translation_speed_variable), abs(active_downward_left_translation_speed), motor_state)
		key_respond_from_user = getKey()
		if key_respond_from_user == '\x1b': #Esc key
			twist.linear.x = 0; twist.linear.y = 0; twist.linear.z = 0
			twist.angular.x = 0; twist.angular.y = 0; twist.angular.z = 0
			for count in range (0,10):			
				cmd_vel_publisher.publish(twist)
			downward_left_translation_speed_variable = 0.00
			active_downward_left_translation_speed = 0.00
			break
		elif key_respond_from_user == 's': #start/stop motor
			if downward_left_translation_speed_variable != active_downward_left_translation_speed: #motor have stopped, now start motor
				active_downward_left_translation_speed = downward_left_translation_speed_variable
				twist.linear.x = -(active_downward_left_translation_speed); twist.linear.y = -(active_downward_left_translation_speed); twist.linear.z = 0
				twist.angular.x = 0; twist.angular.y = 0; twist.angular.z = 0
				for count in range (0,10):				
					cmd_vel_publisher.publish(twist)
			else: #motor is started, now stop motor
				active_downward_left_translation_speed = 0.00
				twist.linear.x = -(active_downward_left_translation_speed); twist.linear.y = -(active_downward_left_translation_speed); twist.linear.z = 0
				twist.angular.x = 0; twist.angular.y = 0; twist.angular.z = 0
				for count in range (0,10):				
					cmd_vel_publisher.publish(twist)
				
		elif key_respond_from_user == 'g': #increase speed
			if downward_left_translation_speed_variable < 0.50:
				downward_left_translation_speed_variable += 0.01
				if active_downward_left_translation_speed != 0.00: #motor is moving
					active_downward_left_translation_speed = downward_left_translation_speed_variable
					twist.linear.x = -(active_downward_left_translation_speed); twist.linear.y = -(active_downward_left_translation_speed); twist.linear.z = 0
					twist.angular.x = 0; twist.angular.y = 0; twist.angular.z = 0
					for count in range (0,10):					
						cmd_vel_publisher.publish(twist)
				
		elif key_respond_from_user == 'b': #decrease speed
			if downward_left_translation_speed_variable > 0.00:
				downward_left_translation_speed_variable -= 0.01
				if active_downward_left_translation_speed != 0.00: #motor is moving				
					active_downward_left_translation_speed = downward_left_translation_speed_variable
					twist.linear.x = -(active_downward_left_translation_speed); twist.linear.y = -(active_downward_left_translation_speed); twist.linear.z = 0
					twist.angular.x = 0; twist.angular.y = 0; twist.angular.z = 0
					for count in range (0,10):					
						cmd_vel_publisher.publish(twist)

def downward_right_translation():
	
	downward_right_translation_speed_variable = 0.00
	active_downward_right_translation_speed = 0.00
	downward_right_translation_msg = """
--------Downward Right Translation for Waiter Robot-------



|-------------------------------------------------------|
|          Downward Right Translation Movement          |
|‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|
|                 Speed variable = %.2f                 | 
|             Current relative speed = %.2f             |
|                                                       |
|                   Max speed = 0.50                    |
|  ⇑   press 'g'                         ⇓   press 'b'  | 
|                                                       |
|                                                       |
|                     Motor %s                     |
|         To toggle start/stop motor, press 's'         |
|           To stop motor and exit, press Esc           |
|-------------------------------------------------------|




--------Downward Right Translation for Waiter Robot-------
"""
	
	import os
	twist = Twist()
	twist.linear.x = 0; twist.linear.y = 0; twist.linear.z = 0
	twist.angular.x = 0; twist.angular.y = 0; twist.angular.z = 0
	for count in range (0,10):	
		cmd_vel_publisher.publish(twist)
	while True:	
		os.system('clear')
		if active_downward_right_translation_speed == 0.00: #motor stopped
			motor_state = "stopped"
		else: #motor started
			motor_state = "started"		
		print downward_right_translation_msg %(abs(downward_right_translation_speed_variable), abs(active_downward_right_translation_speed), motor_state)
		key_respond_from_user = getKey()
		if key_respond_from_user == '\x1b': #Esc key
			twist.linear.x = 0; twist.linear.y = 0; twist.linear.z = 0
			twist.angular.x = 0; twist.angular.y = 0; twist.angular.z = 0
			for count in range (0,10):			
				cmd_vel_publisher.publish(twist)
			downward_right_translation_speed_variable = 0.00
			active_downward_right_translation_speed = 0.00
			break
		elif key_respond_from_user == 's': #start/stop motor
			if downward_right_translation_speed_variable != active_downward_right_translation_speed: #motor have stopped, now start motor
				active_downward_right_translation_speed = downward_right_translation_speed_variable
				twist.linear.x = -(active_downward_right_translation_speed); twist.linear.y = active_downward_right_translation_speed; twist.linear.z = 0
				twist.angular.x = 0; twist.angular.y = 0; twist.angular.z = 0
				for count in range (0,10):				
					cmd_vel_publisher.publish(twist)
			else: #motor is started, now stop motor
				active_downward_right_translation_speed = 0.00
				twist.linear.x = -(active_downward_right_translation_speed); twist.linear.y = active_downward_right_translation_speed; twist.linear.z = 0
				twist.angular.x = 0; twist.angular.y = 0; twist.angular.z = 0
				for count in range (0,10):				
					cmd_vel_publisher.publish(twist)
				
		elif key_respond_from_user == 'g': #increase speed
			if downward_right_translation_speed_variable < 0.50:
				downward_right_translation_speed_variable += 0.01
				if active_downward_right_translation_speed != 0.00: #motor is moving
					active_downward_right_translation_speed = downward_right_translation_speed_variable
					twist.linear.x = -(active_downward_right_translation_speed); twist.linear.y = active_downward_right_translation_speed; twist.linear.z = 0
					twist.angular.x = 0; twist.angular.y = 0; twist.angular.z = 0
					for count in range (0,10):					
						cmd_vel_publisher.publish(twist)
				
		elif key_respond_from_user == 'b': #decrease speed
			if downward_right_translation_speed_variable > 0.00:
				downward_right_translation_speed_variable -= 0.01
				if active_downward_right_translation_speed != 0.00: #motor is moving				
					active_downward_right_translation_speed = downward_right_translation_speed_variable
					twist.linear.x = -(active_downward_right_translation_speed); twist.linear.y = active_downward_right_translation_speed; twist.linear.z = 0
					twist.angular.x = 0; twist.angular.y = 0; twist.angular.z = 0
					for count in range (0,10):					
						cmd_vel_publisher.publish(twist)

def clockwise_rotation():
	
	clockwise_rotation_speed_variable = 0.00
	active_clockwise_rotation_speed = 0.00
	clockwise_rotation_msg = """
------------Clockwise Rotation for Waiter Robot-----------



|-------------------------------------------------------|
|              Clockwise Rotation Movement              |
|‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|
|                 Speed variable = %.2f                 | 
|             Current relative speed = %.2f             |
|                                                       |
|                   Max speed = 0.50                    |
|  ⇑   press 'g'                         ⇓   press 'b'  | 
|                                                       |
|                                                       |
|                     Motor %s                     |
|         To toggle start/stop motor, press 's'         |
|           To stop motor and exit, press Esc           |
|-------------------------------------------------------|




------------Clockwise Rotation for Waiter Robot-----------
"""
	
	import os
	twist = Twist()
	twist.linear.x = 0; twist.linear.y = 0; twist.linear.z = 0
	twist.angular.x = 0; twist.angular.y = 0; twist.angular.z = 0
	for count in range (0,10):	
		cmd_vel_publisher.publish(twist)
	while True:	
		os.system('clear')
		if active_clockwise_rotation_speed == 0.00: #motor stopped
			motor_state = "stopped"
		else: #motor started
			motor_state = "started"		
		print clockwise_rotation_msg %(abs(clockwise_rotation_speed_variable), abs(active_clockwise_rotation_speed), motor_state)
		key_respond_from_user = getKey()
		if key_respond_from_user == '\x1b': #Esc key
			twist.linear.x = 0; twist.linear.y = 0; twist.linear.z = 0
			twist.angular.x = 0; twist.angular.y = 0; twist.angular.z = 0
			for count in range (0,10):			
				cmd_vel_publisher.publish(twist)
			clockwise_rotation_speed_variable = 0.00
			active_clockwise_rotation_speed = 0.00
			break
		elif key_respond_from_user == 's': #start/stop motor
			if clockwise_rotation_speed_variable != active_clockwise_rotation_speed: #motor have stopped, now start motor
				active_clockwise_rotation_speed = clockwise_rotation_speed_variable
				twist.linear.x = 0; twist.linear.y = 0; twist.linear.z = 0
				twist.angular.x = 0; twist.angular.y = 0; twist.angular.z = active_clockwise_rotation_speed
				for count in range (0,10):				
					cmd_vel_publisher.publish(twist)
			else: #motor is started, now stop motor
				active_clockwise_rotation_speed = 0.00
				twist.linear.x = 0; twist.linear.y = 0; twist.linear.z = 0
				twist.angular.x = 0; twist.angular.y = 0; twist.angular.z = active_clockwise_rotation_speed
				for count in range (0,10):				
					cmd_vel_publisher.publish(twist)
				
		elif key_respond_from_user == 'g': #increase speed
			if clockwise_rotation_speed_variable < 0.50:
				clockwise_rotation_speed_variable += 0.01
				if active_clockwise_rotation_speed != 0.00: #motor is moving
					active_clockwise_rotation_speed = clockwise_rotation_speed_variable
					twist.linear.x = 0; twist.linear.y = 0; twist.linear.z = 0
					twist.angular.x = 0; twist.angular.y = 0; twist.angular.z = active_clockwise_rotation_speed
					for count in range (0,10):					
						cmd_vel_publisher.publish(twist)
				
		elif key_respond_from_user == 'b': #decrease speed
			if clockwise_rotation_speed_variable > 0.00:
				clockwise_rotation_speed_variable -= 0.01
				if active_clockwise_rotation_speed != 0.00: #motor is moving				
					active_clockwise_rotation_speed = clockwise_rotation_speed_variable
					twist.linear.x = 0; twist.linear.y = 0; twist.linear.z = 0
					twist.angular.x = 0; twist.angular.y = 0; twist.angular.z = active_clockwise_rotation_speed
					for count in range (0,10):					
						cmd_vel_publisher.publish(twist)

def anticlockwise_rotation():
	
	anticlockwise_rotation_speed_variable = 0.00
	active_anticlockwise_rotation_speed = 0.00
	anticlockwise_rotation_msg = """
----------AntiClockwise Rotation for Waiter Robot---------



|-------------------------------------------------------|
|            AntiClockwise Rotation Movement            |
|‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|
|                 Speed variable = %.2f                 | 
|             Current relative speed = %.2f             |
|                                                       |
|                   Max speed = 0.50                    |
|  ⇑   press 'g'                         ⇓   press 'b'  | 
|                                                       |
|                                                       |
|                     Motor %s                     |
|         To toggle start/stop motor, press 's'         |
|           To stop motor and exit, press Esc           |
|-------------------------------------------------------|




----------AntiClockwise Rotation for Waiter Robot---------
"""
	
	import os
	twist = Twist()
	twist.linear.x = 0; twist.linear.y = 0; twist.linear.z = 0
	twist.angular.x = 0; twist.angular.y = 0; twist.angular.z = 0
	for count in range (0,10):	
		cmd_vel_publisher.publish(twist)
	while True:	
		os.system('clear')
		if active_anticlockwise_rotation_speed == 0.00: #motor stopped
			motor_state = "stopped"
		else: #motor started
			motor_state = "started"		
		print anticlockwise_rotation_msg %(abs(anticlockwise_rotation_speed_variable), abs(active_anticlockwise_rotation_speed), motor_state)
		key_respond_from_user = getKey()
		if key_respond_from_user == '\x1b': #Esc key
			twist.linear.x = 0; twist.linear.y = 0; twist.linear.z = 0
			twist.angular.x = 0; twist.angular.y = 0; twist.angular.z = 0
			for count in range (0,10):			
				cmd_vel_publisher.publish(twist)
			anticlockwise_rotation_speed_variable = 0.00
			active_anticlockwise_rotation_speed = 0.00
			break
		elif key_respond_from_user == 's': #start/stop motor
			if anticlockwise_rotation_speed_variable != active_anticlockwise_rotation_speed: #motor have stopped, now start motor
				active_anticlockwise_rotation_speed = anticlockwise_rotation_speed_variable
				twist.linear.x = 0; twist.linear.y = 0; twist.linear.z = 0
				twist.angular.x = 0; twist.angular.y = 0; twist.angular.z = -(active_anticlockwise_rotation_speed)
				for count in range (0,10):				
					cmd_vel_publisher.publish(twist)
			else: #motor is started, now stop motor
				active_anticlockwise_rotation_speed = 0.00
				twist.linear.x = 0; twist.linear.y = 0; twist.linear.z = 0
				twist.angular.x = 0; twist.angular.y = 0; twist.angular.z = -(active_anticlockwise_rotation_speed)
				for count in range (0,10):				
					cmd_vel_publisher.publish(twist)
				
		elif key_respond_from_user == 'g': #increase speed
			if anticlockwise_rotation_speed_variable < 0.50:
				anticlockwise_rotation_speed_variable += 0.01
				if active_anticlockwise_rotation_speed != 0.00: #motor is moving
					active_anticlockwise_rotation_speed = anticlockwise_rotation_speed_variable
					twist.linear.x = 0; twist.linear.y = 0; twist.linear.z = 0
					twist.angular.x = 0; twist.angular.y = 0; twist.angular.z = -(active_anticlockwise_rotation_speed)
					for count in range (0,10):					
						cmd_vel_publisher.publish(twist)
				
		elif key_respond_from_user == 'b': #decrease speed
			if anticlockwise_rotation_speed_variable > 0.00:
				anticlockwise_rotation_speed_variable -= 0.01
				if active_anticlockwise_rotation_speed != 0.00: #motor is moving				
					active_anticlockwise_rotation_speed = anticlockwise_rotation_speed_variable
					twist.linear.x = 0; twist.linear.y = 0; twist.linear.z = 0
					twist.angular.x = 0; twist.angular.y = 0; twist.angular.z = -(active_anticlockwise_rotation_speed)
					for count in range (0,10):					
						cmd_vel_publisher.publish(twist)

def scissor_up():
	
	motor_active_flag = False
	scissor_up_msg = """
---------Scissor Upward Movement for Waiter Robot---------



|-------------------------------------------------------|
|                Scissor Upward Movement                |
|‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|
|                     Motor %s                     |
|         To toggle start/stop motor, press 's'         |
|           To stop motor and exit, press Esc           |
|-------------------------------------------------------|




---------Scissor Upward Movement for Waiter Robot---------
"""
	
	import os
	twist = Twist()
	twist.linear.x = 0; twist.linear.y = 0; twist.linear.z = 0
	twist.angular.x = 0; twist.angular.y = 0; twist.angular.z = 0
	for count in range (0,10):	
		cmd_vel_publisher.publish(twist)
	while True:	
		os.system('clear')
		if motor_active_flag == False: #motor stopped
			motor_state = "stopped"
		else: #motor started
			motor_state = "started"		
		print scissor_up_msg % motor_state
		key_respond_from_user = getKey()
		if key_respond_from_user == '\x1b': #Esc key
			twist.linear.x = 0; twist.linear.y = 0; twist.linear.z = 0
			twist.angular.x = 0; twist.angular.y = 0; twist.angular.z = 0
			for count in range (0,10):			
				cmd_vel_publisher.publish(twist)
			motor_active_flag = False
			break
		elif key_respond_from_user == 's': #start/stop motor
			if motor_active_flag == False: #motor have stopped, now start motor
				twist.linear.x = 0; twist.linear.y = 0; twist.linear.z = 1.00
				twist.angular.x = 0; twist.angular.y = 0; twist.angular.z = 0
				for count in range (0,10):				
					cmd_vel_publisher.publish(twist)
				motor_active_flag = True
			else: #motor is started, now stop motor
				twist.linear.x = 0; twist.linear.y = 0; twist.linear.z = 0
				twist.angular.x = 0; twist.angular.y = 0; twist.angular.z = 0
				for count in range (0,10):				
					cmd_vel_publisher.publish(twist)

def scissor_down():
	
	motor_active_flag = False
	scissor_down_msg = """
--------Scissor Downward Movement for Waiter Robot--------



|-------------------------------------------------------|
|               Scissor Downward Movement               |
|‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|
|                     Motor %s                     |
|         To toggle start/stop motor, press 's'         |
|           To stop motor and exit, press Esc           |
|-------------------------------------------------------|




--------Scissor Downward Movement for Waiter Robot--------
"""
	
	import os
	twist = Twist()
	twist.linear.x = 0; twist.linear.y = 0; twist.linear.z = 0
	twist.angular.x = 0; twist.angular.y = 0; twist.angular.z = 0
	for count in range (0,10):	
		cmd_vel_publisher.publish(twist)
	while True:	
		os.system('clear')
		if motor_active_flag == False: #motor stopped
			motor_state = "stopped"
		else: #motor started
			motor_state = "started"		
		print scissor_down_msg % motor_state
		key_respond_from_user = getKey()
		if key_respond_from_user == '\x1b': #Esc key
			twist.linear.x = 0; twist.linear.y = 0; twist.linear.z = 0
			twist.angular.x = 0; twist.angular.y = 0; twist.angular.z = 0
			for count in range (0,10):			
				cmd_vel_publisher.publish(twist)
			motor_active_flag = False
			break
		elif key_respond_from_user == 's': #start/stop motor
			if motor_active_flag == False: #motor have stopped, now start motor
				twist.linear.x = 0; twist.linear.y = 0; twist.linear.z = -(1.00)
				twist.angular.x = 0; twist.angular.y = 0; twist.angular.z = 0
				for count in range (0,10):				
					cmd_vel_publisher.publish(twist)
			else: #motor is started, now stop motor
				twist.linear.x = 0; twist.linear.y = 0; twist.linear.z = 0
				twist.angular.x = 0; twist.angular.y = 0; twist.angular.z = 0
				for count in range (0,10):				
					cmd_vel_publisher.publish(twist)

def tray_up():
	
	tray_up_speed_variable = 0.00
	active_tray_up_speed = 0.00
	tray_up_msg = """
----------------Tray Up for Waiter Robot------------------



|-------------------------------------------------------|
|                  Tray Upward Movement                 |
|‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|
|                 Speed variable = %4.0f                 | 
|             Current relative speed = %4.0f             |
|                                                       |
|                   Max speed = 50                      |
|  ⇑   press 'g'                         ⇓   press 'b'  | 
|                                                       |
|                                                       |
|                     Motor %s                     |
|         To toggle start/stop motor, press 's'         |
|           To stop motor and exit, press Esc           |
|-------------------------------------------------------|




----------------Tray Up for Waiter Robot------------------
"""
	
	import os
	twist2 = Twist()
	twist2.linear.x = 0; twist2.linear.y = 0; twist2.linear.z = 0
	twist2.angular.x = 0; twist2.angular.y = 0; twist2.angular.z = 0
	for count in range (0,10):	
		cmd_vel2_publisher.publish(twist2)
	while True:	
		os.system('clear')
		if active_tray_up_speed == 0.00: #motor stopped
			motor_state = "stopped"
		else: #motor started
			motor_state = "started"		
		print tray_up_msg %(abs(tray_up_speed_variable), abs(active_tray_up_speed), motor_state)
		key_respond_from_user = getKey()
		if key_respond_from_user == '\x1b': #Esc key
			twist2.linear.x = 0; twist2.linear.y = 0; twist2.linear.z = 0
			twist2.angular.x = 0; twist2.angular.y = 0; twist2.angular.z = 0
			for count in range (0,10):			
				cmd_vel2_publisher.publish(twist2)
			tray_up_speed_variable = 0.00
			active_tray_up_speed = 0.00
			break
		elif key_respond_from_user == 's': #start/stop motor
			if tray_up_speed_variable != active_tray_up_speed: #motor have stopped, now start motor
				active_tray_up_speed = tray_up_speed_variable
				twist2.linear.x = 0; twist2.linear.y = 0; twist2.linear.z = active_tray_up_speed
				twist2.angular.x = 0; twist2.angular.y = 0; twist2.angular.z = 0
				for count in range (0,10):				
					cmd_vel2_publisher.publish(twist2)
			else: #motor is started, now stop motor
				active_tray_up_speed = 0.00
				twist2.linear.x = 0; twist2.linear.y = 0; twist2.linear.z = active_tray_up_speed
				twist2.angular.x = 0; twist2.angular.y = 0; twist2.angular.z = 0
				for count in range (0,10):				
					cmd_vel2_publisher.publish(twist2)
				
		elif key_respond_from_user == 'g': #increase speed
			if tray_up_speed_variable < 50.00:
				tray_up_speed_variable += 1.00
				if active_tray_up_speed != 0.00: #motor is moving
					active_tray_up_speed = tray_up_speed_variable
					twist2.linear.x = 0; twist2.linear.y = 0; twist2.linear.z = active_tray_up_speed
					twist2.angular.x = 0; twist2.angular.y = 0; twist2.angular.z = 0
					for count in range (0,10):					
						cmd_vel2_publisher.publish(twist2)
				
		elif key_respond_from_user == 'b': #decrease speed
			if tray_up_speed_variable > 0.00:
				tray_up_speed_variable -= 1.00
				if active_tray_up_speed != 0.00: #motor is moving				
					active_tray_up_speed = tray_up_speed_variable
					twist2.linear.x = 0; twist2.linear.y = 0; twist2.linear.z = active_tray_up_speed
					twist2.angular.x = 0; twist2.angular.y = 0; twist2.angular.z = 0
					for count in range (0,10):					
						cmd_vel2_publisher.publish(twist2)

def tray_down():
	
	tray_down_speed_variable = 0.00
	active_tray_down_speed = 0.00
	tray_down_msg = """
---------------Tray Down for Waiter Robot-----------------



|-------------------------------------------------------|
|                 Tray Downward Movement                |
|‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|
|                 Speed variable = %4.0f                 | 
|             Current relative speed = %4.0f             |
|                                                       |
|                   Max speed = 50                      |
|  ⇑   press 'g'                         ⇓   press 'b'  | 
|                                                       |
|                                                       |
|                     Motor %s                     |
|         To toggle start/stop motor, press 's'         |
|           To stop motor and exit, press Esc           |
|-------------------------------------------------------|




---------------Tray Down for Waiter Robot-----------------
"""
	
	import os
	twist2 = Twist()
	twist2.linear.x = 0; twist2.linear.y = 0; twist2.linear.z = 0
	twist2.angular.x = 0; twist2.angular.y = 0; twist2.angular.z = 0
	for count in range (0,10):	
		cmd_vel2_publisher.publish(twist2)
	while True:	
		os.system('clear')
		if active_tray_down_speed == 0.00: #motor stopped
			motor_state = "stopped"
		else: #motor started
			motor_state = "started"		
		print tray_down_msg %(abs(tray_down_speed_variable), abs(active_tray_down_speed), motor_state)
		key_respond_from_user = getKey()
		if key_respond_from_user == '\x1b': #Esc key
			twist2.linear.x = 0; twist2.linear.y = 0; twist2.linear.z = 0
			twist2.angular.x = 0; twist2.angular.y = 0; twist2.angular.z = 0
			for count in range (0,10):			
				cmd_vel2_publisher.publish(twist2)
			tray_down_speed_variable = 0.00
			active_tray_down_speed = 0.00
			break
		elif key_respond_from_user == 's': #start/stop motor
			if tray_down_speed_variable != active_tray_down_speed: #motor have stopped, now start motor
				active_tray_down_speed = tray_down_speed_variable
				twist2.linear.x = 0; twist2.linear.y = 0; twist2.linear.z = -(active_tray_down_speed)
				twist2.angular.x = 0; twist2.angular.y = 0; twist2.angular.z = 0
				for count in range (0,10):				
					cmd_vel2_publisher.publish(twist2)
			else: #motor is started, now stop motor
				active_tray_down_speed = 0.00
				twist2.linear.x = 0; twist2.linear.y = 0; twist2.linear.z = -(active_tray_down_speed)
				twist2.angular.x = 0; twist2.angular.y = 0; twist2.angular.z = 0
				for count in range (0,10):				
					cmd_vel2_publisher.publish(twist2)
				
		elif key_respond_from_user == 'g': #increase speed
			if tray_down_speed_variable < 50.00:
				tray_down_speed_variable += 1.00
				if active_tray_down_speed != 0.00: #motor is moving
					active_tray_down_speed = tray_down_speed_variable
					twist2.linear.x = 0; twist2.linear.y = 0; twist2.linear.z = -(active_tray_down_speed)
					twist2.angular.x = 0; twist2.angular.y = 0; twist2.angular.z = 0
					for count in range (0,10):					
						cmd_vel2_publisher.publish(twist2)
				
		elif key_respond_from_user == 'b': #decrease speed
			if tray_down_speed_variable > 0.00:
				tray_down_speed_variable -= 1.00
				if active_tray_down_speed != 0.00: #motor is moving				
					active_tray_down_speed = tray_down_speed_variable
					twist2.linear.x = 0; twist2.linear.y = 0; twist2.linear.z = -(active_tray_down_speed)
					twist2.angular.x = 0; twist2.angular.y = 0; twist2.angular.z = 0
					for count in range (0,10):					
						cmd_vel2_publisher.publish(twist2)

def toggle_tray_open_close():
	pass #TODO (Loy Chee Wah) : Program this sub-program after getting the command to control motor!
				





if __name__=="__main__":
    	settings = termios.tcgetattr(sys.stdin)
	
	cmd_vel_publisher = rospy.Publisher('cmd_vel', Twist, queue_size=1)
	cmd_vel2_publisher = rospy.Publisher('cmd_vel2', Twist, queue_size=1)
	encoder5_subscriber = rospy.Subscriber('encoder5', Float32, encoder5_subscriber_callback)
	rospy.init_node('chee_wah_waiter_robot_teleop')


	try:	
		import os	
		while True:		
			os.system('clear')			
			print starting_msg
			key_respond_from_user = getKey()
			if key_respond_from_user == '\x1b': #Esc key
				os.system('clear')
				print "You have choose to exit the Teleop Program for Waiter Robot. Goodbye! :D"
				exit(0)
			elif key_respond_from_user == 'w': #upward_translation
				upward_translation()
			elif key_respond_from_user == 'x': #downward_translation
				downward_translation()
			elif key_respond_from_user == 'a': #leftward_translation
				leftward_translation()
			elif key_respond_from_user == 'd': #rightward_translation
				rightward_translation()
			elif key_respond_from_user == 'q': #upward_left_translation
				upward_left_translation()
			elif key_respond_from_user == 'e': #upward_right_translation
				upward_right_translation()
			elif key_respond_from_user == 'z': #downward_left_translation
				downward_left_translation()
			elif key_respond_from_user == 'c': #downward_right_translation
				downward_right_translation()
			elif key_respond_from_user == 'h': #clockwise_rotation
				clockwise_rotation()
			elif key_respond_from_user == 'f': #anti-clockwise_rotation
				anticlockwise_rotation()
			elif key_respond_from_user == 'v': #scissor_up
				scissor_up()
			elif key_respond_from_user == 'n': #scissor_down
				scissor_down()
			elif key_respond_from_user == 'r': #tray_up
				tray_up()
			elif key_respond_from_user == 'y': #tray_down
				tray_down()
			elif key_respond_from_user == 't': #toggle_open/close_tray_dispenser
				toggle_tray_open_close()
				

	except Exception as error:
		print error
		raise

	finally:
		twist = Twist()
		twist.linear.x = 0; twist.linear.y = 0; twist.linear.z = 0
		twist.angular.x = 0; twist.angular.y = 0; twist.angular.z = 0
		for count in range (0,10):		
			cmd_vel_publisher.publish(twist)
