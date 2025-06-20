bl_info = {
    "name": "TKLx",
    "author": "Your Name",
    "version": (0, 3, 0),
    "blender": (3, 0, 0),
    "location": "View3D > Sidebar > TKLx",
    "description": "Quick view buttons for TKL and laptop users",
    "category": "3D View",
}

import bpy

class TKLX_OT_view_front(bpy.types.Operator):
    bl_idname = "tklx.view_front"
    bl_label = "Front View"
    bl_description = "Switch to Front View or Back View (Ctrl)"

    def execute(self, context):
        view_type = 'BACK' if getattr(self, 'reverse', False) else 'FRONT'
        for area in context.window.screen.areas:
            if area.type == 'VIEW_3D':
                for region in area.regions:
                    if region.type == 'WINDOW':
                        with context.temp_override(area=area, region=region):
                            bpy.ops.view3d.view_axis(type=view_type)
                        return {'FINISHED'}
        return {'CANCELLED'}

    def invoke(self, context, event):
        self.reverse = event.ctrl
        return self.execute(context)

class TKLX_OT_view_left(bpy.types.Operator):
    bl_idname = "tklx.view_left"
    bl_label = "Left View"
    bl_description = "Switch to Left View or Right View (Ctrl)"

    def execute(self, context):
        view_type = 'RIGHT' if getattr(self, 'reverse', False) else 'LEFT'
        for area in context.window.screen.areas:
            if area.type == 'VIEW_3D':
                for region in area.regions:
                    if region.type == 'WINDOW':
                        with context.temp_override(area=area, region=region):
                            bpy.ops.view3d.view_axis(type=view_type)
                        return {'FINISHED'}
        return {'CANCELLED'}

    def invoke(self, context, event):
        self.reverse = event.ctrl
        return self.execute(context)

class TKLX_OT_view_top(bpy.types.Operator):
    bl_idname = "tklx.view_top"
    bl_label = "Top View"
    bl_description = "Switch to Top View or Bottom View (Ctrl)"

    def execute(self, context):
        view_type = 'BOTTOM' if getattr(self, 'reverse', False) else 'TOP'
        for area in context.window.screen.areas:
            if area.type == 'VIEW_3D':
                for region in area.regions:
                    if region.type == 'WINDOW':
                        with context.temp_override(area=area, region=region):
                            bpy.ops.view3d.view_axis(type=view_type)
                        return {'FINISHED'}
        return {'CANCELLED'}

    def invoke(self, context, event):
        self.reverse = event.ctrl
        return self.execute(context)

class TKLX_OT_view_cam_or_render(bpy.types.Operator):
    bl_idname = "tklx.view_cam_or_render"
    bl_label = "Cam/Render View"
    bl_description = "Switch to Camera View or Render (Ctrl)"

    def execute(self, context):
        show_render = getattr(self, 'show_render', False)
        if show_render:
            # This triggers the same as pressing F12 (single frame render)
            bpy.ops.render.render('INVOKE_DEFAULT')
            return {'FINISHED'}
        else:
            for area in context.window.screen.areas:
                if area.type == 'VIEW_3D':
                    for region in area.regions:
                        if region.type == 'WINDOW':
                            with context.temp_override(area=area, region=region):
                                bpy.ops.view3d.view_camera()
                            return {'FINISHED'}
        return {'CANCELLED'}

    def invoke(self, context, event):
        self.show_render = event.ctrl
        return self.execute(context)

class TKLX_PT_ViewPanel(bpy.types.Panel):
    bl_label = "TKLx View Shortcuts"
    bl_idname = "TKLX_PT_viewpanel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "TKLx"

    def draw(self, context):
        layout = self.layout
        layout.label(text="Quick View Buttons:")
        col = layout.column(align=True)
        row1 = col.row(align=True)
        row1.operator("tklx.view_front", text="Front")
        row1.operator("tklx.view_left", text="Left")
        row2 = col.row(align=True)
        row2.operator("tklx.view_top", text="Top")
        row2.operator("tklx.view_cam_or_render", text="Cam")
        # Add a third row with empty buttons for symmetry, or add more functions if desired
        row3 = col.row(align=True)
        row3.label(text="")
        row3.label(text="")

classes = (
    TKLX_OT_view_front,
    TKLX_OT_view_left,
    TKLX_OT_view_top,
    TKLX_OT_view_cam_or_render,
    TKLX_PT_ViewPanel,
)

def register():
    for cls in classes:
        bpy.utils.register_class(cls)

def unregister():
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)

if __name__ == "__main__":
    register()
