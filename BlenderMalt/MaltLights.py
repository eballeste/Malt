# Copyright (c) 2020 BlenderNPR and contributors. MIT license. 

import math
import bpy

class MaltLight(bpy.types.PropertyGroup):

    def sync_data(self, context):
        light = self.id_data
        light.color = self.color
        #light.shadow_soft_size = self.radius
        if light.type == 'SPOT':
            light.cutoff_distance = self.radius
            light.spot_size = self.spot_angle
            light.spot_blend = self.spot_blend_angle / self.spot_angle

    color : bpy.props.FloatVectorProperty(
        name='Color',
        default=(1,1,1),
        subtype='COLOR',
        update=sync_data,
    )
    radius : bpy.props.FloatProperty(
        name='Radius',
        default=5,
        update=sync_data,
    )
    spot_angle : bpy.props.FloatProperty(
        name='Angle',
        default=1,
        subtype='ANGLE',
        min=0,
        max=math.pi,
        update=sync_data,
    )
    spot_blend_angle : bpy.props.FloatProperty(
        name='Blend',
        default=0.1,
        subtype='ANGLE',
        min=0,
        max=math.pi,
        update=sync_data,
    )

    def draw_ui(self, layout):
        layout.prop(self, 'color')
        if self.id_data.type != 'SUN':
            layout.prop(self, 'radius')
        if self.id_data.type == 'SPOT':
            layout.prop(self, 'spot_angle')
            layout.prop(self, 'spot_blend_angle')

classes = [
    MaltLight
]

def register():
    for _class in classes: bpy.utils.register_class(_class)
    bpy.types.Light.malt = bpy.props.PointerProperty(type=MaltLight)

def unregister():
    for _class in reversed(classes): bpy.utils.unregister_class(_class)
    del bpy.types.Light.malt
