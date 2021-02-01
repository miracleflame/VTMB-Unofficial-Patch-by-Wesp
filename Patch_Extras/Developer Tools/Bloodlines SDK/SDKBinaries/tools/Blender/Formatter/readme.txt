Formatter by DLLullu
--------------------


You will need the Alien Swarm SDK (for the compiler) and it's free.

You will need Crowbar for Valve models with all the links (here Alien Swarm links).

And finally this Formatter to make a Bloodlines model out of a Valve model.

I include a smd example (poisonivy) so you can try out the thing.


Now the Valve model will need a skeleton from a Bloodlines model, poisonivy uses the Brujah model's skeleton (armature) with it's animations. So we must copy the mdl and the phy from the Brujah model into a special folder (xmodel) for the Formatter. You should rename it to a smaller name. In the example below, i have renamed mine to BrujahFH. I have changed some unused bones to make a pony tail on the Brujah model. Normally you will use a model with a pony tail like the number 2 or 3 Malk model but I started with the Brujah so... 

What's all of this means: we are reusing the hitbox, the bones, the animations, the links to other animations and the physics, I changed nothing there. What I changed: the mesh inside the model, the textures, a rewrite of the vtx. Oh and I added the eyes data from the Valve model, that is new, yeah. Before it was a pain to do.

For the eyes:

You must put the eyes data into the QC. The data is taken from blender, you put the cursor on the center (or where you want the iris) of each eye and read the coordinates (x,y,z) of the cursor with +0.5 added to the y coordinates. Look below, I have extracted the eyes data from the QC. For the eyes and shapes keys you need to use $model, not $bodygroup! You also need the eyes's attachment.


$model "girl" "brujahFH_poison_female_Armor_0_REF"{
//             ^______^ name use by the formatter for the base model.
  
//                                        X     Y+0.5   Z   =   position center of eyes in the mesh
      	eyeball "eye_right" "Bip01 Head" -1.03 -2.89104 65.64 "eyeball_r" 1 4 "iris_unused" 0.63
	eyeball "eye_left" "Bip01 Head"   1.31 -2.89104 65.64 "eyeball_l" 1 -4 "iris_unused" 0.63
}
//                                        sum\2 sum\2   sum\2
$attachment "eyes" "Bip01 Head"           0.14 -2.89    65.64 absolute


1. open crowbar, choose the compile tab.
2. drag the qc from poisonivy_vtmb into qc input, choose game's "models" folder and set up games to Alien Swarm.
3. compile.
4. use goto to go to the game's "models" folder.
5. drag the newly create mdl to the converter.bat.
6. open the models folder and find the newly create VTMB mdl and copy the 4 files to where you want to use the model.

I think the number 6 is a problem here. The bat file puts the model into a models folder near to it but you can change that location to anywhere you want. There are some examples in the bat file.

I added some texts in the tuto_2 picture.


Readme improved by Wesp5