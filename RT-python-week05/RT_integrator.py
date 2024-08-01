# a simple integrator class
# A ray is hit and then get the color.
# It is the rendering equation solver.
import RT_utility as rtu
import RT_ray as rtr

class Integrator():
    def __init__(self, bDlight=True) -> None:
        self.bool_direct_lighting = bDlight
        pass
    
    def compute_scattering(self, rGen_ray, scene, maxDepth):

        if maxDepth <= 0:
            return rtu.Color()

        # if the generated ray hits an object
        found_hit = scene.find_intersection(rGen_ray, rtu.Interval(0.000001, rtu.infinity_number))
        if found_hit == True:
            # get the hit info
            hinfo = scene.getHitList()
            # get the material of the object
            hmat = hinfo.getMaterial()
            # compute scattering
            sinfo = hmat.scattering(rGen_ray, hinfo)
            # if no scattering (It is a light source)
            if sinfo is None:
                # return Le
                return hmat.emitting()

            Le = rtu.Color()
            # if direct lighting is enabled
            if self.bool_direct_lighting:
                 # for each point light
                for light in scene.point_light_list:
                    # check if there is an occlusion between a point light and a surface point.
                    rayStartingPoint = hinfo.getP()
                    dirV = light.center - rayStartingPoint
                    
                    distance = dirV.len()

                    newRay = rtr.Ray(rayStartingPoint, dirV)

                    # if not occluded.
                    if not scene.find_occlusion(newRay, rtu.Interval(0.000001, hinfo.getT())):
                        # accumulate all unoccluded light
                        

                        Le = Le + (light.material.emitting()) * (1/distance**2)

                        # 1.render with out inverse square law
                        # Le = Le + light.material.emitting()
                        # 2.render with inverse square law
                        #Le = Le + light.material.emitting() * (1/distance**2)

            # return the color
            return (Le * sinfo.attenuation_color) + self.compute_scattering(rtr.Ray(hinfo.getP(), sinfo.scattered_ray.getDirection()), scene, maxDepth-1) * sinfo.attenuation_color

        return scene.getBackgroundColor()

