'''
TEMP NOTES:

In unreal the directory layout is "/All/Content/..." whereas in python we specify it as "/Game/...". 
 Really confusing and annoying, but that's life.

U:\BA_UE5\04_production\02_3d\01_maya\scenes\01_assets\01_props\decorations\artwork\anatomyPoster_var01\02_published


command to get the path of the project on your drive:
    unreal.Paths.get_project_file_path()

Regex expression to get the folder name of the project on your drive:
unreal_project_name = re.search('[^/][\w]*(?=.uproject)', unreal_project_path)


'''


'''
Filename: asset_material_importer.py

This script aims to import static meshses and their materials into unreal whilst automatically assigning them into newly created material instances

'''



import unreal
import re
from pathlib import Path

# Tempory hard coded in location of files etc on U drive. Please sitch to Tu's C:\PZ\00_Pipeline\PZ_Workspaces.json eventually.
project_locations = {'BA': {'maya_location': r'U:\BA_UE5\04_production\02_3d\01_maya\scenes'}, 'BZ': {'maya_location': r'U:\BZ_UE5\04_production\02_3d\01_maya\scenes'}}

filetype_whitelist = ['*.tga']


# This function runs everything to import assets
def importFunc(selected_ue_asset_filepath):
    
    print(f'Python: Running import function...')
    
    global unreal_project_name
    global project_uproject_location
    global project_location_on_disk 
    global filetype_whitelist
   
    # Adjust the filepaths to ensure the path to the select asset is correct
    asset_filepath_adjusted = re.split('^/\w+[^/]', selected_ue_asset_filepath)[-1]
    asset_filepath_adjusted = re.split('[^/]\w+.\w+$', asset_filepath_adjusted)[-2]
    asset_location_on_disk = f'{project_location_on_disk}Content{asset_filepath_adjusted}'

    print(f'Python reports selected mesh path is: {selected_ue_asset_filepath}')
    print(f'Python reports project location fixed: {project_location_on_disk}')
    print(f'Python reports the selected asset filepath on disk: {asset_location_on_disk}')

    #Find the texture files in the folder where the asset is located on disk
    for file_loop in filetype_whitelist:
        # Finds files in the asset location stepping through every filetype in the filetype whitelist
        for i in Path(asset_location_on_disk).rglob(file_loop):
            if i == 0:
                print("No images found!!! ;(")
                break
            else:
                print('images found')
                print(i)
                pass


def main():

    print("python script running normally")

    unreal_project_name = unreal.SystemLibrary.get_game_name()
    project_uproject_location = unreal.Paths.get_project_file_path()
    project_location_on_disk = re.split('[^/]\w+.\w+$', project_uproject_location)[-2]

    print(f'Python reports the unreal project name is: {unreal_project_name}')
    print(f'Python reports uproject location: {project_uproject_location}')

main()

'''
    for i in project_locations:
        if unreal_project_name = project_locations[i]:
            current_path = project_locations[i]['maya_location']
'''


'''
#################
# Import assets #
#################


# Source image
image = "D:/PZWorkspace/unreal_testing_svn/Script/Ganshtyn.png"

# Grabs the presetup task and then passes it to the executeImportTask function to import that task into the engine.
def importMyAssets():
    print('Running importMyAssets')
    texture_task = buildImportTask(image, '/Game/textures/import_tool_testing')
    executeImportTasks([texture_task])

# Setup the importing options and make it into a task
def buildImportTask(filename, destination_path):
    print('Running import_asset')
    task = unreal.AssetImportTask()
    task.set_editor_property('automated', True)
    task.set_editor_property('destination_name', '')
    task.set_editor_property('destination_path', destination_path)
    task.set_editor_property('filename', filename)
    task.set_editor_property('replace_existing', True)
    task.set_editor_property('save', False)
    print("task", task, "filename" ,task.get_editor_property('filename'))
    return task

# This is the part that actually imports it into unreal
def executeImportTasks(tasks):
    print('Running executeImportTasks')
    unreal.AssetToolsHelpers.get_asset_tools().import_asset_tasks(tasks)

##################################
# Create assets in unreal engine #
##################################

#def createGenericAsset(asset_path='', unique_name=True, asset_class=None, asset_factory=None):
#    return unreal.AssetToolsHelpers.get_asset_tools().create_asset(asset_name=name, package_path=path, asset_class
#    if unique_name:
#        asset_path, asset_name = unreal.AssetToolsHelpers.get_asset_tools().create_unique_asset_name(base_package_name=asset_path, suffix='')
#    if not unreal.EditorAssetLIbrary.does_asset_exist(asset_path=asset_path):
#        path = asset_path.rsplit('/', 1)[0]
#        name = asset_path.rsplit('/', 1)[1]
#        return unreal.AssetToolsHelpers.get_asset_tools().create_asset(asset_name=name, package_path=path, asset_class
#    return unreal.load_asset(asset_path)


#def createGenericAsset_EXAMPLE():
#    base_path = '/Game/textures/import_tool_testing'
#    generic_assets = [[base_path + 'material', unreal.Material, unreal.MaterialFactoryNew()]]
#    for asset in generic_assets:
#        print createGenericAsset(asset[0], True, asset[1], asset[2])
#        print createGenericAsset(base_path + 'material', unreal.Material, unreal.MaterialFactoryNew())
#    createGenericAsset(base_path + 'ashtyn_mat', True, unreal.Material, unreal.MaterialFactoryNew())
'''




# learn to:
###########################################
# import static meshes: static mesh import task, or AssetImportTask


#unreal.MaterialInstanceConstantFactoryNew
