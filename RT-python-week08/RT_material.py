# material class
import RT_utility as rtu
import RT_ray as rtr
import math
import RT_texture as rtt

def reflect(vRay, vNormal):
    # return the perfect reflection direction
    return vRay - vNormal*rtu.Vec3.dot_product(vRay, vNormal)*2.0

def refract(vRay, vNormal, fRefractRatio):
    cos_theta = min(rtu.Vec3.dot_product(-vRay, vNormal), 1.0)
    sin_theta = math.sqrt(1.0 - cos_theta*cos_theta)
    cannot_refract = fRefractRatio*sin_theta > 1.0

    if cannot_refract or schlick(cos_theta, fRefractRatio) > rtu.random_double():
        return reflect(vRay, vNormal)
    else:
        perpendiular_dir = (vRay + vNormal*cos_theta)*fRefractRatio
        parallel_dir = vNormal*(-math.sqrt(math.fabs(1.0 - perpendiular_dir.len_squared())))
        return perpendiular_dir + parallel_dir

def halfvector(vView, vLight):
    vH = (vView + vLight)*0.5
    return vH

def schlick(fCosine, fIOR):
    r0 = (1-fIOR) / (1+fIOR)
    r0 = r0*r0
    return r0 + (1-r0)*math.pow(1-fCosine, 5)

class Material:
    def __init__(self) -> None:
        pass

    def scattering(self, rRayIn, hHinfo):
        pass

    def is_light(self):
        return False

class Lambertian(Material):
    def __init__(self, cAlbedo) -> None:
        super().__init__()
        self.color_albedo = rtu.Color(cAlbedo.r(), cAlbedo.g(), cAlbedo.b())

    def scattering(self, rRayIn, hHinfo):
        scattered_direction = hHinfo.getNormal() + rtu.Vec3.random_vec3_unit()
        if scattered_direction.near_zero():
            scattered_direction = hHinfo.getNormal()

        scattered_ray = rtr.Ray(hHinfo.getP(), scattered_direction)
        attenuation_color = self.BRDF(rRayIn, scattered_ray, hHinfo)
        return rtu.Scatterinfo(scattered_ray, attenuation_color)

    def BRDF(self, rView, rLight, hHinfo):
        attenuation_color = rtu.Color(self.color_albedo.r(), self.color_albedo.g(), self.color_albedo.b())
        return attenuation_color


# a mirror class
class Mirror(Material):
    def __init__(self, cAlbedo) -> None:
        super().__init__()
        self.color_albedo = rtu.Color(cAlbedo.r(), cAlbedo.g(), cAlbedo.b())

    def scattering(self, rRayIn, hHinfo):
        # generate a reflected ray
        reflected_ray = rtr.Ray(hHinfo.getP(), reflect(rRayIn.getDirection(), hHinfo.getNormal()))

        # get attenuation_color
        attenuation_color = self.BRDF(rRayIn, reflected_ray, hHinfo)

        # return scattering info
        return rtu.Scatterinfo(reflected_ray, attenuation_color)

    def BRDF(self, rView, rLight, hHinfo):
        attenuation_color = rtu.Color(self.color_albedo.r(), self.color_albedo.g(), self.color_albedo.b())
        return attenuation_color


# A dielectric transparent material 
class Dielectric(Material):
    def __init__(self, cAlbedo, fIor) -> None:
        super().__init__()
        self.color_albedo = rtu.Color(cAlbedo.r(), cAlbedo.g(), cAlbedo.b())
        self.IOR = fIor

    def scattering(self, rRayIn, hHinfo):
        refract_ratio = self.IOR
        if hHinfo.front_face:
            refract_ratio = 1.0/self.IOR

        # generate a refracted ray
        uv = rtu.Vec3.unit_vector(rRayIn.getDirection())
        refracted_dir = refract(uv, hHinfo.getNormal(), refract_ratio)
        scattered_ray = rtr.Ray(hHinfo.getP(), refracted_dir)

        attenuation_color = self.BRDF(rRayIn, scattered_ray, hHinfo)
        # return scattering info
        return rtu.Scatterinfo(scattered_ray, attenuation_color)

    def BRDF(self, rView, rLight, hHinfo):
        attenuation_color = rtu.Color(self.color_albedo.r(), self.color_albedo.g(), self.color_albedo.b())
        return attenuation_color

# a texture
class TextureColor(Material):
    def __init__(self, color_or_texture) -> None:
        super().__init__()
        if isinstance(color_or_texture, rtu.Color):
            self.color_albedo = rtt.SolidColor(color_or_texture)
        else:
            self.color_albedo = color_or_texture

    def scattering(self, rRayIn, hHinfo):
        scattered_direction = hHinfo.getNormal() + rtu.Vec3.random_vec3_unit()
        if scattered_direction.near_zero():
            scattered_direction = hHinfo.getNormal()

        scattered_ray = rtr.Ray(hHinfo.getP(), scattered_direction)
        attenuation_color = self.BRDF(rRayIn, scattered_ray, hHinfo)

        return rtu.Scatterinfo(scattered_ray, attenuation_color)

    def BRDF(self, rView, rLight, hHinfo):
        attenuation_color = self.color_albedo.tex_value(hHinfo.u, hHinfo.v, hHinfo.point)
        return attenuation_color


# A metal class with roughness parameter
class Metal(Material):
    def __init__(self, cAlbedo, fRoughness) -> None:
        super().__init__()
        self.color_albedo = rtu.Color(cAlbedo.r(), cAlbedo.g(), cAlbedo.b())
        self.roughness = fRoughness
        if self.roughness > 1.0:
            self.roughness = 1.0

    def scattering(self, rRayIn, hHinfo):
        # compute scattered ray based on the roughtness parameter
        reflected_direction = reflect(rtu.Vec3.unit_vector(rRayIn.getDirection()), hHinfo.getNormal()) + rtu.Vec3.random_vec3_unit()*self.roughness
        reflected_ray = rtr.Ray(hHinfo.getP(), reflected_direction)
        attenuation_color = self.BRDF(rRayIn, reflected_ray, hHinfo)

        # check if the reflected direction is below the surface normal
        if rtu.Vec3.dot_product(reflected_direction, hHinfo.getNormal()) <= 1e-8:
            attenuation_color = rtu.Color(0,0,0)

        return rtu.Scatterinfo(reflected_ray, attenuation_color)

    def BRDF(self, rView, rLight, hHinfo):
        attenuation_color = rtu.Color(self.color_albedo.r(), self.color_albedo.g(), self.color_albedo.b())
        return attenuation_color    

# Phong reflection model
# fr = kd + ks*(R.V)^roughness
class Phong(Material):
    def __init__(self, cAlbedo, kd, ks, fAlpha) -> None:
        super().__init__()
        self.color_albedo = rtu.Color(cAlbedo.r(), cAlbedo.g(), cAlbedo.b())
        self.kd = kd
        self.ks = ks
        self.alpha = fAlpha

    def scattering(self, rRayIn, hHinfo):
        reflected_direction = -hHinfo.getNormal()
        # check if the reflected direction is below the surface normal
        while rtu.Vec3.dot_product(reflected_direction, hHinfo.getNormal()) <= 1e-8:

            # compute scattered ray
            reflected_direction = hHinfo.getNormal() + rtu.Vec3.random_vec3_unit()
            if reflected_direction.near_zero():
                reflected_direction = hHinfo.getNormal()

        reflected_ray = rtr.Ray(hHinfo.getP(), reflected_direction)
        phong_color = self.BRDF(rRayIn, reflected_ray, hHinfo)

        return rtu.Scatterinfo(reflected_ray, phong_color)

    def BRDF(self, rView, rLight, hHinfo):
        # calculate diffuse color
        diff_color = self.color_albedo * (self.kd*1.0/rtu.pi)
        reflection_vector = rtu.Vec3.unit_vector(reflect(rLight.getDirection(), hHinfo.getNormal()))
        dot_product = max(rtu.Vec3.dot_product(reflection_vector, rtu.Vec3.unit_vector(rView.getDirection())), 0.0)
        spec_color = self.color_albedo * self.ks * (self.alpha+2/2*rtu.pi) * math.pow(dot_product, self.alpha)

        return diff_color + spec_color


# Blinn-Phong reflection model
# fr = kd + ks*(H.N)^roughness
class Blinn(Material):
    def __init__(self, cAlbedo, kd, ks, fAlpha) -> None:
        super().__init__()
        self.color_albedo = rtu.Color(cAlbedo.r(), cAlbedo.g(), cAlbedo.b())
        self.kd = kd
        self.ks = ks
        self.alpha = fAlpha

    def scattering(self, rRayIn, hHinfo):
        reflected_direction = -hHinfo.getNormal()
        # check if the reflected direction is below the surface normal
        while rtu.Vec3.dot_product(reflected_direction, hHinfo.getNormal()) <= 1e-8:

            # compute scattered ray
            reflected_direction = hHinfo.getNormal() + rtu.Vec3.random_vec3_unit()
            if reflected_direction.near_zero():
                reflected_direction = hHinfo.getNormal()

        reflected_ray = rtr.Ray(hHinfo.getP(), reflected_direction)
        blinn_color = self.BRDF(rRayIn, reflected_ray, hHinfo)

        return rtu.Scatterinfo(reflected_ray, blinn_color)

    def BRDF(self, rView, rLight, hHinfo):
        # Calculate diffuse color
        dot_product = max(rtu.Vec3.dot_product(rLight.getDirection(), hHinfo.getNormal()), 0.0)
        diff_color = self.color_albedo * (self.kd*dot_product / rtu.pi)
        
        # Calculate the halfway vector between the light direction and view direction
        H = rtu.Vec3.unit_vector(rView.getDirection() + rLight.getDirection())
        dot_product = max(rtu.Vec3.dot_product(H, hHinfo.getNormal()), 0.0)
        
        # Calculate the specular color using the Blinn-Phong model
        spec_color = self.color_albedo * self.ks * ((self.alpha + 2) / (2 * rtu.pi)) * math.pow(dot_product, self.alpha)

        return diff_color + spec_color

# Cook-Torrance BRDF model
# fr = kd/pi + ks*(DFG/4(w_o.N * w_i.N))
class CookTorrance(Material):
    def __init__(self, cAlbedo, kd, ks, fAlpha) -> None:
        super().__init__()
        self.color_albedo = rtu.Color(cAlbedo.r(), cAlbedo.g(), cAlbedo.b())
        self.kd = kd
        self.ks = ks
        self.alpha = fAlpha

    def scattering(self, rRayIn, hHinfo):
        # Calculate the reflected direction based on Cook-Torrance model (usually for indirect lighting)
        normal = hHinfo.getNormal()
        reflected_ray = rtr.Ray(hHinfo.getP(), rtu.Vec3.random_vec3_on_hemisphere(normal))
        cook_torrance_color = self.BRDF(rRayIn, reflected_ray, hHinfo)
        return rtu.Scatterinfo(reflected_ray, cook_torrance_color)

        return rtu.Scatterinfo(reflected_ray, attenuation_color)

    def BRDF(self, rView, rLight, hHinfo):
        # Calculate the diffuse color (Lambertian reflection)
        diff_color = self.color_albedo * (self.kd / rtu.pi)
        
        # Calculate the halfway vector
        H = rtu.Vec3.unit_vector(rView.getDirection() + rLight.getDirection())
        N = hHinfo.getNormal()
        V = rView.getDirection()
        L = rLight.getDirection()
        
        # Calculate the dot products
        NdotL = max(rtu.Vec3.dot_product(N, L), 1e-6)  # Avoid division by zero
        NdotV = max(rtu.Vec3.dot_product(N, V), 1e-6)  # Avoid division by zero
        HdotN = max(rtu.Vec3.dot_product(H, N), 1e-6)  # Avoid division by zero
        HdotV = max(rtu.Vec3.dot_product(H, V), 1e-6)  # Avoid division by zero
        
        # Fresnel-Schlick approximation
        F0 = 0.04
        F = F0 + (1 - F0) * math.pow(1 - HdotV, 5)
        
        # Geometric attenuation (Schlick approximation)
        k = 0.5 * self.alpha + 0.5
        G = min(1.0, min(2 * HdotN * NdotV / max(HdotV, 1e-6), 2 * HdotN * NdotL / max(HdotV, 1e-6)))
        
        # Normal Distribution Function (GGX or Beckmann)
        alpha2 = self.alpha * self.alpha
        D = math.exp((HdotN * HdotN - 1) / (alpha2 * HdotN * HdotN)) / (math.pi * alpha2 * HdotN * HdotN * HdotN * HdotN)
        
        # Calculate the specular color
        spec_color = self.color_albedo * self.ks * (F * G * D) / max(4 * NdotL * NdotV, 1e-6)
        
        return diff_color + spec_color
    