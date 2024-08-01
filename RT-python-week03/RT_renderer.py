# renderer class

import RT_utility as rtu
import numpy as np
from PIL import Image as im
import RT_pbar

def find_intersection(rGen_ray, iInterval):

    #(1.),(2.) Edit codes here 
    t = 1.5
    iInterval = [rtu.Interval(-3.0+i*8,3.0+i*8) for i in range(3)]
    # iInterval = rtu.Interval(-3.0+t,3.0+t)
    for i in iInterval:
        if (i.surrounds(rGen_ray.at(t).x())):
            if (i.surrounds(rGen_ray.at(t).y())):
                return True
        t+=0.5
    return False

def background_color(rGen_ray):
    unit_direction = rtu.Vec3.unit_vector(rGen_ray.getDirection())
    a = (unit_direction.y() + 1.0)*0.5
    return rtu.Color(1,1,1)*(1.0-a) + rtu.Color(0.5, 0.7, 1.0)*a

def get_color(rGen_ray):

    found_hit = find_intersection(rGen_ray, rtu.Interval(-3.0,3.0))
    if found_hit == True:
        return rtu.Color(1,0,0)

    return background_color(rGen_ray)

class Renderer():

    def __init__(self, cCamera) -> None:

        self.camera = cCamera
        pass

    def render(self):
        renderbar = RT_pbar.start_animated_marker(self.camera.img_height*self.camera.img_width)
        k = 0
        for j in range(self.camera.img_height):
            for i in range(self.camera.img_width):

                pixel_color = rtu.Color(0,0,0)
                # (1.),(2.)shoot a ray at the pixel center
                # generated_ray = self.camera.get_center_ray(i, j)

                # (3.)shoot a ray at a random location inside the pixel
                # generated_ray = self.camera.get_ray(i, j)
                
                # pixel_color = get_color(generated_ray)

                # (4.)shoot multiple rays at random locations inside the pixel
                for l in range(self.camera.samples_per_pixel):
                    generated_ray = self.camera.get_ray(i, j)
                    pixel_color += get_color(generated_ray)
                # pixel_color/=self.camera.samples_per_pixel
                
                self.camera.write_to_film(i, j, pixel_color)
                renderbar.update(k)
                k = k+1


    def write_img2png(self, strPng_filename):
        png_film = self.camera.film * 255
        data = im.fromarray(png_film.astype(np.uint8))
        data.save(strPng_filename)

