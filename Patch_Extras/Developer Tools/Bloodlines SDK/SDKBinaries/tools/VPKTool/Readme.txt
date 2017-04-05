Quick and dirty Bloodlines Tools version 3.9a build 210205-0055
---------------------------------------------------------------
(c) 2004-5 Turvy - All rights reserved. Etc, etc, etc.
---------------------------------------------------------------
This is a tool, that allows you extract Map files + Texture Files and Reconfigure Models files.
-----------
Features :
-----------
Current features are :
* VPK data extraction (001-009 and 101+103 contain data)
* Texture conversion :
* TTZ->VTF, TTZ->TGA
* VTF->TTZ, VTF->TGA
* DDS->VTF, DDS->TTZ
Conversion to TGA currently supports these pixel formats :
* DXT1 (no alpha)
* DXT3 with explicit alpha
* DXT5
* RGBA8888 and BGRA8888
* BGR888
* Texture header modification
* Rudimentary (=useless at the moment) model information
* Model texture path and texture name changing!
(Ugly hack, don't overuse)
* Map entity editor! (Extremely rudimentary, no interface)
* Savegame unpacker (nothing useful as of yet)
* Savegame trimmer (warning, *only* use for mod creation testing)

Notes :
-------
* When converting textures to TTZ, the TTH file is needed
in the same directory. This file is *also* edited, so don't
forget to copy the new TTH too, if you're working in a
different directory.

* The texture path/name changing is a really ugly hack, so don't
overuse it. Don't forget to COMMIT any changes you made when
you're done. Don't commit UNTIL you're done changing either tho,
unless you want the file to be bloated with useless dead info ;)

* The savegame trimmer removes all savegame information except
for the current map information. This means your inventory, quests
and stats are saved, as well as some location specific data, and that
modified map info is reloaded from the BSP files so you can check
out your mods. However, ALL the other information for other places
will have been stripped, meaning that for example in the SM Hub,
you can see Mercurio drag himself back into the appartments, and
talking to Bertram takes you back to the Sabbat Warehouse.
You've been warned ;)

History :
---------
v3.9a build 210205-0055
+ Assigned VPKTool to open VPK files as default in windows
and show their contents
+ Both search fields (VPK list and map) now work with
the classic F3 key.

v3.8a build 050105-1935
+ Added texture header modification
+ Expanded find function for VPK list

v3.7g build 301204-1725
* Fixed a zlib decompression error that occured in heather_body.ttz

v3.7g build 271204-2300
* Fixed the DXT5 alpha decoder. Sorry about that people.

v3.7f build 221204-1350
* Rewrote the VPK file opener.
+ Added find function to VPK list.

v3.7e build 141204-2310
+ Savegame trimmer

v3.7e build 141204-0110
+ Savegame unpacker to HL1/HL2/HL3
(not really useful yet, but work in progress)
+ Find/Find next functions in mapeditor
+ Maximizing works now, input fields change size to follow suit.

v3.7d build 101204-2355
+ VERY rudimentary map changing option

v3.7c build 091204-1020
+ Texture path/texture name changing option

v3.7b build 081204-0200
+ More model information

v3.7b build 071204-1820
+ DXT3 texture decoding
+ This help & about box
