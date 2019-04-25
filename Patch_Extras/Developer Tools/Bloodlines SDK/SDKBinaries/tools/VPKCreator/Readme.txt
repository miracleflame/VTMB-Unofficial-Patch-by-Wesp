--------------------------------
 Vampire Bloodlines' VPK Creator
--------------------------------

This console utility was written by me in order to facilitate the packaging of its 
own game content into the VPK game archives and to minimize dancing with a tambourine 
that many at the same time there were (and maybe at all, not many people have tried 
to do this because of the relative complexity of packing settings, or lack of packaging 
setting-files in defective pirate game versions). In this case, you can easily create 
your own patches and localizations in a convenient form, allowing to keep the original 
content and prevent it from being overwritten (for example, it is helpful in restoring 
game to the original version without having to dig through a pile of unpacked stuff).

Features:
* The program interface is intuitive: to select a particular action you should 
  enter the number corresponding to it, and then follow the screen instructions.
* No file operations with pack_values.txt required (you can completely forget about 
  this): the program uses different way to operate packing procedures and does all 
  internal operations itself automatically.
* All generated pack files are placed into the specified game directory under names 
  "packNNN.vpk" where NNN is an index number of overall VPK file system. No need to 
  worry if some vpks are exist in your project - the VPK Creator will adjust required
  index itself, so all freshly packed content will be connected to game right away.
* When you created an archive, you may delete unzipped content versions (by program 
  built-in feature), since they no longer needed in game.

About engine reading order:
* If there are files with same names in different VPK-archives, the game engine will use 
  file from .vpk that have larger number. That is, "pack011.vpk" file will have a higher 
  priority than "pack003.vpk". The archives with "1xx" numbers vice-versa have a lower 
  priority versus "0xx", so it's not recommended to use them anyway.
* When a user extracts a resource from the .vpk file and places it within the game folder
  (Vampire/CustomMod), the engine will load the user's uncompressed version on startup 
  instead of the one in the VPK file. While this design allows user mods, the downside is 
  that it only one user Mod allowed to be installed in the same dir. Use separated ones!

Special:
Many thanks to Theo de Moree for its VPKBuilder tool which finally allowed to unbind 
packing process from unstable game engine and greatly extend VPK Creator's functional!

// written by psycho-a