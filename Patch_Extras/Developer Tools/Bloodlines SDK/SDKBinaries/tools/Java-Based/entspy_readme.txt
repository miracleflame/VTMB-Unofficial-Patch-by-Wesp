Entspy is program for viewing and editing the entities of compiled map (.bsp) files for
Half-Life 2 Source Engine games (HL2, HL2DM, CS:S & VtBM).


Installation and Running
------------------------

It requires the Java Runtime Environment 5.0 (aka 1.5.0) which can be downloaded from this page:
http://java.sun.com/j2se/1.5.0/download.jsp
By following the "Download JRE" link, or directly from:
http://javashoplm.sun.com/ECom/docs/Welcome.jsp?StoreId=22&PartDetailId=jre-1.5.0_03-oth-JPR&SiteId=JSC&TransactionId=noreg

Place the entspy.jar file anywhere convenient, such as your compiled map directory.

To run the program, double-click on the entspy.jar file. If Java is installed correctly, the
program will run. You can also run the program from the command line with the command:

java -jar entspy.jar

For more information, see http://www.geocities.com/cofrdrbob/

Update v0.8 2 October 2005

Now reads version 20 BSP files (as used in the DoD:S release).

Update v0.7 23 June 2005

A minor update that fixes a rare file corruption error.

Update v0.6 31 May 2005

This update adds a "Map info" menu item that shows information about the map file most recently
loaded.

The map saving routine is also changed. On saving a BSP file, Entspy may now ask you to decide
whether to save an optimised version of the map, or a version which preserves the map's checksum.
Preserving the checksum will cause the map file to waste a certain amount of room on disk.

You should use the first option (save optimized) if you are editing your own map to tweak entity
options. You should use the second option (preserve checksum) if you wish to, for instance, add
spawnpoints to an existing map.

Using the preserve checksum option should allow server owners to run maps with altered entities,
without requiring clients to download the altered version of the map.


If, when saving the map, no option is presented, the map file structure is stored so that the
the checksum is already preserved.


Using Entspy
------------

Once a bsp file is loaded, the window show two halves. On the left is a tree-type list of all
entities in the map, starting with the Worldspawn entity. Entities which are parented are
shown as children of the parent entity.

Selecting an entity in the list shows the properties of that entity on the right side of the
window. The four principal entity properties (classname, targetname, parentname & origin) are
shown at the top, with the complete list in the table below. A property and its value can be
edited by clicking on the table entry or in the top four properties. (Note that no changes
to the map are written to disk until the Save BSP menu command is performed.)

The Link column shows an arrow if an entity property contains the targetname of another
entity. Click the arrow button to jump to the linked entity.


The File menu allows the loading and saving of map files:

Load BSP loads a new map file, discarding any changes in the current map.

Save BSP saves the current map file. If you choose the overwrite the current map, a
backup file (mapname.bsp.bak) will be created.

Quit to exit Entspy.


Under the entity list, there are several controls:

The textbox and adjacent Find button finds entities that match the typed text. The entity
classname and targetname is searched for. Press Find again to find the next match.

The Update button updates the entity list tree structure and inter-entity links if any
changes have been made (e.g. targetnames or parentnames altered).

The Add button adds a new entity to the list.

The Copy button adds a copy of the currently selected entity to the list.

The Delete button deletes the selected entity.


Under the entity properties, there are controls related to that entity:

The "Linked from" control shows a list of all entites which link to this one. Select
from the drop-down list and press the arrow button to go to the linking entity.

The Add button adds a new property line to the entity.

The Copy button copies the selected property line.

The Delete button deletes the selected property line.



Entspy v0.8 2 October 2005  rof@mailinator.com