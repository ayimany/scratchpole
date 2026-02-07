import bpy
import mathutils
import os
import sys

PLATE_CENTER = (128, 128, 0)
OUTPUT_PATH = sys.argv[-1]
INPUT_PATH = sys.argv[-2]

def clear_scene():
    bpy.ops.object.select_all(action='SELECT')
    bpy.ops.object.delete()

def transform_object_to_center(obj):
    bpy.ops.object.origin_set(type='ORIGIN_GEOMETRY', center='BOUNDS')

    bbox_corners = [obj.matrix_world @ mathutils.Vector(corner) for corner in obj.bound_box]

    min_z = min([v.z for v in bbox_corners])
    obj.location.z = -min_z

    bpy.ops.object.origin_set(type='ORIGIN_GEOMETRY', center='BOUNDS')
    obj.location.x = PLATE_CENTER[0]
    obj.location.y = PLATE_CENTER[1]

    bpy.ops.object.transform_apply(location=True, rotation=True, scale=True)


def main():
    clear_scene()
    bpy.ops.import_mesh.stl(filepath=INPUT_PATH)
    obj = bpy.context.selected_objects[0]
    transform_object_to_center(obj)
    bpy.ops.export_mesh.stl(filepath=OUTPUT_PATH)


if __name__ == '__main__':
    main()