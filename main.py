import bpy
import bmesh as bmesh
import mathutils
import sys

PLATE_CENTER = mathutils.Vector((128, 128, 0))
OUTPUT_PATH = sys.argv[-1]
INPUT_PATH = sys.argv[-2]

def clear_scene():
    bpy.ops.object.select_all(action='SELECT')
    bpy.ops.object.delete()

def get_convex_hull_data(obj):
    me = obj.data
    bm = bmesh.new()
    bm.from_mesh(me)

    bmesh.ops.transform(bm, matrix=obj.matrix_world, verts=bm.verts)
    bmesh.ops.convex_hull(bm, input=bm.verts)

    return bm

def find_optimal_orientation(obj):
    bm = get_convex_hull_data(obj)
    best_face = None
    max_area = -1.0

    # Check all tha faces
    for face in bm.faces:
        # Find the largest area
        area = face.calc_area()
        if area > max_area:
            max_area = area
            best_face = face

    if not best_face:
        print("Failed to find optimal orientation :(")
        bm.free()
        return None

    face_normal = best_face.normal.copy()
    target_vector = mathutils.Vector((0, 0, -1))
    rotation_quaternion = face_normal.rotation_difference(target_vector)

    bm.free()

    return rotation_quaternion.to_matrix().to_4x4()


def apply_orientation_n_translation(obj):
    print(f"Obtaining best orientation for {obj.name}")
    rot_matrix = find_optimal_orientation(obj)

    if rot_matrix:
        obj.matrix_world = rot_matrix @ obj.matrix_world
        print("Applied rotation based on convex hull analysis")

    bpy.context.view_layer.update()

    bbox_corners = [obj.matrix_world @ mathutils.Vector(corner) for corner in obj.bound_box]
    min_z = min([v.z for v in bbox_corners])

    obj.location.z = -min_z

    bpy.context.view_layer.update()

    local_bbox_center = 0.125 * sum((mathutils.Vector(b) for b in obj.bound_box), mathutils.Vector())
    world_bbox_center = obj.matrix_world @ local_bbox_center

    offset_x = PLATE_CENTER.x - world_bbox_center.x
    offset_y = PLATE_CENTER.y - world_bbox_center.y

    obj.location.x += offset_x
    obj.location.y += offset_y

    print(f"Obj centered at {PLATE_CENTER}. Location is {obj.location}")


# min zs
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

    bpy.ops.wm.stl_import(filepath=INPUT_PATH)

    obj = bpy.context.selected_objects[0]
    apply_orientation_n_translation(obj)

    bpy.ops.wm.stl_export(filepath=OUTPUT_PATH)

    print("Orientation pipeline finished. Check results to validate correctness.")


if __name__ == '__main__':
    main()