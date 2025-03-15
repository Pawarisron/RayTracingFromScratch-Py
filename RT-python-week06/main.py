import RT_utility as rtu
import RT_camera as rtc
import RT_renderer as rtren
import RT_material as rtm
import RT_scene as rts
import RT_object as rto
import RT_integrator as rti
import RT_light as rtl

def renderMirrorPointLight():

    main_camera = rtc.Camera()
    main_camera.aspect_ratio = 16.0/9.0
    main_camera.img_width = 480
    main_camera.center = rtu.Vec3(0,0,0)
    main_camera.samples_per_pixel = 100
    main_camera.max_depth = 7
    main_camera.vertical_fov = 50
    main_camera.look_from = rtu.Vec3(-2, 2, 1)
    main_camera.look_at = rtu.Vec3(0, 0, -1)
    main_camera.vec_up = rtu.Vec3(0, 1, 0)
    # main_camera.look_from = rtu.Vec3(0, 0, 10)
    # main_camera.look_at = rtu.Vec3(0, 0, 0)
    # main_camera.vec_up = rtu.Vec3(0, 1, 0)
    defocus_angle =0.0
    focus_distance = 10.0
    main_camera.init_camera(defocus_angle, focus_distance)
    # add objects to the scene

    mat_ground = rtm.Lambertian(rtu.Color(0.8, 0.8, 0.0))
    mat_center = rtm.Lambertian(rtu.Color(0.7, 0.3, 0.3))
    mat_glass1 = rtm.Mirror(rtu.Color(0.8, 0.8, 0.8))

    world = rts.Scene()
    world.add_object(rto.Sphere(rtu.Vec3(   0,-100.5,-1),  100, mat_ground))
    world.add_object(rto.Sphere(rtu.Vec3(   0,   0.0,-1),  0.5, mat_center))
    world.add_object(rto.Sphere(rtu.Vec3(-1.0,   0.0,-1),  0.5, mat_glass1))
    world.add_object(rto.Sphere(rtu.Vec3(-1.0,   0.0,-1), -0.4, mat_glass1))
    world.add_object(rto.Sphere(rtu.Vec3( 1.0,   0.0,-1),  0.5, mat_glass1))

    point_light = rtl.Diffuse_light(rtu.Color(1.0, 1.0, 1.0))
    world.add_object(rto.Sphere(rtu.Vec3(0, 2.5, 0), 0.1, point_light))

    intg = rti.Integrator()

    renderer = rtren.Renderer(main_camera, intg, world)
    renderer.render()
    renderer.write_img2png('week06_point_light2.png')    


def renderMirrors():
    main_camera = rtc.Camera()
    main_camera.aspect_ratio = 16.0/9.0
    main_camera.img_width = 480
    main_camera.center = rtu.Vec3(0,0,0)
    main_camera.samples_per_pixel = 100
    main_camera.max_depth = 7
    main_camera.vertical_fov = 30
    main_camera.look_from = rtu.Vec3(0, 0, 10)
    main_camera.look_at = rtu.Vec3(0, 0, 0)
    main_camera.vec_up = rtu.Vec3(0, 1, 0)

    defocus_angle =0.0
    focus_distance = 10.0
    main_camera.init_camera(defocus_angle, focus_distance)
    # add objects to the scene

    mat_ground = rtm.Lambertian(rtu.Color(0.8, 0.8, 0.0))
    mat_center = rtm.Lambertian(rtu.Color(0.7, 0.3, 0.3))
    mat_glass1 = rtm.Mirror(rtu.Color(0.8, 0.8, 0.8))

    world = rts.Scene()
    world.add_object(rto.Sphere(rtu.Vec3(   0,-100.5,-1),  100, mat_ground))
    world.add_object(rto.Sphere(rtu.Vec3(   0,   0.0,-1),  0.5, mat_center))
    world.add_object(rto.Sphere(rtu.Vec3(-1.0,   0.0,-1),  0.5, mat_glass1))
    world.add_object(rto.Sphere(rtu.Vec3(-1.0,   0.0,-1), -0.4, mat_glass1))
    world.add_object(rto.Sphere(rtu.Vec3( 1.0,   0.0,-1),  0.5, mat_glass1))

    intg = rti.Integrator()

    renderer = rtren.Renderer(main_camera, intg, world)
    renderer.render()
    renderer.write_img2png('week06_glass_sky2.png')    


def renderDielectric():
    main_camera = rtc.Camera()
    main_camera.aspect_ratio = 16.0/9.0
    main_camera.img_width = 480
    main_camera.center = rtu.Vec3(0,0,0)
    main_camera.samples_per_pixel = 100
    main_camera.max_depth = 7
    main_camera.vertical_fov = 30
    main_camera.look_from = rtu.Vec3(0, 0, 10)
    main_camera.look_at = rtu.Vec3(0, 0, 0)
    main_camera.vec_up = rtu.Vec3(0, 1, 0)

    defocus_angle =0.0
    focus_distance = 10.0
    main_camera.init_camera(defocus_angle, focus_distance)
    # add objects to the scene

    mat_ground = rtm.Lambertian(rtu.Color(0.8, 0.8, 0.0))
    mat_center = rtm.Lambertian(rtu.Color(0.7, 0.3, 0.3))
    mat_glass1 = rtm.Mirror(rtu.Color(0.8, 0.8, 0.8))
    mat_dielect1 = rtm.Dielectric(rtu.Color(1.0, 1.0, 1.0), 1.0)
    mat_dielect2 = rtm.Dielectric(rtu.Color(1.0, 1.0, 1.0), 1.33)

    world = rts.Scene()
    world.add_object(rto.Sphere(rtu.Vec3(   0,-100.5,-1),  100, mat_ground))
    world.add_object(rto.Sphere(rtu.Vec3(   0,   0.0,-1),  0.5, mat_center))
    world.add_object(rto.Sphere(rtu.Vec3(-1.0,   0.0,-1),  0.5, mat_dielect1))
    # world.add_object(rto.Sphere(rtu.Vec3(-1.0,   0.0,-1), -0.4, mat_glass1))
    world.add_object(rto.Sphere(rtu.Vec3( 1.0,   0.0,-1),  0.5, mat_dielect2))

    intg = rti.Integrator()

    renderer = rtren.Renderer(main_camera, intg, world)
    renderer.render()
    renderer.write_img2png('week06_dielec_sky6.png')   

def renderCustomScene():
    main_camera = rtc.Camera()
    main_camera.aspect_ratio = 16.0/9.0
    main_camera.img_width = 480
    main_camera.center = rtu.Vec3(0,0,0)
    main_camera.samples_per_pixel = 100
    main_camera.max_depth = 10
    main_camera.vertical_fov = 20
    main_camera.look_from = rtu.Vec3(0, 0, 10)
    main_camera.look_at = rtu.Vec3(0, 0, 0)
    main_camera.vec_up = rtu.Vec3(0, 1, 0)

    defocus_angle =0.0
    focus_distance = 10.0
    main_camera.init_camera(defocus_angle, focus_distance)
    # add objects to the scene

    mat_ground = rtm.Lambertian(rtu.Color(0.8, 0.8, 0.0))
    mat_center = rtm.Lambertian(rtu.Color(0.8, 0.3, 0.3))
    mat_glass1 = rtm.Mirror(rtu.Color(0.8, 0.8, 0.8))
    mat_dielect1 = rtm.Dielectric(rtu.Color(1.0, 1.0, 1.0), 1.5)
    mat_dielect2 = rtm.Dielectric(rtu.Color(1.0, 1.0, 1.0), 1.0)
    mat_dielect3 = rtm.Dielectric(rtu.Color(1.0, 1.0, 1.0), 0.5)

    world = rts.Scene()
    world.add_object(rto.Sphere(rtu.Vec3(   0,-100.5,-1),  100, mat_glass1))
    world.add_object(rto.Sphere(rtu.Vec3(   0,   0.0,-1),  0.5, mat_center))
    world.add_object(rto.Sphere(rtu.Vec3(-1.7,  -0.03,-3),  0.5, mat_dielect1))
    world.add_object(rto.Sphere(rtu.Vec3(-0.7,   0.0,-2),  0.5, mat_dielect3))
    world.add_object(rto.Sphere(rtu.Vec3( 0.7,   0.0,-0),  0.5, mat_dielect2))

    point_light = rtl.Diffuse_light(rtu.Color(0.0, 0.5, 0.0))
    world.add_object(rto.Sphere(rtu.Vec3(1.7, 2.5, 0), 0.1, point_light))

    intg = rti.Integrator()

    renderer = rtren.Renderer(main_camera, intg, world)
    renderer.render()
    renderer.write_img2png('week06_custom_scene1.png')  

if __name__ == "__main__":
    # renderMirrors()
    # renderMirrorPointLight()
    renderDielectric()
    # renderCustomScene()

