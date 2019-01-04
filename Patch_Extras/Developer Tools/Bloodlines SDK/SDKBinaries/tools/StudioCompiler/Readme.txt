Studiocompiler

StudioCompiler is a third-party tool written by Cannonfodder for compiling models and materials.
Features

    Model Compiler - builds a .qc file for you for simple models, or compiles using an existing qc file. Can provide info on the reference SMD file and allows the user to replace its materials, which is useful when you forget to texture the model before export, or if you want to use the same SMD's but use a new texture.
    Material Compiler - lets you specify common VMT options without having to edit the VMT file itself. Additionally, there is no requirement for the TGA files to be in any particular directory for it to function properly.
    Model Decompiler - allows you to decompile any HL2 model, for recovery of original work or study of existing resources.
    File Export and Conversion (VMT/VTF) - the Steam browser is built-in, so there is no need to export the files before conversion. Export a material to TGA directly from the GCFs. 

2/2/2011 - Version 0.4 Released !

   Removed steam integration. Now runs anywhere !
   Removed tool integration, now calls sdk tools instead.
   Probably broke lots of decompiler features but basic operations still work and it is updated for latest SDK models.
   Added automatic image conversion using freeimage. It also supports replacing the alpha channel with a specular or glow image.

This version can run anywhere and is updated for the latest orangebox models (Version 49 models cause it to crash).

// Modified by Psycho-A for Bloodlines SDK 05.09.2018 and limitations added by wesp:

The modeling features are in Alpha state, so keep in mind these limitations:
1. The model should not contain more than 10000 polys and 25000 vertexes
2. Only static props (scenery models) are supported - no characters or weapons
3. The model should be single-boned and have only single frame on sequence
4. Collision models may crash game, use model as prop_static or turn them off!