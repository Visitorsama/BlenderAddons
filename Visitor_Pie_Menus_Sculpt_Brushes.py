# ##### BEGIN GPL LICENSE BLOCK #####
#
#  This program is free software; you can redistribute it and/or
#  modify it under the terms of the GNU General Public License
#  as published by the Free Software Foundation; either version 2
#  of the License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software Foundation,
#  Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
#
# ##### END GPL LICENSE BLOCK #####

# <pep8-80 compliant>

bl_info = {
    "name": "Visitor Pie Menu Sculpt Brushes",
    "description": "Brushes pie menus",
    "author": "Visitorsama",
    "version": (0, 1),
    "blender": (2, 82, 0),
    "location": "Sculpt Mode>1,2,3,4,5",
    "support": "TESTING",
    "category": "3D View",
}
import bpy
import os
from bpy.types import Menu

addon_keymaps = []
brush_icons = {}
brush_icons2 = {}

def create_icons():
    global brush_icons
    icons_directory = bpy.utils.system_resource('DATAFILES', "icons")
    brushes = ["crease", "blob", "smooth", "draw", "draw_sharp", "clay", "clay_strips", "inflate", "grab",
        "nudge", "thumb", "snake_hook", "rotate", "flatten", "scrape", "multiplane_scrape", "fill", "pinch",
        "layer", "mask", "elastic_deform", "pose", "simplify"]
    for brush in brushes:
        filename = os.path.join(icons_directory, f"brush.sculpt.{brush}.dat")
        icon_value = bpy.app.icons.new_triangles_from_file(filename)
        brush_icons[brush] = icon_value

def create_icons2():
    global brush_icons2
    icons_directory = bpy.utils.system_resource('DATAFILES', "icons")
    brushes = ["draw", "draw.eraser", "draw.line", "draw.poly"]
    for brush in brushes:
        filename = os.path.join(icons_directory, f"ops.gpencil.{brush}.dat")
        icon_value = bpy.app.icons.new_triangles_from_file(filename)
        brush_icons2[brush] = icon_value

def release_icons():
    global brush_icons
    for value in brush_icons.values():
        bpy.app.icons.release(value)

class VIEW3D_MT_pie_mask_1(Menu):
    bl_label = "Mask Edit 1"
    bl_idname = "VIEW3D_MT_pie_mask_1"
    bl_space_type = 'SCULPT'

    def draw(self, _context):
        layout = self.layout
        pie = layout.menu_pie()

        op = pie.operator("paint.mask_flood_fill", text='Invert Mask', icon="BLENDER")
        op.mode = 'INVERT'
        op = pie.operator("paint.mask_flood_fill", text="Fill Mask", icon="BLENDER")
        op.mode = 'VALUE'
        op.value = 1
        op = pie.operator("paint.mask_flood_fill", text='Clear Mask', icon="BLENDER")
        op.mode = 'VALUE'
        op.value = 0
        op = pie.operator("view3d.select_box", text="Box Mask", icon="BLENDER")
        op = pie.operator("paint.mask_lasso_gesture", text="Lasso Mask", icon="BLENDER")
        
class VIEW3D_MT_pie_mask_2(Menu):
    bl_label = "Mask Edit 2"
    bl_idname = "VIEW3D_MT_pie_mask_2"
    bl_space_type = 'SCULPT'

    def draw(self, _context):
        layout = self.layout
        pie = layout.menu_pie()

        op = pie.operator("sculpt.mask_filter", text='Smooth Mask', icon="BLENDER")
        op.filter_type = 'SMOOTH'
        op.auto_iteration_count = True
        op = pie.operator("sculpt.mask_filter", text='Sharpen Mask', icon="BLENDER")
        op.filter_type = 'SHARPEN'
        op.auto_iteration_count = True
        op = pie.operator("sculpt.mask_filter", text='Grow Mask', icon="BLENDER")
        op.filter_type = 'GROW'
        op.auto_iteration_count = True
        op = pie.operator("sculpt.mask_filter", text='Shrink Mask', icon="BLENDER")
        op.filter_type = 'SHRINK'
        op.auto_iteration_count = True
        op = pie.operator("sculpt.mask_filter", text='Increase Contrast', icon="BLENDER")
        op.filter_type = 'CONTRAST_INCREASE'
        op.auto_iteration_count = False
        op = pie.operator("sculpt.mask_filter", text='Decrease Contrast', icon="BLENDER")
        op.filter_type = 'CONTRAST_DECREASE'
        op.auto_iteration_count = False

class VIEW3D_MT_pie_mask_3(Menu):
    bl_label = "Mask Edit 3"
    bl_idname = "VIEW3D_MT_pie_mask_3"
    bl_space_type = 'SCULPT'

    def draw(self, _context):
        layout = self.layout
        pie = layout.menu_pie()
        
        op = pie.operator("sculpt.mask_filter", text='Smooth Mask', icon="BLENDER")
        op.filter_type = 'SMOOTH'
        op.auto_iteration_count = True
        op = pie.operator("sculpt.mask_expand", text="Expand Mask By Topology", icon="BLENDER")
        op.use_normals = False
        op.keep_previous_mask = False
        op.invert = True
        op.smooth_iterations = 2
        op = pie.operator("sculpt.mask_expand", text="Expand Mask By Curvature", icon="BLENDER")
        op.use_normals = True
        op.keep_previous_mask = True
        op.invert = False
        op.smooth_iterations = 0
        op = pie.operator("mesh.paint_mask_extract", text="Mask Extract", icon="BLENDER")
        op = pie.operator("mesh.paint_mask_slice", text="Mask Slice", icon="BLENDER")
        op.fill_holes = False
        op.new_object = False
        op = pie.operator("mesh.paint_mask_slice", text="Mask Slice and Fill Holes", icon="BLENDER")
        op.new_object = False
        op = pie.operator("mesh.paint_mask_slice", text="Mask Slice to New Object", icon="BLENDER")
        op = pie.operator("sculpt.dirty_mask", text='Dirty Mask', icon="BLENDER")

class VIEW3D_MT_pie_mask_4(Menu):
    bl_label = "Mask Edit 4"
    bl_idname = "VIEW3D_MT_pie_mask_4"
    bl_space_type = 'SCULPT'

    def draw(self, _context):
        layout = self.layout
        pie = layout.menu_pie()

        op = pie.operator("sculpt.mask_filter", text='Smooth Mask', icon="BLENDER")
        op.filter_type = 'SMOOTH'
        op.auto_iteration_count = True
        op = pie.operator("paint.hide_show", text="Show All", icon="BLENDER")
        op.action = 'SHOW'
        op.area = 'ALL'
        op = pie.operator("paint.hide_show", text="Show Bounding Box", icon="BLENDER")
        op.action = 'SHOW'
        op.area = 'INSIDE'
        op = pie.operator("paint.hide_show", text="Hide Bounding Box", icon="BLENDER")
        op.action = 'HIDE'
        op.area = 'INSIDE'
        op = pie.operator("paint.hide_show", text="Hide Masked", icon="BLENDER")
        op.action = 'HIDE'
        op.area = 'MASKED'
        pie.menu("VIEW3D_MT_sculpt_set_pivot", text="Set Pivot", icon="BLENDER")

class VIEW3D_MT_pie_brushes_1(Menu):
    bl_label = "Blue Brushes"
    bl_description = "This brushes are for adding and subtracting volume to the mesh"
    bl_idname = "VIEW3D_MT_pie_brushes_1"
    bl_space_type = 'SCULPT'

    def draw(self, _context):
        global brush_icons
        layout = self.layout
        pie = layout.menu_pie()
        pie.scale_y = 1.2
        
        op = pie.operator("paint.brush_select", text='    Inflate', icon_value=brush_icons["inflate"])
        op.sculpt_tool = 'INFLATE'
        op = pie.operator("paint.brush_select", text='    Draw Sharp', icon_value=brush_icons["draw_sharp"])
        op.sculpt_tool = 'DRAW_SHARP'
        op = pie.operator("paint.brush_select", text='    Clay Strips', icon_value=brush_icons["clay_strips"])
        op.sculpt_tool = 'CLAY_STRIPS'
        op = pie.operator("paint.brush_select", text='    Crease', icon_value=brush_icons["crease"])
        op.sculpt_tool = 'CREASE'
        op = pie.operator("paint.brush_select", text='    Blob', icon_value=brush_icons["blob"])
        op.sculpt_tool = 'BLOB'
        op = pie.operator("paint.brush_select", text='    Draw', icon_value=brush_icons["draw"])
        op.sculpt_tool = 'DRAW'
        op = pie.operator("paint.brush_select", text='    Layer', icon_value=brush_icons["layer"])
        op.sculpt_tool = 'LAYER'
        op = pie.operator("paint.brush_select", text='    Clay', icon_value=brush_icons["clay"])
        op.sculpt_tool = 'CLAY'

class VIEW3D_MT_pie_brushes_2(Menu):
    bl_label = "Red Brushes"
    bl_description = "This brushes are for increasing and decreasing contrast in diferent ways"
    bl_idname = "VIEW3D_MT_pie_brushes_2"
    bl_space_type = 'SCULPT'

    def draw(self, _context):
        global brush_icons
        layout = self.layout
        pie = layout.menu_pie()
        pie.scale_y = 1.2

        op = pie.operator("paint.brush_select", text='    Smooth', icon_value=brush_icons["smooth"])
        op.sculpt_tool = 'SMOOTH'
        op = pie.operator("paint.brush_select", text='    Flatten', icon_value=brush_icons["flatten"])
        op.sculpt_tool = 'FLATTEN'
        op = pie.operator("paint.brush_select", text='    Fill', icon_value=brush_icons["fill"])
        op.sculpt_tool = 'FILL'
        op = pie.operator("paint.brush_select", text='    Scrape', icon_value=brush_icons["scrape"])
        op.sculpt_tool = 'SCRAPE'
        op = pie.operator("paint.brush_select", text='    Multiplane Scrape', icon_value=brush_icons["multiplane_scrape"])
        op.sculpt_tool = 'MULTIPLANE_SCRAPE'

class VIEW3D_MT_pie_brushes_3(Menu):
    bl_label = "Yellow Brushes"
    bl_description = "This brushes are for grabing behavior"
    bl_idname = "VIEW3D_MT_pie_brushes_3"
    bl_space_type = 'SCULPT'

    def draw(self, _context):
        global brush_icons
        layout = self.layout
        pie = layout.menu_pie()
        pie.scale_y = 1.2
        op = pie.operator("paint.brush_select", text='    Pinch', icon_value=brush_icons["pinch"])
        op.sculpt_tool = 'PINCH'
        op = pie.operator("paint.brush_select", text='    Grab',      icon_value=brush_icons["grab"])
        op.sculpt_tool = 'GRAB'
        op = pie.operator("paint.brush_select", text='    Nudge',     icon_value=brush_icons["nudge"])
        op.sculpt_tool = 'NUDGE'
        op = pie.operator("paint.brush_select", text='    Thumb',     icon_value=brush_icons["thumb"])
        op.sculpt_tool = 'THUMB'
        op = pie.operator("paint.brush_select", text='    Snakehook', icon_value=brush_icons["snake_hook"])
        op.sculpt_tool = 'SNAKE_HOOK'
        op = pie.operator("paint.brush_select", text='    Rotate',    icon_value=brush_icons["rotate"])
        op.sculpt_tool = 'ROTATE'
        op = pie.operator("paint.brush_select", text='    Elastic Deform',    icon_value=brush_icons["elastic_deform"])
        op.sculpt_tool = 'ELASTIC_DEFORM'
        op = pie.operator("wm.tool_set_by_id", text='    Pose',  icon_value=brush_icons["pose"],)
        op.name='builtin_brush.Pose'

class VIEW3D_MT_pie_brushes_4(Menu):
    bl_label = "Gray Brushes"
    bl_description = "This brushes are for grabing behavior"
    bl_idname = "VIEW3D_MT_pie_brushes_4"
    bl_space_type = 'SCULPT'

    def draw(self, _context):
        global brush_icons
        layout = self.layout
        pie = layout.menu_pie()
        pie.scale_y = 1.2
        op = pie.operator("wm.tool_set_by_id", text='    Simplify',  icon_value=brush_icons["simplify"],)
        op.name='builtin_brush.Simplify'
        op = pie.operator("wm.tool_set_by_id", text='    Mask',  icon_value=brush_icons["mask"],)
        op.name='builtin_brush.Mask'
        op = pie.operator("wm.tool_set_by_id", text='    Slide Relax', icon_value=995,)
        op.name='builtin_brush.Slide Relax'
        op = pie.operator("wm.tool_set_by_id", text='    Box Mask', icon_value=998,)
        op.name='builtin.box_mask'
        op = pie.operator("wm.tool_set_by_id", text='    Box Hide', icon_value=999,)
        op.name='builtin.box_hide'
        op = pie.operator("wm.tool_set_by_id", text='    Mesh Filter', icon_value=1000,)
        op.name='builtin.mesh_filter'

class VIEW3D_MT_pie_brushes_5(Menu):
    bl_label = "Sculpt 5"
    bl_idname = "VIEW3D_MT_pie_brushes_5"
    bl_space_type = 'SCULPT'

    def draw(self, _context):
        layout = self.layout
        pie = layout.menu_pie()
        pie.scale_y = 1.2
        op = pie.operator("wm.tool_set_by_id", text='    Move', icon_value=968,)
        op.name='builtin.move'
        op = pie.operator("wm.tool_set_by_id", text='    Rotate', icon_value=969,)
        op.name='builtin.rotate'
        op = pie.operator("wm.tool_set_by_id", text='    Scale', icon_value=970,)
        op.name='builtin.scale'
        op = pie.operator("wm.tool_set_by_id", text='    Transform', icon_value=971,)
        op.name='builtin.transform'
        pie.separator()
        pie.separator()
        pie.separator()
        pie.menu(VIEW3D_MT_brushes_6.bl_idname, text="    Annotate", icon_value=972)

class VIEW3D_MT_brushes_6(Menu):
    bl_label = "Annotate"
    bl_idname = "VIEW3D_MT_brushes_6"
    bl_space_type = 'SCULPT'

    def draw(self, _context):
        global brush_icons2
        layout = self.layout
        layout.scale_y = 1.5
        op = layout.operator("wm.tool_set_by_id", text='    Annotate',         icon_value=brush_icons2["draw"],)
        op.name='builtin.annotate'
        op = layout.operator("wm.tool_set_by_id", text='    Annotate Line',    icon_value=brush_icons2["draw.line"],)
        op.name='builtin.annotate_line'
        op = layout.operator("wm.tool_set_by_id", text='    Annotate Polygon', icon_value=brush_icons2["draw.poly"],)
        op.name='builtin.annotate_polygon'
        op = layout.operator("wm.tool_set_by_id", text='    Annotate Eraser',  icon_value=brush_icons2["draw.eraser"],)
        op.name='builtin.annotate_eraser'

kmi_defs = (
    #(identifier,          key,    action,  CTRL, SHIFT,  ALT,   props,                                            nicename)
    ('wm.call_menu_pie', 'ONE',   'PRESS', False, False, True,  (('name', VIEW3D_MT_pie_mask_1.bl_idname),), "Nice Name 01"),
    ('wm.call_menu_pie', 'TWO',   'PRESS', False, False, True,  (('name', VIEW3D_MT_pie_mask_2.bl_idname),), "Nice Name 02"),
    ('wm.call_menu_pie', 'THREE', 'PRESS', False, False, True,  (('name', VIEW3D_MT_pie_mask_3.bl_idname),), "Nice Name 03"),
    ('wm.call_menu_pie', 'FOUR',  'PRESS', False, False, True,  (('name', VIEW3D_MT_pie_mask_4.bl_idname),), "Nice Name 04"),
    ('wm.call_menu_pie', 'ONE',   'PRESS', False, False, False, (('name', VIEW3D_MT_pie_brushes_1.bl_idname),), "Nice Name 05"),
    ('wm.call_menu_pie', 'TWO',   'PRESS', False, False, False, (('name', VIEW3D_MT_pie_brushes_2.bl_idname),), "Nice Name 06"),
    ('wm.call_menu_pie', 'THREE', 'PRESS', False, False, False, (('name', VIEW3D_MT_pie_brushes_3.bl_idname),), "Nice Name 07"),
    ('wm.call_menu_pie', 'FOUR',  'PRESS', False, False, False, (('name', VIEW3D_MT_pie_brushes_4.bl_idname),), "Nice Name 08"),
    ('wm.call_menu_pie', 'FIVE',  'PRESS', False, False, False, (('name', VIEW3D_MT_pie_brushes_5.bl_idname),), "Nice Name 09"),
)

def add_hotkey():
    addon_keymaps.clear()
    kc = bpy.context.window_manager.keyconfigs.addon
    km = kc.keymaps.new(name='Sculpt')
    for (identifier, key, action, CTRL, SHIFT, ALT, props, nicename) in kmi_defs:
        kmi = km.keymap_items.new(identifier, key, action, ctrl=CTRL, shift=SHIFT, alt=ALT)
        if props:
            for prop, value in props:
                setattr(kmi.properties, prop, value)
        addon_keymaps.append((km, kmi))

def remove_hotkey():
    for km, kmi in addon_keymaps:
        km.keymap_items.remove(kmi)
    addon_keymaps.clear()

classes = (
    VIEW3D_MT_pie_mask_1,
    VIEW3D_MT_pie_mask_2,
    VIEW3D_MT_pie_mask_3,
    VIEW3D_MT_pie_mask_4,
    VIEW3D_MT_pie_brushes_1,
    VIEW3D_MT_pie_brushes_2,
    VIEW3D_MT_pie_brushes_3,
    VIEW3D_MT_pie_brushes_4,
    VIEW3D_MT_pie_brushes_5,
    VIEW3D_MT_brushes_6,
)

def register():
    create_icons()
    create_icons2()
    from bpy.utils import register_class
    for cls in classes:
        register_class(cls)

    add_hotkey()

def unregister():
    release_icons()
    from bpy.utils import unregister_class
    for cls in classes:
        unregister_class(cls)
    
    remove_hotkey()

if __name__ == "__main__":
    from bpy.utils import register_class
    for cls in classes:
        register_class(cls)




