#### Overview:
Here is the design of the gripper for the Quoridor game board.
The gripper's movements include rotation (±280°), translation (10 cm), and gripping (4 cm wide). The gripper is powered by two DMS15 motors and one Servo 9G, with a power supply of 5V from an external source, drawing a maximum of 3A.

![Gripper CAD](https://github.com/epfl-cs358/2024sp-quoridor/assets/50048835/445cc4fa-6c80-46bf-b38b-bae95b703bc2)

![Gripper CAD back](https://github.com/epfl-cs358/2024sp-quoridor/assets/50048835/66e1573b-10f0-4464-ac25-8b156bebbb30)

![Image](https://github.com/epfl-cs358/2024sp-quoridor/assets/50048835/825af3c6-33d8-4308-8444-173178728cb7)


![Image](https://github.com/epfl-cs358/2024sp-quoridor/assets/50048835/dc148988-bd27-479b-a26f-81b40256d13d)


![Image](https://github.com/epfl-cs358/2024sp-quoridor/assets/50048835/cdcc2b90-eac9-4781-88a4-f85412c08a20)


#### Required Components
Motors:
- 2x DMS15 Servo
- 1x 9G Servo

Bearings:
- 2 dry bearings (outer diameter: 10mm, inner diameter: 8mm)
- 1 standard bearing (outer diameter: 24mm, inner diameter: 15mm)
- 2 Metal Shafts 100x8mm

Tools: File, lubricant, screwdriver

Equipment: 3D printer, laser cutter (for plates of 5mm and 3mm thickness, or alternatively, these parts can be 3D printed) 


### Assembly Instructions
#### Gripper Assembly

1. Clean the gear and the two racks with the file.
2. Attach the claws to the claw racks using screws (two screws per claw). Ensure the screws are tightened sufficiently to prevent any movement.
3. Mount the gear onto the servo. Apply a bit of force to fit it securely and then screw it in place (Note: This servo is trash).
4. Slide the two claws onto the rack holder, positioning them close together.
5. Use an Arduino to run the servo, setting it to its maximum position (180° = closed).
6. Slide the servo on top of the rack holder. Adjust the claws slightly to ensure the teeth align correctly (this step may require some patience, precision and despair).

#### Moving Part

1. Clean the bearing holder and the main linear part.
2. Insert the bearing and nuts into the bearing holder.
3. Mount the servo on top of the bearing holder.
4. Insert the two dry bearings and nuts into the main linear part.
5. Position the servo with the bearing holder underneath the main linear part.
6. Secure the assembly by adding screws to the top of the main linear part. Use a small screwdriver to access the holes.
7. Slide the rack under the rack holder.
8. Attach the rack holder to the back of the main linear part, ensuring the rack holder protrudes upwards.


#### Main Part

1. Try to pass the 2 metal axes through the two laser-cut 5mm parts. If necessary, use a file to clean the holes, but do not over-file as the axes need to stay securely in place.
2. Place the left and right pillar supports on the 5mm main plate. You can add screws for additional stability, but this is not mandatory.
3. Position the two upper pillar fix on top of the pillar spacers and screw them in place.
4. Place nuts on the right pillar support and the linear servo support, then screw them onto the main plate.
5. Attach the servo circular extender (I dont know how to call that) to the main gear and secure it using the screws provided with the servo.
6. Insert the two metal axes, slide the moving part onto them, and add the two spacers at the top.
7. Position the servo motor and the two pillars, then add screws at the top and base to secure them.
8. Run the two servos with an Arduino, ensuring the rotation is set to 0 and the linear position is also at 0.
9. Attach the main lower plate to the main plate using spacers.
10. Slide the moving part to the top and fix the gear onto the servo motor. The goal is to have the last teeth of the rack engaged by the gear. (Optional: It is recommended to screw it only when everything is installed).
11. Return to the claw assembly. Fix the gripper support servo to the bearing, applying a bit of force to secure it, and add the screws provided with the servo.
12. Insert the servo from the claw into the gripper support servo, ensuring the cables are passed through before positioning the servo. 
13. Add two screws to secure everything. (Optional: It is recommended to do this only when everything is installed and tested to avoid damaging the claw). 

#### Improvements

- The 9G servos are unreliable and prone to malfunction. Consider using higher-quality or bigger servos to improve the performance and longevity of the gripper.
- I don't realy know were the bearing come from. 
- The current setup uses only two axes, which do not fit perfectly with the dry bearings, leading to deformation. Evaluate the use of additional or alternative linear guide systems to achieve better alignment and reduce deformation.
- It is difficult to place and align the nuts, and the surrounding plastic can break. There is sometimes excessive space, especially for 8mm nuts. Consider replacing the nut holder with inserts.