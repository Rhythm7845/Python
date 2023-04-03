#Importing the libraries.
import numpy as np
import matplotlib.pyplot as plt

#Function to normalise a vector.

def normalise(vector):
    return vector / np.linalg.norm(vector)

#Calculates the sign disatance function of a sphere for ray intersection.

def sphere_intersect(center, radius, ray_origin, ray_direction):
    b = 2 * np.dot(ray_direction, ray_origin - center)
    c = np.linalg.norm(ray_origin - center) ** 2 - radius ** 2
    delta = b ** 2 - 4 * c
    if delta > 0:
        t1 = (-b + np.sqrt(delta)) / 2
        t2 = (-b - np.sqrt(delta)) / 2
        if t1 > 0 and t2 > 0:
            return min(t1, t2)
    return None

#Goes through all the spheres in the scene to find the nearest one to the ray.

def nearest_intersected_object(objects, ray_origin, ray_direction):
    distances = [sphere_intersect(obj['center'], obj['radius'], ray_origin, ray_direction) for obj in objects]
    nearest_object = None
    min_distance = np.inf
    for index, distance in enumerate(distances):
        if distance and distance < min_distance:
            min_distance = distance
            nearest_object = objects[index]
    return nearest_object, min_distance

#Defining Screen size.

width = 640
height = 480

#Defining camera and screen.

camera = np.array([0,0,1])
ratio = float(width/height)
screen = (-1,1/ratio,1,-1/ratio) #Sccreen perfectly fits the camera.

#Declares Scene Objects.

objects = [
    { 'center': np.array([-0.2, 0, -1]), 'radius': 0.7, 'ambient': np.array([0.1, 0, 0]), 'diffuse': np.array([0.7, 0, 0]), 'specular': np.array([1, 1, 1]), 'roughness': 100, 'reflection': 0.1 },
    { 'center': np.array([0, -9000, 0]), 'radius': 9000 - 0.7, 'ambient': np.array([0.1, 0.1, 0.1]), 'diffuse': np.array([0.6, 0.6, 0.6]), 'specular': np.array([1, 1, 1]), 'roughness': 100, 'reflection': 0.1 }
]
#Declaes the lights in the scene.
light = { 'position': np.array([-10, -10, -10]), 'ambient': np.array([1, 1, 1]), 'diffuse': np.array([1, 1, 1]), 'specular': np.array([1, 1, 1]) }

#Main RayTracing loop.
image = np.zeros((height,width,3))
for i,y in enumerate(np.linspace(screen[1], screen[3], height)):
    for j,x in enumerate(np.linspace(screen[0], screen[2], width)):
        pixel = np.array([x,y,0])
        origin = camera
        direction = normalise(pixel - origin)
        nearest_object, min_distance = nearest_intersected_object(objects, origin, direction)
        if nearest_object is None:
            continue
        intersection = origin + min_distance * direction
        normal_to_surface = normalise(intersection - nearest_object['center'])
        shifted_point = intersection + 1e-5 * normal_to_surface
        intersection_to_light = normalise(light['position'] - shifted_point)
        _, min_distance = nearest_intersected_object(objects, shifted_point, intersection_to_light)
        intersection_to_light_distance = np.linalg.norm(light['position'] - intersection)
        is_shadowed = min_distance < intersection_to_light_distance
        if is_shadowed:
            continue
        illumination = np.zeros((3))
        illumination += nearest_object['ambient'] * light['ambient']
        illumination += nearest_object['diffuse'] * light['diffuse'] * np.dot(intersection_to_light, normal_to_surface)
        intersection_to_camera = normalise(camera - intersection)
        H = normalise(intersection_to_light + intersection_to_camera)
        illumination += nearest_object['specular'] * light['specular'] * np.dot(normal_to_surface, H) ** (nearest_object['roughness'] / 4)
        image[i, j] = np.clip(illumination, 0, 1)
        
    print("Progress: %d / %d rows." % (i + 1, height))
        
plt.imsave("render.png", image) #Saves the final render.