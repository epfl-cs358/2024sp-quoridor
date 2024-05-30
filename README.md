# 2024sp-quoridor

# 3D printed parts

## Camera mount
- 1x main part
- 1x camera clamp

## Walls

- 10x in red
- 10x in blue

## Player pawns

- 1x in red
- 1x in blue

## Board

- 2x "long"
- 1x "square"

## Angle brackets
- 15x

## Corner brackets

Warning, these are symetrical pieces !
One of each

## End pulley

- 2x

# Laser cutting

## In MDF

## Main board
- 1x Main board, 10mm

## Walls holder
- 2x, 3mm

## In acrylic

## Camera arms

Warning, these are symetrical pieces !
One of each, 5mm

## Wheel plate
-3x 3mm

## Stepper mount
-1x 3mm

## End pulley bracket

- 4x 3mm

## Optionnal : 3D printed T-nuts

The metallic openbuilds t-nuts are recommended. We 3d printed those because we forgot to order them. We ended up doing a slightly modified version of the original openbuilds CAD model, that works better with 3d printers.

## What needs improvements

3mm thick acrylic is not strong enough. We had a failure for an end pulley bracket, the 3d printed part ended up stronger.
![signal-2024-05-30-124640](https://github.com/epfl-cs358/2024sp-quoridor/assets/29517376/95a357cb-7f40-497b-b6b6-f81a8951fffd)

We also a noticed a crack developing on one of the wheel plate
![signal-2024-05-30-124415](https://github.com/epfl-cs358/2024sp-quoridor/assets/29517376/009971cb-2ad9-40ab-97fd-c830cd530be3)

# Assembly instructions

With all the parts cut and printed, we are ready for assembly (note that you can also 3d print as you go, since the three pieces for the board for example take quite long to print)

First, scre in the wall holders pieces to the board. These parts add thickness to the board, so doing this first helps stabilizing it a bit more (MDF tends to bend with time).

Next, screw in the 8 angle brackets to the board.

Attach the V slot aluminium profiles, screwing them in place with the t-nuts

Screw in the corner brackets. These help stabilizing the profiles, and at the end to mount the camera arms.

Now flip the board upside down. We will use the profile as spacer.
Slide in the 3d printed boards part. Glue them. gravity will hold them in place. We used fast super-glue, but with this setup you can use a glue that takes a while to set.

# X axis assembly (built this seperately)

Warning : follow precisely this order, so you don't need to dissassemble sub-assemblies down the line

Mount the wheels to the wheel plate (this is the plate we will later mount the grabber to)
Slide the wheels+plate assembly to the middle of the profile.

Mount the end pulley plates on both side on end of the profile
Mount the stepper pully plate on the other side

Mount the angle bracket to the v-slot. The placement is simple : on each end,  they are next to each other, sarting at the end of the profile.

## Do this two times:

Mount the wheels to the plate, sliding the assembly.

# Combine x axis assembly with the rest
Now we can mount the stepper on the x axis with the belt. Attach the belt to the plate going above the profile like this:

![signal-2024-05-30-131015](https://github.com/epfl-cs358/2024sp-quoridor/assets/29517376/f2b83ba8-ecee-4d5d-bf38-fe47de7ae71f)

Slide in the end switch mount. Tighten it so it does not move, but don't try to be precise with regards to the adjustments

Attach the Y stepper to the stepper motor plate, setup the belt but don't attach it to the grabber plate yet.

Put the grabber assembly on top of the plate, scew it in place

Screw in the  electronic box.
Put the arduino+ramps+motor driver sandwich inside of it. Do the wiring according to the diagram. Pass the cables via the side holes (otherwise you won't be able to close the lid at the end).

# Camera arms

Screw in the arms to the angle brackets
Connect bot arms together
Mount the camera using the clamp

Attach the cable chain to the grabber's wires. This is not a strictly mandatory step, but it helps relieving stress from the cables.


