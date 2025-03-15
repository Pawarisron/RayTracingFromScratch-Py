# object class
import RT_utility as rtu
import math

class Object:
    def __init__(self) -> None:
        pass

    def intersect(self, rRay, cInterval):
        pass

class Sphere(Object):
    def __init__(self, vCenter, fRadius, mMat=None) -> None:
        super().__init__()
        self.center = vCenter
        self.radius = fRadius
        self.material = mMat

    def add_material(self, mMat):
        self.material = mMat

    def printInfo(self):
        self.center.printout()        
    
    # Assignment 1
    def intersect(self, rRay, cInterval):
        
        # find roots of the quadratic solution.
        rayDirection = rRay.getDirection()
        rayOrigin = rRay.getOrigin()
        a = rtu.Vec3.dot_product(rayDirection,rayDirection)
        b = rtu.Vec3.dot_product(rayDirection*2, rayOrigin-self.center)
        c = rtu.Vec3.dot_product(rayOrigin-self.center,rayOrigin-self.center) - (self.radius**2)
        discriminant = (b**2 - 4*a*c)
        # check if the positive root is in the interval
        if(discriminant>=0):
            root = (-b - math.sqrt(discriminant)) / (a*2)
            if(not rtu.Interval.contains(cInterval,root)):
               return None
        else:
            return None
        # generate and return a hit info
        hit_t = root
        hit_point = rRay.at(root)
        hit_normal = (hit_point - self.center) / self.radius
        hinfo = rtu.Hitinfo(hit_point, hit_normal, hit_t, self.material)
        hinfo.set_face_normal(rRay, hit_normal) 
        return hinfo

# Ax + By + Cz = D
class Quad(Object):
    def __init__(self, vQ, vU, vV, mMat=None) -> None:
        super().__init__()
        self.Qpoint = vQ
        self.Uvec = vU
        self.Vvec = vV
        self.material = mMat

        # Assignment 2
        # calculating quad parameters 
        self.uxv = rtu.Vec3.cross_product(self.Uvec,self.Vvec) 
        self.normal = rtu.Vec3.unit_vector(self.uxv)
        self.D = rtu.Vec3.dot_product(self.normal,self.Qpoint)
        self.Wvec = self.uxv/(rtu.Vec3.dot_product(self.uxv,self.uxv))

    def add_material(self, mMat):
        self.material = mMat

    # Assignment 3
    def intersect(self, rRay, cInterval):
        # if the ray is parallel to the plane
        denominator = rtu.Vec3.dot_product(self.normal,rRay.getDirection())
        if(denominator == 0):
            # print("parallel")
            return None
        
        t = (self.D - rtu.Vec3.dot_product(self.normal, rRay.getOrigin())) / denominator
        
        # if the ray hits the plane.
        if(not rtu.Interval.contains(cInterval,t)):
            return None
        
        intersection = rRay.at(t)
        p = intersection - self.Qpoint
        alpha = rtu.Vec3.dot_product(self.Wvec, rtu.Vec3.cross_product(p, self.Vvec))
        beta = rtu.Vec3.dot_product(self.Wvec, rtu.Vec3.cross_product(self.Uvec, p))
        # print(alpha,beta)
        
        # determine if the intersection point lies on the quad's plane.
        if(self.is_interior(alpha, beta) == None):
            return None

        # generate and return a hit info
        hit_t = t
        hit_point = rRay.at(t)
        hit_normal = self.normal
        hinfo = rtu.Hitinfo(hit_point, hit_normal, hit_t, self.material)
        hinfo.set_face_normal(rRay, hit_normal)
        return hinfo

    def is_interior(self, fa, fb):
        delta = 0   
        if (fa<delta) or (1.0<fa) or (fb<delta) or (1.0<fb):
            return None

        return True


class Triangle(Object):
    def __init__(self) -> None:
        super().__init__()

    def intersect(self, rRay, cInterval):
        return super().intersect(rRay, cInterval)