# 2024sp-quoridor

These instructions are structured in 2 sub-assemblies:
- The Gripper
  
- The machine
  - Main part
  - Y axis rail
 
As well as a set of instructions for the Computer Vision:
- Players and walls detection
- Game board and coordinates building

The two sub assemblies can be built in parallel and assembled at the end. The design is such that only two screws hold the gripper to the rest of the assembly, so it's quite easy to modify the gripper seperately.

# Gripper
## Overview:
Here is the design of the gripper for the Quoridor game board.
The gripper's movements include rotation (±280°), translation (10 cm), and gripping (4 cm wide). The gripper is powered by two DMS15 motors and one Servo 9G, with a power supply of 5V from an external source, drawing a maximum of 3A.


<img src="https://github.com/epfl-cs358/2024sp-quoridor/assets/50048835/445cc4fa-6c80-46bf-b38b-bae95b703bc2" alt="Gripper CAD" width="200" />

<img src="https://github.com/epfl-cs358/2024sp-quoridor/assets/50048835/66e1573b-10f0-4464-ac25-8b156bebbb30" alt="Gripper CAD Back" width="200"/>

<img src="https://github.com/epfl-cs358/2024sp-quoridor/assets/50048835/825af3c6-33d8-4308-8444-173178728cb7" alt="Gripper CAD" width="200"/>

<img src="https://github.com/epfl-cs358/2024sp-quoridor/assets/50048835/dc148988-bd27-479b-a26f-81b40256d13d" alt="Gripper CAD" width="200"/>

<img src="https://github.com/epfl-cs358/2024sp-quoridor/assets/50048835/cdcc2b90-eac9-4781-88a4-f85412c08a20" alt="Gripper CAD" width="200"/>

## Required Components:
Motors:
- 2x DMS15 Servo
- 1x 9G Servo

Bearings:
- 2 dry bearings (outer diameter: 10mm, inner diameter: 8mm)
- 1 standard bearing (outer diameter: 24mm, inner diameter: 15mm)
- 2 Metal Shafts 100x8mm

Tools: File, lubricant, screwdriver

Equipment: 3D printer, laser cutter (for plates of 5mm and 3mm thickness, or alternatively, these parts can be 3D printed) 


## Assembly Instructions:
#### Gripper Assembly:

1. Clean the gear and the two racks with the file.
2. Attach the claws to the claw racks using screws (two screws per claw). Ensure the screws are tightened sufficiently to prevent any movement.
3. Mount the gear onto the servo. Apply a bit of force to fit it securely and then screw it in place (Note: This servo is trash).
4. Slide the two claws onto the rack holder, positioning them close together.
5. Use an Arduino to run the servo, setting it to its maximum position (180° = closed).
6. Slide the servo on top of the rack holder. Adjust the claws slightly to ensure the teeth align correctly (this step may require some patience, precision and despair).
7. Optional: you can stick pieces of rubber on the gripper clamp to increase adhesion (I used pieces of rubber glove).

<img src="https://github.com/epfl-cs358/2024sp-quoridor/assets/50048835/54cea055-8bae-47fc-a9ae-b04794caebf2" alt="Gripper CAD" width="200"/>
<img src="https://github.com/epfl-cs358/2024sp-quoridor/assets/50048835/27a740c8-3dff-44fa-bfbb-caf6837366bf" alt="Gripper CAD" width="200"/>
<img src="https://github.com/epfl-cs358/2024sp-quoridor/assets/50048835/dc3b6bea-cae0-42eb-8963-f6001d200c2f" alt="Gripper CAD" width="200"/>
<img src="https://github.com/epfl-cs358/2024sp-quoridor/assets/50048835/e7948dcd-540a-4c1a-87e1-fa2e772d19ea" alt="Gripper CAD" width="200"/>

#### Moving Part:

1. Clean the bearing holder and the main linear part.
2. Insert the bearing and nuts into the bearing holder.
3. Mount the servo on top of the bearing holder.

<img src="https://github.com/epfl-cs358/2024sp-quoridor/assets/50048835/b40d9cee-e101-4d3e-b5fb-eed6ac9bf848" alt="Gripper CAD" width="200"/>

5. Insert the two dry bearings and nuts into the main linear part.
6. Position the servo with the bearing holder underneath the main linear part.
7. Secure the assembly by adding screws to the top of the main linear part. Use a small screwdriver to access the holes.
8. Slide the rack under the rack holder.
9. Attach the rack holder to the back of the main linear part, ensuring the rack holder protrudes upwards.


#### Main Part:

1. Try to pass the 2 metal axes through the two laser-cut 5mm parts. If necessary, use a file to clean the holes, but do not over-file as the axes need to stay securely in place.
2. Place the left and right pillar supports on the 5mm main plate. You can add screws for additional stability, but this is not mandatory.
3. Position the two upper pillar fix on top of the pillar spacers and screw them in place.
4. Place nuts on the right pillar support and the linear servo support, then screw them onto the main plate.
5. Attach the servo circular extender (I dont know how to call that) to the main gear and secure it using the screws provided with the servo.
6. Insert the two metal axes, slide the moving part onto them, and add the two spacers at the top.

<img src="https://github.com/epfl-cs358/2024sp-quoridor/assets/50048835/4596ae2a-ca69-46e4-ba35-8f475dc2592a" alt="Gripper CAD" width="200"/>

8. Position the servo motor and the two pillars, then add screws at the top and base to secure them.
9. Run the two servos with an Arduino, ensuring the rotation is set to 0 and the linear position is also at 0.
10. Attach the main lower plate to the main plate using spacers.
11. Slide the moving part to the top and fix the gear onto the servo motor. The goal is to have the last teeth of the rack engaged by the gear. (Optional: It is recommended to screw it only when everything is installed).
12. Return to the claw assembly. Fix the gripper support servo to the bearing, applying a bit of force to secure it, and add the screws provided with the servo.
13. Insert the servo from the claw into the gripper support servo, ensuring the cables are passed through before positioning the servo. 
14. Add two screws to secure everything. (Optional: It is recommended to do this only when everything is installed and tested to avoid damaging the claw).

## Wiring:

Due to their high power consumption, all 3 servos must be powered by an external power source of at least 5v/3amp.
Here is the electrical diagram to connect them to a Ramps 1.6

![Image](https://github.com/epfl-cs358/2024sp-quoridor/assets/50048835/452fb32d-1a28-4367-88d5-c3750ed1e14c)

1 is the gripper servo, 2 is the rotation servo and 3 is the servo of the linear actuator.

<img src="https://github.com/epfl-cs358/2024sp-quoridor/assets/50048835/cecb0a00-1679-444f-9da6-6fd5bd09c6a7" alt="Wiring" width="200"/>
<img src="https://github.com/epfl-cs358/2024sp-quoridor/assets/50048835/ff0c3b6e-416e-4b07-a10a-85d1822ccaaa" alt="Wiring" width="200"/>
<img src="https://github.com/epfl-cs358/2024sp-quoridor/assets/50048835/adaf3201-f865-4431-a51c-ff7efeda43e7" alt="Wiring" width="200"/>

## Improvements:

- The 9G servos are unreliable and prone to malfunction. Consider using higher-quality or bigger servos to improve the performance and longevity of the gripper.




# Machine sub-assembly

![image](https://github.com/epfl-cs358/2024sp-quoridor/assets/29517376/1fc7a162-6f88-4d96-96cb-83a57a20c5a8)


# 3D printed parts

## Camera mount
- 1x main part
- 1x camera clamp
![image](https://github.com/epfl-cs358/2024sp-quoridor/assets/29517376/adbbcf64-3641-47dd-b6e8-a11756d23917)

## Walls

- 10x in red
- 10x in blue

  Print in this direction to get the best results (no supports necessary)
![2024-05-30-134702_1920x1080_scrot](https://github.com/epfl-cs358/2024sp-quoridor/assets/29517376/3d09f210-a7a0-4fad-8aeb-ed1b799f9204)

## Player pawns

- 1x in red
- 1x in blue

## Board

- 2x "long"
  ![image](https://github.com/epfl-cs358/2024sp-quoridor/assets/29517376/ce00cc08-4ec2-49a2-a95a-216b0ae48254)

- 1x "square"
  ![image](https://github.com/epfl-cs358/2024sp-quoridor/assets/29517376/45a8fca4-3df0-4f03-a79d-38b1126cae2c)

- 1x "little square"
  ![image](https://github.com/epfl-cs358/2024sp-quoridor/assets/29517376/a94eaf2d-1b7b-4fbe-9d79-d3208f63316c)

## Angle brackets
- 15x
![2024-05-30-134950_1920x1080_scrot](https://github.com/epfl-cs358/2024sp-quoridor/assets/29517376/f6f29c9d-7ff3-446a-8e86-82d14438d61e)

## Corner brackets

Warning, these are symetrical pieces !
One of each
![2024-05-30-135919_1920x1080_scrot](https://github.com/epfl-cs358/2024sp-quoridor/assets/29517376/6acdac3e-2437-45e8-a4b9-cae5a715761a)

## End pulley

- 2x
![image](https://github.com/epfl-cs358/2024sp-quoridor/assets/29517376/8f19bba7-aa8f-4a38-b836-9c100816a6ef)

## Optionnal : 3D printed T-nuts

The metallic openbuilds t-nuts are recommended. We 3d printed those because we forgot to order them. We ended up doing a slightly modified version of the original openbuilds CAD model with a bigger diameter, that works better when 3d printing
![2024-05-30-135202_1920x1080_scrot](https://github.com/epfl-cs358/2024sp-quoridor/assets/29517376/5f25eb8e-318d-4ce0-9474-89f75a60be18)

# Laser cutting

## In MDF

## Main board
- 1x Main board, 10mm

## Walls holder
- 2x, 3mm

## In acrylic

## Camera arms
- 2x, 5mm 
![image](https://github.com/epfl-cs358/2024sp-quoridor/assets/29517376/afd10105-d49e-4a6c-a836-ce99f082970e)

## Wheel plate
-3x 3mm
![2024-05-30-143234_1920x1080_scrot](https://github.com/epfl-cs358/2024sp-quoridor/assets/29517376/1165d8d0-3458-4c53-b571-a77d05c8b27f)

## Stepper mount plate
-2x 3mm
![image](https://github.com/epfl-cs358/2024sp-quoridor/assets/29517376/90b7559e-7e34-49a1-b51c-d225ff4424ad)

## End pulley bracket

- 4x 3mm (Two are used per axis)
![image](https://github.com/epfl-cs358/2024sp-quoridor/assets/29517376/07afd105-28bb-4ac9-81d3-f5e6cf29272b)

## What needs improvements

3mm thick acrylic is not strong enough. We had a failure for an end pulley bracket, the 3d printed part ended up stronger.
![signal-2024-05-30-124640](https://github.com/epfl-cs358/2024sp-quoridor/assets/29517376/95a357cb-7f40-497b-b6b6-f81a8951fffd)

We also a noticed a crack developing on one of the wheel plate
![signal-2024-05-30-124415](https://github.com/epfl-cs358/2024sp-quoridor/assets/29517376/009971cb-2ad9-40ab-97fd-c830cd530be3)

# Assembly instructions

With all the parts cut and printed, we are ready for assembly (note that you can also 3d print as you go, since the three pieces for the board for example take quite long to print)

First, screw in the wall holders pieces to the board. These parts add thickness to the board, so doing this first helps stabilizing it a bit more (MDF tends to bend with time).
![2024-05-30-140227_1920x1080_scrot](https://github.com/epfl-cs358/2024sp-quoridor/assets/29517376/d8a8b463-446d-4e9d-a4eb-157b498464bd)

Next, screw in the 8 angle brackets to the board (4 on each side).
![image](https://github.com/epfl-cs358/2024sp-quoridor/assets/29517376/b61fc97c-99ae-467f-9ce0-f964b3b5b405)

Attach the V slot aluminium profiles, screwing them in place with the t-nuts

Screw in the corner brackets. These help stabilizing the profiles, and at the end to mount the camera arms.
![image](https://github.com/epfl-cs358/2024sp-quoridor/assets/29517376/967656fd-ffbd-40a6-ac7b-d746e69eb5a1)

Now flip the board upside down, with the top side of the profile resting on your workspace. We will use the profile as spacer.
Slide in the 3d printed boards part. Glue them. gravity will hold them in place. We used fast super-glue, but with this setup you can use a glue that takes a while to set.
![image](https://github.com/epfl-cs358/2024sp-quoridor/assets/29517376/926f89a9-e75b-4a59-b1be-628a669cf102)

# X axis assembly (built this seperately)

Warning : follow precisely this order, so you don't need to dissassemble sub-assemblies down the line

Mount the wheels to the wheel plate (this is the plate we will later mount the gripper to)
Slide the wheels+plate assembly to the middle of the profile.

Mount the end pulley plates on both side on end of the profile
![image](https://github.com/epfl-cs358/2024sp-quoridor/assets/29517376/99bcf9c4-67c1-4e92-97bd-990249971dec)

Mount the stepper mounting plate on the other side
![WhatsApp Image 2024-05-30 at 15 28 48](https://github.com/epfl-cs358/2024sp-quoridor/assets/29517376/d836d0ac-d9d2-471d-9bea-b0edb8eada4c)

Mount the angle bracket to the v-slot. The placement is simple : on each end,  they are next to each other, sarting at the end of the profile.

## Do this two times, for both sides:

Mount the wheels to the plate and then slide the assembled carriage.

![image](https://github.com/epfl-cs358/2024sp-quoridor/assets/29517376/102ed1bd-8770-4ed6-bd57-feec15d27577)

# Combine x axis assembly with the rest
Now we can mount the stepper on the x axis with the belt. Attach the belt to the plate going above the profile like this:

![signal-2024-05-30-131015](https://github.com/epfl-cs358/2024sp-quoridor/assets/29517376/f2b83ba8-ecee-4d5d-bf38-fe47de7ae71f)

Slide in the end switch mount. Tighten it so it does not move, but don't try to be precise with regards to the adjustments. Adjustements are done when everything is in place.

![9f54f568-a379-4a69-852f-7c88d7756aae](https://github.com/epfl-cs358/2024sp-quoridor/assets/29517376/8f4c6994-8b22-4654-b50b-14ccc19d767d)

Attach the Y stepper to the stepper motor plate, setup the belt but don't attach it to the gripper plate yet.

Put the gripper assembly on top of the plate, screw it in place
![image](https://github.com/epfl-cs358/2024sp-quoridor/assets/29517376/64d5549d-1376-4417-9e9c-a55415f60f21)

Screw in the electronic box.
Put the arduino+ramps+motor driver sandwich inside of it. Do the wiring according to the diagram. Pass the cables via the side holes (otherwise you won't be able to close the lid at the end).

![335123297-452fb32d-1a28-4367-88d5-c3750ed1e14c (1) (1) (1)](https://github.com/epfl-cs358/2024sp-quoridor/assets/29517376/8b67e324-da04-4d95-9206-f31da4b23159)


# Camera arms

1. Screw in the arms to the angle brackets
![WhatsApp Image 2024-05-30 at 14 55 10](https://github.com/epfl-cs358/2024sp-quoridor/assets/29517376/79f65ac9-f04f-4855-94b9-5f24ccd53015)

2. Connect bot arms together
![image](https://github.com/epfl-cs358/2024sp-quoridor/assets/29517376/15dd732c-9721-412f-9e0e-d9e180cd206d)

3. Mount the camera using the clamp
![e45bf986-da7e-4e04-8ccc-194e948133e6](https://github.com/epfl-cs358/2024sp-quoridor/assets/29517376/98a9b2f5-1321-48be-bbb9-9f7cb9f2beeb)


# Button

1. Screw in the button housing to the board
2. screw the button itself to the housing from below

![image](https://github.com/epfl-cs358/2024sp-quoridor/assets/29517376/fb54c6d5-6fcf-4a0f-96e7-083a5544322a)


# The end

Congratulation ! At this point, you should have the full machine assembled like this:
![image](https://github.com/epfl-cs358/2024sp-quoridor/assets/29517376/8d11d0c9-d51f-4480-bb1f-2526c2b5df83)

You can now proceed with adjustements regarding the end switch positioning, as well as the camera angle for the webcam.

# Arduino code 
The arduino code is separated in 2 parts, one is for all movements on the board (the X, Y axis stepper motors and 3 servo motors for the gripper) and the part is for communication and interpreter which will send, receive and decode message from the computer which it will translate to valid moves on the board. <br> <br>

The arduino will be managing communication with itself and the computer with a serial connection.
This diagram shows the communication between all of our components: <br> <br>
![image](https://github.com/epfl-cs358/2024sp-quoridor/assets/125994939/c68cb262-15f6-44b7-a2b7-51a86409bb5d)

The arduino will send a "end turn" message through the serial once the button pressed, then the computer will communicate with the camera to detect the current board state (placement of the player pieces and the walls), with that it will compute the best move for the bot. Finally it will send the move information as the board position of the piece we want to grab, the new board position where we want to place the piece, the piece type, and optionally the orientation of the piece if it is a wall. <br> <br>

To accomplish the first part the arduino will stay idle, but once the player presses the end turn button it will trigger an interrupt. This will cause the arduino to print the message "get next move", which will be sent by the serial port. <br> <br>
Then the arduino will remain idle until it receives the move information from the computer.<br>
There are 2 types of moves, moving a player piece or a wall piece.
If the move is to move a player piece, then the move information will be under this form: <old_position><new_position><player> where old_position and new_position are board position for player pieces which are shown here:
![image](https://github.com/epfl-cs358/2024sp-quoridor/assets/125994939/29b26c79-ad42-4af9-a48e-afd0dd88b5b6)
<br> 
If the move is to move a wall piece, then the move information will be under this form: <old_position><new_position><wall><old_orientation><new_orientation> where old_orientation new_orientation are either horizontal or vertical, and old_position and new_position are board position for wall pieces which are shown here:
![image](https://github.com/epfl-cs358/2024sp-quoridor/assets/125994939/7f252fad-1904-4a52-aeec-def705e5375c)
With all of this information the arduino knows what it has to do.<br> <br> 

Now for actually placing the piece where it needs to go. <br>
First we must move to the piece we desire to move, which we use the 2 X and Y stepper motors. Since the board was made with cells that are 4 times bigger than the gap between cells, it just takes knowing the distance in steps from the position 0 0 of the grabber to board position 00 for a player piece, and the distance in steps from a board position to a neighboring one board position to know how to move any board position for player pieces and wall pieces.<br>
That is the hard part done, then the gripper drops down, grabs the piece, pulls it back up, rotates it if it is needed (for instance if we had to place a vertical wall), moves to the new position, drops down, releases the piece, goes back up and moves back to its origin.<br><br>
Here are some videos that process working flawlessly:
<video src="https://github.com/epfl-cs358/2024sp-quoridor/assets/125994939/afad0169-728d-4bf2-bb4c-040145c0d592" controls></video>
<video src="https://github.com/epfl-cs358/2024sp-quoridor/assets/125994939/391f769e-7cd7-4f65-ab67-2949c7b72846" controls></video>

<br>

# Computer Vision
## Pieces detection
The playing pieces (players and walls) are recognized through color detection.
(to be completed)

## Game board
The board, its cells and wall gaps are not detected as is, but rather re-created after detecting the board's corners.
Each corner is uniquely identified by ArUco markers: they are a sort of QR codes, that can uniquely generated and identified through the use its corresponding library.
Given the corners and the cells' number and dimensions, a grid is recreated: <br>
![image](https://github.com/epfl-cs358/2024sp-quoridor/blob/main/computer_vision/board_test/grid_creation.png)
<br> <br>
You can see on the picture that the grid is purposefully offset near the top. Because the camera is not directly centered on top of the board, walls near the top will tend to look like they are higher on the board then they truly are.
You will find more detail on aruco detection and perspective wrapping in the code /computer_vision/create_grid.py <br>
When creating the grid, the set of intersections between all perpendicular grid lines is stored for future use. For each intersection, we store the absolute coordinates as well as the game-system coordinates (9 units on each side, origin is bottom left) <br>
Then, given the absolute coordinates for the pieces centers, the code uses the set of intersections coordinates to output, for the solver to use, the game-system coordinates of each piece. <br> <br>
When sticking the ArUco markers on the board, you should be mindful that the outer corners should be well-aligned with the board's corners (PS: the markers don't need to have the same size, they should just be well-aligned). <br>
Be careful however that they can be seen entirely from the camera (black square included). Here are corner-case examples: <br>
![image](https://github.com/epfl-cs358/2024sp-quoridor/blob/main/computer_vision/board_test/both_smallest_markers.jpg) <br>
On the image above, the top markers should be small enough that walls placed at the top don't block them
![image](https://github.com/epfl-cs358/2024sp-quoridor/blob/main/computer_vision/board_test/board2.jpeg) <br>
On the image above, the markers are too far down: the black square isn't showing entirely. <br> <br>
And tha't it! Happy building!

