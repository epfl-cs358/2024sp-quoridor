#### Overview:
Here is the design of the gripper for the Quoridor game board.
The gripper's movements include rotation (±280°), translation (10 cm), and gripping (4 cm wide). The gripper is powered by two DMS15 motors and one Servo 9G, with a power supply of 5V from an external source, drawing a maximum of 3A.

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
