Vampire: The Masquerade - Bloodlines Unofficial Patch
-----------------------------------------------------
Copyright by Werner Spahl, "Wesp5", email: spahl@cup.uni-muenchen.de
Main support and talking boards: http://www.planetvampire.com/forum/
Detailed gaming infos: http://www.gamebanshee.com/vampirebloodlines/
The Patches Scrolls page: http://www.patches-scrolls.de/patch/4647/7
ModDB download page: http://www.moddb.com/mods/vtmb-unofficial-patch
Nexus Mods page: https://www.nexusmods.com/vampirebloodlines/mods/80

This is an unofficial patch for Vampire: The Masquerade - Bloodlines
by Troika Games. It's a cumulative patch containing all the previous
releases and works with retail and downloadable versions of any kind
as the Troika Games official patch 1.2 is included. It runs out of a
subfolder so other mods can be run in parallel but applying it to an
international version will revert all localizations back to English!

The default Basic Patch fixes multiple bugs and restores only little
content to stay close to the original. The Plus Patch (+) adds minor
tweaks and lots of content, the Patch Extras include a SDK and more!
Patched loader, client, engine, shaderapidx9, and vampire dlls bring
widescreen support and fix weapon-stats, coronas-gone, refresh-rate,
lights-through-walls, floats-for-females and more-than-2GB-RAM bugs.

To install the patch choose the Bloodlines directory as destination,
select wanted features, install and then start the game from the new
desktop or start menu links. Thanks to Jordan Russel for Inno Setup!
It's important to start a new game after patching, old saves will be
moved to save/incompatible! To uninstall, remove the patch links and
patch directory. Changelogs, known issues and more are listed below.

On issues in Windows install the patch as administrator or use it in
XP compatibility mode. On problems with Steam run Steam and the game
as administrator and copy steam.dll to the game folder, if you get a
"failed to find Steam" error. To start it from the Steam library add
-game Unofficial_Patch to launch options! Disable auto-updating both
in Steam and Galaxy. On issues in Linux run the loader-linux script.

Special thanks to burgermeister for the Public Library, EntenSchreck
for the Hallowbrook Atrium, the Chateau Hotel outside and drafts for
Malkavian Maze, Warrens Shortcut and Museum Entrance! To Atrblizzard
for opening the pier and Psycho-A and duchU for optimizing many maps
too. The maps were edited and compiled using the Unofficial SDK from
Psycho-A and Fire64 and then finished and filled with life by Wesp5.

Special thanks also to the people who modified the dlls of the game,
to Jor and Wabbite who fixed the 2 GB memory bug in shaderapidx9.dll
and Frank7777 who added the refresh-rate fix. To in9 who fixed stats
in client.dll, SomeCommentDoe, Drog Black Tooth and c6 who corrected
lights-through-wall, LOD and save speed in engine.dll, and Behar and
Psycho-A who merged most in loader.dll and added -game installation!

The patch is provided "as is" and any warranties are disclaimed. The
free redistribution of the unchanged patch is permitted but it's not
allowed to use it as a base for derivative works without permission!
Special thanks go to Dan Upright for starting the unofficial patches
and doing the versions up to 1.2, his changelogs are included below.
Many thanks also to the following people who contributed much to it!


Acknowledgments:
----------------
Special thanks to: HungarianPatriot, Anderson, IanW, duchU, Zenith,
GoodGamesPlayer, Wilhelm-Streicher, endthewars, Malkav, -3xA'Lu©?y,
No_Mercy, Behar, atrblizzard, Zer0morph, Psycho-A, AJ, vladdmaster,
burgermeister, Entenschreck, Stosh, gothemasticator, Darth Sithari,
Dheu, Felix, Fabio, foestermalk, StockholmSyndrome, SomeCommentDoe,
Lenuska, Mike89, Crenshinibon, Mash1908, Jekyll_Grim_Payne, psmatt,
Rik, MadeChina, Icleus, DarkAlf666, BeauxChaotica, Valamyr, Gardeb,
Voerman, Wabbite, Xealous, Populism, Giggle Cream, Doe, Mzz, Exulx,
Slim_Laurence, ZeroCredibility, RGE, Magnus Staehr, Dark666Prophet,
MooCHa, ZylonBane, Offkorn, Soulcharmer, DocDeltree, R. Fialcowitz,
Acleacius, Bogj, Bloodi Punk, Yupsi, Mahou Mahou, Khelben, DDLullu,
Sgloomi, Paul Moloney, Alec Maassen van den Brink, and RobinHood70!

Patch Extras:
-------------
VTMB Transcripts: Ellipsis_jones, gothemasticator, IanW and Wesp5.
VTMB Walkthrough: Walkthrough & Guide by vampyri_lestat and Wesp5.

Developer Tools:
----------------
Bloodlines SDK: Full SDK with many tools, by Psycho-A and Fire64.
Game Mod Loader: Combined .dll fixes and -game support, by Behar.
Level Sources: Entity lists and Hammer vmf, by Offkorn and Wesp5.
Original Python Files: Scripts of the original release, by Wesp5.

Bloodlines Trailers E3 2003/2004: Beta contents, by Troika Games.
ModDev Guide: Bloodlines Mod Development Guide, compiled by Dheu.
Restoration Doc and Soundtrack Info: Restored contents, by Wesp5.
ZVTool Readme: For dynamic console editing scripts, by ZylonBane.

Player Mods:
------------
Concept Art: Collection of various Troika art, compiled by Wesp5.
ENBSeries: Shader suite, copy to game folder, by Boris Vorontsov.
Free View Weapons: Copy to vampire/vdata/items, created by Wesp5.
SweetFX: Different shader suite, use ReShade Setup, by CeeJay.dk.

Install64: Windows installer patch for 64 bit, by Iain Patterson.
ResPatch: Widescreen resolution kit, by Wabbite (.NET 2+ needed).
ScreenWindowedOn/Off.reg: To switch fullscreen mode, by Psycho-A.
Trackerscheme.res: Turns Malkavian font off, check txt, by Wesp5.


Version Changelog:
------------------

v10.9                                                  27.04.2021
-----
+Improved braid icon and four models boundaries, thanks to Norrwin.
+Restored way to kill Vandal and improved other SM clinic details.
+Improved Dragon's Breath and vehicle models, thanks to endthewars.
+Removed Pisha snack reward and fixed Persuasion of Phil and Stan.
+Made books sellable again due to real exploit fix, thanks Norrwin.
+Improved controls options menu and settings text for widescreens.
+Removed Kent's driver license item to restore Fatguy melee attack.
+Made Patty go behind Confession and fixed a few turnstile issues.
+Restored tutorial Jack end animation and made crying Jenny louder.
+Removed Mercurio's car from hub if you ratted him out to LaCroix.
+Restored fighters brawling in Al's video game at beachhouse level.
Corrected LODs, transitions and inspections at Hallowbrook Hotel.
Updated BSPSource and NirCmd, thanks to atrblizzard and Nir Sofer.
Restored and corrected junk details on many maps, thanks Norrwin.
Made Tseng hide his guns faster and Carson's killing being logged.
Fixed being stuck on warrens gate and added ammo to Society roof.
Corrected Python script that broke when renaming the patch folder.
Added links for beta videos to Restoration Doc, thanks to tarulu.
Made hunters in Santa Monica attack Tung if they meet him outside.
Restored water splashing at pier and missing ladder at warehouse.

v10.8                                                  21.03.2021
-----
+Improved the turnstile at Club Confession, thanks to EntenSchreck.
+Corrected trigger, sound and badly lit wall at Hallowbrook Hotel.
+Updated tutorial security guard's voice-overs, thanks to Chalvrek.
+Delayed Vick's arena exit and made Tawni's boyfriend holster gun.
+Added exits to Sheriff roof fight and made his sword easy to find.
+Removed whispers, cables and encounters in Subtly Insane history.
+Made it easier to return items in dialogue and restored heat haze.
+Added morgue entry for Doris and Krimeputer entry for beachhouse.
Removed redundant and duplicate tools from the Player Mods folder.
Restored a line of Mandarin and fixed issues with Nadia in crypt.
Fixed Venture Tower icon and holes and made glass roof accessable.
Reset Gangrel sheet stances and Glaze combat area in basic patch.
Locked endgame Skyeline vents and fixed floating or clipping junk.
Fixed sticky floors, camera angles and other map and text issues.
Disabled Arthur's privat computer and movement in the basic patch.
Added sign to Hollywood cemetery gate and fixed name in computer.
Fixed a temple trap trigger and covered bad Society rock textures.
Adjusted cabbie endgame lines and removed Ash sewers auto-ending.
Fixed virus and timer issues on returning to the Kamikaze Zen map.
Corrected Tremere haven condition, tutorial windows and a ladder.
Fixed texture flickering on downtown washer and courier shoe hole.
Made every armed NPC in downtown fight back when you attack them.
Corrected Blade Brother name in basic and Luckee Star body issues.
Removed disciplines when talking to the Mandarin at Fu Syndicate.
Added model Formatter to convert models to SDK, thanks to DDLullu.
Improved game save/load speed by modifying engine.dll, thanks c6.
Made SDK work with new and open source Java, thanks Caner Özdemir.

v10.7                                                  20.09.2020
-----
+Fixed Nines Chateau trigger and sweeper greeting Nosferatu player.
+Restored Potence and Celerity view particles and improved others.
+Corrected getting secret from Christopher and flirting with Nadja.
+Fixed second museum visit of Nosferatu and VV's lapdance slowing.
+Restored Obfuscator not appearing and repaired minor model issues.
+Fixed Arthur repeating his phone call and feed stuck in tutorial.
+Restored "TrueSight" for Bishop Vick, Blood Guardian and Cathayan.
+Improved Mercurio and Jenny sounds and made them plus patch only.
+Swapped Brujah clone with Damsel at the ending, thanks to DDLullu.
+Decreased chances of werewolf easter egg and prophet not ranting.
+Added safety measures to casting hand models, thanks EntenSchreck.
+Removed heat effect from fire and delayed Pisha leaving the city.
+Fixed being able to take Romero's zombie quest after pimpin quest.
+Moved Malcolm's black mail money from apartments into his office.
+Improved Giovanni trap section and circumvented Bruno not burning.
+Removed unfitting Humanity changes and added some missing sounds.
Added script and Skin Editor to SDK, thanks DDLullu and hlstriker.
Restored original music to the radio on the pier for basic patch.
Fixed reentering issues and door breaking at the Giovanni Mansion.
Added missing XP if you found Ginger Swan before meeting courier.
Corrected ground stutter and sarcophagus key drop, thanks Norrwin.
Fixed possible ways to get stuck in tutorial and big warrens map.
Added missing solidity of sewer and temple models, thanks Norrwin.
Corrected tutorial MAC-10 loudness and minor map and text issues.
Repaired an auto-locking door and stuck fanblades at Fu Syndicate.
Fixed blocking Confession barkeeper and sewers Ash talking early.
Corrected posters staying in SM haven and improved Empire dancing.
Added and changed dropping sounds of some items, thanks Psycho-A.
Fixed several maps so that new dropping sounds don't mess them up.
Corrected Boris dialogue problem after he survived fighting Dema.
Stated Auspex and Divine Vision amplification and fixed Ming aura.
Added story pitch in page_text.ttz to transcripts, thank to IanW.
Fixed talking with Heather after you dealt with McFly in two ways.
Made Glaze Masquerade area and Fu Syndicate start as combat area.
Fixed teleporting SWAT and crossguy Humanity loss at Fu Syndicate.
Restored black monitors and case for Milligan, thanks endthewars.
Disabled Mass Suicide for zombies and fixed a Giovanni ragdolling.
Fixed stripper and girl off work leaving Vesuvius' dressing room.

v10.6                                                  14.04.2020
-----
+Repaired broken melee of Ming and created new item gained message.
+Improved all cars and tutorial guard audio, thanks to endthewars.
+Fixed Frenzy to really use the boosted stats, thanks EntenSchreck.
+Adjusted firearms ammo cost and restored one for the basic patch.
+Restored Jeanette and Therese dialogue and many more unused lines.
+Made Heather throw away old pizza and not being visible as ghost.
+Fixed normal SWAT being biteable and Hallowbrook Atrium confusion.
+Made killing junkyard dog cost Humanity and Pisha meal disappear.
Corrected alternative way of hitmen's peace and minor file issues.
Removed two plus emails from basic and fixed other minor details.
Fixed Nines' camera view at observatory and Romero's combat stats.
Specific Crowbar tool created for Bloodlines, thanks to ZeqMacaw.
ZeqMacaw's and DDLullu's tools integrated in SDK, thanks Psycho-A.
Fixed bombguy's explosion radius and two shopping carts' physics.
Restored dispatching Dima for Malkavians and raised tutorial ammo.
Removed shortcut at museum and fixed guard dropping workroom key.
Fixed name of museum in computers and basic max flamethrower ammo.
Repaired "Bloodsucker Communion" name and Numina names and icons.
Fixed tutorial location continuity in downtown, thanks endthewars.
Restored sound to Vesuvius easter egg and made it easier to find.
Fixed exploit to get the werewolf blood and some dialogue details.
Corrected loader-linux script to work for bash, thanks to GaGGaG.
Fixed possible courier and warrens computer problems in Hollywood.

v10.5                                                  24.01.2020
-----
+Renamed Holy Sight to Vision and fixed Divine Light cross texture.
+Added Society icon to title and heat haze effect to fire barrels.
+Restored Faith Heal, discipline particles and Gangrel sheet model.
+Included Velvet's famous private show, many thanks burgermeister.
+Added ladder and food to Society and missing cabbies and manholes.
+Adjusted Dragon's Breath max ammo and made some NPC corpses stay.
+Made Romero's blood refill, and opened King's Way map after quest.
+Removed random whispers in dialogue and gave Lasombra Shin Gunto.
+Corrected female player models for Velvet's dance, thanks DDLullu.
+Fixed Hallowbrook Atrium walls and Giovanni Mansion backtracking.
+Restored two missing XPs to Ocean House quest and two Nines lines.
+Added option to come back to Nines in endgame for two more lines.
+Restored film projector into Malkavian Maze, thanks to endthewars.
Fixed Bertram's CD label and added Kamikaze Zen missing passwords.
Made Serial quest independent from Muddy and forced patch folder.
Fixed possible problem if people kill Igor without talking to him.
Restored no Humanity loss for civilians in combat areas to basic.
Added No-more-LOD and Make-Model-Solid tools, many thanks DDLullu.
Fixed Ming's sanctum view, teleport timing and a temple map hole.
Corrected female Tremere lenses and hair problems, thanks DDLullu.
Fixed female Malkavian hair hole, Dane door and cemetery fadings.
Changed impact blood, Chantry endgame locking and haven newspaper.
Updated binkw32.dll to version 1.8x for Linux Wine, thanks dhewg.
Fixed warehouse forklift, door sound and Ocean House lift texture.
Corrected invisible or minor map, file, text and dialogue issues.
Fixed warrens clipping, rat sounds downtown and Mercurio's stains.
Improved some minor texture and model issues, thanks to Psycho-A.

v10.4                                                  18.07.2019
-----
+Restored clipboard to SM clinic and made Fu switch turn alarm off.
+Prolonged Brainwipe and restored Sleep and Command Flee or Leave.
+Changed Deaf history and corrected minor dialogue and text issues.
+Added sounds to Veil of Madness, Blood Theft and Dragon's Breath.
+Enhanced variety of sound schemes by restoring twenty-nine sounds.
+Restored sounds to Mitnick's keyboard, Yukie and temple teleport.
+Made Knox take Gimble's license and Luca keep any used invitation.
+Fixed Zhao being alive and Bruno being killed quest log problems.
+Changed order of levels in the library quest, thanks Vaarna_Aarne.
+Made tube box sellable and removed three more items after quests.
+Restored killer's side of phone call in diner and two leave lines.
+Removed dog if Mercurio pacified beachhouse and cop cars on pier.
+Unlocked stage door at Empire Hotel and fixed pier murder problem.
+Delayed tutorial guard popup and fixed exploit at werewolf blood.
+Restored a King's Way room and copied Die My Darling song to pier.
+Added way to feed of Arthur after his quest and fixed some hairs.
+Made Mandarin and Arthur glasses plus and added Grout's wife aura.
+Improved disciplines casting hand switch, thanks to EntenSchreck.
+Made seductive feeding multiple times of Phil and Romero possible.
+Increased flamethrower ammo and made Larry more immune to fights.
+Improved library quest notes and location of teeth marks in intro.
Prevented Dima from vanishing and Hollywood prostitute talk-loop.
Fixed Bach encounter exploit and moved Ming sanctum XP to sanctum.
Added missing Tawni's TV sound and removed some lens reflections.
Restored courier and Mercurio lines and removed more auto-endings.
Corrected wrong zombie sounds and fixed walkthrough inaccuracies.
Improved Tseng shelf weapons and SDK, thanks DDLullu and Psycho-A.
Fixed crouching Blood Hunt enemies and early sewer Ash exit talk.
Restored breaking and machine sounds to observatory and SM clinic.
Added crane sounds to warehouse and changed crane sounds on Dane.
Improved Ocean House breaking wood, fling, noise and beach sounds.
Restored a Dane cop call, two Nadia lines and fixed her cowering.
Fixed transparent girders at warehouse and other minor map issues.

v10.3                                                  18.04.2019
-----
+Made magic projectile of fatguys do aggravated damage like Ming's.
+Corrected plus and basic Arthur lines and fixed Gimble phone bug.
+Added Unofficial Patch contributors to credits and restored basic.
+Fixed note in tattoo parlor and teleporting of Confession dancer.
+Removed Humanity gain of serial killer if you kill him afterwards.
+Swapped Colt Anaconda and Desert Eagle damage and added .38 kick.
+Improved Sabbat ending and choice dialogues, thanks burgermeister.
+Made Obfuscator appear after warehouse and adjusted maximal ammo.
+Restored fridge model and Giovanni spirit texture, thanks DDLullu.
+Added some food plates and film can textures, thanks to Psycho-A.
+Fixed Gary's blood packs, and dialogues of Boris, Phil and Slater.
+Restored Bloodlines name to main menu logo, thanks Candy Narwhal.
+Added Blood Malady effect for supernaturals immune to Blood Theft.
+Updated Ash, Copper and Serial quest states when you failed them.
+Changed medical emails conditions and guard sounds away from cops.
+Readded Bedlam and Mass Suicide disciplines, thanks EntenSchreck.
+Removed second CIS computer password and restored many new models.
+Restored full mission impossible, jewelry and Ming combat tracks.
+Reskinned Beckett's wolf form to look more real, thanks Zer0morph.
Fixed breakable observatory stairs, and Dragon's Breath max ammo.
Improved dialogues of Cal, Carson, Isaac, Lily, VV and of Malcolm.
Restored old diner map and improved vampire.exe, thanks Psycho-A.
Deleted Coffee Shop and Smoke Shop door handles from hub in basic.
Fixed Gangrel and Toreador female hands, thanks MooCHa and Jenya.
Disabled plus lines of Bertram, Jack, Heather, Carson and LaCroix.
Corrected some sounds and fixed internal issues, thanks Psycho-A.
Fixed Tommy fix and restored several weapons parameters for basic.
Removed seminude prostitute from SM again and from Chinatown too.
Restored beachhouse PC difficulty and locked Tung's tank in basic.
Improved elevator display and climbing back in vent at SM clinic.
Fixed map holes outside Ocean House and lowered ghost music there.
Corrected overlapping music and several portals at the warehouse.
Covered trigger texture inside Ocean House and removed a laughter.
Fixed warrens doors, restored whispers and removed rats in basic.
Moved Club Confession's restroom and fixed cash register lighting.
Corrected Romero leaving and unlocked Red Spot backdoor in basic.
Fixed minor hospital issue and Dane computer text and screenshots.
Removed Larry's floats in basic patch and made them less in plus.
Unlocked junkyard kennels for basic and removed Sin Bin plus logs.
Fixed LOD effect in Chinatown hub and improved the Giovanni well.
Restored visibly vanishing Gary and removed zombie fleeing sounds.
Swapped blade and thrower and restored two ghouls to Hallowbrook.
Removed King's Way cat sounds and Blood Hunt heli sounds in basic.
Hid a wall hole during taxi ride and removed all special letters.
Corrected ModDev Guide detail and updated SDK, thanks to Psycho-A.
Restored basic dialogue popup and Ocean House Malkavian whispers.
Fixed a hitman problem and removed some unnecessary SM hub blocks.
Swapped pictures of restored Ocean House and Halloween newspaper.
Removed plus Hallowbrook sound and warehouse intro music in basic.
Fixed combat music on blood hunt map and duplicated Therese line.
Removed plus inspection in the Tattoo Shop and sound for clothing.
Corrected reel to reel at Grout's Mansion and stuck museum guard.
Fixed distraction of Giovanni backdoor guard and minor map issues.
Restored three Heather lines, two Lily lines, and subtitle names.
Fixed hit blood spatters and thin bloods leaving beachhouse beach.
Repaired model, texture, sign and sound details, thanks Psycho-A.
Fixed wrong stalker voices and a dead NPC hearable at beach house.
Corrected all phone animations and export script, thanks DDLullu.
Repaired Venture Tower elevator, portals and Giovanni zombie trap.

v10.2                                                  25.01.2019
-----
+Placed a dead dog into Fu Syndicate and filled Kamikaze Zen shelf.
+Made Sheriff laugh when conjuring bats and made them attack less.
+Added console key and all hotkeys to the controls options submenu.
+Fixed details in library level and text and dialogue details too.
+Corrected maximum ammo of flamethrower and made Carson pack stuff.
+Prevented exploit of selling books and removed Trip button sound.
+Unlocked Red Spot storage door and repaired beachhouse NPC update.
+Updated the Krimeputer log entries on Brian's and Muddy's deaths.
+Made Carson remove McGee's corpse and raised MAC-10 magazine cost.
+Fixed silent Heather dialogue and made warrens ladder accessible.
+Locked a haven door and moved Malcolm's bribe to Mercurio's house.
+Repaired problems when revisiting the beachhouse and the warrens.
Removed quest update for Copper and locked Gimble's door in basic.
Fixed some more wrong Humanity losses and cut off Heather sounds.
Corrected Tommy Dominate reaction and possible poster quest issue.
Modified barber chair with Lily to animate bonds, thanks DLLullu.
Removed copying bin files into main folder and SDK virus triggers.
Made tutorial door open better and removed basic last Jack lines.
Fixed female Tremere hair and sheet warform model, thanks DLLullu.
Restored Gangrels to Masquerade cutscene and added theatre email.
Made male Gangrel not crouch to fit transformation to warform fix.
Fixed Giovanni crypt line artifacts and armored a Venture bridge.
Removed basic discipline changes and restored bump mapping option.
Added a few weapon drop sounds and fidget and upset sound groups.
Removed weird tongue of Sheriff warform model, thanks to Barabbah.
Removed corpses of blood dolls and other NPCs on revisiting maps.
Improved python and loader file compatibility, thanks to Psycho-A.
Made video victim's model unique and corrected ghoul sound group.
Corrected mirrors and details on several maps, thanks to Psycho-A.
Fixed Milligan's business card and Dane screenshots, thanks IanW.
Made NPCs recognize the deaths of Misti, Venus, Mercurio and Knox.
Fixed Leopold Society cellar ladder and floating towels in basic.
Added way to use all animations for all models, thanks to DDLullu.

v10.1                                                   23.10.2018
-----
+Fixed Gary giving packs if you already have some and made it plus.
+Shortened Bat's Communion to work with Beastmistress history too.
+Added Humanity gain for saving the quick Nosferatu in the warrens.
+Updated thin bloods on beachhouse beach and added monastery beds.
+Changed surplus Tremere history and improved Andrei's atrium exit.
+Restored billboard and Chateau computer and fixed Obfuscate info.
+Fixed some bad Humanity losses and wrong basic poster quest email.
+Restored Arthur's computer and improved formats, thanks Psycho-A.
+Updated tutorial guard voice and SDK, thanks voerman and Psycho-A.
+Modified Chupacabra and Insectoid histories to avoid warform bug.
+Changed Steyr and SWAT zoom and Glock magazine size to real value.
+Made Kamikaze Zen money stay in plus and Andrei don't drop braid.
+Some superfluous items can be given to Pisha, Skelter and Strauss.
+Made Carson quest more logical by having the player phone Gimble.
+Added male blood doll to Smoke Shop and a surprise to pier ending.
+Moved Knox in Asylum to restore lines of Cal and some for Arthur.
+Corrected Auspex stats if you use "no changed disciplines" option.
+Swapped final poster quest poster and restored it to Ground Zero.
+Restored partial damage to supernaturals with several disciplines.
+Updated some entries in some computers to reflect NPC fatalities.
+Fixed four Humanity cost altering histories, thanks miracle.flame.
+Removed plus and extras installer sub-options to avoid confusion.
+Improved snatching cutscene and made museum outside a combat area.
+Fixed an ignoring-Sabbat-ending issue and sneaking out with Kiki.
+Made Hengeyokai not freeze on Blood Theft and fixed Ji quest loop.
+Improved library and made Red Spot gum ball machine destructable.
+Finally fixed the dead-dog-still-hurting and Milligan freeze bugs.
Made sure beachhouse thugs are dead if Mercurio appears at beach.
Prevented player from using idle animation during a few cutscenes.
Added info to hacking popup and fixed minor map and text details.
Fixed condition for telling Damsel that you killed a werewolf too.
Changed criminal level of several weapons to get police to react.
Fixed talking to Zhao from the shelves and sneaky Glaze newspaper.
Corrected warrens, hospital, society and 609 maps by recompiling.
Unified formatting of newspaper articles and improved GUI details.
Disabled bad icons and buttons for inactive Ocean House elevator.
Fixed Presence hair and cleared Disciplines before more cutscenes.
Covered level holes in observatory, Red Dragon and Venture Tower.
Fixed vanishing details downtown, at Ocean House, and in cemetery.
Added missing monster sounds reacting to Dementation disciplines.
Made the patch copy all bin files into main folder to fix crashes.
Added toilet doors to a few maps and fixed minor dialogue issues.
Moved breakroom at the SM clinic so the geometry fits the outside.
Made blood dolls reappear after killing to avoid staying corpses.
Moved sarcophagus loading scene to Giovanni Mansion back entrance.

v10.0                                                   15.06.2018
-----
+Swapped Nines line at Malkavian Mansion and added new music there.
+Improved Chateau details and added persuaded Gargoyle and killer.
+Fixed Giovanni Mansion random whispers and added Copper's remains.
+Corrected noclipping taxi at the museum and TV in Skyeline haven.
+Made Ocean House diary and Lily's and VV's photos fit description.
+Restored killing innocents Humanity loss and tutorial guard feed.
+Opened Ocean House, junkyard, basement and beachhouse after quest.
+Reopened coffee shop, library, crackhouse, garage and fishmarket.
+Opened museum and Giovanni Mansion after quests for Pisha's items.
+Restored thrown weapons slot for grenade and fixed Imalia webcam.
Fixed female casting hands, object and NPC models, thanks DDLullu.
Corrected problems with tutorial vampire enemies and disciplines.
Made warehouse and beachhouse props solid and fixed downtown moon.
Updated SDK and added darker SweetFX setting, thanks to Psycho-A.
Darkened more beachhouse lamps and fixed gender of embrace scream.
Fixed Fu Syndicate Barabus hacking check and a Ginger Swans date.
Moved linux loader into main folder and added warning popup to it.
Modified several dlls to not create empty files, thanks Psycho-A.
Fixed LaCroix particles and Fortitude for basic disciplines setup.
Added missing door to Ocean House and fixed two railing problems.
Restored some safety windows and fixed minor map and text details.
Unlocked a door at the Fu Syndicate and corrected more doorknobs.
Fixed character sheet hunter models and updated free view weapons.

v9.9                                                    07.01.2018
----
+Provided shortcuts to skip most endgame fighting, see walkthrough.
+Added beheading blood and restored props to Chateau and junkyard.
+Improved rotate camera movement setup and SDK, thanks to Psycho-A.
+Restored Vision of Death and Suicide damages and Aggravated Soak.
+Added door trap to warrens shortcut and improved museum fire exit.
+Fixed casting hands, feeding histories and Pearl of Dubai effect.
+Restored Yukie animations, missing ambient schemes and Chang jump.
+Fixed bugs with Trip's drug and Gary's fleshy ball poster quests.
+Improved title menu and character sheet clan symbols, thanks IanW.
+Activated Gallery light switch and fixed menu particles time lag.
+Created homosexual history for all clans and adjusted intro scene.
+Made Venture Tower song Malkavians only and fixed license issues.
+Added possible Copper to Chateau and improved masquerade cutscene.
+Implied sleeping near tutorial and warehouse including bloodloss.
+Changed Close to the Beast history because of wolf warform issues.
Corrected many inside/outside door handles and background screen.
Prevented Romero cemetery cutscene freezing if Presence is active.
Disabled extra lines from basic and charity money humanity check.
Fixed Hannah's appointment book date and other minor text details.
Hid map bugs in SM hubs, clinic, Society, Luckee Star and others.
Fixed blueblood, Lily, Bertram, Yukie, LaCroix and thug dialogues.
Corrected hand and sound of Nines intro cutscene, thanks DDLullu.
Restored basic pistol ammos and fixed tutorial bug, thanks Malkav.
Fixed incorrect Lotus Blossom location on Chinatown busstop maps.
Replaced buggy Chinatown phone sound and restored wallbreak sound.
Added Windows 10 mouse fix to Extras, thanks to Dusk of Oolacile.

v9.8                                                     13.08.2017
----
+Lowered damage of both rifles and restored original stats to basic.
+Corrected auras of NPCs at Confession, junkyard, pier and library.
+Modified enemies in maze mausoleum and added a connection to Patty.
+Fixed dead dog biting, some map details and added a Tourette line.
+Removed civilian Humanity losses and increased Dementation 2 range.
+Improved stat messages for Auspex, Fortidude, Potence and Protean.
+Updated radio subtitles and SDK, thanks miracle.flame and Psycho-A.
+Fixed Andrei problems when you meet him in the Hallowbrook Atrium.
+Added fleshy ball to King's Way for a final poster quest from Gary.
+Improved Lasombra and other minor model issues, thanks to DDLullu.
+Changed Copper quest to success when you intimidated him for money.
+Moved chewing gum to arcade and animated machines, thanks DDLullu.
+Restored a Milligan line and created necessary license item for it.
+Gave Jezebel a .38 so she can damage you if you jump onto the bed.
Improved the famous Skyeline bug and Giovanni crypt map transition.
Fixed dripping sound loop at ending and misleading Jeanette email.
Disabled the background music when you talk to Gary in the warrens.
Fixed Slater dialogue loop and other minor dialogue and text bugs.
Added Blood Boil explosion sound and increased decal view distance.
Replaced Python update with map sources and improved other Extras.
Corrected mirrored crates textures and fixed two warrens stairways.
Fixed eyes in Lily cutscene and raised club outside music volumes.
Reset clothing using console and improved werewolf blood quest log.
Added drop_type1or2MDL decompressor for models, thanks to DDLullu.
Fixed basic Potence not stacking and removed second effect in plus.
Added missing ladder-climbing sounds to several recompiled levels.

v9.7                                                     30.03.2017
----
+Restored Chateau Hotel to ending, thanks EntenSchreck and Psycho-A.
+Swapped clone Brujah at solo ending with Toreador for male Brujah.
+Made Gary gift different bloodpacks and fixed missing Kathayan bug.
+Stopped shaking Malkavian lines in Ocean House and at observatory.
+Removed radio 5 duplicates and added missing vcds, thanks Psycho-A.
+Fixed map details, cleaned files and updated SDK, thanks Psycho-A.
+Removed Lotus Blossom patron with bad shadow and fixed green drips.
+Restored missing song to Venture Tower and another to Asylum door.
+Made crypt ghosts vanish and added missing door to Chinese Theatre.
+Removed cast ammo and unused Thaumaturgy particles, thanks maxoku.
+Recreated missing Dane cops conversation, thanks to Zeno and Stosh.
Corrected freeze during Beckett's "Wait" cutscene when Obfuscated.
Fixed lights and textures in SM clinic and Asylum, thanks Psycho-A.
Improved badly fixed missing Tommy line and minor dialogue issues.
Prevented restarting of Carson quest and added missing steps sound.
Recreated floats and subtitles, thanks miracle.flame and Psycho-A.
Fixed four level holes at the Ocean House and one in Venture Tower.
Mirrored SM area maps and improved details of others, thanks IanW.
Fixed unbalanced XP of Bad Luck Farmer quest and minor text issues.
Disabled confusing new corpse and vanished cars in parking garage.
Repaired bad icons and flickering for upper Venture tower elevator.
Fixed Zhao exploit and walkthrough errors, thanks to sunsmountain.
Corrected lip-sync of prostitutes in cemetery and her dialogue bug.
Improved Empire Hotel mafia TV room sound switch and music radius.
Permanently turned on bump mapping and repaired museum combat area.
Fixed Nadia sequence, frozen zombies and Ming endgame camera shot.
Made Santa Monica blueblood return after Domination, thanks Malkav.
Corrected and improved Linux Wine loader script, thanks Wrzlprmft.
Disabled low poly model LOD in engine.dll, thanks Drog Black Tooth.
Fixed camera after endgame Cabbie discussion and his cut-off line.
Moved Milligan flee script and added model tutorial, thanks Icicle.
Repaired broken Asylum door music and two Blood Hunt Asylum holes.
Improved tutorial Sabbat gunfire and restored Chunk and Trip lines.
Put 4GB patch in Patch_Extras/Player Mods, thanks Daniel Pistelli.
Fixed invincible burning Lasombra and signs and curtain at theatre.

v9.6                                                     02.10.2016
----
+Fixed warform-weapons bug, moved Yugo to pier and limo onto street.
+Adjusted some weapon damages and made crossbow fire burning bolts.
+Added shake to forklift hit and improved two friend emails timings.
+Changed Shin Gunto to look different to katana, thanks to Lenuska.
+Added door to SM haven bathroom and masquerade area outside museum.
+Mentioned Clan Lasombra in the world loading tips, thanks to IanW.
+Fixed museum areaportals and small texture issues, thanks Psycho-A.
+Added observatory inspections and fixed male blood doll get stuck.
+Increased cemetery gate's health more and fixed a coffee shop door.
+Made Chang brother's Tiger's Claws weapon usuable, thanks Lenuska.
+Restored six models to Society, Foxy Boxes, theatre, and warehouse.
+Made two additional options available for plus patch installation.
+Added dialogue lines to give some surplus items to Gary and Damsel.
+Raised conditions to persuade Gimble and unlocked door afterwards.
+Sold crossbow ammo later and changed two tutorial elevator buttons.
+Added taxi to maps and fixed jars transparency at Grout's Mansion.
+Moved flamethrower into new atrium and made braid Mitnick's reward.
+Placed some things in empty Giovanni rooms and fixed player start.
Blocked way into locked SM junkyard and corrected Chunk levitating.
Made Sin Bin ATM machine not vanish and Romero sit after boinking.
Fixed Givanni sound schemes and monitors in Skyeline and SM clinic.
Delayed Mercurio cutscene to make player move where he can see it.
Improved weapons, timings, ocean and widescreen cut of Ming ending.
Made crackhouse girl flee and hid two mirrored theatre door signs.
Removed restored weapons from basic and restored all the stats too.
Recompiled Kamikaze Zen map to fix vent without exit and lighting.
Corrected bad elevator light at Red Dragon and Jezebel's door lock.
Fixed decapitation shot and restored basic drugbox value and rain.
Unified keypad sounds and fixed wrong detection and sounds on Dane.
Fixed museum door not being locked and some minor dialogue issues.
Lowered Asylum music volume after loading and fixed minor map bugs.
Added original Japanese and Russian words to translated subtitles.
Fixed Empire mafia reaction and reduced pier artefacts and effects.
Updated SDK and fixed audio loop at Fu Syndicate, thanks Psycho-A.
Made manholes in Venture Tower cellar and Ocean House sewers close.
Fixed bad Kerri dialogue start and delayed Jeanette and Ming ones.
Used autoexec.cfg to fix talk dsp sound and frame rate door issues.
Enhanced some areaportals at Leopold Society and Giovanni Mansion.
Recompiled Zhao's Warehouse to fix huge doors vanish at a distance.
Fixed Nosferatu causing Masquerade violations exiting Luckee Star.
Adjusted volume of some NPC lines and corrected NPC coughing loops.
Fixed some Ocean House rails, areaportals, shadows and a map hole.
Made persuaded Chunk not attack and incapacitated drop gallery key.

v9.5                                                     24.04.2016
----
+Recreated Smoke Shop in SM and integrated it into the libray quest.
+Created Coffee Shop in SM and integrated it into the libray quest.
+Restored nine random sounds to Giovanni Mansion and Malkavian Maze.
+Added two new Malkavian Maze areas and riddle, thanks to Psycho-A.
+Improved cook model, oilrig reflection and SDK, thanks to Psycho-A.
+Fixed Patty-turnstile-issue and many map details, thanks Psycho-A.
+Restored four muffled sounds to downtown and two to Hollywood hubs.
+Fixed SPAS secondary fire spread and made Chastity biteable again.
+Added skulls to ritual chamber and fixed Red Spot storage door bug.
+Fixed delayed identification of occult powerups and infobar icons.
+Added new notes to museum outside and to the two Santa Monica hubs.
+Made Edward's theme play only after the Ocean House has been left.
+Restored two newspaper headers and fixed whispers, thanks Psycho-A.
+Fixed library guard sound group and added post-installation-infos.
+Made male blood doll bi and fixed some other minor dialogue issues.
+Corrected compiler errors on some of the build maps, thanks duchU.
+Fixed library LaSombra becoming invincible after flamethrower fire.
+Restored wolf warform model and fixed critical pier Rosa dead bug.
+Recompiled beachhouse to fix dead dog hurting bug, thanks Psycho-A.
Recompiled burning Mansion to fix exit room bugs, thanks Psycho-A.
Removed basic maze note, plus emails and ignitions on Fu explosion.
Disabled bad downtown hospital sounds and illogical debris vanish.
Added infos about Auspex auras, Numina and more to the walkthrough.
Removed other clans whispers in tutorial, warrens and Ocean House.
Changed name of combination hunter shield Numina to "Faith Shield".
Restored Sin Bin machine breaking and adjusted Giovanni door lock.
Corrected netcafe sound schemes switch and fixed many streetlights.
Fixed SM schrecknet door lock and disabled a Venture Tower button.
Improved Isaac and prince dialogue issues, thanks to FrederickVael.
Fixed Ming temple clipping columns and improved notes readability.
Made tutorial popups center in widescreen as well, thanks Psycho-A.

v9.4                                                     06.10.2015
----
+Restored museum entrance and downtown area, thanks to EntenSchreck.
+Opened pier after murder is gone, thanks atrblizzard and Psycho-A.
+Fixed aura for crying woman in SM and improved library quest again.
+Made LaCroix give you the museum keys and Blood Theft always work.
+Added random thunder sounds to waterfront and removed tutorial key.
+Created plus default cfg and corrected basic one, thanks Psycho-A.
+Fixed warrens snatching sound and turned Ocean House sprinkler off.
+Cleaned SM apartment and fixed Vandal gesture, thanks to Psycho-A.
+Added twelve original musical compositions, thanks to Rik Schaffer.
+Restored lockpick sound, warehouse music and Last Round barkeeper.
+Added guard outside Empire hotel and made new maps fit screenshots.
+Improved details for all new maps and the SDK, thanks to Psycho-A.
+Corrected occult item heal rate and descriptions in plus and basic.
+Restored Blood Hunt newspaper and fixed bus stops and poles there.
+Moved finding out about the Gargoyle XPs to avoid preferring sides.
+Added subtitles for Malkavian whispers and radio, thanks Psycho-A.
+Fixed some Presence dialogue options and Vandal's background music.
+Restored flamethrower lethality and fixed some interface graphics.
Corrected Milligan not leaving his apartment in case you were loud.
Removed Tourette gun from model and made her give it in basic too.
Fixed many particle, material and subtitle errors, thanks Psycho-A.
Added script to run Bloodlines and mods under Wine, thanks to SCO.
Corrected Johansen's Empire hotel name and weapons and keys sounds.
Updated SweetFX and more presets, thanks Psycho-A and Citizenkane.
Corrected pier streetlights on three maps and removed police tapes.
Fixed some Johansen, Lily, Dima, Boris and Copper dialogue issues.
Improved game mod loader to fix disappearing shadows, thanks Behar.
Corrected Malkavian ghouls sounds and restored basic wallet scale.

v9.3                                                     26.04.2015
----
+Recreated Malkavian Maze and Warrens Shortcut, thanks EntenSchreck.
+All four new levels optimized, thanks to atrblizzard and Psycho-A.
+Improved library quest emails and restored big moon to Ocean House.
+Made tutorial guard and Luckee Star easter egg vanish after scene.
+Fixed blood pack appearing in SM haven and Skelter blocking stairs.
+Improved library and atrium maps and removed Giovanni well spirit.
+Made it possible to do the cemetery quest after getting Romero fun.
+Included eye replacer mod, but made it deselectable, thanks Nivea.
+Added installer option to deselect casting and changed disciplines.
+Corrected beachhouse dog vanishing and dealing damage after death.
+Made auto-move and walk/run toggles be definable, thanks to Malkav.
+Fixed Johansen always following you and Romero's whore trying too.
+Made it possible to freely select one of Beckett's new disciplines.
+Corrected cabbie sewer animation and Venture Tower elevator issue.
Repaired Confession cross and restored dance spot, thanks Psycho-A.
Fixed Plaquebearer quest bug and added all concept arts to Extras.
Made abandoned warehouse bum leave later if you didn't talk to him.
Removed character sheet music overlaying others, thanks Zer0morph.
Fixed three mirrored keycard backsides and centered the area icons.
Improved Grout's wife tube and electronic voices, thanks Psycho-A.
Fixed hostess, Boris, Phil, Johansen, Gimble and LaCroix dialogues.
Made Empire hotel TV unreactive and prevented invincible Cathayan.
Added museum light, Chinatown newsboxes and fixed minor map issues.
Moved Knox/Bertram XP to Knox dialogue and added pics reflections.
Fixed walk-through columns at Venture Tower and warrens reflection.
Made Igor react to killed allies and heart monitor to dead victim.
Stopped several dialogue NPCs staying tranced after being fed upon.
Restored two cool unused lines for Knox and fixed Venus money bug.
Improved wet reflections and other texture issues, thanks Psycho-A.
Showed Carson's finger and fixed Flynn's eye clip, thanks DDLullu.
Added -game mod loader and improved SDK, thanks Behar and Psycho-A.
Improved Blender scripts and added sheet injector, thanks DDLullu.
Fixed player in Carson cutscene and unlocked door, thanks Psycho-A.

v9.2                                                     30.10.2014
----
+Fixed issue with cleaned appartment and removed some cable shaking.
+Added more Trip and turnstile lines and unknown Occult item infos.
+Corrected Obfuscator aura and one missing halo for tutorial wolves.
+Restored missing Ocean House newspaper and made photos look sepia.
+Added quest state for warehouse bonus and fixed minor text details.
+Restored generators to Leopold Society and improved warehouse one.
+Added toiletries to Skyeline haven and fixed SM victim standing up.
+Changed library boss teleport behaviour and fixed his cover nodes.
+Moved Braid Talisman into the Hallowbrook atrium and removed blade.
+Restored Copper Masquerade violation and added a line about Nines.
+Added Combat to feat names, restored Soak and called Social Public.
Repaired dialogues of Knox, Heather, Therese, Vandal and Dane cop.
Fixed some dirt floating inside of holes and more minor map issues.
Made only Chunk use the Gallery Noir entrance to hide during rain.
Repaired popping Ocean House sounds and getting stuck with witness.
Fixed Jack not replying due to Python vamputil.py, thanks Hasimir.
Doubled distance in which detail models fade away, thanks to QUAKE.
Fixed Skyeline elevator issue and VPK packing, thanks vladdmaster.
Added updated fileutil.py into Python 2.7.2 folder, thanks Hasimir.
Hid Ocean House and Grout's Mansion blocks and a downtown texture.
Moved patch info to gameplay menu and fixed madness sounds effects.

v9.1                                                     04.08.2014
----
+Improved Gimble to Vandal dialogue and options to get Trip's quest.
+Fixed volume of Blood Hunt music and active discpline's durations.
+Corrected library decal problems and stuff in bloodless apartments.
+Made Hallowbrook atrium skipable but moved Ra blade there as goal.
+Added line of Venus to get rid of the turnstile in Club Confession.
+Fixed beachhouse dog clipping and tutorial guard attacking player.
+Updated Free View Weapons to plus version and fixed some histories.
+Halved damage of Giovanni ghosts and increased Obfuscator trigger.
+Fixed missing blood pack after Blood Hunt and Barabas breaking out.
+Added sound to Blood Guardian summoning and removed a blood trail.
+Changed Sheriff's sword from Brawl to Melee and improved Lily line.
+Delayed quick Nosferatu leaving and improved Pisha leaving issues.
+Corrected library and Asylum elevator problems, thanks vladdmaster.
+Moved unused Asian music to Kamikaze Zen and restored Lotus music.
+Added occult item Research text and fixed issue with Heather quest.
+Forced Skelter dialogue a second time and moved saves to old/save.
+Added library note inspection and restored tree to Leopold Society.
+Fixed Nosferatu issue for male blooddoll and warrens spiderchicks.
Removed Beckett warehouse stealth message and sleepers standing up.
Fixed tutorial invisible-popups-teleporting and minor text issues.
Repaired possible Ming after Hallowbrook bug and warrens doorblock.
Fixed Christopher, Damsel, Gary, Johansen and McFly dialogue bugs.
Corrected syntax errors using VTMBedit and fatguys not using claws.
Fixed sewer sound transitions on SM, Hollywood and Chinatown hubs.
Removed visible Pisha victim and improved scary Ocean House sounds.
Corrected tilted Hollywood streetlights and removed Asphole block.
Made Steam default folder and added numbers to Empire hotel floors.
Fixed map holes at Skyeline vent top and Leopold Society sea cave.
Repaired Grout's candles and Heather's clothes, thanks vladdmaster.
Adjusted health bar frame and weapon/discpline highlight graphics.
Hid Blood Hunt flickering with dumpsters and removed sewer copcars.
Added Nines' gesture and improved Wong Ho one, thanks vladdmaster.
Restored Giovanni meeting guys and fixed Ocean House model details.

v9.0                                                     22.04.2014
----
+Added Heather to sewers for Nosferatu and improved new idle sounds.
+Made stealth killing Johnny possible when using Obfuscate level 5.
+Added possibility to keep the quick Nosferatu in the warrens alive.
+Cleaned Mercurio's apartment after a time and fixed a SM map hole.
+Added seven missing infobar sounds and created seven infobar icons.
+Restored drug stealing quest of Trip for one XP and Finance bonus.
+Removed Blood Guardian waterspray and made Lily's purse unsellable.
+Fixed bug with casting Bloodbuff breaking off lockpicking attempt.
+Raised high firearms book requirement to 9 and updated travel maps.
+Made Hallowbrook atrium barrels solid and enemies navigate better.
+Restored Justicar to Camarilla ending and Jack's face for Lasombra.
+Moved fire axe to crashing elevator top and fatguy to atrium exit.
+Restored unused models to Society of Leopold, warehouse and Zhao's.
+Changed library to combat zone and fixed rotunda decal flickering.
+Repaired hearing warehouse boss conversation twice and some floats.
+Made Nadia react to zombies damaging player and removed fake door.
+Gave Occult Nut a Scholarship bonus and fixed new discipline lines.
+Fixed icons at Giovanni Mansion and made Bruno react to feed-kill.
Added modified trackerscheme into Extras to change Malkavian fonts.
Repaired Carson, Knox, Damsel, Yukie, Regent and Hatter dialogues.
Fixed two inverted textures and renamed Sheriff's warform Behemoth.
Restored three King's Way headrunner for Nosferatu and Malkavians.
Lowered McFly's float rate and fixed references to missing Heather.
Added documents to Extras to reveal where restorations originated.
Attached floor number to Empire Arms suite names in hotel computer.
Fixed three wrong loop sounds and moved a Mandarin line elsewhere.
Corrected some bug fixes that were lost in 8.9, thanks vladdmaster.
Restored blast door to Giovanni crypt and fixed tutorial door bug.
Improved Nosferatu Nines intro and map details, thanks vladdmaster.
Fixed sewer sound transitions on SM, Hollywood and Chinatown hubs.
Corrected two bad Lotus Blossom icons and lowered Skyeline humming.

v8.9                                                     02.02.2014
----
+Recreated missing Hallowbrook atrium level, thanks to EntenSchreck.
+Moved Sabbat choice into Hallowbrook atrium and added missing XPs.
+Restored male blood doll at Red Dragon by using former Tong mugger.
+Recreated "maze" room at Grout's Mansion and restored three icons.
+Fixed some minor discipline issues and restored the basic versions.
+Restored ten decals, moved others and removed restored from basic.
+Fixed warform using occult items issue and improved Bloodheal rate.
+Added two inspections, warehouse boss talk trigger and moved Yugo.
+Increased flamethrower fuel and provided Desert Eagle ammo earlier.
+Disarmed Dominated guard bomb on taking and fixed one sound there.
+Avoided crashing when testing out too many histories, thanks to AJ.
+Added Intimidating Milligan for Nosferatu and fixed armor effects.
+Made it possible to give redundant items to LaCroix and other NPCs.
+Unleaked and improved library and atrium maps, thanks to Psycho-A.
+Restored discipline or weapon selection toggle and Flynn as vendor.
+Moved crying girl near cops at pier and changed her to unique NPC.
+Restored Ocean House boiler model and animated warehouse generator.
+Fixed details of thug, Andrei, Ox, LaCroix, VV and Lily dialogues.
+Made spooky cover sound once and plus only and added steam to Yugo.
+Removed thugs from diner after quest if you avoided fighting them.
+Fixed warrens mist issue and made fatguys use the claws more often.
+Restored or fixed fourty NPC gestures and fixed Confession blocks.
+Made Braid Talisman raise Wits and restored SM Chunk avoiding rain.
+Added Empire hotel and ending dance spots and made Glaze one plus.
Fixed two particles, a door and added loading tips texts to Extras.
Restored three skyboxes to warehouse, Dane and Hallowbrook atrium.
Corrected Grout's Mansion decals, tutorial bucket and tattoo boxes.
Fixed croucher laughs and no floats for females bug, thanks to AJ.
Updated SweetFX to 1.5 and included a preset, thanks to eeekitties.
Fixed pause messages in engine.dll, random sounds and many floats.
Added widescreen resolution support to engine.dll, thanks to Behar.
Repaired many sound files with broken looping, thanks to Psycho-A.
Improved installer by providing additional choices on installation.
Added Bloodlines SDK to Extras folder, thanks Psycho-A and Fire64.
Corrected three interesting places with wrong bum animations in SM.

v8.8                                                     24.10.2013
----
+Added animations for all active disciplines, thanks to EntenSchreck.
+Made new elevator arrows light up and stealth work on clinic guard.
+Fixed Lasombra teleport death and made new occult items undroppable.
+Added Humanity for keeping Zhao alive and restored two feed sounds.
+Fixed getting new discipline, grenade, divine light and Vandal line.
+Restored jenny_cries sequence on SM hub for Jeanette near Mercurio.
+Removed buggy Command schedules and fixed Vision of Death and Sleep.
+Restored animal movement for new warform and swapped some MP items.
Made King's Way door consistent and fixed a Society of Leopold lock.
Restored Muddy fighting killer animation and so fixed the cutscene.
Fixed warehouse thug with long range eyesight and minor text issues.
Restored sounds at Society of Leopold and made others more audible.
Fixed SM and Hollywood hub club music and restored a Vesuvius sound.
Added or removed doorknobs to make it obvious which doors are real.
Restored unused floats of Larry and five civilians, cops and guards.
Removed histories, skip intro and Nosferatu/NPC changes from basic.

v8.7                                                     23.07.2013
----
+Added a Sabbat option to endgame and improved library level details.
+Turned library boss to Lasombra and made him appear at SM junkyard.
+Improved restored broadsword damage and made Dane items undroppable.
+Added dialogue to diner trap and moved Obfuscator to original spot.
+Set eight occult powerups to be unknown unless Research stat is met.
+Removed girl body from King's Way again and two Ash sewer switches.
+Made turnstile turn and restored Empire TV news, thanks vladdmaster.
+Fixed downtown elevators and added five arrows, thanks vladdmaster.
+Added credits to easter egg ending and moved Yugo near SM blueblood.
+Removed a Gangrel animation and fixed idle howling during dialogue.
+Fixed Mandarin dialogue not starting if Obfuscated and a Carson bug.
+Made Strauss give Fae Charm and Isaac Pearl or money when in basic.
+Placed two patrons into Lotus Blossom and lowered perceptions there.
+Restored several unused doors to tattoo shop and Hallowbrook lobby.
+Increased level 3 Dementation and Domination disciplines' durations.
+Made Romero boink possible after zombie quest and Wong Ho stand up.
Activated Asian vampire laptop screensaver and cover sound variable.
Fixed basic poster quest order and only Nosferatu getting CD email.
Corrected several downtown NPCs stats and Beckett's cut lines again.
Added netcafe entry update for Ash and fixed Venture Tower handles.
Fixed final Masquerade violation crashes and five bad opening doors.
Corrected console errors on game start and a museum guard AI place.
Restored plaguebearer quest log, Regent line and Kerri waiting line.
Hid male Gangrel player model hole and rearranged UP Python scrips.
Prevented zero Humanity in Johansen dialogue and delayed Nines line.
Corrected Anders/Ingvar and Larry's quest errors using sound files.
Repaired bad Ocean House basement sprite and traffic lights on hubs.
Locked morgue freezers, fixed text issues and improved level names.
Improved observatory cutscene cameras and fixed high stats tutorial.
Fixed killing downtown Ming and replaced boat-ending Asian vampire.
Corrected tutorial issues and restored one sign, thanks vladdmaster.

v8.6                                                     24.04.2013
----
+Improved getting new discipline and keeping the .38 in the tutorial.
+Restored Confession turnstile, King's Way animation and six decals.
+Made Pearl of Dubai Charisma powerup again and fixed Mercurio money.
+Restored discipline crosshair, tutorial graphic and some particles.
+Improved Presence dialogue options and raised haven bum cash to $10.
+Added new idle animations, some with whispers, thanks EntenSchreck.
+Restored Dominate Command instead of Trance, thanks to EntenSchreck.
+Added Humanity losses and gains to SM blueblood and tutorial guard.
+Removed Toreador and Ventrue stats bonuses and improved library map.
+Restored embrace and discipline hud particles, thanks EntenSchreck.
Returned Steyr AUG Sabbats to Hallowbrook and Zulo fire sensitivity.
Made Beckett invincible at the pier and updated walkthrough issues.
Corrected XP and restored log for unravelling Knox and Bertram plan.
Fixed Phil and Vandal dialogues and raised Well Educated penalties.
Moved possible Gimble's door block and added missing tutorial sound.
Fixed Romero moving strange if you block him and minor text issues.

v8.5                                                     12.02.2013
----
+Shortened library level cutscene and killing actions at Ground Zero.
+Improved library riddle, boss navigation and fixed bookcase issues.
+Added and fixed some last library textures, thanks to burgermeister.
+Fixed idles with Imalia and Mitnick and changed horror tape titles.
+Made Nosferatu break Masquerade easier and Romero return once again.
+Restored Ocean House valve, sprinkler, cans, doors and some sounds.
+Fixed Danielle and Gimble problem and a misplaced Ocean House spark.
+Moved easter eggs hint from note to restored laptop at Luckee Star.
+Restored two menu effects and unused Pisha eyes for Lasombra female.
+Repaired Blood Shield light effect and updated Presentable history.
+Removed Domination's Mass Suicide to add Sleep, thanks EntenSchreck.
+Restored Malkavian disciplines Veil and Voice, thanks EntenSchreck.
+Fixed Thaumaturgy disciplines not working again after player frenzy.
+Changed Jian into broadsword and armed Chang brother with a katana.
+Restored ten scenery props into sewers and Hallowbrook hotel levels.
+Improved Bloodheal sound and restored HUD sounds and botch message.
+Added way to get a new discipline from Beckett, thanks EntenSchreck.
+Restored water, steam, fire and vomit effects, thanks EntenSchreck.
+Fixed dead guard acting at Skyeline Apartments and stuck headrunner.
+Restored character creation questions and a sewer-cabbie animation.
Improved tutorial popups and removed forced Andrei speech subtitles.
Prevented dead Tommy Flayton from writing review, thanks to Malkav.
Returned Heather before talking to Prince but referred to new haven.
Removed hatch reflection and updated and restored model sewer maps.
Deleted computer restorations from basic and restored two passwords.
Removed getting poster from VV in basic and fixed guard bodies bug.
Fixed double business card, clinic guard, Damsel and Isaac problems.
Repaired warrens and boiler pipes and reconciling sisters extra XP.
Added SweetFX to Extras folder, thanks for the tip to Caner Özdemir.

v8.4                                                     08.11.2012
----
+Recreated library, thanks for beta testing to vladdmaster and Stosh.
+Unrestored library props elsewhere and fixed warform missing model.
+Fixed dead beachhouse dog doing damage and getting extra gallery XP.
+Added Humanity loss for killing Ash or Johansen at Leopold Society.
+Improved warehouse boss perception and swapped model with bartender.
+Removed Giovanni sarcophagus shortcut and added missing Bertram XP.
+Restored two spiderchick and fatguy animations, thanks EntenSchreck.
+Made Kiki leave Red Dragon and corrected original music at SM pier.
+Modified Potence and Thaumaturgy animations, thanks to EntenSchreck.
+Removed beachhouse's money detection and made dog start peacefully.
+Made name plate unsellable and updated walkthrough of library quest.
Fixed Humanity loss of Hollywood thugs and missing Heather options.
Prevented ways to break hospital, Mandarin and Romero quest scripts.
Fixed cabbie's seating for some maps and people not giving jewelry.
Restored Johansen dialog Humanity changes and cut-off Beckett lines.
Fixed Venture Tower cameras and restored one Asylum elevator sound.
Added magazine quest state for killing Flynn and aborted getting it.
Corrected Hallowbrook hotel door opening at and moved two spawners.
Fixed Isaac/Gargoyle quest state bug and adjusted several histories.
Removed bad sentence of Mercurio and one of Isaac's two "evening"s.
Fixed Ocean House double ghost, elevator buttons and a missing moon.
Corrected floating Mercurio and passive guard inside Venture Tower.
Added newspaper of stealth Glaze and changed Fu newspaper condition.
Corrected King's Way details and a Hollywood Asian theater trigger.
Fixed Ash, Jack, Vandal, Romero, Mercurio and Therese dialogue bugs.
Restored inaccessible Prince, Damsel, Flynn, Hatter and Ming lines.
Improved TV and radio state consistencies in SM and downtown havens.
Decreased crossguy reaction and fixed bad doorknob at Fu Syndicate.
Fixed Sabbat Obfuscator stats, warehouse inspection and Bertram bug.
Disabled buggy spawner in warrens level and fixed Noir cop problem.

v8.3                                                      24.09.2012
----
+Restored guard dog that can do damage at beachhouse, thanks Lenuska.
+Added missing steam to clinic, Ocean House, Vesuvius and Hollywood.
+Fixed female Gangrel idle and crossbow wield models, thanks DDLullu.
+Restored Kiki to Red Dragon and actors being killed at Ground Zero.
+Corrected new Knox line subtitles and removed cast autoexec binding.
+Restored sequence of Arthur, Wong Ho, Yukie and the pinball player.
+Added shaking cables and a hidden Ash sewers whisper for Malkavians.
+Restored Mr. Ox's pipe and made all restored gestures be plus only.
+Removed .38 of Flynn and made the GLOCK of Boris be plus patch only.
+Restored hot tub guy sequence and corrected Chastity disappearance.
+Moved Vesuvius barkeeper to Confession and changed invincible Larry.
+Changed Gangrel warform to wolf version, thanks to RR_DF_RaptorRed.
+Restored Pearl of Dubai as Celerity powerup and braid for computers.
+Removed Nosferatu change again, because it only affected the radar.
+Repaired temple Chang skin and gave katana to him and blade brother.
+Restored King's Way props, Giovanni ghost sounds and temple chants.
+Corrected broken Venus script, doubled Arthur and minor text issues.
+Fixed first person hand for female Tremere, thanks to EntenSchreck.
+Restored over twenty unused sound effects and random schemes sounds.
+Made Kiki at Red Dragon react to damage and fixed nonmoving Arthur.
+Changed Giovanni spirits and restored warehouse explosion particles.
+Corrected disappearing Chang brother bug by dropping blade in plus.
Hexedited floats in parking garage and downtown hub, thanks DDLullu.
Fixed hacking Krimeputer and added missing particle impact effects.
Returned warform hopping again and five intersting place animations.
Repaired bad clockhands in intro, bailbonds and observatory levels.
Fixed sick bum respawning downtown and warehouse locked double door.
Removed bugged plaguebearer sewers lock and Mandarin dialogue loop.
Added BSPDetail, Blender, VampEd and import/export to Extras folder.
Restored SWAT rifle from Mercurio and dropped Chang blade in basic.

v8.2                                                     30.07.2012
----
+Restored first person Thaumaturgy animation, thanks to EntenSchreck.
+Placed a GLOCK pistol in Fu Syndicate and increased new idle rates.
+Restored Presence dialogue tutorial popup and missing junkyard dogs.
+Made NPCs act longer distance to Nosferatu, thanks to EntenSchreck.
+Corrected Danielle disappearing from Asylum and added oak animation.
+Restored option to stealth kill Johnny and to get gallery bonus XP.
+Fixed beachhouse cash bug by using cigarbox and a loop with the bum.
+Restored leaf and smoke to Grout's Mansion and fog to warrens lake.
+Extended first warrens spiderchick cutscene, thanks to EntenSchreck.
+Added option to sell severed arms to Pisha and tutorial armor info.
Corrected some new histories bugs and added handle to Venture Tower.
Fixed an elevator icon at Venture Tower and corrected two map ones.
Restored several dialogue gestures of Venus and a big line for Knox.
Fixed a few gender related bad dialogue sound files, thanks to UDM.
Added fixed lockpick and physcannon item files to free view weapons.
Restored Ocean House moon and fixed floating rails issues downtown.

v8.1                                                     26.06.2012
----
+Restored third person Thaumaturgy animation, thanks to EntenSchreck.
+Fixed tutorial guard Humanity issues and getting stuck with Gimble.
+Added Fortitude, Potence and more particles, thanks to Entenschreck.
+Restored private dance for Misti and Beckett leaving the warehouse.
+Improved new idling and new bats, thanks to Entenschreck and Malkav.
+Restored Andrei scene and Presence effects, thanks to Entenschreck.
+Moved new Gary poster quest items around to prepare for library map.
+Improved poster quest logs and canceled Vandal quest on paying him.
+Added missing Animalism particles and update to Ash's Leopold quest.
+Restored an Ocean House ghost sequence and missing tutorial sounds.
+Added Blood Eye as Purge partial resistance, thanks to EntenSchreck.
Improved cameras of Nines' intro, roof exit and epilogue cutscenes.
Fixed claws usage in gallery, Hallowbrook hotel and Grout's Mansion.
Corrected Yukie and Pisha dialogue issues and restored Nines' line.
Restored Venture Tower bodies after Sabbat attack, thanks to Malkav.
Removed illogical first SM quest info and fixed minor text details.
Fixed impossible warrens start location and teleporting at junkyard.
Added cfg and scripts for modding, thanks to Dheu and EntenSchreck.
Restored three more histories for each clan and minor level details.

v8.0                                                     30.04.2012
----
+Restored many particles and idle animations, thanks to Entenschreck.
+Made werewolf damageable, thanks to Lenuska and also andagangrel89.
+Added note to Luckee Star to give some hint on werewolf easter eggs.
+Restored Sheriff conjuring Bat's Communion, thanks to Entenschreck.
+Dropped Sheriff sword on the roof, thanks MooCHa for missing models.
+Restored guard in the tutorial, thanks MalkyJeff and burgermeister.
+Corrected issues of new Vandal options and removed Skyeline trigger.
+Restored proper Giovanni spirit use and inventory disciplines slot.
+Increased cemetery gate health and restored basic patch spawn rates.
+Improved bobcat, forklift, Chinese mugger and Obfuscator sequences.
+Restored sewer-cabbie rat for Malkavians and wolf-ending easter egg.
+Enabled dynamic light for torch and fixed special Vesuvius meeting.
+Restored Blood Theft instead of Blood Salvo, thanks to Entenschreck.
+Added dialogue Presence and Tremere Domination-in-dialogue effects.
Removed most restored models, skins, icons and key binds from basic.
Reduced slime particles at temple and hid observatory debug switch.
Corrected Ocean House quests not closing if you refused the gallery.
Improved plus/basic Python code and fixed morphine quest state bug.
Fixed minor map problems and many dialogue details, thanks to Fabio.
Corrected Luckee Star hotel easter egg and Gimble intercom problem.
Re-fixed hostess bug and added crosshair to free view melee weapons.
Fixed bugs with Ash and Chastity quests and with the medical guard.
Added shoe textures to Ash, Ash double and Slater, thanks to MooCHa.
Restored eight sounds to Ocean House, two to SM and one to warrens.
Closed museum and Hallowbrook map holes and changed the doors there.
Fixed Tseng, guard, stripper, raver and more models, thanks MooCHa.

v7.9                                                     24.11.2011
----
+Restored Giovanni spirit, video victim and over fifty scenery props.
+Changed condition for forklift sequence and restored Protean icons.
+Added option to send Gimble to Vandal and a museum panel inspection.
+Restored final two music pieces, thanks to Malkav and Rik Schaffer.
Corrected Romero not mailing and Vandal not giving additional lines.
Fixed chandelier and camera rod textures, also drinking glass clip.
Removed newspaper from downtown in basic and fixed minor map issues.
Added Packfile Explorer 3.9 to Extras folder, thanks to Dave Gaunt.
Fixed Hitman quest problem and restored lines of Lu Fang and Carson.
Repaired dancer behaviour at Confession and added it for Glaze too.
Restored Blood Hunt music, ballroom shaft of light and Sin Bin sign.

v7.8                                                     21.10.2011
----
+Added Masquerade violation on public sweeper kill, thanks to Malkav.
+Made artificial claws do only lethal damage according to WoD rules.
+Moved new music from warrens to tutorial and fixed Kamikaze Zen bug.
+Restored hidden sequence of Obfuscated Sabbat in SM to other place.
Toned new music on the pier down and improved Obfuscate description.
Added original particles to basic so it will revert them from plus.
Decreased skybox reflections in SM and the ENB mod, thanks to Felix.
Re-fixed theatre camera bug and corrected several minor map issues.
Fixed schrecknet commands being available after hubs were activated.
Added diagonal third person view camera commands to keydef options.
Removed Jack from haven during taxi ride and repaired Phil/Bill fix.
Made it possible to continue E's quest after visiting Vandal often.
Added bus stop and sewer map landmarks, also fixed lamp texture bug.
Repaired Victor loop and added glass breaking sounds to beachhouse.

v7.7                                                     18.08.2011
----
+Fixed Hatter staying unapproachable and a very rare crash at Zhao's.
+Made Vandal quest available later and added an XP for alternatives.
+Changed Zhao bonus XP point condition so you need to kill all Tongs.
+Improved warehouse forklift sequence and added observatory railing.
Corrected placing nonexistent theatre camera and minor text details.
Fixed clinic guard not dropping key if killed by seductive feeding.
Returned dialogue history definition and made camera keys definable.
Made Isaac gift money on basic issue and reset endgame haven state.
Added ENB series mod to Extras directory, thanks to Boris Vorontsov.
Modified installer so it can automatically run ResPatch at the end.
Updated Extras weapons to switch depending on view using plus stats.
Fixed sliding chute down and elevator call issues in Venture Tower.
Corrected wrong material settings of Pisha's hair, thanks to PsyCHo.
Added Python 2.7.2 update to Extras directory, thanks ColonelAlias.
Changed installer so it will only update 1.2 vampire.dll for retail.
Made Phil/Bill fix trigger only if Phil is dead, which removes him.

v7.6                                                     17.07.2011
----
+Restored unused OST music, thanks Rik Schaffer, SteveMV and Kendrel.
+Made keeping Jack's .38 pistol possible and restored bisexual Phil.
+Added Humanity loss for sending Copper to Nines and no-stake option.
+Tried to fix possible name plate bug and updated missing fists fix.
Repaired spawning of Hallowbrook enemies and more minor map details.
Fixed lost Mercurio email and removed added Gargoyle XP from basic.
Added dumpster downtown to cover map hole and made Phil stay longer.
Corrected Imalia only giving one camera and the missing pier music.
Added Malkavian whispers transcript to Extras, thanks to an unknown.
Fixed Nosferatu and Malkavian detection script of King's Way level.
Added info about auto-moving and walk/run toggles to tutorial popup.

v7.5                                                     30.05.2011
----
+Corrected restored content appearing in Giovanni Mansion and temple.
Made Heather meet you out from Venture Tower and fixed Gargoyle XP.
Set cameras stack limit to five and fixed bad stack limit variables.
Moved unreachable NPCs at Hallowbrook hotel and fixed door opening.
Fixed Regent's lip-sync, warehouse pallet and railing clipping bugs.
Stopped VV sending emails if pissed and fixed some minor text bugs.
Fixed wrong weapon stats shown using new client.dll, thanks to int9.
Made Red Dragon hostess stay and repeat her elevator conversations.
Returned original poster order and clerk sexual bias to basic patch.
Fixed claw brother being susceptible to one-hit-kill by Possession.

v7.4                                                     18.04.2011
----
+Made Danielle stay on sending Patty to Vandal and removed safe node.
Removed many notable restorations from basic patch to be plus only.
Made skip intro always work > 800x600 and fixed double pawnshop key.
Corrected prostitutes privacy, Ash switch and Giovanni name issues.
Included auto-moving and walk/run toggle, thanks to Dheu and Malkav.
Fixed parking garage gang war problem and Ming as Nines size issue.
Returned Larry's locations in basic patch and removed his email too.
Corrected facing Ming Obfuscated and readded claws inventory infos.
Fixed tutorial conditions for high stats and area discipline popups.
Repaired asking Strauss about dealt-with-gargoyle and text details.
Removed body bag models from Dane and added one into Giovanni crypt.
Restored Nines line, sister reconciliation and fixed Bertram issue.
Swapped Anarchs back in basic patch and fixed getting XPs at Zhao's.
Tweaked Strength history to avoid making Bloodstar powerup useless.
Fixed camera cycle and possible mute Chunk, thanks to burgermeister.

v7.3                                                     11.01.2011
----
+Moved Yukie temple end trigger and fixed spider chick Boil reaction.
+Corrected a Giovanni candidate quest state and removed entry items.
+Made inspection particles a bit less intrusive, thanks to ZylonBane.
Restored GLOCK to cop on the pier and mafia patrol to Empire hotel.
Corrected conditions for mentioning Rossilini and other text issues.
Fixed problems on approaching Skelter and during the intro walkout.

v7.2                                                     11.11.2010
----
+Made SM haven stay always active and placed Ash's cell key on crate.
+Adjusted sell values, melee stats and fixed netcafe headrunner bug.
Fixed possible video courier retrigger bug and some dialogue issues.
Prevented Heather's comeback when returning from lower Hallowbrook.

v7.1                                                     16.09.2010
----
+Added lower player sell values to all weapons which were missing it.
+Restored missing Bertram quest state and fixed broken Isaac update.
+Repaired Venture Tower bomb timer and added it to elevator trap too.
+Moved Pearl of Dubai to Regent and restored Isaac Fae Charm reward.
Added lights-through-walls fix to engine.dll, thanks SomeCommentDoe.
Improved breaking museum windows and fixed more minor level errors.
Removed new Mitnick quest and Chastity's sword from the basic patch.
Fixed headrunner dropping through netcafe floor and a German popup.
Locked gallery front after crime and restored lockpick to warehouse.
Corrected wrong painting positions after slashing then re-entering.
Fixed mirrored beer labels and minor dialogue problems of some NPCs.
Restored Therese and Jeanette reconciling and cash to Kamikaze Zen.
Improved missing fists fix and made pool stripper appear later only.
Made SM laptop stay in old haven in case of random Skyeline issues.
Tweaked Cleopatra history to avoid making Obfuscate powerup useless.
Removed Fae Charm from Tseng to avoid bug on getting it from Isaac.
Fixed blood doll sound and line so it doesn't refer to women as men.
Made Fu Syndicate doors move slower and added a lantern to warrens.
Disabled endless arrow spawning in the chests of first temple level.

v7.0                                                     17.06.2010
----
+Repaired Tourette ammo and added XP and redemption for the Gargoyle.
+Improved Yukie translation and removed GLOCKs from the Hallowbrook.
+Added SWAT rifle ammo model and restored several blunt weapon stats.
+Decreased bomb timer to 30 seconds and edited endgame Skelter line.
Restored about a hundred unused floats and removed bad ones of Kiki.
Removed SM clinic combat zone and added netcafe combat zone switch.
Fixed tutorial blood reset and improved Chunk Gallery Noir sequence.
Opened beachhouse door on combat and moved blanket to Hannah's bed.
Fixed Gary's photo sound, Ricky's glasses and improved emails order.
Removed Grout's trigger after use and Murietta's key if not needed.
Swapped some pedestrians to reduce clones and added Yukie quest log.
Fixed Yukie boots, Sabbat ankh and Barabus feet, thanks to DDLullu.
Displaced two buggy Luckee Star doors and made the sweeper stronger.
Corrected Lily cutscene and stalker hair models, thanks to DDLullu.
Fixed female Tremere hair texture, thanks to the skin of p0rnstar13.
Added emotions to Ming's temple lines and fixed Hallowbrook script.
Swapped Mitnick clone with player model and added temple door sound.
Tried to fix zombies and stalkers occasionally using normal voices.
Restored Barabus line and fixed minor dialogue issues of a few NPCs.
Fixed Yukie stats at shop, Maria invitation and Venture Tower door.

v6.9                                                     31.03.2010
----
+Made Tourette give ammo and repaired mugger and bum humanity issues.
Fixed wrong Luckee Star keycard model and Chunk's sitting position.
Added new warehouse quest log and animation to new DJ at Confession.
Improved minor text issues of quest logs, tutorial popups and info.
Fixed dialogues of Jack, Mercurio, Regent, Knox, Bertram and Imalia.
Stopped Dane cop from looping and removed one unvoiced line of his.
Forced dialogues of Hannah, video courier and Skelter at Last Round.
Prevented random missing hands bug and restored unused Venus lines.
Fixed refresh-rate problem in shaderapidx9.dll, thanks to Frank7777.
Removed push blockade at Fu Syndicate and bad decals at the museum.

v6.8                                                     12.02.2010
----
+Made bail bond returnable to Lily and restored VV's poster to basic.
Restored three paintings into Empire hotel and moved others around.
Fixed static NPCs on downtown hub and restored some Society weapons.
Restored report to SM clinic and newspaper pictures to Ocean House.
Swapped wrong Luckee Star key model and SPAS into Hallowbrook hotel.
Restored two context icons into Grout's room and sarcophagus crypt.
Repaired dialogues of Heather, Jack, Arthur, Pisha, Dima and hooker.
Fixed Isaac reward in basic and restored context icon to eye quest.
Restored three infobar icons and three scenery models to King's Way.
Corrected Ocean House steam cloud directions and minor map details.
Prevented restored NPC conversations from triggering multiple times.
Hid doors icons at Grout's Mansion and used phone prop to open one.
Restored rain to beachhouse and removed it from Ocean House outside.

v6.7                                                     22.12.2009
----
+Prevented feeding twice from Romero and getting him a rival in love.
+Made Tourette give you her gun and forced endgame Skelter dialogue.
+Moved frenzy powerup from basement into hollow book in Grout's room.
+Forced Nosferatu to use Empire Arms vents and fixed map transition.
+Fixed Regent's reward and Yukie bug and improved on her translation.
Moved some new props and restored a few more to warrens and Asylum.
Restored Fu Syndicate alarm switch sequence and three context icons.
Fixed Jack, Isaac and LaCroix dialogues and theatre web log update.
Added walkthrough including patch changes, thanks to vampyri_lestat.
Moved new raver as DJ into Confession and returned old DJ to Glaze.
Fixed intro paintings, added two more and swapped two with Skyeline.
Corrected look-through problems of male Tremere and Ventrue models.
Removed poster quests from basic patch and added a log for Tourette.
Finally fixed Beckett's "wait" freeze bug, thanks to burgermeister.
Corrected Heather changing clothes and added Gary to intro sequence.
Added missing endgame quest logs and pause key option to keys menu.
Restored four female and two male hand skins and Nosferatu eyeballs.

v6.6                                                     16.11.2009
----
+Gave Humanity for Dominating Milligan and fixed tutorial key and XP.
+Added Masquerade redemption for Gary's photo and fixed weapon info.
Translated Japanese and Russian text, thanks to szhinji and Lenuska.
Made Misti refill and fixed prophet and pinball dude not animating.
Fixed fire not triggering at junkyard and basic poster quests mixup.
Returned original flicker-less decals to Dane, netcafe and warrens.
Fixed some dialogue issues of Imalia, LaCroix, Isaac, Jack and Phil.
Adjusted a too strong history and removed many possible text loops.
Locked outer Tawni door and corrected bad Giovanni invitation names.
Corrected clipping problems for Venture Tower lamp and cop glasses.
Fixed frenzy for all clans and eye colours, thanks to Zer0Morph2000.
Prevented Heather from appearing in Hallowbrook if you ignored her.
Restored dialogue tutorial popups and removed Ventrue's rat feeding.
Added the frenzy animation to common NPC models, thanks to DDLullu.
Fixed Voerman emails not appearing and Copper suddenly having money.
Restored Isaac's gift for the warrens in basic being Toreador only.
Used white SWAT skin at Venture Tower and Nines skin at solo ending.
Placed alternative Cal skin into diner and rookie cops on the Dane.
Restored Lu Fang, Therese and hustler to Lotus Blossom and Vesuvius.
Used new Ming skin in Empire hotel and hustler and girl in Asphole.
Restored headless security corpse and severed head to warrens level.
Placed two scrubs into Grout's Mansion and bartender in Last Round.
Added raver and female models into Glaze and missing VW bus to pier.
Placed alternative Chang in temple and fixed Luckee Star fireplace.
Used alternative stripper skins at Sin Bin, Vesuvius and Giovanni's.
Restored over two hundred scenery props and over forty sign decals.
Added breakable tomb stone, gas tank, board and phones to warehouse.
Fixed and added breakable air compressor and board into Ash sewers.

v6.5                                                     18.09.2009
----
+Added mugger to Chinatown and pinball player sequence to Last Round.
+Granted Humanity when comforting Copper and removed loss for Nines.
+Lessened Dragon's Breath damage and made bolts buyable a bit sooner.
+Added SM haven key and missing particle effects for a lot of claws.
+Provided newspaper downtown and restored Skyeline and junkyard ones.
Restored unused shovelhead to Hallowbrook and alternate Tong model.
Raised health of Larry and re-fixed Copper leaving for the infusion.
Fixed log bugs for Haxxor, Gargoyle, Pisha, Lily and pimpin quests.
Made the bad luck talisman not sellable and corrected Knox's secret.
Increased claws range and lowered Desert Eagle accuracy on running.
Returned Protean warform hopping and basic stats but lost it's info.
Improved netcafe and pawnshop trigger fixes and minor text details.
Made installer recognize the default directories, thanks to voodoo_.

v6.4                                                     30.07.2009
----
+Corrected Venture Tower Dominated guard timer to be plus patch only.
+Adjusted reload sound of Dragon's Breath and fixed a Mitnick quest.
+Increased Dragon's Breath and crossbow damage and lowered ammo cost.
+Added missing inspection nodes for throwing star and warrens GLOCK.
+Fixed Tremere Domination for Trip and added one for the hotel clerk.
Corrected replacing Lily giving no XP and fixed Lily on beach line.
Repaired bad elevator button at Empire hotel and Dima not attacking.
Fixed Knox's and Johansen's secret issues and phone start in diner.
Corrected Beckett's bonus dialogue once more and minor text details.
All dialogue files checked for similar bugs, thanks to RobinHood70.
Added two quest states regarding the Gargoyle, Isaac and the Regent.
Made talisman locker not disappear and fixed Nadia dialogue issues.
Changed camera spot icons at Tawni's place and removed notice timer.
Fixed endgame floating astrolite and near dead patient standing up.

v6.3                                                     02.07.2009
----
+Added Mitnick quest for library card and changed Gary's quest items.
+Increased Dragon's Breath damage and created a separate round type.
+Placed a katana into Fu Syndicate and a girl into VV's private pool.
+Added Humanity point and lines for giving Lily's items back to her.
+Swapped crossbows in temple basement with Steyr AUGs like in ending.
+Removed Humanity loss for killing victims at the Hallowbrook hotel.
+Added explosion and boss flag for the Venture Tower Dominated guard.
Fixed missing Dima and Russians issues and cop and Bruno subtitles.
Improved Gargoyle logs and delayed phone dialogues to fit animation.
Fixed edicts errors generated by use of Auspex, thanks to SunBlade.
Exchanged Venture Tower guard models and armed them with Steyr AUGs.
Fixed Arthur/Knox issue and Kiki's standing hair, thanks to MooCHa.
Corrected Beckett's bonus dialogue and two wrong Ocean House sounds.
Removed three more plus items to improve basic patch compatibility.

v6.2                                                     25.05.2009
----
+Restored Dragon's Breath available from Mercurio, thanks to Lenuska.
+Swapped Pyro Crossbow at Fu Syndicate with squashed Odious Chalice.
+Exchanged the Pyro Crossbows of temple guards with normal crossbows.
+Removed prop grenade and made Gary ask for squashed Odious Chalice.
+Raised minimum Humanity for killing innocents to three like in hubs.
+Placed GLOCK near killed sewerworker as mentioned in his clipboard.
Returned boss flags for Chastity and Mercurio and fixed Fu terminal.
Removed restored items in basic patch to improve mod compatibility.
Corrected Phil dropping freezer passcode note and minor text issues.
Fixed grenade icon, Empire note and possible Leopold Society crash.
Removed some SM clinic ambient sounds and made Dima go wait outside.
Restored Arthur and Knox bounty hunter lines and fixed Isaac issue.
Removed a few unusable Ming temple doorknobs and corrected fax date.
Improved Protean claws inventory model and icon, thanks to Lenuska.

v6.1                                                     22.04.2009
----
+Restored active fragmentation grenade from Nines, thanks to Lenuska.
Made Hannah's vents unlock and removed blueblood after alley foray.
Added two more times to feed from Heather and fixed Sin Bin PC text.
Fixed dialogues for Patty, Gary, Romero, Pisha, Arthur and Beckett.
Made Auto-Level button unambiguous and fixed icons at the warehouse.
Doubled explosion damage of shellboxes and fixed Leopold Society's.
Restored an unused poster to parking garage and six more to netcafe.
Fixed getting a second key from Empire clerk and minor text issues.
Prevented museum guard from dropping multiple storage room keycards.
Made Jack acknowledge stealth killing the tutorial sneaking Sabbat.
Moved Empire hotel computer to backroom and raised helicopter noise.
Fixed log update issue when killing Boris and a Cal dialogue issue.
Made it possible to trigger serial killer quest from all newspapers.
Fixed tutorial Humanity bug and other Python errors, thanks to mzz.
Restored laughter of Mr. Ox and a few sounds around the Ocean House.
Corrected a wrong sign in warrens and removed icon of Mitnick's PC.
Swapped wrong manhole covers for Griffith Park and Giovanni Mansion.
Removed test button in Ventrue clan popup and minor level problems.
Improved sound effects of morgue doors and Kamikaze Zen vault doors.
Fixed texture error with the third Gangrel armor, thanks to MooCha.
Restored some missing sound schemes and fixed a few particle errors.
Added missing third card playing thug to conversation at warehouse.
Corrected console bugs and replaced grenade icon, thanks to Lenuska.
Fixed Protean level 5 melee switching and Giovanni guard awareness.
Restored missing Malkavian lines for Damsel and some last subtitles.

v6.0                                                     15.02.2009
----
+Added Tremere Domination tutorial info and fixed all clans CD email.
+Repaired Heather remembrance dialogue and Gary's poster quest bugs.
+Made Ventrue enemies use disciplines and SWAT in armor not biteable.
+Added quest logs for Giovanni candidates and for the final endgame.
+Restored security guard and a sequence into the Skyeline Apartments.
+Made Romero pimpin quest available after zombie and fixed Firearms.
Set the date of the game to 22.10.2004 and fixed minor text issues.
Added option to pay Vandal in case you can't find him a replacement.
Restored two Asylum emails and added Johansen to Empire suite list.
Swapped an unique quest car at Giovanni's and repaired it's texture.
Restored meeting sequences for the downtown, Hollywood and SM hubs.
Moved library card to locked Empire room and fixed Chunks attacking.
Added subtitles for the remaining conversations, thanks to Voerman.
Stopped Copper from leaving for infusion and improved selling order.
Repaired Nadia's "c'mon" sequence, speaker names and a door handle.
Restored Ventrues to Tower using females and Toreadors as variation.
Swapped wrecks on Blood Hunt map and added missing bar-break sound.
Fixed quest log update and XP gain on reaching Ming's inner sanctum.
Made sweeper and Bertram Tung use disciplines if they are attacked.
Restored censored blood for intro and added some to the Hallowbrook.
Fixed pony tail of Kerri and glasses of Mandarin, thanks to MooCha.
Removed not working blood return when fighting against the Tzimisce.
Prevented spoiling the secret of the Giovanni candidate you choose.
Restored Dima and clinic guard text and removed a model at junkyard.
Fixed several bad particle files for magic fires and other effects.
Made Leatherface and Drifter player histories more likely to frenzy.
Added radio transcripts, thanks ellipsis_jones and gothemasticator.
Restored two Ocean House ghosts and Hellcat plus forklift sequences.
Removed Fu Syndicate lobby keypad code to avoid breaking the level.
Included official patch 1.2 files because official VTMB site closed.

v5.9                                                     18.12.2008
----
+Made player heal before Blood Hunt and repaired bad CD quest update.
+Added Heather remembrance lines and fixed Gary's poster quest bugs.
+Made Isaac recognize the Tzimisce defeat for non-Toreador clans too.
+Added ring and watch to pawnshop and fixed two Copper log problems.
+Made damage by fire more consistent for Andrei and Sheriff warforms.
+Fixed quest log updates for Ash, Romero and Heather on their death.
+Made Chastity not biteable and fixed Sin Bin handle and area change.
Corrected Milligan not leaving cutscene and improved anti-cheating.
Fixed beastform model and added slash sound to Heather's last scene.
Corrected Gimble and Nines Obfuscate issues and minor text details.
Fixed minor dialogue problems of Heather, Knox, Skelter and Beckett.
Added subtitles for cutscenes and conversations, thanks to Voerman.
Restored some Ocean House and beachhouse lines and Chunk-Asylum fix.
Corrected basic healing rate and added one sound to Muddy cutscene.
Removed XP for Romero loving after zombie quest but made him return.
Fixed Vandal endgame freeze and wrong door sound at the Ramen shop.
Fitted Cathayan report dates to morgue PC dates and fixed bum quest.
Swapped Igor's .38 with GLOCK 19 and gave more hit points to Larry.
Replaced money in Kamikaze Zen safe by name plate to fix XP problem.
Exchanged Brawl and Finance book locations inside the Empire hotel.
Swapped dancers between clubs to avoid too many similar ones nearby.
Gave GLOCKs to hunters in Ash sewers to fit gun shown on the model.
Restored the uncensored US decapitation cutscene, thanks to Keleigh.

v5.8                                                     11.11.2008
----
+Added two new poster quests for card, plate, star and grenade props.
+Made Ventrue start off with Charisma +1 instead of Camarilla bonus.
+Re-named .38 "Colt Police Positive Special" and fixed Regent reward.
+Sending Copper after the president triggers a Masquerade violation.
Made Isaac recognize the Tzimisce defeat even if you pissed him off.
Restored basic Blood Buff and Heather plus horror tapes label name.
Corrected Obfuscate issues with serial killer, Hengeyokai and Boris.
Put purse in diner if Doris is dead and fixed Gallery cops leaving.
Restored multiple endgame stock-ups by closing Skyeline haven vents.
Replaced unknowable names for Danielle, Spicoli and Sin Bin dancer.
Fixed log updates regarding Therese spirit and Regent plague quests.
Added cop cars to beachhouse map and fixed other minor map details.
Corrected dialogues of Mercurio, E, Trip and Isaac Gargoyle problem.
Added one XP for stealing the Kamikaze Zen money and adjusted logs.
Lowered award for killing a demon in his human form to two XPs only.
Adjusted fonts issues regarding Dementation and Tremere Domination.
Removed the Lotus patron after you placed the talisman successfully.
Edited history and occult item descriptions to display percentages.
Included > 2 GB patched shaderapidx9.dll, thanks to Jor and Wabbite.
Improved several book drop sounds and bush hook stealth kill sound.
Added purse to Lily's items and lights to Venture Tower police cars.
Fixed minor dialogue problems with Trip, Flynn, Heather and Copper.
Re-fixed tutorial .38 exploit and added ModDevGuide, thanks to Dheu.
Turned Chantry haven into Masquerade area to fix Tremere detriment.

v5.7                                                     01.10.2008
----
+Restored Skelter and his dialogue to Luckee Star during the endgame.
+Adjusted maximal ammo to match clip size and raised rifle accuracy.
+Made Toreador start with Appearance +1 and increased falling damage.
+Restored crossbow bolts and rifle bullets buyable from all vendors.
Moved Fat Larry into Confession alley and restored Fae Charm reward.
Changed severed arm pickup sound and added two missing mode sounds.
Fixed taxi driver, E, Razor, Yukie, Mercurio, Nadia and Jack issues.
Made Larry send spam email to show that vendors update their stock.
Swapped several Ventrues with helipad SWATs and fixed their texture.
Removed second tutorial enemy for Presence because of common popup.
Prevented talking with Chunk when someone else attacked the Gallery.
Corrected sliding doors, some handles and an icon at Venture Tower.
Fixed logs for Copper, Heather, werewolf blood and Metalhead quests.
Corrected wrong icons at the Ocean House and Jezebel Locke's trunk.
Made Astrolite undroppable again and added a Regent Blood Hunt line.
Unified burning barrel and fire explosion damage on several levels.
Turned the Firemage and Ventrues into females for male clan members.
Fixed issues for bums, Pisha, Copper, Empire clerk and Bishop Vick.
Added missing cabbie aura to three maps and fixed minor text issues.
Corrected temple maps start orientation, inspections and a tin can.
Improved corpse variety in warrens lair and a Blood Hunt enemy pair.

v5.6                                                     03.09.2008
----
+Made Jack remove .38 to fix exploit and repaired broken Isaac logs.
+Decreased crossbows criminal level and fixed Sin Bin state reload.
+Fixed broken Empire hotel card printer usage and made it plus only.
+Restored first dot Domination options for Tremere during dialogue.
+Added overlooked Humanity losses and restored sheet music of basic.
+Disabled "TrueSight" of killer, Vick, Cathayan and Blood Guardian.
+Made Romero train up to Firearms 4 and Beckett up to Scholarship 4.
+Increased XP gain on freeing Ash and delivering Imalia's magazine.
Added a few Shin Guntos to sewer hunters and improved end fade out.
Adjusted double Ithaca reload sound and added several drop sounds.
Repaired Barabus quest re-update and a wrong Zhao died quest state.
Corrected faulty Isaac lip-sync issue and some minor text details.
Added sound to Kiki cutscene and fixed Hollywood bus stop map typo.
Removed a talk icon in diner and corrected lg Firearms book value.
Made player get a look at Gimble's hand and fixed some map details.
BSPEdit updated to edit several prop stats, thanks to RobinHood70.
Fixed dialogue issues for Ming, VV, Trip, Boris, Vandal and Damsel.
Made unfinished Regent's plague quest fail in case you betray him.
Fixed ghouling quest not updating and improved Bertram's quest log.
Added Vandal gesture for females and fade out at the tutorial end.
Resolved bug when entering the Fu Syndicate while being Obfuscated.
Prevented continuing E's quest after you failed it by killing him.
Fixed dialogue bugs of Skelter, Arthur, blueblood, clerk and Venus.
Added a missing light switch and missing door sound to King's Way.
Removed reference to Ricky at Glaze and made upstairs guards fight.
Repaired several cut off dialogue lines and a few lip-sync issues.
Moved Jack down to Skelter and improved Tin Can Bill's expressions.
Included 64 bit install and memory tool, thanks to Iain Patterson.
Removed buggy SM haven board and Mercurio's note after you met him.
Moved Ash song from Empire hotel to the unfinished museum diorama.
Added default 1.2 map entities and Python files, thanks to Offkorn.
Restored katanas to Tongs and removed the one at the Fu Syndicate.
Turned hospital into Elysium area during your encounter with Pisha.
Fixed dialogues for Jack, Mercurio, Regent, Razor and taxi driver.
Changed three history Humanity penalties to avoid Humanity of zero.
Lowered surf computer difficulty and added a Gargoyle quest state.
Made Tawni laptop reflect mission and fixed Zygaena and Yukie bugs.
Stopped Maria and Victor from dropping invitations they don't own.
Added inspection nodes to some trapdoors in the Giovanni crypt map.

v5.5                                                    31.07.2008
----
+Moved Pyro Crossbow from Society to Syndicate instead of bloodpack.
+Changed new stealth rules so that only highest sneaking is harder.
Made Ocean House quest failure update when reconciling the sisters.
Fixed details with Isaac, Boris, Jack, Heather, Mercurio and Phil.
Implemented ZVTool and added readme to Extras, thanks to ZylonBane.
Lessened vents fade outs at Skyeline Apartments and fixed a decal.
Added second T-Rex sound to museum and corrected some text details.
Restored XPs at Glaze for peaceful approach and fixed the monitor.
Fixed morphine quest after warehouse and .38 ammo tutorial exploit.
Added blood loss when ghouling Heather and having fun with others.
Made Sin Bin ATM indestructible to avoid breaking connected script.
Improved card printer usage and added a few more inspection nodes.
Restored original descriptions for crossbow bolts and rifle rounds.
Added several missing doors and adjusted SM endgame bus stop maps.
Moved restored female raver to the Asylum and fixed teeth textures.
Hid Giovanni crypt trapdoor icons and fixed Nadia and zombie bugs.
Removed second Domination tutorial enemy and Johansen basic issues.

v5.4                                                    12.06.2008
----
+Repaired braid Perception powerup and Yukie and VV dialogue issues.
+Restored third person melee and moved first person view to Extras.
Corrected minor dialogue and map details and two item descriptions.
Swapped tape messages at Grout's Mansion and fixed clipping ghoul.
Restored Toreador Humanity XP bonus and burning Tzimisce creations.
Added many expressions towards Nosferatu and adjusted some others.
Fixed missing Patty quest update and a possible Boris and Dima bug.
Repaired warehouse bum leaving and Romero fun sound playing again.
Fixed Dane crane switch directions and removed Venture window taxi.
Removed Misti freebie for Nosferatu and added a sweeper reference.
Changed sound for dead body container and some npctemplate genders.
Added short-time bar replacement for Venus in case you killed her.
Made Glaze monitor turn off earlier and fixed Zhao death reference.
Moved Kamikaze Zen vent exit into a back alley to make more sense.
Corrected wrong observatory manhole sound and many bad drop sounds.
Placed females at the Blood Hunt and restored Heather clothes fix.
Corrected a TBO sign typo and male Tremere model, thanks to MooCHa.
Fixed Prodigy history not being available and Dane computer issue.
Corrected contradiction of Wong Ho newscaster and newspaper report.
Fixed Pestilence for bosses and visible taxi TV icon and triggers.
Restored netcafe headrunner sequence and a Giovanni guard sentence.
Corrected Skelter/Patty issues and removed wrong gestures of Jack.
Restored unused Daniel Ash - Come Alive song into the Empire hotel.
Added TV sound to Nosferatu haven and made sweeper defend himself.

v5.3                                                    15.05.2008
----
+Tweaked new stealth rules and made rating visible at Tawni's place.
+Added first person melee without weapon models, thanks to Offkorn.
+Restored plus conditions for hg Firearms, Computer and Dodge books.
+Made braid raise Perception and improved Fu Syndicate test timing.
Fixed blood return and purge and added XP for hacking freezer code.
Removed warehouse bum before cutscene and made tubes not sellable.
Added some idle expressions to Gimble and Jack during the tutorial.
Fixed minor dialogue bugs, a Dane computer issue and version info.
Restored Jeanette scene for females and Larry's quest for everyone.
Prevented surplus CD quest email and corrected Maria dress detail.
Fixed Beckett's Scholarship bonus and Pearl item, thanks to MooCHa.
Removed Tzimisce creation burning death and an Empire door handle.
Fixed occasion of Yukie not getting her sword and minor map issues.
Corrected looping conversation and look-through duct at warehouse.
Restored beachhouse inspections and changed Eldritch Prodigy bonus.
Corrected wrong newspaper icons and restored valve and oven icons.
Replaced sky at the Ocean House hotel to get rid of oversized moon.

v5.2                                                    23.04.2008
----
+Made occult braid raise Unarmed feat instead of computer knowledge.
+Restored several Persuasion, stat updates and research conditions.
+Made stealth harder and restored Melee and Defense powerup effects.
+Fixed Nadia Humanity loss and moved a recorder at Grout's Mansion.
+Corrected unofferable gum and renamed Asian vampire "The Cathayan".
Re-added lost guard model and fixed Russians discipline reactions.
Added about hundred expressions to thirty NPCs and a .38 for Flynn.
Placed cops at SM conversation and some missing lamps into museum.
Forced player in DMP cutscene and offered Vandal's quest later too.
Added Skelter quest state and fixed Isaac and Barabus log updates.
Improved Heather and Malcolm dialogues and cash description limits.
Fixed Imalia's quest second chance and repeating Romero fun sound.
Removed bad warrens re-entry sound and adjusted the clipboard date.
Auto-closed warehouse door and placed temple bar up on his guides.
Fixed overlooked Shin Gunto, Galdjum and flamethrower basic issues.
Added junkyard sound using a car and fixed downtown bus stop name.
Restored Gangrel frenzy damage and some first discipline durations.
Fixed minor dialogue bugs, some basic/plus mixups and a few props.
Replaced Misti clones at Vesuvius and added a few inspection nodes.
Adjusted hospital scream and several wrong door and weapon sounds.
Unlocked one temple door for Yukie and secured two others later on.
Locked Red Spot back door and restored missing gesture for Damsel.
Removed Humanity loss for killing any kind of hunters on main hubs.

v5.1                                                    08.04.2008
----
+Made Tseng sell Shin Guntos and normal crossbows instead of Slater.
+Made only Mercurio sell SWAT rifle rounds and Pyro Crossbow bolts.
+Removed Intimidation powerup of grenade prop and added it to basic.
+Renamed SWAT rifle "Remington M24 SWS" and made cameras stackable.
+Made Yukie invincible at endgame and streamlined Gary's phone call.
+Improved Santa Monica rain speed and visuals, thanks to ZylonBane.
Fixed new item models and female Tremere glasses, thanks to MooCHa.
Restored five vendor and three context icons and Giovanni's cabbie.
Fixed second Sabbat at the warehouse and MP readme info and clans.
Restored a Gargoyle gesture and removed a few of Regent and Prince.
Armed sewer hunters showing a sword on the model with Shin Guntos.
Added special Jeanette email and repaired super-sensible Fu guards.
Removed Romero returning from basic but added him to pimpin quest.
Placed female bums into SM and adjusted cash inventory description.
Restored Protean 4/5 damage and some enemy discipline resistances.
Added Firemage cast animation and improved name of Dominated guard.
Moved female disease bum near to Last Round to make her lines fit.
Fixed many enemies not damaging each other even being Blood Boiled.
Delayed Boris' Dementation reaction and made Dima leave when sent.
Turned all armor and Ocean House pendant not stashable or loosable.
Locked buggy temple door for good and fixed more props and sounds.
Repaired Tseng shelves problem and added a missing Shu quest state.
Corrected Vandal, Isaac, Misti, Victor and Luca dialogue problems.
Added sound for Giovanni sliding doors and two missing email lines.
Fixed Lu, Heather, Gargoyle, Regent, Trip and Ash dialogue issues.
Renamed Cathayan "Fernando Cougat" and fixed Heather's morgue date.
Corrected bad Jeanette quest update and made Cal getting re-hired.
Fixed several left over basic/plus stat details, thanks to Offkorn.
Added warehouse start astrolite check and fixed minor text issues.
Removed unfitting sounds at Lotus Blossom and some dialogue pauses.
Fixed asking Malcolm about saved Heather and Knox's quest looping.
Re-fixed Thaumaturgy with non-humans and fixed Newscaster position.
Fixed double doors at Giovanni Mansion and removed Bruno's clones.
Added a Vandal line for females and fixed two Venture double doors.
Made Chang's threat stay in dialogue and fixed Lily's diary dates.
Restored hotel guard and warehouse Markus models, thanks to gardeb.
Added fade and sound when loving Romero and sound to pimpin quest.

v5.0                                                    17.03.2008
----
+Made more basic/plus changes using variable and fixed text details.
+Moved Tawni poster to Tremere bathroom and restored a Regent line.
+Made Bach and Cathayan drop both weapons and removed a basic issue.
+Granted XP for Copper and poster quests and adjusted poster order.
+Restored Vandal's alternative for Nosferatu and warehouse bonus XP.
Removed inappropriate Buddha moving sound and included Python code.
Added museum and Bertram log states and Blood Buff to Elysium tip.
Made Hatter drop screenplay on death and corrected Blood Boil info.
Added breaking sound to warrens vent and Ocean House floor boards.
Stopped Skelter from blocking you and adjusted Hannah's book dates.
Fixed basic Ra blade description and it's invisible stats in plus.
Made sarcophagus key not giveable and fixed a basic Imalia exploit.
Improved Tommy's quest log and fixed Regent and Trip endgame bugs.
Made netcafe entry for Ash Rivers update and delayed Tawni's state.

v4.9                                                    06.03.2008
----
+Made crossbow bolts available earlier and Tseng hide his inventory.
+Hid an elder vitae pack in Fu Syndicate and repaired grenade icon.
+Added Humanity to overlooked dialogue for giving money to Mercurio.
Fixed basic patch loading tips not changing and minor text issues.
Decreased patch size by setting basic/plus changes with a variable.
Swapped Damsel and Skelter places to correct a line of the latter.
Removed blind door handles at the Ocean House and the Empire hotel.
Changed installer default directory to fit original retail folder.
Added pain sounds to Mercurio cutscene and reliefs to Fu Syndicate.
Fixed bad Nadia dialogue section and restored more missing sounds.
Placed howitzer gun at Leopold Society and removed a Mercurio loop.
Re-fixed Carson taking his laptop and resolved a Sin Bin PC issue.
Added Heather's missing line after Dominating or Dementating McFly.
Prevented continuing Mitnick's quest after failing a previous hub.
Improved an Ocean House ghost laughter and added vent break sounds.
Moved serial killer card back and corrected several toppled props.

v4.8                                                    22.02.2008
----
+Recovered grenade as Intimidation powerup and fixed netcafe laptop.
+Created new Gary quest to swap pull toy prop with poster of Tawni.
+Added Humanity points for granting money to haven bum and Mercurio.
+Made killing pier cops loose Humanity and gave one the baton only.
+Changed Pearl of Dubai powerup to Charisma so Nosferatu can use it.
+Swapped Gary's quest order and his CD for a box with vacuum tubes.
+Added overlooked Humanity loss after killing Phil at the SM clinic.
+Exchanged knowledge requirements of high Computer and Dodge books.
Made Isaac give his gift sooner and SWAT cops use Steyr AUGs only.
Fixed side quest breaking bug at Empire hotel after speaking Boris.
Made Carson pack his laptop and fixed bad loading tip word choice.
Fixed Imalia still being pissed off after selling her the magazine.
Restored sound to Bach's grenades and fixed minor dialogue issues.
Delayed reaction to changes of Heather's state in medical computer.
Updated netcafe entry for Tawni Sessions dependent of quest state.
Placed serial killer card more reasonable and restored more sounds.
Prevented continuing the Tawni quest after you have been detected.
Added gestures to a Jack tutorial line and fixed stealth kill icon.
Fixed Ming dropping out of dialogue and a possible Gary phone bug.
Corrected bad Ming-Xiao, Tzimisce fatguy and Ra blade damage stats.

v4.7                                                    14.02.2008
----
+Created seperate quest for freeing Ash from the Society of Leopold.
+Added seperate quest and an XP for saving Heather by ghouling her.
+Created seperate quest for Gary's posters and lowered some of them.
+Added seperate quest for exploiting thin-blood Copper by the pier.
+Fixed bug that prevented the CD quest to initialize in a rare case.
Made inventory icon and damage stats visible for the Protean claws.
Added patch version information to base character creation window.
Forced talking to Boris sequence even if you removed Dima silently.
Prevented Gary's posters from appearing in your initial haven too.
Restored cash box item into Gallery Noir and added inspection node.
Removed Heather reference on Malcolm's computer after she is gone.
Repaired bugs regarding quest updates when talking to the Mandarin.
Turned power on and timer off on re-visiting the Kamikaze Zen map.
Seperated Malcolm's overlapping certificates and fixed more sounds.
Removed Kuei-jin's burning death and invisible block at warehouse.
Locked a double door in Ming's temple that would open accidentally.
Added quest logs for Isaac's gift and replaced Dane report object.
Fixed a Vandal endgame condition and removed more Nadia not-voices.

v4.6                                                    04.02.2008
----
+Added male Seduction feeding to the SM blueblood and Tommy Flayton.
+Created option to keep Heather alive but missing the armor though.
+Fixed Danielle's lines, Gary's poster order and Bertram's CD quest.
+Adjusted NPC reload times for both crossbows and added missing XP.
Included fixed engine.dll and improved installer, thanks to MooCHa.
Added log for sending Patty to alley and fixed two connected bugs.
Synced scream in hospital and rotated bus stop texture in downtown.
Changed damage of Ming's spit to bash and fixed minor text issues.
Prevented Tremere from being able to loose their haven for treason.
Fixed re-persuading or killing Tommy Flayton after quest was over.
Made Romero give you ammo with his rifle instead of magic box fill.
Restored overlooked Dodge powerup into Ocean House in basic patch.
Corrected Heather not giving silver ring when you already have one.
Restored missing XP for second Pisha item and removed Nadia sound.
Fixed killing the Gargoyle after persuading him and a dialogue bug.
Hid invisible block at the theatre and corrected a few more props.
Removed dialogue loop for McFly and restored another missing sound.
Made Empire door locks consistent and added sound to Sin Bin kick.

v4.5                                                    10.01.2008
----
+Swapped two Gary's quest emails and restored a silent Bertram line.
+Repaired Blood Buff not adding up and blocked Ash sewers map hole.
Restored three cage dancers and Venus' laptop into club Confession.
Added Lotus key board inspection and fixed trailer key inspection.
Lowered Dane computer difficulty and fixed more sounds and objects.
Restored Giovanni cutscene sound and created an installer version.
Improved first Heather scene and updated MP clans and descriptions.
Added sounds to Muddy, Ash, Pisha, ghouling and jumping cutscenes.
Merged light-gone-after-loading fix with MemFix, thanks to Wabbite.
Made Vandal acknowledge payment and fixed swapped nosave messages.
Fixed Mitnick appearing after quest and more invisible Python bugs.
Made new Danielle lines rotate and more speeches stay in dialogue.
Removed morphine from CS and register sounds playing without Doris.
Fixed missing detail on Chinatown sewer map and minor text issues.
Harmonized Presence chances and loosened tutorial anti-cheat check.
Lowered money from Julius to $100 and made leaving Pisha clean up.
Fixed the known inventory-and-container-bug, thanks to RobinHood70.
Repaired text of Isaac, Trip, Gargoyle, Cal, Mercurio and Therese.

v4.4                                                    06.12.2007
----
+Made it possible to specify which clothes Heather should wear next.
+Deleted crossbow from Sin Bin and fixed Yukie double swords issue.
+Removed Humanity for Dementating McFly and tutorial .38 on default.
Restored SM haven for traitorous Tremere and fixed sewer shortcut.
Included memory and widescreen resolution tools, thanks to Wabbite.
Many Malkavian lines added for blood dools, thanks to RobinHood70.
Made basic patch install as default and removed overlooked changes.
Swapped Lily cutscene Phil with scrubs and adjusted Vandal's line.
Re-did Ginger Swan knowledge fix and warehouse re-entering stopper.
Corrected boss flags for Mercurio, Chastity and Tzimisce creation.
Fixed Venus' reaction for persuading Boris and Asylum email issues.
Restored newscaster and Cal lines and fixed minor dialogue errors.
Repaired Imalia's quest failure message and new Vandal alternative.
Fixed possible random crashes on exiting Grout's Mansion and Dane.
Corrected hostess not getting elevator and phoning without a phone.
Added inspection to text at Society and a few more missing sounds.

v4.3                                                    05.11.2007
----
+Fixed Blood Buff effects for Tremere and restored crossbow damages.
+Increased Romero training condition and added Intimidation for Ji.
+Added Nosferatu options for Vandal's quest and a gascan inspection.
Fixed Venus' cut rate and Vandal's freebie, thanks to RobinHood70.
Unhid meeting sequence in Chinatown and fixed prostitutes hair bug.
Restored over 60 unused lines, thanks for the list to RobinHood70.
Prevented dead Chunk from dancing and fixed Lotus tub guy reaction.
Restored over 30 missing sounds and removed crackhouse respawning.
Made prostitute leave you when attacked and removed some more keys.
Added list to readme presenting changes sorted  by theme and area.
Allowed some more feeding from Heather and improved her last scene.
Improved Bach and Johnny cutscenes and Chang disciplines immunity.
Made Pisha's quests fail on fight and fixed Gallery bar inspection.
Repaired bum, Mercurio, Tseng, Yukie and Danielle dialogue issues.
Fixed new line on phone not working and minor log and text details.
Unstuck Ricky and swapped a few prostitutes to seperate like ones.
Repaired Cal not letting you up and dead Mercurio sending an email.
Corrected Flynn giving guymag for free and a Nadia dialogue error.
Fixed laser beams again and removed Patty's corpse from Confession.
Repaired Jeanette scene blood condition and Giovanni backtracking.
All dialogue and Python scripts streamlined, thanks to RobinHood70.
Corrected sewers level load orientation and two comfort reactions.

v4.2                                                    19.09.2007
----
+Added inaccessible Blood Heal and Blood Buff infos to loading tips.
Reconstructed Bertram's PC and incooperated text of unused emails.
Made Tawni quest show failure at once and added Tourette condition.
Translated Russian text and fixed Boris' and Chunk's fight scenes.
Restored over 20 never heard NPC lines, thanks for the list to mzz.
Updated BSPEdit tool and fixed laser beams, thanks to RobinHood70.
Made Milligan leave after Intimidation and Pisha react accordingly.
Adjusted Mitnick's position, some subtitles and more text details.
Fixed clipping and blocking Venture Tower debris, thanks to MooCHa.
Removed last respawning at Giovanni Mansion and alert state error.
Corrected clerk adressing women "Sir" and some badly placed decals.
Repaired possible syntax issues for many dialogues, thanks to mzz.
Fixed some dialogue problems of Knox, Skelter, LaCroix and Heather.
Made SM blueblood stay dead and cop cars on pier vanish correctly.

v4.1                                                    28.08.2007
----
+Prevented Humanity from reaching zero and removed loss for pendant.
+Removed gum when sold to Copper and fixed parking garage exchange.
Put morphine into cs cabinet and fixed a Danielle Persuasion error.
Added a humane farewell line to Heather and fixed a Tourette loop.
Lowered hacking skill of Asylum computers and swapped Copper lines.
Made police investigate Gallery crime independent of your actions.
Corrected a Vandal condition and several similar dialogue problems.
Repaired broken Romero quest return and several minor text issues.

v4.0                                                    17.08.2007
----
+Created Appearance powerup from Pearl of Dubai as reward for Isaac.
+Made Strauss reward you with the Fae Charm instead of usual money.
+Recovered chewing gum to sell to Copper and stashed it on the pier.
+Re-changed Eliza and Thistle effects as they didn't work randomly.
+Made armor absorb half the aggravated damage and raised Blood Heal.
+Removed Humanity for killing Milligan directly and fixed card bug.
+Restored warrens door difficulty and fixed switches at observatory.
Restored rat crowd to warrens and ancient text to Leopold Society.
Placed library keycard at Ramen and fixed some minor text problems.
Moved dogs into junkyard and Skelter to Nines' side at one ending.
Swapped cop Anacondas with Ithacas and made Pisha leave eventually.
Restored Romero to be back after his quest and fixed zombie scene.
Fixed cut off conversations and restored a hidden one to warehouse.
Restored hidden models to Dane, to Blood Hunt and on junkyard map.
Placed Russians more inconspicuous and removed the two added locks.
Removed cop cars from the Santa Monica pier after the police left.
Added Fu Syndicate emergency doorcode and restored tire iron skill.
Recovered three unseen newspapers and repaired a newspaper mix up.
Renamed "Replica Katana" "Shin Gunto" and restored two item models.
Made Mercurio's email arrive later and fixed several email issues.
Repaired warrens electrical terminal computer and fixed many props.
Added some missing inspection nodes and made diner cook move more.
Changed Giovanni vampire guard stats and restored Dane crane icons.
Fixed Tong sounds at Zhao's and Hannah, Milligan and Pisha issues.
Repaired Trip and Vandal not choosable at endgame in special cases.
Fixed several name issues and explained others using loading tips.
Added missing doors to Venture Tower rooftop and Blood Hunt levels.
Turned your Santa Monica haven into Elysium area when Jack visits.
Improved Barabus' hack position and made PCs accessable afterwards.
Corrected Chunk's brother's subtitles and changed Chunk dance fix.
Reformatted Sin Bin inventory pages and fixed more minor PC issues.
Put Heather's name in the morgue file in case you left her to die.

v3.9                                                    16.07.2007
----
+Restored Eliza and Thistle powerups to their original descriptions.
+Added Luca Domination and removed Wong Ho and Ming dialogue loops.
Fixed some overlooked basic patch details like Galdjum at Tseng's.
Added icon to Giovanni lever and lowered Leopold barrel inspection.
Locked Johansen in and fixed a possible bug in the Giovanni crypt.
Made Venture debris stay longer and be visible through the windows.
Allowed only one visit to each supply destination at taxi endgame.
Made female Sabbat Lasombra only and swapped some Hallowbrook guns.
Corrected Al's mumbling at the beachhouse and apologizing to Knox.
Fixed Steyr AUG damage and hid unimplemented dialogue history keys.
Prevented entering burning warehouse and fixed a Domination issue.
Fixed doors at Venture Tower and temple and a bad lip-sync of Phil.

v3.8                                                    03.07.2007
----
+Lowered difficulty of one critical door to fit with new Blood Buff.
+Corrected Blood Heal and Buff tutorial popups at high resolutions.
+Made Mercurio sell Steyr AUGs earlier and sorted Larry's inventory.
+Increased Blood Heal healing rate and improved activation details.
+Added Domination options for Danielle and Romero quest prostitutes.
Added Humanity gain for saving Johansen instead of missing torture.
Modified placeholder names and descriptions of four upgrade books.
Made NPCs act comforting to more disciplines and added male sounds.
Altered duplicate Lu Fang conditions and re-added Nadia sentences.
Made Vandal more talkative and Milligan react right when Dominated.
Repaired completing Larry's quest being impossible in basic patch.
Added and corrected inspection nodes for containers at Ocean House.
Fixed GLOCK running animation and corrected SWAT crosshair errors.
Swapped teleporting female Lasombra and fixed a Nines dialogue bug.
Restored cabbie and E lines and fixed some of Bertram and Strauss.
Fixed Potence, Ravens, Trance, Wipe and Hysteria issues and sounds.

v3.7                                                    12.06.2007
----
+Added Blood Heal discipline and slowed automatic heal rate by half.
+Changed Cadaverous Flesh history and occult heal rate accordingly.
+Lessened criminal levels of both crossbows and raised their damage.
+Lowered Blood Buff effect to two points and corrected info symbol.
+Modified Eliza to raise Brawl and lowered high Firearms book grade.
Restored Leopold Society clans and clan equipments for multiplayer.
Swapped low Dodge book and Dodge item places at hotel and Mansion.
Made indirect disciplines not traceable and decreased maximal ammo.
Removed Humanity gains from Milligan and fixed Wong Ho background.
Fixed several crosshair issues and wrong icons near the Dane crane.
Corrected several tutorial popups and mentioned camera adjustment.
Repaired critical basic patch bugs and restored overlooked changes.
Fixed clinic guard Humanity loss and some other minor text issues.
Removed Masquerade redemption and double XP for sending Patty away.
Made Potence stack with strength and fixed the npctemplate* files.
Corrected Arthur's $201 reward, Vandal, Ji and Slater lines issues.
Removed player knowing the names of Ox's patron and Asian vampire.
Prevented picking of two temple doors and repaired Hollywood music.

v3.6                                                    23.05.2007
----
+Changed warehouse bonus XP to stealth and corrected magazine sizes.
+Made Trip sell bat and tire iron from start and added basic patch.
+Made getting secret informations from Knox and Johansen consistent.
+Swapped Galdjum and Lockpicking powerups between Mr. Ox and haven.
+Delayed body armor until Blood Hunt and repaired npctemplate* bugs.
+Removed additional XP for killing Bruno and skipping the tutorial.
+Moved flamethrower to Bach's hideout and Ra blade to Andrei's lair.
+Raised condition for Jeanette encounter and removed connected bug.
Included config and infos for multiplayer support, thanks to Exulx.
Made serial killer react to violence and Bertram react to attacks.
Fixed player shown alive at wrong endings and restored warform hop.
Repaired Boris, Kerri, Mercurio, Heather and newscaster dialogues.
Fixed lockpicking and pickup sounds and some NPCs not staying dead.
Adjusted Heather's last clothes, more props and minor text issues.
Repaired Blood Strike, Salvo and Purge working sometimes not right.
Fixed two wrong auras in Santa Monica clinic and endgame taxi bug.
Restored Desert Eagle ammo model and fixed other inventory details.
Swapped several female hunters that were talking with male voices.
Fixed Domination, replica katana and Empire hotel lockpicking bugs.
Corrected conditions for Vandal, Trip and Mercurio during endgame.
Replaced broken female fire axe texture, thanks to Offkorn and Doe.
Restored lines of Andrei, Gary, Trip, Mercurio and of two endings.

v3.5                                                    15.03.2007
----
+Placed Yukie into endgame temple like planned and fixed more props.
+Unified irregular maximal ammo values and changed some ammo worth.
+Inverted Milligan Humanity loss and clarified a tutorial quest log.
+Lowered flamethrower lethality and Eldritch Prodigy damage effect.
Swapped Boris' Colt with a GLOCK and updated CIS computer details.
Added female Desert Eagle and gave it to hunters, thanks to MooCHa.
Restored about ten unused lines from Jack, Knox, Trip and LaCroix.
Fixed missing stealth kill sounds for replica katana and bush hook.
Restored Protean claw effects and solved some smaller text issues.
Added missing lamps to the Ocean House trailer and locked the door.
Stopped Doris from falling in floor and the need to reset options.
Fixed wrong auras of Ash, Barabus and Julius and raised dog health.


v3.4                                                    23.02.2007
----
+Added civilian Humanity loss to Giovanni, pier and Blood Hunt maps.
+Hid the Ocean House killer axe and increased chance to notice him.
+Gave .38 and an XP on tutorial completion but no items on skipping.
+Moved Ra blade to Fu Syndicate and restored Yukie's visible sword.
+Made Mercurio sell the body armor but only after Hallowbrook hotel.
Restored female rat drain, male Hysteria, Mira and Heather sounds.
Made more Chinatown enemies wield new blade and lowered it's worth.
Placed Gary in council cutscene and synced courtroom sword sounds.
Added unused quest logs and missing muzzle flashes to the tutorial.
Made Giovanni snort girl mortal and fixed XP on Dementating Chunk.
Swapped a Tremere history and showed player alive at Anarch ending.
Corrected more misplaced props and flickering blood at DMP studio.
Repaired lip-sync of Romero plus line and Strauss giving no reward.
Restored missing flamethrower stats and voices at Grout's Mansion.
Adjusted GLOCK deploy sound and restored missing Desert Eagle ones.
Fixed Milligan Pisha bug, Lotus Blossom key board and Carson's PC.
Created a few missing Malkavian lines for Damsel, McFly and Imalia.
Fixed lines of Gary, Kanker, Venus, Jeanette and more text issues.
Restored invisible tabletops and many absent light and lift cables.
Renamed flaming to "Pyro Crossbow" and adjusted the warrens dates.
Added stealth bonus hints and cut Heather's hair, thanks to MooCHa.
Included Bloodlines editing tools and fixed a Pisha quest log bug.

v3.3                                                    11.01.2007
----
+Awarded XP after letting Julius go and restored Ming/Fu connection.
Removed flickering reservoir decals and fixed many floating props.
Replenished Misti's blood and repaired broken Tremere blood return.
Gave new blade to temple and Society enemies and fixed respawning.
Prevented Boris' door from closing and Dima from vanishing in view.
Fixed hospital screams and dialogue bugs of Arthur, Cal and Pisha.
Shortened Ventrue loading tip and some histories names to fit page.
Made ghouling Heather easier again and added camera moving to cfg.

v3.2                                                    30.11.2006
----
+Added Humanity loss when killing innocents in several combat areas.
+Corrected GLOCK name, modified clothes text and added cl_smooth 0.
Made sure the quick Nosferatu dies and rendered Empire TV inactive.
Put unused cat outside King's Way and fixed flickering Dane blood.
Modified bad discipline effects for non-humans, thanks to Populism.
Used hidden Ithaca sound, gave Colt to Boris and fixed more props.
Renamed Bloodsuckers' to Bats' Communion and updated female Sabbat.
Made Imalia and Mitnick turn better and Isaac give his gift later.
Improved first Heather dialogue and fixed Vandal and Bertram lines.
Changed Yukie log, two PC prompts and wrong level re-enter sounds.
Fixed hunters spawning on main hubs and another Imalia's quest bug.
Repaired possible freeze on freeing Lily and left over respawning.

v3.1                                                    20.10.2006
----
+Lowered Venus' cut to $125 and turned the character page music off.
Corrected dialogues issues with Christopher, Milligan and Jezebel.
Unbarred Ming's temple door and hopefully fixed Beckett's wait bug.
Made Copper leave for infusion and restored Pisha's meal cutscene.
Removed hunter when Ash is gone and erected more tipped over props.
Fixed Romero's trunk refill and reduced zombie spawning frequency.
Deleted extras at theatre and restored Larry's quest for Nosferatu.
Restored Jeanette/Therese struggling scene and some Heather lines.
Changed some weapon infos and fixed Giovanni Mansion diving boards.
Made speech stop when Bruno enters and fixed some Giovanni guards.

v3.0                                                    05.10.2006
----
+Granted Humanity for persuading Therese and Jeanette to make peace.
+Lowered baseball bat, tire iron and new katana skill requirements.
Darkened Beckett's glasses and fixed some others, thanks to MooCHa.
Added speech to Jack's cheat lines and lessened Ming's bar weight.
Erected several tipped over props and added a few inspection nodes.
Corrected a few bugs in dialogues of Milligan, Julius and LaCroix.
Moved the bum in the abandoned building and restored his fast exit.
Fixed entering the pawnshop crash caused by sound, thanks to Bogj.

v2.9                                                    13.09.2006
----
+Made Larry's quest independent of buying and fixed briefcase scene.
+Tseng will offer the SPAS directly and the flaming crossbow later.
Renamed new blade dropped by the Asian vampire to "Replica Katana".
Released trapped Fu Syndicate guard and added Julius killed lines.
Removed another warehouse spawning and restored beachhouse weapons.
Fixed superguards at Giovanni Mansion and the bonus sweeper lines.
Changed flaming crossbow text and added some more inspection nodes.
Corrected typos and lines for newscaster, Lily, Copper and Vandal.

v2.8                                                    22.08.2006
----
+Made enemies drop weapon when killed except Changs and in tutorial.
+Removed .38 got for skipping the tutorial and added the quest log.
+Removed Humanity for sending Copper and fixed a bad bloodpack line.
+Lowered .38 ammo price and time when crossbow bolts are available.
Swapped histories around again to alter those that made no changes.
Added missing inspection node to Bertram's CD and many more items.
Unlocked Boris' doors for Venus quest and corrected Dima condition.
Repaired possible crash on Gallery load and resetable quest state.
Moved misplaced Ra texture folder and corrected female wield model.
Restored exploding King's Way runner and altered book loading tip.
Fixed options when asking Trip for weapons and a Prince line error.
Removed respawning warehouse thugs and missing beachhouse weapons.
Made clinic guard not open doors twice and added a Nurse condition.
Fixed Eerie Presence bonus and reactivated the downtown sewer map.

v2.7                                                    08.08.2006
----
+Moved Computer and Firearms books from Trip to clinic and Carson's.
+Removed the zoom mode of the "Jamie Sue" and balanced with damage.
+Made Melee and Defense powerups increase the skill instead of feat.
Fixed Python script errors in Grout's Mansion and Vesuvius levels.
Repaired bug that could make Imalia angry before getting her quest.
Cops use GLOCKs and dead enemies will drop a little bit more ammo.
Fixed paying angered Vandal error and added a Gargoyle quest state.
Corrected several histories in which the Melee bonus did not work.
Restored Zygaena appearing in the Red Dragon after talking to Ming.
Fixed wrong conditions in dialogues of LaCroix, Beckett and Tseng.
Circumvented bug that made it possible for Boris to be unreachable.
Missing texture for the Ra blade reconstructed, thanks to Xealous.

v2.6                                                    27.07.2006
----
+Venus will now give you a constant $250 payment when you visit her.
+Made Tseng not offer blood as he doesn't even know about vampires.
Added missing XP for plague quest and fixed Hannah quest state bug.
Made Chunk not dance at Asylum anymore after you met him downtown.
Removed another double Malkavian line and clarified two quest logs.
Fixed a bug that reset Yukie's quest if you spoke with Ming again.

v2.5                                                    30.06.2006
----
+Made Mitnick mail his reward already after the first schrecknet hub.
+Raised chances for Jeanette and Therese peace and Jeanette winning.
+Lowered Persuasion requirements for all Giovannis to the same value.
+Hacking and Lockpicking powerup models centered, thanks to DDLullu.
Modified XP and log for one plague quest state, thanks to Acleacius.
Made Mercurio morphine quest update if you already had some on you.
Fixed XP gain for entering Gallery Noir by seducing Chunk once more.
Removed a surplus Malkavian line and altered some answers to Venus.
Restored missing Masquerade redemption for ways to get rid of Patty.
Fixed GLOCK walking animation and changed the Ra blade description.
Repaired VV and Jeanette sending you their emails at the wrong time.
Corrected a condition when telling Damsel about the Chang brothers.

v2.4                                                    13.06.2006
----
+Made condition to notice Johansen's secret similar to that for Knox.
+Granted Humanity on saving Wong Ho and adjusted warning conditions.
+Restored Jeanette encounter that somehow got lost in recent changes.
Fixed a stats condition issue that may result in several new lines.
Visible fangs added to all vampires missing them, thanks to DDLullu.
Gaining the Tremere haven is now independent from the quests order.
Raised Obfuscate frame rate using autoexec.cfg, thanks to Acleacius.
Changed conditions and text for entering Gallery with Chunk's help.
Corrected two lines to Isaac and Knox and changed a Muddy quest log.
Fixed speaking to LaCroix before going to the Society another time.
Removed double Masquerade redemption gained by taking care of Patty.
Added variable for Vick's death that may clear up connected quests.

v2.3                                                    23.05.2006
----
+Decreased kick of MAC-10 and Steyr AUG and restored Ra blade damage.
+Lowered Humanity points gainable during the serial killer dialogue.
+Made you loose a Humanity point when giving the pendant to Jeanette.
Removed illogical player@directory prompts from computer terminals.
Standardized key names in options, loading tips and tutorial popups.
Made charity money stay available after the paintings were slashed.
Altered an Imalia line and a quest state for "bonus" magazine quest.
Checking of texts and subtitles finished by RobinHood70 and myself.
Put ten "Jamie Sue" rounds in Romero's trunk for the cemetery quest.
Persuading Jeanette and Therese to make peace is like intended now.
Stopped VV sending her poster so you won't miss out on Gary's email.
Fixed a double answer to Gary and modified Victor/Maria Persuasion.
Altered some histories that made no change, no sense or added items.
Repaired Giovanni and Hitman quests not being recognized correctly.
Changed a Pisha line to reflect the possibility you killed Milligan.
Added the missing graph files for the modified Venture Tower level.
Stopped dead Malcolm sending mail and Adam repeating one line again.
Corrected a last name on the Santa Monica bus stop and sewer signs.
Fixed small bugs in Damsel, Knox, Beckett, Venus and Ming dialogues.
Restored lost lines of Flynn and moved some Malkavian lines around.
Removed bug allowing all clans to move using one downtown sewer map.
Correctly stated Brujah unarmed bonus and Nosferatu Seduction zero.
Made speaking to LaCroix before going to the Society possible again.
Shortened a Strauss line that incorrectly stated moving your stuff.

v2.2                                                    22.03.2006
----
+Made you lose a Humanity point when making Ash exchange his clothes.
+The special Jeanette encounter is now possible one additional time.
+Made you loose Humanity on taking money as reward of Imalia's quest.
+Added infos for flaming crossbow bolts and made vendors offer them.
+Awarded XP for killing Bruno Giovanni in the second Mansion map too.
+Renamed flaming crossbow "Kuei-jin" and lowered crossbows accuracy.
Removed Barabus line calling you a Cammy and fixed a line with Mira.
Fixed graphics of baton, VV photo, Megahurtz card and Gary's tapes.
Included the unused histories so that each clan has seven plus none.
Swapped trouble making history conditions with similar limitations.
Provided twenty places for Malkavian voice whispers during dialogue.
Restored welcome lines of Bertram including XP gain and log update.
Repaired story state continuity problem after talking to the Changs.
Made Bruno attack on lockpicking the Giovanni Mansion meeting-room.
Removed respawning at Lotus Blossom, temple, Venture and Giovanni's.
Moved Giovanni loading tips up and added lost lines of the sweeper.
Removed Gallery Noir key after use and made several items droppable.
Lowered additional damage done by all weapons using the zoom modus.
Restored XP gain for entering the Gallery Noir by befriending Chunk.
Checking of text and subtitles continued by RobinHood70 and myself.
Corrected one occasion where Mr. Ox would not give the right reward.
Fixed missing state and XP for bad luck talisman quest from Mr. Ox.
Changed text of Isaac, Beckett, Romero, Knox and Bertram's postures.
Fixed Venus giving you a quest twice and a question about Jeanette.
Corrected Tawni quest failure warning to work with all quest states.
Fixed quest state reset on drop and re-pick up of the Salvage card.
Added Pisha line about quest item and checked state for another one.
Corrected a warrens sign and added lines for Malkavians and Kanker.
Removed an endsequences taxi bug and added some missing level names.
Made Strauss offer you money or talisman and fixed a Chunk problem.
Mr. Ox will react correctly when you already have acquired the eyes.
Repaired not working Muddy quest fix and changed plague quest logs.
Restored Yukie to shop from the start and checked line about temple.
Prevented activating hubs a second time and revisiting Ocean House.
Made Tseng talk only of known people and Johansen scream more often.
Deleted invisible blocks at the warehouse to provide stealthy exit.
Fixed wrong conditions of Gimble, Jack, Strauss, Bertram and Slater.
Wong Ho and hostess will be gone from the Red Dragon for all clans.
Removed bonus for stealth killing Johnny and made guards more aware.
Changed Grout quest log, sewer key description and a Mitnick email.
Modified Milligan's Intimidate dialogue so that it makes more sense.
Many Malkavian responses and Dementation uses fixed by RobinHood70.
Fixed Protean tutorial text, body armor description and a quest log.

v2.1                                                    10.02.2006
----
+Swapped the damage of Desert Eagle/Colt Anaconda and SPAS-15/Ithaca.
+Made Galdjum and Heart of Eliza occult items be rewarded by Mr. Ox.
+Letting Julius go free for money end will up with Humanity balanced.
+Lessened damage for frenzy check and corrected shown armor ratings.
+Created new braid icons and placed unused chewing gum in Ramen shop.
+Made vendors sell SWAT rifle bullets and lowered price of fire axe.
Modified discipline options for Kerri and removed one line for Knox.
Made everybody lose a Humanity point for sending Milligan to Pisha.
Deleted unfinished threat to LaCroix and fixed some bad XP messages.
Moved one Tawni quest camera into the kitchen to fit Imalia's text.
Added line so you can give the CD to Bertram if you already have it.
Made CDC guys leave later and Chunk not send you up again at times.
Corrected typos, mapname LA to downtown and subtitles to fit speech.
Removed npctemplate* files, delete those if found in /vdata/system.
Renamed Sabbat Thug speaker name to Thug and a few Trips to Vandals.
Redid lost changes to Wong Ho dialogue about the silver haired man.
Made Giovanni guard at the rear entrance of the Mansion speak again.
After giving Ash the bloodpack it will be gone from your inventory.
Fixed Damsel recognizing Malkavians and Romero offering them pimpin.
Repaired more problems in Hitman quest and added a new quest state.
Added plague bearer quest log hint and allowed sewer-warrens detour.
The morgue computer will now mention Crumb only after he is around.
Restored sounds for the Ra blade and made killing Lu lower Humanity.
Fixed dialogues asking Flynn about Castity and Wong Ho about glaze.
Made Dane cop acknowledge quest and repaired sending Patty to Pisha.
Added a line for Skelter and deleted a tutorial answer for Ventrue.
Replaced a few bad icons in Venture Tower and lower Giovanni levels.
Fixed Strauss dialogue about Gargoyle weakness and one quest state.
Plugged Ash introduction hole and Therese knowing ghost item riddle.
Restored a broken Vandal line and conditioned a response for Nines.
Fixed telling Damsel of the alliance and corrected feed loading tip.
Deleted icons of unopenable doors at Lotus Blossom and Luckee Star.
Fixed Mitnick's reward and corrected text on three inventory models.
Added conditions to Beckett's Assyrian dialogue and removed a loop.
Changed Ji's superhero and Johnny's asshole lines to reflect gender.
Stopped taxi driving you to Mercurio during endgame when he's dead.
Stealing charity money will not cost Humanity if you know its usage.

v2.0                                                    13.01.2006
----
+Made crossbow bolts purchaseable sooner and added a doll easter egg.
+Lessened MAC-10 kickback on firing with increasing Firearms skills.
Removed an annoying side table in Gary's lair and hid two map holes.
Cut exclamation of Nadia that was audible when she was not present.
Provided baseball bat and tire iron to anyone skipping the tutorial.
Corrected Hitman quest rewards and added peace-talk lines for both.
All dialogues matched to speech and fixed thoroughly by RobinHood70.
Repaired a lot of lines that were not audible to female characters.
Removed Empire key after use and continued standardizing many names.
Made Prince react to Persuasion for money when sending you to Ming.
Restored additional lines of Jack, Imalia, Ming-Xiao and the cabbie.
Fixed money bugs with Bill, Hatter, Heather, Misti and prostitutes.
Moved dance spot at club Confession because of the cross-zoom error.
Removed an exploit with Copper and fixed Jeanette taking the knife.
Restored Ventrue specific Prince dialogue and some more unused text.
Corrected bug caused by 1.9 corruption that broke Chinatown quests.
Restored feeding on rats that would not work for some people in 1.9.
Changed wrong status display for the power of pump 118a in warrens.
Fixed problems with morphine quest and more after angering Mercurio.
Restored unused Nosferatu and Malkavian lines of Tseng and Wong Ho.
Fixed possibility of Beckett not talking on return from the Society.
Made Empire clerk bisexual responding to Seduction from either sex.

v1.9                                                    01.12.2005
----
+Put Obfuscate and Lockpicking powerups in sewer and downtown havens.
+Granted occult Hacking powerup as reward for doing Mitnick's quest.
Corrected Ra blade description from fast speed to aggravated damage.
Moved Pearl of Dubai and pull toy props to Arthur's bail bonds map.
Placed two of the unused female raver models at the club Confession.
Removed critical bum cutscene and illogical Pisha feeding cutscene.
Put unfinished dogs at Giovanni Mansion and fixed Mira dialogue bug.
Fixed a quest bug with the Fu Syndicate elevator and an Isaac text.
Made Grout's wife fully visible and repaired a Muddy quest shortcut.
Fixed a bug with Patty appearing in the alley although she is dead.
Swapped location labels of the missing sewer map with worldmap ones.
Made the Hallowbrook hotel's naming consistent throughout the game.
Resized unspectacular lower resolution fonts for better readability.
Made Hannah actually die at the time that she is supposed to do so.
Corrected the corrupted Intimidation font "W" at higher resolutions.

v1.8                                                    21.10.2005
----
Restored female Sabbat and put three into the first Hallowbrook map.
Added the missing Dodge II manual to second Giovanni Mansion level.
Placed the Pearl of Dubai and the occult braid into the SM pawnshop.
Restored guard models to Giovanni Mansion and fixed a lip-sync bug.
Put little used male Asian nurse model into the Santa Monica clinic.
Corrected formatting of a few haven PC emails and the Sin Bin note.
Continued adjusting location names by correcting bus and sewer maps.
Corrected a wrong dialogue option for female Malkavians with Nadia.
Made cemetery quest easier and fixed Romero raising female Firearms.
Removed unused subdirectories on two of the Kamikazi Zen computers.
Fixed several dialogue errors regarding Beckett, Flayton and Hatter.
Repaired dialogue getting cut of in the Fu Syndicate for Nosferatu.
Fixed Carson's apartment key not being removed after it's been used.

v1.7                                                    02.09.2005
----
+Lessened the sway of zoomed weapons and balanced with magnification.
+Granted an XP for keeping Zhao alive and changed quest accordingly.
+Awarded an XP for killing Bruno Giovanni and changed respective log.
+Made Yukie give you the Ra blade instead of getting it of Chastity.
Corrected bug that made it possible to get Ox's harvest quest twice.
Restored original funny answers when not being able to read a tome.
Repaired wrong subtitles speaker names with Vandal and other people.
Placed female hunters at the Leopold Society and removed the torch.
Fixed feat conditions for Muddy bum dialogue and a missing variable.
Restored original models for the low and high grade Computer tomes.
Fixed bug of Heather not appearing at the haven for female vampires.
Corrected bad names of the cafe and other locations plus map names.
Restored many mistyped Intimidate options and some answers to Pisha.

v1.6                                                    08.08.2005
----
+Re-branded Uzi, MAC-10, GLOCK 17c, Ithaca and both Remington rifles.
+Adjusted damage values of Steyr AUG, SWAT rifle and Ithaca shotgun.
Lowered lockpicking skill needed for chemical substances door to 10.
Made Model Citizen quest show failure directly after leaving Tawni.
All dialogues were spell checked for typos and more by Paul Moloney.
Several mistyped variables found could provide additional dialogue.
Corrected still not working Hitman quest fix and other related bugs.
Fixed variables in texts of Ash, Bertram, Boris, Venus and Mitnick.
Reconstructed lip-sync for the misplaced Isaac text restored by Dan.
Prevented triggering the building scene before getting Muddy quest.
Fixed double option with wrong link in the dialogue file of LaCroix.
Renamed Blood Purge and spell checked every text besides subtitles.
Cleared up the log texts of the Muddy quest and Pishas occult quest.

v1.5                                                    14.06.2005
----
+Awarded an XP for getting Imalia's magazine to compensate for money.
+Provided a Humanity point for not telling Hannah that Paul is dead.
+Lowered award for freeing Ash from the Society of Leopold to one XP.
+Adjusted knockback ranges for McLusky, SWAT rifle and the shotguns.
Fixed Hitman quest bug that showed failure for making them friends.
Corrected some errors in Hitman quest log, dialogues and doll texts.
Fixed bugs in the dialogue files of Ash and VV to get unused lines.
Corrected a bug that kept the Santa Monica haven active for Tremere.
Modified the dialogue files of Damsel and Isaac to fix bad options.

v1.4                                                    04.05.2005
----
+Removed illogical placed flamethrower and Ra blade from Hallowbrook.
+Made rifles and crossbows use single shots to fit reload animation.
+Put flaming crossbow, torch and flamethrower at the Leopold Society.
+Chastity will have the Ra blade and a crossbow can be found nearby.
+Imalia's magazine quest is now also available after her Tawni quest.
+Made CD quest available to all clans as Malkavian lines were there.
+Vendors will sell crossbow bolts and Slater sells a crossbow itself.
+Changed damage of blunt weapons to fist < arm < baton < bat < iron.
Barabus will not be in the Fu Syndicate anymore when you have left.
Fixed Tawni and friend noticing you before accepting Imalia's quest.
Repaired SWAT rifle crosshairs and set damage close to "Jamie Sue".

v1.3                                                    23.03.2005
----
After providing Romero with a sexy night he will give you his rifle.
Made Bach drop rifle or sword on defeat, may remove teleport light.
Provided two XP for freeing Ash from the Society of Leopold caverns.
The White Cloud doors in Chinatown are unlocked from the beginning.
Modified inventory texts of "Jamie Sue", Bach's rifle and Steyr AUG.
Removed Dan's "Ginger Swan fix", because the quest was not updated.
Isaac-Tzimisce dialogue line will disappear after quest is complete.
Corrected some subtitles so the Hengeyokai surprise is not spoiled.
Changed lots of subtitles so not every thug is called a Sabbat thug.
Edited quest log texts of Necromantic to prevent misunderstandings.
Corrected Isaac dialogue options so you can't get his gift right on.
Changed the strange "untie" lines in the Johansen dialogue options.
Removed Yukie's untakeable sword and changed some lines accordingly.
Modified some dialogue of Wong Ho in regard to a silver haired man.
Yukie will not appear before you visited the temple to fit her talk.
Wong Ho and hostess will not be in the Red Dragon after he is gone.
The Hallowbrook hotel cutscene will only happen if Heather is alive.

v1.2                            originally released by Dan Upright 
-----
fixed an indentation error in warrens.py that was causing scripts to 
stop working

v1.1                            originally released by Dan Upright 
-----
included romero's dialogue file, so the fix from v1.0 stands a 
better chance of working this time around

v1.0                            originally released by Dan Upright 
-----
patch now automated (and merged with leopatch)
prince/beckett cutscene fix is back in
fixed a typo in beckett's dialogue that was breaking an auto-link 
(thanks to doug thompson)
fixed beckett's dialogue trailing off as you're teleported into the 
ventrue lobby
fixed romero locking up if you're a woman, you flirted with him and 
completed the zombie quest
fixed imalia's newspaper from appearing when you fail the tawni 
quest
fixed the society of leopold crash with style and grace (meaning all 
clans should now transition unbugged to the correct landmark in la)
undid a previous mess i'd made of gary's poster quests - should work 
as originally intended now

v0.9                            originally released by Dan Upright 
-----
fixed beckett trying to increase your scholarship when it's already 
at max (thanks to Executor for this and the similar fix in v0.8)
updated fix for society of leopold exit crash (see leopatch0.3.rar)

v0.8                            originally released by Dan Upright 
-----
removed the prince/beckett cutscene fix until a reported bug is 
confirmed/fixed
placed the sound file for a line of isaac's dialogue in the correct 
directory (had been incorrect since v0.1)
fixed beckett trying to increase your inspection feat and failing - 
now increases investigation instead

v0.7                            originally released by Dan Upright 
-----
hunters won't spawn if the courier is behind the fast buck in 
hollywood - should stop people being killed during this cutscene
the highlight for imalia's newspaper shouldn't appear when the 
newspaper isn't there anymore
shouldn't be possible to get stuck in vv's dialogue so that you 
can't take the chastity quest
if you get the quest log entry for the igor quest from venus, igor 
should be there
the prince/beckett mini-cutscene/broken convo bug should be fixed 
(i disabled the cutscene)
updated fix for society of leopold exit crash (see leopatch0.2.rar)

v0.6                            originally released by Dan Upright 
-----
if you try to use the locked computer in warrens4 without the 
keycard, the keycard is highlighted if your inspection feat was too 
low to highlight it automatically
cleaned up brother kanker's dialogue - shouldn't get stuck in a loop 
anymore
zygaena shouldn't be in the red dragon after you've killed him 
anymore
shouldn't teleport to king's way Mansion after watching snuff film 
with isaac
shouldn't be able to get stuck with vandal's dialogue so he thinks 
you're on the replacing lily quest when you're not
if you've already read about rolf toten on the krimeputer when you 
find the bail bond, you don't need to read about him again
if you've already read about virgil crumb on the krimeputer when you 
get the driver's license, you don't need to read about him again
should no longer get a masquerade violation for convincing the 
serial killer not to kill again
should now get xp for completing the replacing lily quest
relinked the xp award for finding lily's items to the experience 
table
fixed a logic error in beckett's dialogue that resulted in "no valid 
responses" when talking about disciplines

v0.5                            originally released by Dan Upright 
-----
if you've already read about ginger swan when you talk to the 
courier, you shouldn't need to go back and read again
bonus xp for completing warehouse quest without killing should now 
be awarded even if you don't make it to beckett before the timer 
runs out
fixed another incorrect gender reference in samantha's dialogue

v0.4                            originally released by Dan Upright 
-----
should no longer be able to get both rewards for the hitman quest in 
chinatown
bonus xp for completing warehouse quest without killing should be 
awarded
isaac should now no longer refer to everyone as a toreador
gargoyle quest completion lines should now stop reappearing before 
you've been to king's way, not just after
isaac should give everyone a gift for completing the king's way 
quest
fixed some responses to samantha in hollywood that were referring to 
the player as the incorrect gender

v0.3                            originally released by Dan Upright 
-----
xp for killing bach and saving johansen in the leopold quest should 
now be given
when intimidating vandal, you should now get the free bloodpack
fix for society of leopold exit crash (see leopatch0.1.rar)
added changelog for those who want to know exactly what's been 
altered

v0.2                            originally released by Dan Upright 
-----
skipping the tutorial now gives lockpicks, the .38 and two xp
the computer in the nocturne theatre being hackable for mitnick's 
quest before you've even met mitnick
mercurio giving morphine quest reward twice if you have morphine the 
first time you meet him
food critic quest should now always give reward, only worked in v0.1 
under very specific circumstances (if you've already completed this 
quest, you'll notice it become unfinished in your log - go to your 
haven and type "tomSetQuestFour()" to complete it and get the reward)
dialogue option from asylum blood donor showing up for the 
confessions blood donor when playing as a female

v0.1                            originally released by Dan Upright 
-----
mercurio not selling the swat rifle
lily's sire's license plate not showing up in quest log
food critic quest not giving a reward
serial killer quest failing when persuading him not to kill again
isaac's conversation not allowing anyone but toreadors to mention 
the tzimisce
gargoyle quest completion lines constantly reappearing in isaac's 
conversation
dialogue line showing up twice when venus gives you money
melee attacks doing zero damage when breaking obfuscate level 1 or 2 
with an attack
being able to tell strauss you solved his gargoyle problem even if 
you didn't know he had a gargoyle problem
gary's email quests for the posters sometimes not all appearing


Sorted Changelog:
-----------------
All major bugfixes and gameplay changes are listed below sorted by
area or theme, excluding typos and minor dialogue and text issues.

General:
+Opened Ocean House, junkyard, basement and beachhouse after quest.
+Reopened coffee shop, library, crackhouse, garage and fishmarket.
+Updated some entries in some computers to reflect NPC fatalities.
+Opened King's Way, the museum and Giovanni Mansion after quests.
+Updated Ash, Copper and Serial quest states when you failed some.
+Made several corpses not dissappear immediately after cutscenes.
+Added missing manholes and taxis with cabbies to several levels.
Made all enemies drop weapon except for balance or impossible cases.
All illogical spawning and respawning is removed on several levels.
Fixed refresh-rate, coronas, floats and > 2 GB memory bugs in dlls.
Added about hundred missing facial expressions to about thirty NPCs.
Swapped Colt Anacondas with Ithacas for cop crews arriving by car.
Cops use GLOCKs, SWAT cops use AUGs and dead enemies drop more ammo.
Fixed hunters spawning on main hubs and a few NPCs not staying dead.
Removed illogical player@directory prompts from computer terminals.
Fixed several name issues and explained others using loading tips.
Corrected subtitle languages, speakers and added some missing ones.
Moved Giovanni loading tips up and improved several map load names.
Swapped prostitutes to seperate alike ones and fixed following bug.
Restored newscaster lines, missing Malkavian answers and his desk.
Corrected enemies not being able to hurt each other on some levels.
Made long lines at the end of dialogues stay inside the dialogues.
Removed Humanity loss for killing any kind of hunters on main hubs.
Unified burning barrel and fire explosion damage on several levels.
Restored uncensored intro beheading scene and swapped club dancers.
Added radioshow and Malkavian whispers transcripts to Extras folder.
Doubled explosion damage of shellboxes and fixed Leopold Society's.
Included official patch 1.2 files and gas valves to all fireplaces.
Swapped wrong manhole covers for Griffith Park and Giovanni Mansion.
Fixed edicts errors generated by multiple usage of Auspex on maps.
Added frenzy for NPC models and restored special situations on hubs.
Swapped several pedestrian models on a few levels to reduce cloning.
Translated Japanese and Russian dialogue parts for Yukie and Boris.
Improved cameras of Nines' intro, roof exit and epilogue cutscenes.
Added mods.cfg file and some Python scripts to make modding easier.
Corrected bad clockhands in intro, bailbonds and observatory levels.
Hexedited floating garbage in parking garage and downtown hub maps.
Fixed cabbie's seating on some maps and people not giving jewelry.
Corrected some minor level issues and console errors on game start.
Added some missing doors and and several female bums to hub levels.
Made King's Way door consistent and fixed a Society of Leopold lock.
Added or removed doorknobs to make it obvious which doors are real.
Fixed map holes in museum, warrens, Skyeline Apartments and SM hub.
Closed holes at observatory, Society, Hallowbrook Hotel and LA hub.
Fixed Jack not replying in tutorial and added a few toilett doors.
Stopped several dialogue NPCs staying tranced after being fed upon.
Used autoexec.cfg to fix dsp sound talk and frame rate door issues.
Made game and NPCs recognize death of Knox, Mercurio and Heather.
Moved linux loader into main folder and added warning popup to it.
Fixed map holes in Venture Tower and observatory and ground stutter.
Made the patch copy all bin files into main folder to fix crashes.
Prevented player from using idle animation during a few cutscenes.
Made NPCs recognize the death of Misti, Venus, Mercurio and Knox.
Removed corpses of blood dolls and other NPCs on revisiting maps.
Made seductive feeding multiple times of Phil and Romero possible.
Added missing solidity for sewer and temple models and some others.

Interface:
+Made pause, camera-moves, auto-move and walk/run toggles definable.
+Restored vendor and context icons and disciplines and thrown slot.
+Added answers for not reading tomes and improved note readability.
+Restored six character creation questions and several menu effects.
+Made skip intro button always work and removed all special letters.
+Restored discipline or weapon selection toggle and Flynn as vendor.
+Added seven missing infobar sounds and created seven infobar icons.
+Mentioned Clan Lasombra and the Nagaraja in the world loading tips.
+Improved title menu and character sheet clan symbols and fixed lag.
+Added console key and hotkeys to options, and item gained message.
Adjusted fonts issues regarding Dementation and Tremere Domination.
Added missing newspaper icons and increased the Obfuscate frame rate.
Corrected the corrupted Intimidation font "W" at higher resolutions.
Standardized key names in options, loading tips and tutorial popups.
Made all important sounds unique and fixed mixed up nosave messages.
Renamed Auto-Level button and removed Ventrue clan popup test button.
Added original Japanese and Russian words to translated subtitles.
Unified formatting of newspaper articles and improved GUI issues.

Graphics:
+Restored Nosferatu eyeballs, many clan idles and several hand skins.
+Made Malkavians see shaking cables and cars have transparent glass.
+Added elevator button lights and arrows and improved traffic lights.
+Improved rain and inspection effects and restored many particles.
+Added missing steam to clinic, Ocean House, Vesuvius and Hollywood.
+Included eye replacer, bloodlines logo and added blood to beheading.
Fixed frozen hunter, Gangrel warform and crouch on character sheet.
Corrected and added landmark names and icons of bus and sewer maps.
Swapped location labels of the missing sewer map with worldmap ones.
Added missing fangs to some vampires and fixed beast form model bug.
Darkened Beckett's glasses and fixed other glasses and eyes issues.
Restored invisible tabletops and many absent light and lift cables.
Added many missing inspection nodes and fixed many misplaced props.
Fixed bad fire particle files and badly placed or flickering decals.
Repaired clipping, holes, necks and Presence hair of various models.
Adjusted health bar frame and weapon/discpline highlight graphics.
Increased distance in which detail models and decals will fade away.
Hid invisible Ocean House and Grout's Mansion blocks by furniture.
Corrected many inside/outside door handles and background screen.
Fixed three mirrored keycard backsides and centered the area icons.
Added native widescreen support and improved readability of notes.
Corrected some areaportals in Leopold Society and Giovanni Mansion.
Disabled low poly model LOD and fixed pause messages in engine.dll.
Corrected mirrored crate textures and reset clothing using console.
Fixed hair of female Tremere and removed tongue of Sheriff warform.
Added way to use all animations on all NPCs and fixed phone ones.

Sounds:
+Added subtitles for Malkavian whispers and Deb of Night radio show.
+Restored unused OST music and fixed music at pier and Asylum door.
+Added random thunder sounds to pier and beachhouse to fit flashing.
+Removed radio 5 duplicates and repaired missing vcds and subtitles.
Added and fixed sounds for weapons, stats, events, ambience and more.
Provided twenty places for Malkavian voice whispers during dialogue.
Added sounds to silent cutscenes and made guards use cop sound files.
Improved sound effects of morgue doors and Kamikaze Zen vault doors.
Repaired cut off conversations and added sound schemes to computers.
Prevented restored NPC conversations from triggering multiple times.
Repaired many sound files with broken looping and fixed missing ones.
Corrected Anders/Ingvar and Larry's quest errors using sound files.
Fixed blood doll sound and line so it doesn't refer to women as men.
Removed a bad sentence of Mercurio and one of Isaac's two "evening".
Fixed SM and Hollywood hub club music and improved electronic voices.
Corrected no floats for females bug, croucher laughs and many floats.
Removed other clans whispers in tutorial, warrens and Ocean House.
Fixed sewer sound transitions in SM, Hollywood and Chinatown hubs.
Removed character sheet music overlaying and unified keypad sounds.
Lowered idle sound rate and missing sound to Blood Boil explosion.
Added missing monster sounds reacting to Dementation disciplines.
Restored breaking and machine sounds to observatory and SM clinic.
Added crane sounds to warehouse and changed crane sounds on Dane.
Improved Ocean House breaking wood, fling, noise and beach sounds.

Stats:
+Included and modified the cut histories, so that each clan has ten.
+Created homosexual history for all clans and adjusted intro scene.
+Made stealth harder to maximize it out and increased falling damage.
+Lessened damage for frenzy check and corrected shown armor ratings.
+Raised minimum Humanity for killing innocents to three like in hubs.
+Added Combat to feats to avoid confusion and renamed Social Public.
+Made Nosferatu break Masquerade easier and Frenzy use boosted stats.
+Swapped trouble making history conditions with similar limitations.
+Added config, commands and special equipped clans for multiplayer.
+Implied sleeping near tutorial and warehouse including bloodloss.
+Restored killing any innocents inside combat areas cost Humanity.
+Removed whispers, cables and encounters in Subtly Insane history.
Fixed crashes on final Masquerade violation gained during dialogues.
Prevented Humanity from reaching zero and adjusted cash descriptions.
Correctly stated Brujah unarmed bonus and Nosferatu Seduction zero.
Shortened Ventrue loading tip and some histories names to fit page.
Restored many mistyped Intimidate options and feat condition errors.

Disciplines:
+Restored casting hand animations and several discipline particles.
+Added Bloodheal discipline and slowed automatic heal rate by half.
+Restored Thaumaturgy Blood Theft, bloody eye effects and vamplight.
+Added inaccessible Bloodheal and Bloodbuff infos to loading tips.
+Restored low Tremere dialogue Domination and discipline crosshair.
+Added Presence in dialogue and improved Presence combat effects.
+Restored Domination Command and Sleep, Dementation Veil and Voice.
+Changed Cadaverous Flesh history and occult heal rate accordingly.
+Lowered Bloodbuff effect to two points and corrected info symbol.
+Adjusted Blood Shot and Boil damages and added missing Boil sound.
+Restored Potence effects and made it stack correctly with strength.
+Changed active discpline durations to fit better to graphic effect.
+Improved stat messages for Auspex, Fortidude, Potence and Protean.
+Changed Close to the Beast history because of wolf warform issues.
+Reduced Bat's Communion duration and prolonged Brainwipe duration.
+Added Blood Malady effect to supernaturals immune to Blood Theft.
+Restored Spirit Heal and combined Mind Shield and Shield of Faith.
+Created icons and cross for Holy Light and Divine Vision Numinas.
Made indirect disciplines not traceable and NPCs comfort loud ones.
Fixed disciplines for non-humans and Protean claw effects and icons.
Trimmed Bloodsuckers' to Bloodsucker and renamed Purge Blood Purge.
Fixed Potence, Ravens, Trance, Wipe and Hysteria issues and sounds.
Removed not working Blood Shot blood return when fighting Tzimisces.
Harmonized Presence chances and adjusted description of Blood Boil.
Edited history and occult item descriptions to display percentages.
Cleared disciplines before many more cutscenes than in the original.
Made Chang brothers and serial killer be resistant to Blood Purge.
Mentioned light amplification effects of Auspex and Divine Vision.
Disabled Vision of Death, Suicide and Mass Suicide for the zombies.

Items:
+Made it possible to give redundant items to NPCs and removed others.
+Lowered Firearms book condition and swapped some researchable books.
+Added unused models to three books, a script, a report and a data CD.
+Set eight occult powerups to unknown unless a Research stat is met.
+Made Strauss give Fae Charm and Isaac Pearl or money when in basic.
+Modified Ocean House diary and Lily's photo textures to fit text.
Modified placeholder names of four upgrade books and lowered a value.
Removed some keys after use and fixed some item drop and sell flags.
Fixed graphics of baton, VV photo, business cards and Gary's tapes.
Made sarcophagus key and clothes not stashable and fixed drop sounds.
Fixed the same-objects-in-inventory-and-containers-not-visible bug.

Weapons:
+Made first person melee fighting possible, the files are in Extras.
+Lowered criminal level awareness and accuracies of both crossbows.
+Made Bach and the Asian vampire drop both of their weapons on death.
+Adjusted NPC reloading of both crossbows and added SWAT rifle ammo.
+Restored missing flamethrower stats and increased the fuel capacity.
+Corrected zoom values, magazine sizes, ammo types and gun worths.
+Made rifles and crossbows use single shots to fit reload animation.
+Removed the zoom mode of the "Jamie Sue" and balanced with damage.
+Lowered additional damage on zoom mode and increased rifle accuracy.
+Lessened the sway of zoomed weapons and used real gun magnification.
+Adjusted MAC-10, Steyr, SWAT and shotgun kick and knockback stats.
+Branded .38, Uzi, MAC-10, GLOCK 19, Ithaca and the Remington rifles.
+Adjusted maximal ammo to reflect 10 or 20 spare clips and 50 shots.
+Made artificial claws do lethal damage and enabled torch lighting.
+Changed Sheriff's sword from Brawl to Melee and added Shin Gunto.
+Made magic projectile of fatguys do aggravated damage like Ming's.
+Swapped Colt Anaconda and Desert Eagle damage and added .38 kick.
Fixed melee attacks doing zero damage when breaking Obfuscate 1&2.
Increased claws range, added an icon and missing particle effects.
Corrected Ra blade description from fast speed to aggravated damage.
Added broken female fire axe texture and missing Ra blade texture.
Reconstructed the missing Desert Eagle ammo and female wield models.
Fixed GLOCK walk and run animations and several crosshair problems.
Adjusted GLOCK deploy sound and restored missing Desert Eagle ones.
Restored Ithaca, Ra blade, katana and bushhook stealth kill sounds.
Fixed claws usage in gallery, Hallowbrook hotel and Grout's Mansion.
Repaired bad Ming-Xiao, Tzimisce fatguy and Ra blade damage stats.
Changed severed arm pickup sound and added two missing mode sounds.
Fixed weapon stats shown using new client.dll and added claws info.

Vendors:
+Made Trip sell ring, watch, bat and tire iron but no books anymore.
+Moved Computers and Firearms books from Trip to clinic and Carson's.
+Vendors will sell crossbow bolts and Tseng sells a crossbow itself.
+Mercurio offers a Dragon's Breath, the body armor and a SWAT rifle.
+Made vendors sell SWAT rifle bullets and lowered price of fire axe.
+Tseng will offer Shin Guntos and the SPAS directly but no powerups.
+Made Tseng not offer blood and hide his special inventory better.
+Prevented exploit of selling books and removed Trip button sound.

Tutorial:
+Added unused quest logs, Sabbat goon muzzle flashes and a fade out.
+Made keeping Jack's .38 gun possible and repaired missing hands bug.
+Restored tutorial dialogue guard and removed Ventrue's rat feeding.
Fixed some popups issues, restored one and mentioned camera commands.
Removed second tutorial enemies for not mass affecting disciplines.
Added Jack gesture, armor info, sounds and fixed stealth kill icon.
Removed .38 ammo exploit and added check and options for high stats.
Made Jack acknowledge a special stealth kill and fixed blood reset.
Fixed location continuity, MAC-10 loudness and a way to get stuck.

Haven:
+Made it possible to specify which clothes Heather should wear next.
+Swapped two of Gary's emails and fixed them sometimes not appearing.
+Placed Obfuscate and Galdjum powerups at sewer and downtown havens.
+Made Malkavians loose Humanity when sending McFly to threaten cops.
+Added option to keep Heather alive and added a humane farewell line.
+Made Larry send spam email and improved two friend emails timings.
+Added four new Gary poster quests and made Heather throw away pizza.
+Made SM haven stay active, added bathroom door and locked another.
Corrected Mercurio sending wrong timed emails and fixed email order.
Repaired VV and Jeanette sending you their emails at the wrong time.
Fixed Heather not appearing at haven and allowed some more feeding.
Stopped CD quest email from arriving after the quest was finished.
Corrected a bug that kept the Santa Monica haven active for Tremere.
Gaining the Tremere haven is now independent from the quests order.
Prevented Tremere from being able to loose their haven for treason.
Corrected Heather not giving silver ring when you already got one.
Stopped Gary's posters from appearing in your unused old haven too.
Removed buggy SM haven board and Mercurio's note after you met him.
Turned Chantry haven into Masquerade area to fix Tremere detriment.
Improved TV and radio state consistencies in SM and downtown havens.
Fixed talking with Heather after you dealt with McFly in two ways.

Santa Monica:
+Added male seduction to blueblood and removed him after alley trip.
+Made CD quest available to all clans and fixed beachhouse cash bug.
+Reconstructed Bertram's PC and incooperated text of unused emails.
+Added dialogue to diner trap and restored Obfuscator and guard dog.
+Restored jenny_cries sequence and fixed a SM schrecknet door lock.
+Activated spooky cover sound and Asian vampire laptop screensaver.
+Made only Chunk use porch in rain and drop key when incapacitated.
+Restored Trip's drug quest and fixed Trip's pawnshop door crashing.
+Made player sending Gimble to Vandal loose humanity then regain it.
+Cleaned Mercurio's apartment and fixed some wrong bum animations.
+Made player phone Gimble in shop and Carson's killing being logged.
+Unlocked door in Gimble's lair, showed his hand and fixed cutscene.
+Made Carson pack his stuff and corrected skybox reflection on hub.
+Restored fighters brawling in Al's video game at beachhouse level.
Fixed morphine quest updates after angering Mercurio and warehouse.
Made diner cook move more and stopped Doris from falling into floor.
Fixed Lily's sire's license plate in quest log and her diary dates.
Corrected prophet stop preaching and removed some first quest info.
Added Lily's purse to her stuff and uncovered it if Doris is dead.
Made Bertram react to attacks and taking CD if you already have it.
Added check for having the astrolite and cops to pier conversation.
Made it possible to trigger serial killer quest from all newspapers.
Added cop cars to beachhouse level and corrected floating Mercurio.
Adjusted Cathayan report dates and prevented him getting invincible.
Made getting secret informations from Knox and Johansen consistent.
Restored rain to beachhouse and removed buggy Ocean House version.
Added bloss loss to ghouling Heather and having fun with Jeanette.
Opened beachhouse door on combat and restored Al's and glass sounds.
Corrected XP and restored log for unravelling Knox and Bertram plan.
Blocked a way from the SM hub into the junkyard before it's opened.
Delayed Mercurio cutscene to make player move where he can see it.
Darkened more ground floor lamps at beachhouse after power is off.
Made hunters in Santa Monica attack Tung if they meet him outside.

The Asylum:
+Added one more Jeanette encounter with enough Seduction and blood.
+Granted Humanity for persuading Therese and Jeanette to make peace.
+Added Domination to Danielle and prevented dead Chunk from dancing.
+Made it easier to save Jeanette and made Tourette give you her gun.
Fixed Jeanette taking knife, PC, music and some elevator problems.
Persuading Jeanette and Therese to conciliate is like intended now.
Corrected Ocean House quests not closing if you refused the gallery.
Made Ocean House quest failure update when reconciling the sisters.
Removed Chunk after you met him downtown and restored female raver.
Corrected wrong Jeanette quest update and made Cal getting re-hired.
Fixed misleading emails and lines for whoever did get the pendant.

Bail Bonds:
+Restored Arthur's computer and his starting monologue on the phone.
+Updated Krimeputer log entries for beachhouse's and Muddy's deaths.
+Added way to feed of Arthur after his quest and fixed restart loop.
Made you remember former knowledge of Rolf Toten and Virgil Crumb.

Medical Clinic:
+Restored bisexual Phil, fixed him dropping note and made him stay.
+Created Vandal quest for Nosferatu and added XP for alternatives.
+Added quest and XP for saving Heather and removed the combat zone.
+Made Vandal quest available later too and stealth work for guard.
+Added Humanity loss for not freeing Lily and fixed cutscene eyes.
+Improved emails, elevator display and climbing back into the vent.
+Moved Malcolm's black mail money from your mailbox into his office.
+Put Heather's and Doris' name in the morgue file in case they died.
+Restored way to kill Vandal and improved other SM clinic details.
Fixed getting Vandal's freebie and made him more talkative overall.
Repaired not getting XP for replacing Lily and hacking the passcode.
Stopped dead Malcolm mailing you and monitor react to dead victim.
Made clinic guard remember the dialogue and lowered his vision stat.
Fixed morgue computer mentioning Crumb and locked morgue freezers.
Made Vandal acknowledge quest payment and corrected two wrong auras.
Swapped Lily cutscene Phil with scrubs model Bill if Phil is dead.
Prevented asking Malcolm about Heather when you already saved her.
Modified barber chair with Lily to animate bonds and fixed lighting.
Made Phil only refer to clinic computer if you already accessed it.
Fixed clinic guard not dropping key if killed by seductive feeding.
Made it possible to continue E's quest after visiting Vandal often.
Moved breakroom so geometry fits and fixed werewolf blood exploit.

Elizabeth Dane:
+Added boat model, props, missing door sounds and fixed screenshots.
Lowered difficulty of Dane computer and made cop acknowledge quest.
Restored several rookie cops and repaired Dane crane switch icons.
Stopped Dane cop from looping and fixed illogical camera detection.

Gallery Noir:
+Restored XP for entering peacefully and improved Chunk's sequence.
+Activated light switch and added cash box item and botch message.
+Added sound to Blood Guardian summoning and removed a blood trail.
+Stealing charity money will not cost Humanity if you know about it.
Fixed Gallery bar inspection and made charity money stay available.
Prevented talking with Chunk when someone else attacked the Gallery.
Made police always investigate crime and locked gallery front then.
Corrected wrong painting positions after slashing then re-entering. 

Serial Killer:
+Lowered gainable Humanity points and restored killer's phone call.
+Restored one dog model to and fixed sounds and actions at junkyard.
Removed Masquerade violation and failure for convincing the killer.
Made killer react to diner violence and quest independent from Muddy.
Corrected freezes on meeting the killer and Gimble while Obfuscated.

Ocean House:
+Restored missing Ocean House newspaper and made photos look sepia.
+Hid Ocean House killer's axe and increased chance of noticing him.
+Restored Ocean House sprinkler sequence, some cans and some sounds.
+Swapped low Dodge book with Defense powerup and restored moon sky.
+Restored Hellcat and valve sequences and fixed some lantern sparks.
+Made Edward's theme play only after the Ocean House has been left.
Hid clipping boxes and added a missing door, trailer and bar lamps.
Added and corrected inspections of containers and steam pipe damage.
Restored ghost whispers, scenes, laughter and vent breaking sounds.
Fixed railings, areaportals, shadows, vanishing junk and map holes.
Swapped door handle that could be used too soon and fixed one icon.
Fixed double ghost, elevator buttons, bad sprite and scary sounds.
Disabled bad icons and buttons for not active Ocean House elevator.
Fixed outside map holes, a texture and lowered ghost music volume.
Restored two missing XP in the Ocean House quest and swapped one.

Pier:
+Awarded XP point for letting Julius free and fixed his wrong aura.
+Sending Copper after the president triggers a Masquerade violation.
+Added a Humanity loss for sending Copper to kill the head vampire.
+Restored chewing gum for Copper into arcade and animated screens.
+Added seperate quest and an XP for exploiting the thin-blood Copper.
+Made killing pier cops loose Humanity and gave one the baton only.
Lowered money available from Julius and the surf computer difficulty.
Prevented Copper from suddenly having money and added bus to pier.
Removed cop cars after the police left and added Die My Darling song.
Prevented doing E's quest for dead E and fixed rain through bridge.
Showed thin bloods on beach when looking down from the beachhouse.
Made sure beachhouse thugs are dead if Mercurio appears at beach.

Warehouse:
+Changed warehouse bonus XP to stealth and prevented re-entering it.
+Restored part of forklift crash and Troika raver with conversation.
+Added breakable tomb stone, gas tank, board and phones to warehouse.
+Restored Beckett leaving and removed the warehouse bum as a witness.
Corrected blocked door and locked double door and made boxes solid.
Fixed thug with too good eyesight and removed Beckett stealth alert.
Added inspection to gascan and fixed transparent girders and icons.
Corrected looping conversation, walk-into ventduct and buggy pallet.
Added missing card player, animated generator and restored lockpick.
Corrected overlapping music, near-distance portals and missing ladder.

Downtown:
+Moved frenzy powerup from basement into hollow book in Grout's room.
+Removed Larry's quest buy condition and fixed the briefcase scene.
+Added sewer haven TV sound and lessened crackhouse victims exploding.
+Moved Fat Larry to demo-trailer place and gave him more hit points.
+Swapped Damsel and Skelter and moved Jack down to fit the dialogues.
+Added Last Round pinball player and bartender and moved female bum.
+Provided newspaper downtown and restored Skyeline and junkyard ones.
+Added Gary to intro cutscene and synced the courtroom sword sound.
+Restored Malkavian "sewer-cabbie" rat and interesting place types.
+Swapped Igor's .38 with GLOCK 19 and fixed Beckett's "wait" cutscene.
+Recreated library level with quest and missing Hallowbrook atrium.
+Added Heather to sewers for Nosferatu and delayed Vick's arena exit.
+Moved finding out about the Gargoyle XP to avoid preferring sides.
Removed theatre intro extras and a computer being hackable too soon.
Hid an invisible block at the theatre and fixed sick bum respawning. 
Prevented triggering building scene before getting the Muddy quest.
Moved bum in the LA abandoned building and fixed getting stuck there.
Removed an all clans moving sewer map and a plaguebearer sewers lock.
Fixed parking garage gang war problem and Ming as Nines size issue.
Made Regent's quest fail if you betray him and added Blood Hunt line.
Moved dumpster to map hole and fixed floating rails and hub windows.
Fixed condition for telling Damsel that you killed a werewolf too.
Corrected Nosferatu NPC stats, shopping cart physics, and the moon.
Fixed possible problem if people kill Igor without talking to him.
Made Igor attack the player if his friends are killed or attacked.
Fixed LaCroix particles and hid floating Masquerade cutscene NPCs.
Restored plaguebearer quest log, Regent line and cool Nines gesture.
Fixed suitcase exchange at the parking garage and added one poster.
Made abandoned warehouse bum and crackhouse girl leave after a time.
Fixed two theatre door signs and discipline removal in crackhouse.
Restored Gangrels to Masquerade cutscene and added theatre email.
Made every armed NPC in downtown fight back when you attack them.

Confession:
+Restored laptop, turnstile, gestures, three cage dancers and a DJ.
+Made Patty go behind the church and fixed above cross camera bug.
Fixed blocking Confession barkeeper and Venus giving right payments.
Restored missing Venus reaction to persuading Boris to give up dept.
Added short-time club replacement for Venus in case you killed her.
Fixed dead Patty appearing in alley and staying around in Confession.
Restored correct Masquerade redemption for ways to get rid of Patty.
Added log for sending Patty to alley and fixed teleporting dancers.

Empire Arms:
+Improved card printer usage so you need to check the computer first.
+Put library card in room and unlocked Boris' doors for Venus quest.
+Exchanged Brawl and Finance book locations and added Johansen suite.
+Restored two security guards and fixed Russian discipline reaction.
+Made Empire clerk bisexual and restored unused Ming skin for singer.
+Swapped Boris' .38 with a GLOCK and added dance spot to the lobby.
Fixed Igor not appearing and improved Russians position and reaction.
Prevented Boris' door from closing and made Dima go outside and wait.
Forced talking to Boris and fixed Obfuscate and Dementation problems.
Fixed Jezebel's lock and trunk, and the Empire TV sound on/off bug.
Moved Empire hotel computer into backroom and restored mafia patrol.
Repaired bad elevator button at Empire hotel and Dima not attacking.
Stopped Empire hotel TV from being turned off because of lighting.
Added floor number to suite names in computer and numbers to floors.
Improved Empire Hotel mafia TV room sound switch and music radius.
Gave Jezebel a Glock to hurt you on bed and stopped vanishing Dima.
Corrected Boris dialogue problem after he survived fighting Dema.

Malkavian Mansion:
+Restored leaf, smoke, maze room and bed trigger to Grout's Mansion.
+Added aura for Grout's wife and fixed jars transparency problems.
Fixed possible crash on leaving, Obfuscate freeze and candle skins.
Disabled Grout's trigger after use to improve Comp Mod compability.
Corrected Grout's wife tube and hid secret door icons in basement.
Rebuild la_malkavian_4.bsp map in Hammer to fix exit room problems.

Hospital:
+Added option to give severed arms to Pisha and fixed line condition.
Fixed level re-enter sounds, card quest update and scripts breaking.
Milligan and Pisha react to Domination, Intimidation and Dementation.
Turned hospital into Elysium area during your encounter with Pisha.
Made all clans lose a Humanity point for sending Milligan to Pisha.
Added Pisha line about quest item and checked state for another one.
Made Pisha leave eventually and her quests fail when attacking her.
Corrected first Pisha victim being visible before sequence starts.
Disabled bad downtown hospital sounds and illogical debris vanish.

Museum:
+Made Beckett train up to Scholarship 4 and added museum entrance.
Restored Ash song into museum and added missing second T-Rex sound.
Added doorcode quest log at museum and improved breaking the windows.
Prevented museum guard from dropping multiple storage room keycards.
Fixed museum laser beams errors and an invisible air vent blockade.
Corrected Beckett's bonus dialogue and fixed stuck museum guard AI.
Removed shortcut at museum and fixed guard dropping workroom key.

Skyeline Apartments:
+Restored security guard with scenes and fixed elevator and monitor.
+Rewarded one Humanity for Dominating Milligan and added toileteries.
+Restored a Milligan line and created necessary license item for it.
Fixed Milligan not leaving and restored his black monitors and case.
Adjusted Hannah's dates, forced her lines and made her actually die.
Modified XP and log for plague quest state and made CDC stay longer.
Added missing XP for plague quest and fixed Hannah quest state bug.
Lessened vents fade outs, loud humming sound and fixed a wrong decal.
Made Hannah's apartment vent doors unlock on entering the password.

Venture Tower:
+Added a new discipline, Celerity/Fortidude/Animalism, from Beckett.
Made Prince react to Persuasion for money when sending you to Ming.
Corrected wrong subtitles for Chunk's brother and Chunks fighting.
Fixed Venture Tower debris clipping issues and security camera cycle.
Made Venture debris stay longer and be visible through the windows.
Added missing light effects to cop cars and restored guard bodies.
Swapped Malkavian fireplace with restored and added Gary to council.
Fixed possible mute Chunk, if this happens press the camera button.
Corrected doors, handles, cameras, walk-through columns and an icon.

Hollywood:
+Added male seduce feed for Tommy and fixed re-persuading or killing.
+Fixed quest log updates on Ash and Romero dying during their quest.
+Added Masquerade violation and Humanity loss on public sweeper kill.
+Restored two actors to Ground Zero backstage and a cat to Kings Way.
+Unlocked Red Spot's storage door and locked it's back door instead.
+Added Malkavian whisper to Ash sewers and restored Gargoyle gesture.
Fixed food critic quest reward and endless prostitute dialogue loop. 
Added DMP combat zone switch, fixed headrunner sequence and drop bug.
Prevented hunters during the courier dialogue cutscene and forced it.
Fixed wrong observatory manhole sound and locked outer Tawni door.
Made sweeper defend himself and added a sweeper reference to Isaac.
Fixed Humanity loss when killing thugs and Chinese Theatre trigger.
Restored new female bartender and two unused hustlers to Hollywood.
Removed bad warrens hatch reflection and forced Tzimisce subtitels.
Made celebrity database update and stopped VV from sending poster. 
Stopped dead Tommy writing review and fixed slanting streetlights.
Restored three King's Way headrunners and fixed Red Spot door bug.
Corrected netcafe sound schemes switch and fixed many streetlights.
Switched badly fixed missing Tommy line with better fitting float.
Fixed possible courier and warrens computer problems in Hollywood.
Added missing XP if you found Ginger Swan before meeting courier.

Abrams Jewelry:
+Added XP and a Masquerade redemption for dealing with the Gargoyle.
Made Isaac give the reward for defeating the Tzimisce to all clans.
Stopped instant teleport to King's Way Mansion after watching film.
Made Isaac recognize the Tzimisce defeat even if you pissed him off.
Fixed some Isaac bugs regarding Toreador and his King's Way reward.
Reconstructed lip-sync for Dan's restored line and fixed another one.
Isaac-Tzimisce dialogue line will disappear after quest is complete.
Used money as alternative for Isaac's gift issue in the basic patch.
Added Gargoyle quest states and fixed connected quest start issue.
Made video victim's model unique and corrected ghoul sound group.

Asp Hole:
+Made you loose a Humanity point for making Ash exchange his clothes.
+Added and fixed breakable air compressor and board into Ash sewers.
Fixed wrong aura of Ash and removed hunter from club when he is gone.
Restored unused girl and hustler skins for the Asp Hole bartenders.
Armed Ash sewers hunters with Shin Guntos and improved end fade out.
Fixed map hole with opened tunnel divider and angles on re-entering.
Gave GLOCKs to hunters in Ash sewers and removed two unused switches.

Cemetery:
+Restored Romero returning after his quests and made gates stronger.
+Made Romero train up to Firearms 4 and give you ammo with his rifle.
+Added Domination to prostitute and made her leave you when attacked.
+Made Romero pimpin and zombie quest available both after each other.
+Prevented getting Romero a rival in love and made his blood refill.
+Created option to have some fun with Romero after the zombie quest.
After providing Romero with a sexy night he will give you his rifle.
Fixed ammo trunk respawning and Romero entry and exit script issues.
Added fade and sound for pleasing Romero and sound to pimpin quest.
Fixed Romero locking up for females flirting after the zombie quest.
Removed fight after zombie quest failing to prevent getting stuck.
Fixed cemetery quest scripts breaking if you flee into the warrens.
Corrected lip-sync of prostitutes in cemetery and a dialogue issue.
Prevented Romero cemetery cutscene freezing if Presence is active.
Added sign to Hollywood cemetery gate and fixed name in computer.

Luckee Star:
+Fixed Hatter being unapproachable when you threatened him too early.
+Added laptop and note with easter eggs hint and fixed card name bug.
Deleted icons of unopenable doors at Luckee Star and repaired music.
Fixed quest state reset on drop and re-pick up of the Salvage card.
Added missing sound to Luckee Star cutscene and fixed the fireplace.
Fixed easter egg at Luckee Star hotel and made it easier to access.
Made Hatter drop screenplay on death and changed a wrong key model.
Displaced two buggy Luckee Star doors that were closed occasionally.
Restored Muddy fighting killer animation and so fixed the cutscene.
Fixed Nosferatu causing Masquerade violations exiting Luckee Star.

Sin Bin:
Fixed opening or breaking the ATM machine and handle and area change.
Reformatted Sin Bin inventory pages and fixed Ginger Swan knowledge.
Modified discipline options for Kerri and fixed Sin Bin state reload.
Fixed bug after escorting Ash before reporting Chastity back to VV.
Added magazine quest state on killing Flynn and aborted getting it.
Made Sin Bin ATM machine not vanish and Romero sit after boinking.

Hollywood Apts.:
Moved a Tawni quest camera into kitchen and added missing TV sound.
Made quest log and laptop show failure and fixed being noticed early.
Prevented continuing the Tawni quest after you have been detected.
Updated netcafe entries for Tawni and Ash dependent of quest states.
Changed camera spot icons and made Tawni's boyfriend holster gun.

Vesuvius:
+Restored Velvet and Misti dances, pool girl and a special sequence.
Removed Misti freebie for Nosferatu, her clones and made her refill.
Fixed stripper and girl off work leaving Vesuvius' dressing room.
Restored sound to Vesuvius' easter egg and made it easier to find.

Warrens:
+Added unused rat crowd model and removed bad warrens re-entry sound.
+Restored three female body parts and two blockades and fixed stairs.
+Placed GLOCK near killed sewerworker and extended spiderchick scene.
+Restored two unseen newspaper cuts and made web cameras stackable.
+Improved corpse variety in warrens lair and made ladder accessible.
+Added possibility to keep the Nosferatu alive for a humanity gain.
Repaired warrens electrical terminal computer and pump 118a display.
Made sure the quick Nosferatu dies and adjusted some warrens dates.
Replaced fighting Mitnick clone with male or female Nosferatu model.
Highlighted keycard of locked sewer cover and fixed water reflection.
Allowed sewer-warrens detour and made Imalia and Mitnick turn better.
Corrected a wrong sign in warrens and removed icon of Mitnick's PC.
Restored missing Bertram CD quest state update and fixed a cutscene.
Added missing lamps, blocked a pipe and fixed missing arch clipping.

Nosferatu Lair:
+Granted occult Perception powerup as reward during Mitnick's quest.
+Made you lose Humanity for taking money as reward of Imalia's quest.
+Awarded an XP for getting Imalia's magazine to compensate for money.
+Imalia's magazine quest is now also available after her Tawni quest.
+Added new quest logs and an XP for Gary's posters and changed order.
+Restored unused models to the Nosferatu warrens to fix a map hole.
+Added Masquerade redemption for sending the Nosferatu photo to Gary.
+Made Gary give different bloodpacks as the protection talked about.
Repaired bug that could make Imalia angry before getting her quest.
Prevented Imalia's newspaper from appearing when you fail her quest.
Repaired Imalia still being angry after you sold her the magazine.
Removed an annoying side table in Gary's lair and hid two map holes.
Swapped Gary's quest order and his CD for a box with vacuum tubes.
Prevented continuing Mitnick's quest after failing a previous hub.
Fixed schrecknet commands being available after hubs were activated.

Chinatown:
+Made killing Lu lower Humanity and added Intimidation to Ji and Lu.
+Added XP and humanity for keeping Zhao alive and added Tong mugger.
+Placed a dead dog into Fu Syndicate and filled Kamikaze Zen shelf.
+Made Glaze a Masquerade area and Fu Syndicate start as combat area.
Made Tseng talk only of known people and restored Ming/Fu connection.
Corrected Hitman quest rewards and added peace-talk lines for both.
Fixed Hitman quest bug that showed failure when making them friends.
Repaired quest updates when talking to the Mandarin and streetlights.
Corrected contradicting Wong Ho news and improved Tseng shelf models.
Fixed bug when talking to Zhao from outside and LOD on the main hub.
Added newpaper for stealth Glaze and changed Fu newspaper condition.
Recompiled Zhao's Warehouse to fix the doors vanishing at a distance.
Fixed bad Lotus Blossom map location and replaced buggy phone sound.

Fu Syndicate:
+Added squashed Odious Chalice, katana, GLOCK and some more scenery.
+Restored alarm off switch and removed lobby keypad and push barrier.
Resolved issues with Obfuscated players and guards still seeing them.
Improved Barabus' hack position and made PCs accessable afterwards.
Released the trapped elevator guard and fixed wrong aura of Barabus.
Added emergency doorcode and fixed laser beams error after loading.
Made Barabus leave with you and not be breaking out all on his own.
Improved crossguy reaction, test timing, door speed and ignitions.
Repaired auto-locking door, stuck fanblades and teleporting SWAT.
Removed disciplines when talking to the Mandarin at Fu Syndicate.

Glaze:
+Restored XP for stealth killing Johnny and made guards fight back.
Removed reference to Ricky at Glaze and made monitor turn off sooner.
Added several missing lines to Johnny's cutscene and unstuck Ricky.

Kamikaze Zen:
+Added name plate and one XP for stealing it from Kamikaze Zen safe.
Adjusted logs and added missing passwords for two email accounts.
Turned power on and timer off on re-visiting the Kamikaze Zen map.
Made Glaze monitor turn off earlier and fixed Zhao death reference.
Moved Kamikaze Zen vent exit into a back alley to make more sense.
Recompiled Kamikaze Zen map to fix vent without exit and lighting.
Fixed virus and timer issues on returning to the Kamikaze Zen map.

Lotus Blossom:
+Restored many China shop props to Lotus Blossom and Lu Fang skin.
+Added two patrons into Lotus Blossom and lowered perceptions there.
Removed Lotus patron after your talisman success but not the locker.
Repaired several Lotus Blossom icons and fixed reaction of tub guy.

Red Dragon:
+Granted Humanity for saving Wong Ho and adjusted warning conditions.
+Restored Kiki, male blood doll and unused throwing star into desk.
+Made Red Dragon male blood doll not get stuck in chairs on attack.
Wong Ho and Kiki won't be in the Red Dragon anymore after they left.
Corrected subtitles to keep a surprise and restored Wong Ho sitting.
Prevented dead Zygaena from appearing and fixed bad elevator lights.
Corrected hostess not getting elevator and phoning without a phone.
Lowered award for killing a demon in his human form to two XPs only.

White Cloud:
+Made Lockpicking and Strength occult items be rewards from Mr. Ox.
The White Cloud doors in Chinatown are unlocked from the beginning.
Corrected bug that made it possible to get Ox's harvest quest twice.
Mr. Ox will react correctly when you already have acquired the eyes.

Yukie:
+Restored evasion and corrected Obfuscate bug on entering fishmarket.
Fixed bad door sound and restored Yukie to Ramen shop from the start.
Restored shop stats, fixed quest issues and made her use her sword.

Giovanni Mansion:
+Restored Dodge II manual, cabbie and a Domination option for Luca.
+Added quest logs for Giovanni candidates and for the endgame finish.
+Restored spirits attacking if crypt coffins are hit and blast door.
+Made Nadia react to zombies damaging player and removed fake door.
+Changed two icons at Giovanni Mansion and made Bruno react to feed.
+Placed some things in empty Giovanni rooms and fixed player start.
+Corrected getting secret from Christopher and flirting with Nadja.
+Improved Giovanni trap section and circumvented Bruno not burning.
Fixed reentering issues and door breaking at the Giovanni Mansion.
Removed inconsistent alert states, fixed lever icons and zombie bugs.
Fixed doors and back door guard and removed invisible Bruno clones.
Made Bruno attack on lockpicking and his speech stop when he enters.
Fixed Nadia lines playing without her and made a snort girl mortal.
Removed Kuei-jin's burning death and lying patron hooker getting up.
Repaired Chang story state continuity problem and a Maria dress bug.
Made crypt backtracking possible and improved door icons and sounds.
Added inspection nodes to some trapdoors and fixed guard awareness.
Stopped wrong invitations being dropped and corrected names on them.
Swapped unique car, fixed it's texture and improved Nadia sequence.
Prevented spoiling secrets of all candidates and fixed Victor loop.
Fixed claw brother being susceptible to one-hit-kill by Possession.
Moved truck loading scene to back entrance and fixed missing sounds.
Added distraction of Giovanni backdoor guard and fixed zombie trap.
Restored two short Nadia lines and improved elevator level sound.

Society of Leopold:
+Placed Ash's cell key in big cave and fixed Bach encounter exploit.
+Created quest for freeing Ash and added more beds and toilet doors.
+Added Humanity gain for saving Johansen and loss for killing him.
+Johansen will only follow you if you told him during the dialogue.
+Added ladder and food and hid issues on the roof with ammo boxes.
After giving Ash the bloodpack it will be gone from your inventory.
Restored missing sounds to Bach cutscene and missing XP on escaping.
Replaced some male hunters with females and swapped several weapons.
Fixed exit crash with style and grace and cellar ladder top issue.
Prevented Humanity from reaching zero in the dialogue with Johansen.

Hallowbrook Hotel:
+Opened Hallowbrook Hotel shortcut door in atrium to skip interior.
+Added a Sabbat option to endgame including skipping the whole hotel.
+Moved Ra blade to lair, flamethrower to atrium and removed GLOCKs.
+Forced Heather remembrance lines and added slash sounds and blood.
+Added crashed elevator with metal grating and fixed bad door script.
+Restored shovelhead and Lasombra models and Firemage cast animation.
Fixed Hallowbrook name differences and invincible burning Lasombra.
The Heather cutscene will only happen if she is alive and your ghoul.
Made Heather's last clothes fit and added animations to her scene.
Turned Tremere Firemage into a female for males and swapped AUGs in.
Prevented Heather's comeback when returning from lower Hallowbrook.
Moved unreachable NPCs, fixed door openings and premature spawning.
Fixed way to kill downtown Ming and replaced cutscene Asian vampire.

Blood Hunt:
+Made werewolf damageable by normal weapons and removed debug switch.
+Healed player after Griffith Park and repaired Observatory switches.
+Added observatory inspections and fixed taxi TV icon and triggers.
+Restored Skelter and grenade to Luckee Star and delayed Nines line.
+Added helicopter to rooftop, missing doors and fixed cop cars issue.
Corrected bad bus stops, not solid poles and removed buggy Potence.
Turned haven into Elysium area and placed females at the Blood Hunt.
Swapped wrecks on Blood Hunt map and repaired helipad SWAT texture.
Repaired Trip and Vandal not choosable at endgame in special cases.
Prevented taxi from driving to dead Mercurio and hid taxi ride hole.
Removed Jack from haven at taxi ride and improved observatory scene.
Fixed weird camera after endgame Cabbie discussion and his cut line.
Corrected breakable stairs at observatory and fixed many map holes.
Fixed crouching Blood Hunt vampires by swapping several used weapons.

Temple:
+Restored Yukie as companion to temple and Ming endgame camera shot.
+Gave guards Shin Guntos and removed unusable Ming temple doorknobs.
Unlocked a temple door for Yukie and secured three others later on.
Disabled arrow chest spawning and fixed facing Ming while Obfuscated.
Corrected start orientation, inspections, trap trigger and a tin can.
Prevented picking of two temple doors and unbarred big temple gate.
Fixed quest log update and XP gain on reaching Ming's inner sanctum.
Added missing temple door sound and restored Chang and buddha skins.
Reduced slime particle spawning in temple and fixed clipping columns.
Fixed sanctum view, teleport timing, key drop and a temple map hole.

Endgame:
+Provided shortcuts to skip most fighting and locked Skyeline vents. 
+Restored Sheriff conjuring Bat's Communion and added his sword too.
+Made Ventrue enemies use disciplines and SWAT in armor not biteable.
+Added exits to Sheriff roof fight and made his sword easy to find.
+Restored wolf-ending easter egg and a added timer to elevator bomb.
+Added timed explosion and boss flag for LaCroix's Dominated bomber.
+Restored Justicar and white SWATs, and cleaned up Nines at ending.
+Added patch contributors to credits and fixed a taxi ride map hole.
Corrected Venture Tower lamp, a passive guard and made bomb hurt one.
Added endgame quest logs and improved subtitles for Dominated guard.
Swapped Ventrues in Tower with females or Toreadors to avoid clones.
Fixed sliding chute, elevator, portals and a lock in Venture Tower.
Showed player alive at Anarch ending and added Damsel and Skelter. 
Made Chunk not attack you if you convinced him during the endgame.
Repaired bad icons and flickering for upper Venture tower elevator.
Improved many details in Ming ending and masquerade ending cutscene.
Fixed Venture Tower icon and holes and made glass roof accessable.


Restored Content:
-----------------
Summary of unused stuff added in the basic (-) and plus (+) versions
of the patch, including all item location changes of the plus patch.

Levels:
+ Smoke Shop.
+ Coffee Shop.
+ Chateau Hotel.
+ Public Library.
+ Malkavian Maze.
+ Museum Entrance.
+ Warrens Shortcut.
+ Hallowbrook Atrium.

Endings:
+ Joining Sabbat ending.
+ Easter egg wolf ending.

Quests:
+ Drug quest from Trip.
+ Library quest from Beckett.
+ Gary poster quest for name plate.
+ Gary poster quest for fleshy ball.
+ Gary poster quest for throwing star.
+ Gary poster quest for squashed chalice.

Disciplines:
+ Bloodheal discipline.
+ Sleep instead of Suicide.
+ Madness as Bedlam partial.
+ Spirit Heal Numina for hunters.
+ Faith Shield Numina for hunters.
+ Bloody Eye as Blood Purge partial.
+ Blood Theft instead of Blood Salvo.
+ Blood Malady as Blood Theft partial.
+ Active discipline casting animations.
+ New disciplines available from Beckett.
+ Toreador and Brujah Presence in dialogue.
+ Tremere first level Domination in dialogue.

Weapons:
+ Broadsword in the library.
+ Sheriff sword from Sheriff.
+ Dragon's Breath from Mercurio.
+ Tiger's Claws from Claw Brother.
+ Fragmentation grenade from Nines.
+ Pyro crossbow from several enemies.
+ Shin Gunto swords from several enemies.
+ SWAT sniper rifle from Mercurio or Bach.

Powerups:
+ Occult Wits powerup in Kamikaze Zen level.
+ Occult Obfuscate powerup in Nosferatu haven.
+ Occult Charisma powerup as reward from Isaac.
+ Occult Security powerup as reward from Mr. Ox.

Items:
+ Fleshy ball in King's Way.
+ Charity money box in gallery.
+ Name plate in Kamikaze Zen safe.
+ Throwing star on Red Dragon desk.
+ Driver's license from Simon Milligan.
+ Wooden pulltoy in Metalhead Industries.
+ Library card found in the new library level.
+ Chewing gum sellable to Copper found on pier.
+ Vacuum tubes box found in the new library level.
+ Squashed Odious Chalice hidden inside Fu Syndicate.
+ Models for Colt Anaconda and Desert Eagle magazines.
+ Models for Dane report, screenplay, cd and three books.

Encounters:
+ Kiki at Red Dragon.
+ Guard dog at the beachhouse.
+ Male blood doll at Red Dragon.
+ Security guard in the tutorial.
+ Yukie helping in first temple map.
+ Last dialogue at Hallowbrook hotel.
+ Meeting Skelter during Anarch endgame.
+ Security guards at Empire Arms hotel entrance.
+ Sewer-cabbie rat for Malkavians in downtown hub.
+ Security guard and sequence at Skyeline Apartments.

Options:
+ Killing of Vandal possible.
+ Venus' computer at Confession.
+ Laptop and note at Luckee Star.
+ Santa Monica pier end accessable.
+ Sending Gimble or Patty to Vandal.
+ Timed explosion of Dominated bomber.
+ Dance spots at Glaze and Empire hotel.
+ Revisiting possible of seven locations.
+ Bertram's CD quest available to all clans.
+ Arthur's and Bertram's computers accessible.
+ Talking to thugs and killer phoning in diner.
+ Private dancing from VV and Misti at Vesuvius.
+ Having fun with Jeanette possible one more time.
+ Improved handling of Empire Arms keycard printer.
+ Zombie and pimpin quest available after the other.
+ Warrens, Hallowbrook, Temple and Venture shortcuts.
+ Imalia's magazine quest available after Tawni quest.
+ Surplus items can be given to Lily, LaCroix and others.

Situations:
+ Hollywood sweeper fighting back.
+ One dog and Lasombra at junkyard.
+ Giovanni spirits in Giovanni crypt.
+ Sheriff using Bloodsucker Communion.
+ Two actors being killed at Ground Zero.
+ Cat and Sabbat leader sequence at King's Way.
+ Special sequences on all hubs and in Vesuvius.
+ Rat crowd and spiderchick sequences in warrens.
+ Female crying, broken limo and Obfuscator on SM hub.
+ Hellcat, valve and sprinkler sequences at Ocean House.
+ DJ, barkeeper, cage dancers and turnstile at Confession.
+ Boss, forklift accident and Beckett leaving at warehouse.

Scenery:
+ Ten props at beachhouse and five on pier.
+ Six props in theatre and four in tutorial.
+ Twelve props in museum and two in hospital.
+ Leaves and smoke outside of Grout's Mansion.
+ Ten props in warrens and eleven in Ash sewers.
+ Seven props in Fu Syndicate and one in temple.
+ Nine props on Dane and and seven in Last Round.
+ Five props in Luckee Star and three in Vesuvius.
+ Twenty props in King's Way and five in Hollywood.
+ Twelve props in Red Dragon and four in White Cloud.
+ Nine props in Hallowbrook hotel and two in Chantry.
+ Twenty-three props at warehouse and three in Asylum.
+ Sixteen props in Lotus Blossom and two in fishmarket.
+ Twenty-two props in Ocean House and eight in SM clinic.
+ Twenty-five props at Grout's and nineteen at Giovanni's.
+ Thirteen props in Empire hotel and four in Venture Tower.
+ Twenty-four props in tattoo shop and seven props in Tsengs.
+ Two props at junkyard and three in Foxy Boxes and Chinatown.
+ Twenty-four props in netcafe and nineteen at Society of Leopold.
+ One prop on each hub, downtown, diner, Zhao's and two at Skyeline.
+- Six props at warrens and two at Society of Leopold.
+- Two props at Gimble's, four at observatory and one in SM.

Moved items:
+ Moved Galdjum from Warrens into Skyeline haven.
+ Ra blade moved from Hallowbrook room to basement.
+ Moved flamethrower from Hallowbrook room to atrium.
+ Heart of Eliza moved from Tseng to be Mr. Ox reward.
+ Moved Fae Charm from Tseng to Regent as quest reward.
+ Exchanged Brawl and Finance book places at Empire hotel.
+ Swapped Dodge powerup and book at Ocean House and Grout's. 
+ Moved Computer and Firearms books to SM clinic and Carson's.

Restored characters:
+ Female citizen at pier.
+ Rookie cops on the Dane.
+ Alternative Cal in diner.
+ Receptionist at Vesuvius.
+ Girl in VV's private pool.
+ Clean Nines at solo ending.
+ Female ravers at the Asylum.
+ Alternative Chang at temple.
+ Justicar at Camarilla ending.
+ Pinball player in Last Round.
+ Two new SWATs in Venture Tower.
+ Lasombra at junkyard and library.
+ Alternative singer at Empire hotel.
+ Bartenders at Last Round and Glaze.
+ Headless corpse and head in warrens.
+ Two scrubs corpses in Grout's Mansion.
+ Receptionist and Tongs in Lotus Blossom.
+ Lasombras and shovelheads at Hallowbrook.
+ Girl and hustler bartenders at the Asphole.
+ Strippers in Sin Bin, Vesuvius and Giovanni's.

Other restorations:
+ Flynn as normal vendor.
+ Nosferatu and Pisha eyes.
+ Voiced conversation on Dane.
+ Over fifty dialogue gestures.
+ Fighting video game characters.
+ Auto-moving and walk/run toggles.
+ Sixteen HUD and five vendor icons.
+ Sixteen unknown items descriptions.
+ Active torch and Blood Shield light.
+ Discipline and thrown inventory slots.
+ Ten context icons and nine newspapers.
+ Pause, hotkey and camera keydefinitions.
+ Discipline and weapon selection toggling.
+ Eight clan hand models and four skyboxes.
+ Main menu and many other particle effects.
+ Over sixty decal graphics and terminal texts.
+ Over fifty clan idles and many more animations.
+ Six character questions and three tutorial popups.
+ Histories mode offering ten histories for each clan.
+ Two songs and twenty-four compositions of Rik Schaffer.
+- Over two hundred dialogue lines. 
+- Twenty Malkavian whispers in dialogue.
+- Over hundred sounds, floats and conversations.
+- Multiplayer mode including special MP clans with equipment.


Unrestored Content:
-------------------
Features and stuff found referenced in the game files that are
not implemented or too far from being finished to be restored.

Actions:
* Carrying bodies (context icon found).
* Staking vampires (context icon found).
* Feeding grapple (animation and info found).
* Dice rolls and botch (icons and info found).

Stats:
* Histories giving items (infos found).
* Encumbrance and willpower (info found).
* Generation and blood pools (info found).
* HUD light level warning (graphics found).
* Alternate creation stats (tutorial info found).
* Alternate popups (tutorial_popups* files found).
* Occult item powerups inventory category (info found).
* Thrown weapon inventory category (info and icon found).
* Animal Ken, Athletics and Occult abilities (info found).
* Jumping, Throwing and Animal Friendship feats (info found).

Disciplines:
* Auspex giving enhanced FOV (info found).
* Animalism Serpents Succumbre (info found).
* Domination Command levels and Sleep (info found).
* Thaumaturgy Blood Malady and Bloody Eye (info found).
* Dementation Haunting and Voice of Madness(info found).
* Presence Awe, General and Daze 1/2 levels (info found).
* Discipline and Numina levels shown in HUD (graphics found).
* Protean 5 Wolf warform (info, textures and animations found).
* Bloodbuff-Dexterity/Stamina/Strength disciplines (info found).
* Numinas Mind Shield and Shield of Faith (icons and info found).

Items:
* Electronic lockpick (info found).
* Written item (info and file found).
* Riot gear (stats found in traitseffects.txt).
* Flak jacket (stats found in traitseffects.txt).

Weapons:
* Razor melee weapon (info found).
* Stake (info, icons and animations found).
* LAW rocket launcher (icon and particles found).
* Panic rifle = stake launcher (icons and particles found).
* Smoke grenade (info found).
* Molotov cocktail (info found).
* Concussion grenade (info found).
* Throwing star (info, file and model found).
* Enfield rifle instead of SWAT (info and icon found).
* Smith&Wesson M64 instead of .38 (info and icon found).
* Armsel Striker instead of SPAS-15 (info and icon found).
* Dual Sig P220Ss instead of Desert Eagle (info and icons found).

Mapping:
* Law and bunker buildings (textures found).
* Thugs retreating (sm_warehouse scripts found).
* Kiki and thugs in Ramen shop (Python scripts found).
* Beckett coming from left (sm_warehouse scripts found).
* Disabled options (ch_fulab, sp_giovanni_2a/b info found).
* Disabled events (hw_warrens_3, la_malkavian_5 info found).
* Disabled triggers (sp_genesis, sm_oceanhouse_2 info found).
* Disabled cutscene effects (la_hub, sm_vamparena info found).
* Maps e3_chinese, e3_combat, e3_confession, e3_hub (info found).
* Maps sp_boat, sp_camwarehouse, sp_lonewolf, sp_smut (info found).

Models:
* Thirdperson hacking (animation found).
* Thirdperson lockpicking (animation found).
* Thirdperson bomb placing (animation found).
* Thirdperson keypad hacking (animation found).
* Zhao reloading dual pistols (animation found).
* Burning people running around (animation found).
* Spiderchick splitting on death (animation found).
* Bat swarm as animals to befriend (npc class found).
* Duplicate props with different sizes (models found).
* Cowering and wine interesting places (animations found).
* Booth and barstool interesting places (animations found).
* Trash, dummy and other props without texture (models found).
* Props with alternate skins or in combinations (models found).
* More pipes, pillows, barbells and billiard balls (models found).

Textures:
* Old style blood drop GUI (textures found).
* Sewer travelmap interface (textures found).
* Alternate Yukie and raver clothes (textures found).
* Alternate SWAT rifle and Lily purse (textures found).
* Alternate Ocean House ghosts and werewolf (textures found).
* Alternate Jack, Jeanette, Tong and Dane cop (textures found).
* Alternate heads for Julius and Venus (textures found).
* Alternate heads for Nines and Therese (textures found).
* Alternate heads for Slater and Mitnick (textures found).
* Alternate pawnshop sign and eyes (icon and textures found).
* Alternate spiderchick and alternate fatguy (textures found).
* Alternate heads for Boris, Flynn and Romero (textures found).
* Two alternate cats and two alternate dogs (textures found).
* Two alternate shirts and trousers for Venus (textures found).

Music and Sounds:
* Mid_Short cutscene29 (mp3 missing).
* Mid_Short cutscene30 (mp3 missing).
* Mid_Short cutscene35 (mp3 missing).
* Mid_Short cutscene stem2 (mp3 missing).
* Mid_Short cutscene stem12 (mp3 missing).
* Mid_Short cutscene stem13 (mp3 missing).
* Vampire Extra Music Stem6 (mp3 missing).
* Whispers/Ambiguous/Moon alt (wav missing).
* Whispers/Distrust/Hemlock alt (wav missing).
* Whispers/Crying/Child_cry alt (wav missing).
* Whispers/Moaning/Woman_moan alt (wav missing).
* Whispers/Moaning/Child_moan_alt2 (wav missing).
* Alternate Mike and Carl conversation (wav found).
* Alternate computer usage sound group (wavs found).
* Alternate Dane cop adressing the player (wav found).
* Alternate backup lines of major characters (mp3s found).

Others:
* Lots of unused sounds (wav files found).
* Lots of unused particles (scripts found).
* Lots of unused textures (image files found).
* Lots of unused animations (references found).
* Wearable jewelry (info and textures found).
* Masquerade area striked message (icon found).
* Different HUD user interface (graphics found).
* Lock and discipline crosshairs (graphics found).


Modified items:
---------------
To create new items, unused, duplicates and NPC weapons were 
modified, the latter items can not be taken from containers.

-item_d_holy_light -> is not visible in inventory
item_g_garys_cd (Tung's CD duplicate) -> Pull Toy
item_g_jumbles_flyer (flyer duplicate) -> Fleshy Ball
item_g_ring_serial_killer_1 (unused) -> Pearl of Dubai
item_g_wireless_camera_2 (camera duplicate) -> Name Plate
item_g_wireless_camera_3 (camera duplicate) -> Squashed Chalice
item_g_wireless_camera_4 (camera duplicate) -> Throwing Star
-item_i_written -> is not visible in inventory
item_k_key_generic (unused) -> Museum Keys
item_p_occult_hacking (unused) -> Braid Talisman
item_p_occult_lockpicking (unused) -> Antique Locket
item_p_occult_obfuscate (unused) -> Zharalketh (just restored)
item_w_avamp_blade (not obtainable in basic) -> Shin Gunto
item_w_chang_blade (not obtainable in basic) -> Broadsword
item_w_chang_claw (not obtainable in basic) -> Tiger's Claws
-item_w_chang_energy_ball -> is not visible in inventory
-item_w_chang_ghost -> is not visible in inventory, has blue lights
item_w_claws_ghoul (NPC) -> Milligan's Driver's License
item_w_claws_protean4 (claw duplicate) -> Library Card 
item_w_claws_protean5 (claw duplicate) -> Vacuum Tubes
item_w_gargoyle_fist (NPC) -> item_p_occult_thaum_damage Daimonori
item_w_hengeyokai_fist (NPC) -> item_p_occult_heal_rate Mummywrap
item_w_manbat_claw (NPC) -> item_p_occult_dodge Weekapaug Thistle
-item_w_mingxiao_melee (NPC) -> Ming can't use it if changed
-item_w_mingxiao_spit (NPC) -> Ming can't use it if changed
item_w_mingxiao_tentacle (NPC) -> Bubble Bum
item_w_rem_m_700_bach (not obtainable in basic) -> SWAT Rifle
item_w_sabbatleader_attack (NPC) -> item_p_occult_hacking Braid
item_w_sheriff_sword (not obtainable in basic) -> Sheriff Sword
item_w_tzimisce_melee (NPC) -> item_p_occult_experience Saulocept
-item_w_tzimisce2_claw (NPC) -> Fatguy can't use it if changed
item_w_tzimisce2_head (NPC) -> Thaumaturgy Casting
item_w_tzimisce3_claw (NPC) -> item_p_occult_frenzy Tarulfang
item_w_werewolf_attacks (NPC) -> item_p_occult_obfuscate Zharalketh
item_w_zombie_fists (NPC) -> item_p_occult_passive_durations Galdjum
-weapon_physcannon (manipulation) -> hand won't work if changed

The Occult Ability was intended to be the requirement for using
occult items. If it wasn't met, these messages were randomized:

  You can't identify this item, but it has a "Made in Hell" 
  label on the bottom.
You have no clue what this thing is, but it looks eeeeeevil.
  You cannot identify this item, perhaps you should finish 
  eating the soul doughnut?
It isn't a WWJD bracelet, so you have no idea what it could be.
  If Ozzy were here, I'm sure he could tell you what this is.
Maybe if you were a bit more goth you would have a clue what 
this thingie is.
  You haven't seen one of these before, but Bun Bun left it here, 
  so it can't be good news.
Hmm, when you gaze upon this object, the skies darken and lightning 
flashes. Those aren't good clues to what this is though.

The surfaceprop on-drop-sound classes available for *.phy files are: 
flesh, kitchen_utensils, metal, paper, plastic, ring, stone or wood.


Context Icons:
--------------
0 none 1 carry 2 pc 3 locked 4 key 5 card 6 container 7 tv 8 phone
9 hand 10 door 11 use 12 switch 13 sewer 14/15 talk f/m 16 warning 
(tube) 17 bomb 18 note 19 kill 20 chance 21-27 elev 1 - 7 28 8 (b) 
29 g 30 no elevator 31 up 32 down 33 stop (sword) 34 drop (valve) 
35 arrow > (oven) 36 arrow < (books) 37 sconce 38 recorder 39 key 
40 clipboard 41 newspaper 42 spotlight 43/44 graph 45 cash (stake) 
46 book 47 payphone 48 webcam 49 penthouse 50 bus map 51 sewer map
52 skull 53 pad locked 54 pad opened 55 break 56 bus map 57 sewer
lines 58 door closed 59 transition 60 sewer transition 61 pedestal
62/63 dance m/f 64 lever 65 use 66-71 malk symbols 72 push


Multiplayer Support:
--------------------
Each multiplayer clan starts with 100 XP, $500 and unique equipment.
Players can't damage each other thus only coop gameplay is possible!

Server:
1. exec multiplayer.cfg   enable multiplayer support on this server
2. map 'name'             load map 'name', admin must only spectate
3. noclip                 server admin needs to stay in noclip mode
4. sv_gravity "800"       after clients connected switch gravity on 

Client:
1. connect 'host'/'ip'    connect to server 'host'/'ip' as a client
2. vclan 'mp-clan'        play as 'mp-clan' with starting equipment
3. say/say_team '...'     talk ingame to everyone/your team members
4. name 'player'          optional set name of yourself to 'player'
5. team 'team'            optional assign yourself into team 'team'
6. vgender int 0/1        optional to switch the character's gender

If you want to play as a hunter after changing the clan you need to
restart the game at least once until the HUD graphics were updated.


Console Commands:
-----------------
Open the console (default key "~") from the main menu only, or type
"chareditor" if it freezes! All commands can be added to cfg files.

god               Godmode
noclip            Flymode
notarget          Enemies will not attack
buddha            Player takes damage but does not die
chareditor        Switches to sheet
impulse 101       Gives most weapons
cmdlist           Lists all console commands
cvarlist          Lists all console variables
frenzyplayer      Frenzies player (which unfreezes cutscenes)
camera_kill       Kills camera mode (which unfreezes cutscenes)
vstats xxx y z    Stat editor: xxx get/buy/sell y stat z points
vgender int 0/1   Changes gender: 0 female, 1 male
vclan name        Changes clan to name: Player_... for singleplayer
vhistories        Lists codes for all histories of current clan
vhistory nn       Activates the history with the code nn
give name         Gives item to player: name item_...
use name          Uses the item
giftxp n          Gives n experience points
blood n           Gives n blood points
money n           Gives... not what you think ;)
map name          Start map name: ch_.../hw_.../la_.../sm_.../sp_...
buildcubemaps     Rebuild cubemaps, not from menu, then reload level
changelevel2 m n  Teleports player to map m at landmark n 
restart           Restarts the current map
developer 0-3     Displays more error messages.
G.variable(= n)   Displays (sets) value of game variable
gclearall         Clears all G. variables
debug_area_type n Changes area to 0 combat, 1 masquerade, 2 elysium
ent_dump ENT      Dumps all info about entity ENT
mat_fullbright 1  Turns the lighting to maximum
fov n (normal 0)  Change field of view for widescreens
r_anamorphic 1    Enables stretching for widescreens
v_hidegui 1       Hides the HUD for taking screenshots
cl_showpos        Displays coordinates
cl_showfps        Displays frame rate
picker            Displays object data
showtrigger 1     Displays trigger areas
surround 1        Enable surround sound mode
snd_gain 2        Compensate for loudness loss in surround mode
ai_show_hints     Shows pathfinding hints for NPCs
ai_show_interesting 1  Shows special places that NPCs will use
vcollide_wireframe 1  Shows collision wireframes for floorblocks


Story States:
-------------
These are the values of the variable G.Story_State during the game.
It can be modified to get different results in dialogues or levels!

-6	Started New Game.
-5	Character Creation.
-4	During opening cinematic, added by wesp.
-3	During tutorial.
-2	Tutorial done, transition to haven.
-1	Entered haven.
0	Entered Santa Monica.
1	Convinced Trip to sell you guns.
2	Showing Elysium tip for the first time (temporary).
3	Showing combat tip for the first time (temporary).
5	Spoke with Beckett at warehouse.
10	Entered downtown.
15	Elizabeth Dane completed.
20	Spoke with Bach at Grout's Mansion.
25	Spoke with Prince after Grout's Mansion.
30	Spoke with Beckett at museum.
35	Spoke with Prince after museum.
40	Spoke with the Tzimisce, added by wesp.
45	Spoke with Gary.
50	Mandarin started experiments.
55	Rescued Barabus.
60	Spoke with Chang brothers, added by wesp.
65	Spoke with Prince after Giovanni Mansion.
70	Spoke with Johansen.
75	Spoke with Prince after Society of Leopold.
80	Spoke with Ming-Xiao after Hallowbrook.
85	Spoke with Prince about Ming-Xiao.
90	Spoke with Jack after Griffith park.
95	Spoke with endgame cabbie.
100	Cabbie takes you to Chinatown (Kuei-Jin ending).
105	Cabbie takes you to Chinatown (Sabbat ending), added by wesp.
110	Cabbie takes you to Prince (Prince ending).
115	Cabbie takes you to Anarchs (Anarch ending).
120	Cabbie takes you to Chantry (Camarilla ending).
125	Cabbie takes you to Chinatown (Solo ending).


Hammer Information:
-------------------
When using the Bloodlines Hammer to create a new map the tips below
might be helpful. Compile the release version with -final settings.

* The decompiler omitts detail models, like /trash_stuff/junk_*.mdl.
* The decompiler sometimes mucks areaportals up, fix or remove them.
* Toolsinvisible slows VVIS, use clip except for functional brushes.
* Toolsnoviz isn't working, use func_details, especially for skybox.
* Func_Details may add junk planes, in that case turn back to world.
* Func_Details do not seal the world, use normal brushes to do that.
* Always use nodraw textures for surfaces that the player can't see.
* Always check for entities outside the world which can cause leaks.
* Fix reflection differences by joining the brushes to func_details.
* Fix bright reflection on brushes by placing cubemap in dark areas.
* For a map transition landmark names on both maps must be the same.
* For a map transition landmark position and angles need flag 1 set.
* Cubemap reflections are dependent on brushes, textures and groups.
* Cubemap reflections of dynamic entities can be rebuild inside map.
* NPC Entities that are killed are inaccessible, modify them before.
* NPC Entities freeze if old animations can't play, kill them first.
* "Physics Penetration Error": prop_physics mustn't intersect other.
* "Bad Collision Data": clip brush in entity, use invisible instead.
* "Pause 0" closes prop_signs with Use, "Pause 1" needs mouse click.
* "func_ladder" is needed to make brushes climable with right sound.


Public Library:
---------------
The library level was build to present a smaller but darker version
of the real library, using the original Troika assets listed below.

Troika Design Infos:
Brian Mitsoda was asked via email on 18.10.2011 about the library, 
he replied: "The library design never even made it into an alpha 
stage. It was discussed, part of the level was built, but there was
never any finalized quest plans or layout. There was some idea of 
it being a side quest connected to one of the major characters and 
the Sabbat, but it never really got beyond that. There was also some 
discussion of an optional boss there, but that was never designed 
fully. My memory fails me on a lot of the finer details since it was 
never a major focus of design." So the rest had to be improvised.

Restored Models:
models/gibs/computergibs.mdl
models/scenery/misc/globe/globe.mdl
models/scenery/misc/podium/podium.mdl
models/scenery/misc/socket/socket.mdl
models/scenery/misc/globe/globe_small.mdl
models/scenery/misc/umbrella/umbrella.mdl
models/scenery/misc/info_booth/info_booth.mdl
models/scenery/misc/socket_tube/socket_tube.mdl
models/scenery/misc/lib_fountain/lib_fountain.mdl
models/scenery/structural/librail/librail.mdl
models/scenery/structural/bradbury/boardstatic
models/scenery/structural/liblight/liblight.mdl
models/scenery/structural/libcolumn/libcolumn.mdl
models/scenery/structural/escalator/escalator.mdl
models/scenery/structural/gio_bust_one/gio_bust_one.mdl
models/scenery/structural/gio_bust_two/gio_bust_two.mdl
models/scenery/structural/gio_statue_two/gio_statue_two.mdl
models/scenery/furniture/ladder/ladder.mdl
models/scenery/furniture/blankets/blankets.mdl
models/scenery/furniture/table/library_table.mdl
models/scenery/furniture/stepladder/stepladder.mdl
models/scenery/furniture/bookcase/library_bookcase_lg.mdl
models/scenery/furniture/bookcase/library_bookcase_small.mdl
models/scenery/furniture/bookcase/library_bookcase_small2.mdl
models/scenery/furniture/camwarehouse_cart\camwarehouse_cart.mdl
models/character/pc/male/gangrel/armor_0/gangrel_male_beastial.mdl

Restored Textures:
art/libwlla, art/libwllb, art/libwllc
decals/details/paperk, decals/details/paperm
decals/details/papern, decals/details/paperq
blends/ritualcolumnbot, blends/ritualcolumntop
tile/libfloorc, concrete/libstat, concrete/libwlla
plaster/libwlla, plaster/libwllb, plaster/libwlld
plaster/libwllf, plaster/libwllh, plaster/libtrima
plaster/libtrimb, plaster/libceilinga, plaster/libdoorb
art/librarysign1, art/librarysign2, art/librarysign3
wood/libceilingb, wood/libceilingc, wood/libceilingd
wood/libdoora, wood/libdoorb, wood/libfloora, wood/libfloorb
wood/libwlla, wood/libwllb, objects/libescrise, objects/libescrun
carpet/libtapestrya, carpet/libtapestryb, carpet/libtapestryc


Hallowbrook Atrium:
-------------------
The atrium map was build to look similar to the famous Bradbury 
Building atrium, using the original Troika assets listed below.

Troika Design Infos:
The planned existence of the level was obvious because a map with 
the name la_bradbury_1 was missing, and both the transition from 
la_hub_1 and an unused backwards transition from the la_bradbury_2 
entrance door were called roof_transition. The existing rails and 
stairway models pretty much defined the size and design of the map
which looks close but not exactly like the real Bradbury atrium.

Restored Models:
models/scenery/world/bradbury/stairs
models/scenery/structural/bradbury/boardsa
models/scenery/structural/stairs/brad_stairs1
models/scenery/structural/brad_rails/brad_rails1
models/scenery/structural/brad_rails/brad_rails2
models/scenery/structural/brad_rails/brad_stairs1a
models/scenery/structural/brad_rails/brad_stairs1b
models/scenery/structural/brad_elevator/brad_elevator
models/items/newspaper/ground/newspaper_sun.mdl
models/character/monster/tzimisce/creation1/creation1_unused.mdl
models/character/npc/common/freshcorpses/Femalecorpse_Posedonground

Restored Textures:
decals/pictures/deadrise_poster1, decals/stains/zombiedust
decals/details/graf_03, decals/structural/electricalpipesdecal_A
decals/structural/electricalpipesdecal_B/...decal_C, signs/exit
brick/brbwndwa, brick/brbarch, brick/brbarchbtm, carpet/bradcarpeta
wood/braddoora, metal/bradgatea, plaster/bradwlla, plaster/bradwndwa


Malkavian Maze:
---------------
The maze map in Grout's Mansion was build around concept art and 
beta screenshots, using the original Troika assets listed below.

Troika Design Infos:
There is little specific knowledge about the maze except for many
models and textures whose names place them there, the three beta 
screenshots that show unknown Mansion areas, and some concept art 
that looks so weird that it would fit in there as well. The maze
was also used to restore some of the Chateau Marmont Hotel, which 
Brian Mitsoda wrote could've been "Probably Malkavian Mansion?"

Restored Models:
models/objects/projector.mdl
models/scenery/structural/chateau/deco1.mdl 
models/scenery/structural/chateau/balltop.mdl
models/scenery/structural/chateau/winframe.mdl
models/scenery/structural/chateau/cm_awning2.mdl
models/scenery/structural/chateau/cm_supports.mdl
models/scenery/structural/chateau/cmarch.mdl
models/scenery/structural/chateau/cmcarch.mdl
models/scenery/structural/chateau/cm_rail1.mdl
models/scenery/structural/chateau/cm_rail2.mdl
models/scenery/structural/chateau/cm_stairs7.mdl
models/scenery/structural/chateau/cm_stairs6b.mdl
models/scenery/structural/chateau/cm_bani_top.mdl
models/scenery/structural/chateau/cm_bani_link.mdl
models/scenery/structural/chateau/cm_bani_rail.mdl
models/scenery/structural/chateau/ceilingarch.mdl
models/scenery/structural/apartment/roofb.mdl 
models/scenery/structural/malkavian/malk_bed.mdl
models/scenery/structural/malkavian/malk_nightstand
models/scenery/structural/malk_mirror/malk_mirror
models/scenery/structural/ballroomtrima.mdl
models/scenery/structural/ballroomtrimb.mdl
models/scenery/structural/ballroomcolumnb.mdl
models/scenery/structural/ballroomcolumnc.mdl
models/scenery/structural/ballroomcolumnc2.mdl
models/scenery/structural/ventrue_tower/ballroomwndwlight.mdl
models/scenery/structural/ventrue_tower/ballroomdomebroken.mdl
models/scenery/furniture/fireplace/fireplace.mdl
models/scenery/furniture/conc_chair/conc_chair.mdl
models/scenery/furniture/chair/wooden_cafe_chair.mdl
models/scenery/furniture/wall_art/frame.mdl (15 skins)
models/scenery/furniture/short_diningroom_table/s..._d..._t...mdl 
models/character/npc/unique/santa_monica/vandal/andrew.mdl
models/character/npc/unique/santa_monica/malcolm/jasper.mdl

Restored Textures:
concrete/malkmazeflra, concrete/malkmazeflrb
decals/details/crem_hectore, decals/details/crem_jaime
decals/details/crem_sbokkes, decals/details/crem_brock
decals/details/crem_cashton, decals/details/crem_dmarsh
decals/details/malklitec90, decals/details/malklitec180
plaster/malkwllc, plaster/malkwlld, plaster/malkwlld_a
plaster/malkwndwa, plaster/malkdoora, plaster/malkliba
plaster/malkmazea, plaster/malkmazeb, plaster/malkwlle
plaster/malkwll02, plaster/malkwllbtrim, tile/malkfloora
plaster/lawwlla, wood/lawtrma, wood/galdoora
wood/malkmazedra, wood/malkmazedrb, wood/malkmazedrc
wood/malkmazedrd, wood/malkmazedre, wood/malkmazewood
wood/malkwllb_c, wood/malkmazestairstop, wood/malkmazestairs
wood/malkmazeceilinga, wood/malkmazeceilingb, blends/malkfloorb
stone/lawflra, tile/lawceilingc, tile/cmfloorb, tile/cmfloorc
glass/ohglassa, glass/confwndwa, glass/cath_stain01/02/03
stone/floora, concrete/bunkerflra, concrete/bunkerflrb 
concrete/bunker, concrete/bunkerb, concrete/bunkerb 
plaster/cmdoora, plaster/cmdoorc, plaster/cmdoorf
plaster/cmposta, plaster/cmpostb, plaster/cmwndwd
plaster/cmwllc/d, plaster/cmwlle/f, plaster/cmwllg
plaster/cmdoord, plaster/cmwndwb, plaster/cmdwndwb_a
plaster/cmceilingb, plaster/cmdwndwc, plaster/cmwndwclit

Restored Assets:
sound/whispers/crying/man_cry.wav
sound/whispers/crying/woman_cry.wav
sound/usable/openable/wood_cabnet/*
sound/disciplines/animalism/burrowing beetle/cycle.wav


Warrens Shortcut:
-----------------
The shortcut map was build around two beta screenshots to offer
a compact sewer, using the original Troika assets listed below.

Troika Design Infos:
Except for the two beta screenshots the design of the original
beta sewers remain a mystery, but Leonard Boyarsky himself said 
in an interview by Sebastian Thor from Eurogamer 08.2014 about 
a possible Bloodlines remake: "I hope they shorten the sewers; 
those things go on forever, unfortunately." Therefore this map.

Restored Models:
models/scenery/misc/lever/lever.mdl
models/scenery/misc/pipeend/pipeend.mdl
models/scenery/misc/door_trap/doortrap.mdl
models/scenery/misc/prophetsign/prophetsign.mdl
models/scenery/misc/door_trap/doortrap_hinge.mdl
models/scenery/misc/wooden_spool/wooden_spool_bottom.mdl
models/scenery/misc/wooden_spool/wooden_spool_top_big.mdl
models/scenery/misc/wooden_spool/wooden_spool_top_small.mdl
models/scenery/physics/cannister/cannister01.mdl
models/scenery/pipes/metal_pipe_blue01.mdl
models/scenery/pipes/metal_pipe_blue02.mdl
models/scenery/pipes/metal_pipe_green01.mdl
models/scenery/pipes/metal_pipe_green02.mdl
models/scenery/pipes/valve_wheel/valve_wheel01.mdl
models/scenery/structural/dane/hammer01.mdl
models/scenery/structural/dane/wrench01.mdl
models/scenery/structural/tower/pipes.mdl
models/scenery/structural/sewer/busted.mdl
models/scenery/structural/oilfield/piped.mdl
models/scenery/structural/stake/gas_pipes4.mdl
models/scenery/structural/sewer/sew_stair02.mdl
models/scenery/structural/sewer/sew_stair03.mdl
models/scenery/structural/dane/pipe_wrench01.mdl
models/scenery/structural/gatesewer/gatesewer.mdl
models/scenery/structural/warrens/warr_subdoor.mdl
models/scenery/structural/warrens/pipeend_large.mdl
models/scenery/structural/warrens/warr_02_ladder.mdl
models/scenery/structural/stake/building2windowa.mdl
models/scenery/structural/SewerPipes/PipeMed_P2.mdl
models/scenery/structural/SewerPipes/PipeMed_P5.mdl
models/scenery/structural/SewerPipes/PipeMed_P9.mdl
models/scenery/structural/SewerPipes/PipeMed_P11.mdl
models/scenery/structural/SewerPipes/PipeLarge_P2.mdl
models/scenery/structural/SewerPipes/PipeLarge_P6.mdl
models/scenery/structural/SewerPipes/PipeSmall_P6.mdl
models/scenery/structural/SewerPipes/PipeSmall_P11.mdl
models/scenery/structural/warrens/warr_subdoor_latch.mdl
models/scenery/structural/trash_stuff/trash_litterd_lit.mdl
models/scenery/structural/warrens/warr_01_pipes_bcnosign.mdl
models/scenery/structural/plaguebearer_sewer/plague_xsupport.mdl 
models/scenery/furniture/charredmattress/charredmattress.mdl
models/character/monster/creation1/creation1_lower.mdl
models/character/monster/creation1/creation1_torso.mdl
models/character/monster/undead/female/undead_femalepart1.mdl
models/character/monster/undead/female/undead_femalepart2.mdl
models/character/monster/undead/female/undead_femalepart3.mdl
models/character/npc/common/skeleton/skeleton_male.mdl
models/character/npc/common/skeleton/skeleton_female.mdl
models/character/npc/unique/Downtown/Headless_Corpse/sg_head.mdl
models/character/npc/common/corpse/security_guard/sg_headless.mdl

Restored Textures:
decals/stains/puda, decals/structural/bldg261l_decala
decals/structural/phonejackb, decals/structural/shadow_peter
decals/stains/wllstaina, decals/stains/wllstainc, brick/warrarcha
ground/warrfloorb, ground/warrfloorc, ground/warrfloord
dev/dev_signflammable01a, concrete/sewflrapud, concrete/oilsewerc
stone/warrceilinga, stone/warrwllc, stone/warrwlld, stone/warrwlle

Restored Assets:
particles/demo_river_mist_emitter
sound/epic/wind.wav, sound/area/santa_monica/clinic/click3.wav


Chateau Hotel:
--------------
The chateau map was build around a modified version of the real
Chateau Marmont, using the original Troika assets listed below.

Troika Design Infos:
Brian Mitsoda wrote that "The Chateau was probably built for an 
earlier build, but was dropped as a location in the game before 
I came on board." So it might have been a prototype for both the
Ocean House hotel or Grout's Mansion. The textures and a concept
art show that is was supposed to look similar to the real one.

Restored Models:
models/scenery/life/bats/bats.mdl
models/scenery/life/weedc/weedc.mdl
models/scenery/structural/chateau/deco1.mdl
models/scenery/structural/chateau/column.mdl
models/scenery/structural/chateau/balltop.mdl
models/scenery/structural/chateau/cm_rail1.mdl
models/scenery/structural/chateau/cm_rail2.mdl
models/scenery/structural/chateau/winframe.mdl
models/scenery/structural/chateau/cm_awning1.mdl
models/scenery/structural/chateau/cm_awning2.mdl
models/scenery/structural/chateau/cm_supports.mdl
models/scenery/structural/chateau/cmarch.mdl
models/scenery/structural/chateau/cmcarch.mdl
models/scenery/structural/chateau/cm_stairs7.mdl
models/scenery/structural/chateau/cm_stairs6b.mdl
models/scenery/structural/chateau/cm_bani_top.mdl
models/scenery/structural/chateau/cm_bani_link.mdl
models/scenery/structural/chateau/cm_bani_rail.mdl
models/scenery/structural/chateau/ceilingarch.mdl
models/scenery/structural/chateauroof/chateauroof.mdl
models/scenery/furniture/Computer_New/comp_gold.mdl

Restored Textures:
models/scenery/structural/asphole/bilboardb
plaster/cmwlla, plaster/cmwllb, plaster/cmwllc, plaster/cmwlld
plaster/cmwlle, plaster/cmwllf, plaster/cmwllg, plaster/cmceilingb
plaster/cmposta, plaster/cmpostb, plaster/cmdwndwc, plaster/cmwndwd
plaster/cmdoora, plaster/cmdoorb, plaster/cmdoorc, plaster/cmdoord
plaster/cmdoore, plaster/cmdoorf, plaster/cmwndwa, plaster/cmwndwb
plaster/cmdwndwb_a, plaster/cmwndwclit, plaster/cmelevceila


Museum Entrance:
----------------
This map was enhanced because many outside textures for the museum
were found and two beta screenshot content could be recreated too.

Restored assets:
models/scenery/plants/populus/populus.mdl
models/scenery/structural/musarch/musarchext.mdl
models/scenery/street/lamppost_tall/lamppost_tall.mdl
plaster/musdoora, plaster/musdoorb, plaster/musdoord
plaster/stkdoora, brick/musdoorc, brick/muswll brick/muswllh
brick/muswlli, brick/muswllj, brick/muswllk, brick/musbalconya


Coffee Shop:
------------
This map was recreated because all other SM bus map locations can
be entered and more Chateau Marmont hotel assets were restorable.

Restored assets:
models/scenery/misc/liquor/bot1.mdl
models/scenery/misc/liquor/bot4.mdl
models/scenery/misc/clothing/clothing4.mdl
models/scenery/structural/chateau/column.mdl
models/scenery/misc/pooltablelamp/pooltablelights1.mdl
models/scenery/furniture/refrigerator/refrigeratorold_anim2x.mdl
plaster/cmwndwa, plaster/cmdoora/b/e, plaster/cmelevceila
plaster/cmwllb, plaster/cmwllc, tile/cmdoora, stone/chfloora


Smoke Shop:
-----------
This map was recreated because all other SM bus map locations can
be entered and there also were files with smokeshop in the names.

Restored assets:
models/scenery/furniture/liquorbottles/liquorbottle_1.mdl
models/scenery/furniture/diningtableoldbeachhouse/d..._new.mdl 
environmental/music/music_rock.wav, glass/glasssmokeshop
metal/brass, decals/signs/smokeshop, decals/signs/thomas
objects/flyera, objects/flyerd, objects/flyere, objects/flyerf
objects/aspbar, stone/smoketrim, wood/galfloora, wood/pierceiling


Open Gameplay Issues:
---------------------
When the patron in the Sin Bin does not leave, pay his booth once.
Occasionally Beckett stays in wolf form when meeting him, reload.
If the Odius Chalice is not working move it to the left inventory.
Loading will remove Bach's holy light effect and reset the radio.
All enemies drop only one weapon, some exit-map icons are missing.
If containers auto-close, right-click the objects to choose them.
Occasionally mailboxes do not receive rewards or objects drop out.
There is a way to exploit armors and stats, but that is a secret.
If you can't type or the Skyeline map is full of objects, restart.
Sometimes the slow down effect of Tzimisce fatguys stays, reload.
Selling too much to vendors makes goods unavailable or game crash.
Sometimes the black inside of tunnels or manholes will disappear.
If LaCroix ignores a delivered sarcophagus set G.Story_State = 60.
Feeding on rats may trigger melee mode and their bodies levitate.
Don't save or leave levels with disciplines active or on a ladder.
Blood, Health and disciplines bars sometimes freeze or disappear.
The news will not always fit to your actual actions but that's TV.
Some buildings look differently from the inside than the outside.
Occasionally enemies do not show weapons or move into solid stuff.
Ranged weapons with aggravated damage will not show a yellow bar.
Sometimes the sarcophagus will already be stored in the warehouse.
If you save and load in stealth bonus areas the effect will stay.
Sometimes you can hear rain sounds although it not actually rains.
If you pull out weapons after a taxi ride right-click on the map.
Sometimes entities will vanish being out of sight in third person.
Don't feed on quest NPCs and attack them to break feeding trance.
If game crashes when entering certain levels drop inventory items.
Sometimes unknown occult items identify only after level changes.
Visible colorful brushes means you continued an incompatible save.
Occasionally you may not be able to throw the grenade from Nines.
If a new game starts black remove all saves, or try windowed mode.


Open Technical Issues:
----------------------
When you get a SweetFX "d3d11" error rename dxgi.dll to d3d11.dll.
To get rid off the bik intro movies just rename the media folder.
Append -dxlevel 80(90) -window(fullscreen) to shortcut on crashes.
On "failed to load the launcher" error check game/patch location.
When audio is missing on HDMI set snd_surround "0" in the console.
If the mouse is missing from the menus, disable trail in windows.
On index buffer errors with ATI cards install drivers without CCC.
Use console from main menu only or type "chareditor" if it froze.
If transparency effects are broken check if onboard video is used.
To avoid crashes don't play sounds with the Windows Media Player.
If you experience random crashes turn the environmental audio off.
To avoid loosing saves don't install into standard program files.
On crashes try setting "mat_compressedtextures" "1" in config.cfg.
To fix multiple eyes on NVIDIA cards override anisotropic filter.
If controls lag or the game crashes try Win98 or XP compatibility.
Set resolution -w x -h y and use 3D-Analyze app for Intel G31/33.
The skip intro button is only available for resolutions > 800x600.
If background sounds are too low, add snd_refdist "80" to config.
To improve performance add to shortcut -heapsize x, x being RAM/2.
On runtime error remove \Python\Pythoncore\2.1\ line in registry.
If character movement feels skidding add "sv_friction" "8" to cfg.
Special dialogue fonts will only appear at resolutions > 800x600.
On low frame rate kill rain: "particles_enable_precipitation" "0".
If you experience random attacking bind attack away from "enter".
When you get a "vertex buffer" error, disable additional monitors.
On cutscenes freeze use "camera_kill", "frenzyplayer" or ALT-TAB.
If you can't read papers re-bind "use" away from the mousebuttons.
Weird water animations can be disabled using "mat_drawwater" "0".
On crashes with "violation in module Vgui2.dll" change resolution.
If dialogues are looping re-bind "use" away from any mousebutton.
"Bad inline model" error means you continued an incompatible save.


Patch Permission:
-----------------
PM to Dan Upright 27.01.2005 on Planet Vampire: If you really plan 
to do no update any more, would it be okay for me to include my 
fixes into your patch and upload it to some place like fileplanet? 
PM from Dan Upright 01.02.2005 on Planet Vampire: knock yourself 
out mate - i've been meaning to update my patch to work with the 
official 1.2 for a while now, but i don't object to passing the 
torch (i don't even have the game installed anymore) good luck 
with it and just ask if you need help with anything =]
Leonard Boyarsky in an interview by Sebastian Thor from Eurogamer 
08.2014 about the UP: "Your dedication is amazing, thank you!"


Wesp5 Projects:
---------------
Mods:
* Vampire: The Masquerade - Bloodlines Unofficial Patch
* White Gold: War in Paradise Unofficial Patch
* The Precursors Unofficial Patch
* Half-Life: Xen-Warrior
* Theme Doom Patch
Addons:
* The Dark Mod Unofficial Patch
* The Babylon Project Unofficial Patch
* Half-Life: Counter-Strike Training Addon
* Half-Life: Opposing Force Aliens Addon
* Half-Life: Uplink Addon
* Gunman Chronicles: Pistol Addon
* Gunman Chronicles: Demo Addon
* Quake 2 Plus Compilation
* Quake Plus Compilation
