import bpy

# === CONFIGURATION ===
input_file = r"C:/path/to/your/pixel_data.txt"  # Replace with your actual file path
voxel_size = 0.1  # Size of each cube
z_spacing = 0.2   # Space between layers (adjust if using multiple frames)

# === CLEAR EXISTING OBJECTS ===
bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.delete(use_global=False)

# === READ RGB DATA FROM FILE ===
with open(input_file, 'r') as file:
    lines = file.readlines()

# === CREATE VOXELS (CUBES) ===
for y, line in enumerate(lines):
    pixels = line.strip().split(' ')
    
    for x, pixel in enumerate(pixels):
        # Parse RGB value from the format "(R, G, B)"
        rgb = pixel.strip('()').split(',')
        r, g, b = map(int, rgb)
        
        # Normalize RGB to [0, 1] for Blender's color range
        color = (r / 255.0, g / 255.0, b / 255.0, 1.0)
        
        # Create material for the cube (Voxel)
        mat = bpy.data.materials.new(name=f"Mat_{x}_{y}")
        mat.use_nodes = True
        bsdf = mat.node_tree.nodes["Principled BSDF"]
        bsdf.inputs["Base Color"].default_value = color
        
        # Create the voxel (cube) object
        bpy.ops.mesh.primitive_cube_add(size=voxel_size, location=(x * voxel_size, -y * voxel_size, 0))
        cube = bpy.context.object
        
        # Assign material to the cube
        cube.data.materials.append(mat)

print("✅ Voxel model created from RGB data.")
