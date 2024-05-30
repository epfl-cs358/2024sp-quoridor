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

<img src="https://github.com/epfl-cs358/2024sp-quoridor/assets/50048835/cecb0a00-1679-444f-9da6-6fd5bd09c6a7" alt="Wiring" width="200"/>
<img src="https://github.com/epfl-cs358/2024sp-quoridor/assets/50048835/ff0c3b6e-416e-4b07-a10a-85d1822ccaaa" alt="Wiring" width="200"/>
<img src="https://github.com/epfl-cs358/2024sp-quoridor/assets/50048835/adaf3201-f865-4431-a51c-ff7efeda43e7" alt="Wiring" width="200"/>

## Improvements:

- The 9G servos are unreliable and prone to malfunction. Consider using higher-quality or bigger servos to improve the performance and longevity of the gripper.
- I don't realy know were the bearing come from. 
- The current setup uses only two axes, which do not fit perfectly with the dry bearings, leading to deformation. Evaluate the use of additional or alternative linear guide systems to achieve better alignment and reduce deformation.
- It is difficult to place and align the nuts, and the surrounding plastic can break. There is sometimes excessive space, especially for 8mm nuts. Consider replacing the nut holder with inserts.
