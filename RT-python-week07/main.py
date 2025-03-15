import RT_utility as rtu
import RT_camera as rtc
import RT_renderer as rtren
import RT_material as rtm
import RT_scene as rts
import RT_object as rto
import RT_integrator as rti
import RT_light as rtl
import RT_texture as rtt

def renderProceduralTexture():
    main_camera = rtc.Camera()
    main_camera.aspect_ratio = 16.0/9.0
    main_camera.img_width = 480
    main_camera.center = rtu.Vec3(0,0,0)
    main_camera.samples_per_pixel = 128
    main_camera.max_depth = 5
    main_camera.vertical_fov = 60
    main_camera.look_from = rtu.Vec3(-2, 2, 1)
    main_camera.look_at = rtu.Vec3(0, 0, -1)
    main_camera.vec_up = rtu.Vec3(0, 1, 0)

    defocus_angle =0.0
    focus_distance = 10.0
    main_camera.init_camera(defocus_angle, focus_distance)
    # add objects to the scene

    mat_center = rtm.Lambertian(rtu.Color(0.7, 0.3, 0.3))

    # create textures
    mat_tex_checker_bw = rtm.TextureColor(rtt.CheckerTexture(1.0, rtu.Color(0.0, 0.0, 0.0), rtu.Color(1.0, 1.0, 1.0)))   # black and white checker board
    mat_tex_checker = rtm.TextureColor(rtt.CheckerTexture(0.5, rtu.Color(0.37, 0.29, 0.55), rtu.Color(0.90, 0.60, 0.55)))      # colorful checker board
    mat_tex_solid = rtm.TextureColor(rtt.SolidColor(rtu.Color(0.89, 0.65, 0.44)))        # solid color

    world = rts.Scene()
    world.add_object(rto.Sphere(rtu.Vec3(   0,-100.5,-1),  100, mat_tex_checker_bw))
    world.add_object(rto.Sphere(rtu.Vec3(   0,   0.0,-1),  0.5, mat_center))
    world.add_object(rto.Sphere(rtu.Vec3(-1.0,   0.0,-1),  0.5, mat_tex_checker))
    world.add_object(rto.Sphere(rtu.Vec3( 1.0,   0.0,-1),  0.5, mat_tex_solid))

    intg = rti.Integrator()

    renderer = rtren.Renderer(main_camera, intg, world)
    renderer.render()
    renderer.write_img2png('week07_texture_sky.png')    

def renderEarth():
    main_camera = rtc.Camera()
    main_camera.aspect_ratio = 16.0/9.0
    main_camera.img_width = 480
    main_camera.center = rtu.Vec3(0,0,0)
    main_camera.samples_per_pixel = 128
    main_camera.max_depth = 5
    main_camera.vertical_fov = 60
    main_camera.look_from = rtu.Vec3(-2, 2, 1)
    main_camera.look_at = rtu.Vec3(0, 0, -1)
    main_camera.vec_up = rtu.Vec3(0, 1, 0)

    defocus_angle =0.0
    focus_distance = 10.0
    main_camera.init_camera(defocus_angle, focus_distance)
    # add objects to the scene

    mat_tex_checker_bw = rtm.TextureColor(rtt.CheckerTexture(0.2, rtu.Color(0.0, 0.0, 0.0), rtu.Color(1.0, 1.0, 1.0)))   # black and white checker board
    mat_tex_earth = rtm.TextureColor(rtt.ImageTexture("RT-python-week07/textures/earthmap.jpg"))        # earth texture
    mat_tex_basketball = rtm.TextureColor(rtt.ImageTexture("RT-python-week07/textures/basketball.jpg"))   # basketball
    mat_tex_soccer = rtm.TextureColor(rtt.ImageTexture("RT-python-week07/textures/soccer.jpg"))       # soccer
    mat_tex_pepsi = rtm.TextureColor(rtt.ImageTexture("RT-python-week07/textures/pepsi.jpg"))        # pepsi logo

    world = rts.Scene()
    world.add_object(rto.Sphere(rtu.Vec3(   0,-100.5,-1),  100, mat_tex_earth))
    world.add_object(rto.Sphere(rtu.Vec3(   0,   0.0,-1),  0.5, mat_tex_checker_bw))
    world.add_object(rto.Sphere(rtu.Vec3(-1.0,   0.0,-1),  0.5, mat_tex_basketball))
    world.add_object(rto.Sphere(rtu.Vec3( 1.0,   0.0,-1),  0.5, mat_tex_soccer))

    world.add_object(rto.Quad(rtu.Vec3(1.0, 0.0, -1), rtu.Vec3(1.0, 2.0, -1), rtu.Vec3(1.0, 0.0, 1), mat_tex_pepsi))

    intg = rti.Integrator()

    renderer = rtren.Renderer(main_camera, intg, world)
    renderer.render()
    renderer.write_img2png('week07_texture_earth_sky_final.png')    

def renderMetal():
    main_camera = rtc.Camera()
    main_camera.aspect_ratio = 16.0/9.0
    main_camera.img_width = 480
    main_camera.center = rtu.Vec3(0,0,0)
    main_camera.samples_per_pixel = 128
    main_camera.max_depth = 5
    main_camera.vertical_fov = 60
    main_camera.look_from = rtu.Vec3(-2, 2, 1)
    main_camera.look_at = rtu.Vec3(0, 0, -1)
    main_camera.vec_up = rtu.Vec3(0, 1, 0)

    defocus_angle =0.0
    focus_distance = 10.0
    main_camera.init_camera(defocus_angle, focus_distance)
    # add objects to the scene

    mat_metal1 = rtm.Metal(rtu.Color(0.89, 0.65, 0.44), 1.0)
    mat_metal2 = rtm.Metal(rtu.Color(0.89, 0.65, 0.44), 0.8)
    mat_metal3 = rtm.Metal(rtu.Color(0.89, 0.65, 0.44), 0.1)
    mat_metal4 = rtm.Metal(rtu.Color(0.89, 0.65, 0.44), 0.05)
    mat_metal5 = rtm.Metal(rtu.Color(0.89, 0.65, 0.44), 0.0005)
    mat_metal6 = rtm.Metal(rtu.Color(0.89, 0.65, 0.44), 0.0001)
    mat_tex_checker_bw = rtm.TextureColor(rtt.CheckerTexture(1.0, rtu.Color(0.0, 0.0, 0.0), rtu.Color(1.0, 1.0, 1.0)))   # black and white checker board
    mat_tex_earth = rtm.TextureColor(rtt.ImageTexture("RT-python-week07/textures/earthmap.jpg"))        # earth texture
    mat_tex_basketball = rtm.TextureColor(rtt.ImageTexture("RT-python-week07/textures/basketball.jpg"))   # basketball
    mat_tex_soccer = rtm.TextureColor(rtt.ImageTexture("RT-python-week07/textures/soccer.jpg"))       # soccer
    mat_tex_pepsi = rtm.TextureColor(rtt.ImageTexture("RT-python-week07/textures/pepsi.jpg"))        # pepsi logo

    world = rts.Scene()
    world.add_object(rto.Sphere(rtu.Vec3(   0,-100.5,-1),  100, mat_tex_earth))
    world.add_object(rto.Sphere(rtu.Vec3(   0,   0.0,-1),  0.5, mat_metal1))
    world.add_object(rto.Sphere(rtu.Vec3(   0,   0.0, 0.1),  0.5, mat_metal2))
    world.add_object(rto.Sphere(rtu.Vec3( 1.1,   0.0, 0.1),  0.5, mat_metal3))
    world.add_object(rto.Sphere(rtu.Vec3( 1.1,   0.0,-1),  0.5, mat_metal4))
    world.add_object(rto.Sphere(rtu.Vec3( 1.1,   0.0,-2.1),  0.5, mat_metal5))
    world.add_object(rto.Sphere(rtu.Vec3(-1.1,   0.0,-1),  0.5, mat_metal6))

    light = rtl.Diffuse_light(rtu.Color(0.4, 0, 0.0))
    world.add_object(rto.Quad(rtu.Vec3(-1.0, 2.0, -2.0), rtu.Vec3(2.0, 0.0, 0.0), rtu.Vec3(0.0, 0.0, 2.0), light))

    intg = rti.Integrator()

    renderer = rtren.Renderer(main_camera, intg, world)
    renderer.render()
    renderer.write_img2png('week07_metal_balls_final_2.png')

if __name__ == "__main__":
    # renderProceduralTexture()
    renderEarth()
    # renderMetal()