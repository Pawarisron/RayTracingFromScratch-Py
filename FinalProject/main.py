import RT_utility as rtu
import RT_camera as rtc
import RT_renderer as rtren
import RT_material as rtm
import RT_scene as rts
import RT_object as rto
import RT_integrator as rti
import RT_light as rtl
import RT_texture as rtt
import PT_effect as pte

#These will be references for the final proj
def renderDoF():
    main_camera = rtc.Camera()
    main_camera.aspect_ratio = 16.0/9.0
    main_camera.img_width = 480
    main_camera.center = rtu.Vec3(0,0,0)
    main_camera.samples_per_pixel = 100
    main_camera.max_depth = 5
    main_camera.vertical_fov = 60
    main_camera.look_from = rtu.Vec3(-2, 2, 1)
    main_camera.look_at = rtu.Vec3(0, 0, -1)
    main_camera.vec_up = rtu.Vec3(0, 1, 0)

    defocus_angle = 2.0
    aperture = 1.0
    focus_distance = 5.0
    main_camera.init_camera(defocus_angle, focus_distance)
    # main_camera.init_camera(aperture, focus_distance)
    # add objects to the scene

    tex_checker_bw = rtt.CheckerTexture(0.32, rtu.Color(.2, .2, .2), rtu.Color(.9, .9, .9))

    mat_tex_checker_bw = rtm.TextureColor(tex_checker_bw)

    mat_blinn1 = rtm.Blinn(rtu.Color(0.8, 0.5, 0.8), 0.5, 0.2, 8)
    mat_blinn2 = rtm.Blinn(rtu.Color(0.4, 0.5, 0.4), 0.5, 0.6, 8)
    mat_blinn3 = rtm.Blinn(rtu.Color(0.8, 0.5, 0.4), 0.5, 0.2, 8)


    world = rts.Scene()
    world.add_object(rto.Sphere(rtu.Vec3(   0,-100.5,-1),  100, mat_tex_checker_bw))
    world.add_object(rto.Sphere(rtu.Vec3(-1.0,   0.0,-1),  0.5, mat_blinn1))    # left
    world.add_object(rto.Sphere(rtu.Vec3(   0,   0.0,-1),  0.5, mat_blinn2))    # center
    world.add_object(rto.Sphere(rtu.Vec3( 1.0,   0.0,-1),  0.5, mat_blinn3))    # right

    intg = rti.Integrator(bSkyBG=True)

    renderer = rtren.Renderer(main_camera, intg, world)
    # renderer.render()
    renderer.render_jittered()
    renderer.write_img2png('week10_jitter_DoF.png')    

def renderMoving():
    main_camera = rtc.Camera()
    main_camera.aspect_ratio = 16.0/9.0
    main_camera.img_width = 480
    main_camera.center = rtu.Vec3(0,0,0)
    main_camera.samples_per_pixel = 20
    main_camera.max_depth = 5
    main_camera.vertical_fov = 60
    main_camera.look_from = rtu.Vec3(-2, 2, 1)
    main_camera.look_at = rtu.Vec3(0, 0, -1)
    main_camera.vec_up = rtu.Vec3(0, 1, 0)

    defocus_angle = 0.0
    focus_distance = 5.0
    main_camera.init_camera(defocus_angle, focus_distance)
    # add objects to the scene

    tex_checker_bw = rtt.CheckerTexture(0.32, rtu.Color(.2, .2, .2), rtu.Color(.9, .9, .9))

    mat_tex_checker_bw = rtm.TextureColor(tex_checker_bw)

    mat_blinn1 = rtm.Blinn(rtu.Color(0.8, 0.5, 0.8), 0.5, 0.2, 8)
    mat_blinn2 = rtm.Blinn(rtu.Color(0.4, 0.5, 0.4), 0.5, 0.6, 8)
    mat_blinn3 = rtm.Blinn(rtu.Color(0.8, 0.5, 0.4), 0.5, 0.2, 8)


    sph_left = rto.Sphere(rtu.Vec3(-1.0,   0.0,-1),  0.5, mat_blinn1)
    sph_left.add_moving(rtu.Vec3(-1.0,   0.0,-1) + rtu.Vec3(0.0, 0.5,0.0))

    world = rts.Scene()
    world.add_object(rto.Sphere(rtu.Vec3(   0,-100.5,-1),  100, mat_tex_checker_bw))
    world.add_object(sph_left)    # left
    world.add_object(rto.Sphere(rtu.Vec3(   0,   0.0,-1),  0.5, mat_blinn2))    # center
    world.add_object(rto.Sphere(rtu.Vec3( 1.0,   0.0,-1),  0.5, mat_blinn3))    # right

    intg = rti.Integrator(bSkyBG=True)

    renderer = rtren.Renderer(main_camera, intg, world)
    renderer.render_jittered()
    renderer.write_img2png('week10_moving_nojitter.png')    

def renderMetal():
    main_camera = rtc.Camera()
    main_camera.aspect_ratio = 16.0/9.0
    main_camera.img_width = 480
    main_camera.center = rtu.Vec3(0,0,0)
    main_camera.samples_per_pixel = 3
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
    mat_tex_earth = rtm.TextureColor(rtt.ImageTexture("textures/earthmap.jpg"))        # earth texture
    mat_tex_basketball = rtm.TextureColor(rtt.ImageTexture("textures/basketball.jpg"))   # basketball
    mat_tex_soccer = rtm.TextureColor(rtt.ImageTexture("textures/soccer.jpg"))       # soccer
    mat_tex_pepsi = rtm.TextureColor(rtt.ImageTexture("textures/pepsi.jpg"))        # pepsi logo

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
    renderer.write_img2png('final_test2.png')

def renderFinal1():
    main_camera = rtc.Camera()
    main_camera.aspect_ratio = 16.0/9.0
    main_camera.img_width = 1920
    main_camera.center = rtu.Vec3(0,0,0)
    main_camera.samples_per_pixel = 100
    main_camera.max_depth = 5
    
    # Camera Positions
    main_camera.vertical_fov = 90
    # main_camera.look_from = rtu.Vec3(0, -5, 2)
    main_camera.look_from = rtu.Vec3(5, -7, 6)
    main_camera.look_at = rtu.Vec3(0, 0, 0.5)
    main_camera.vec_up = rtu.Vec3(0, 0, 1)

    defocus_angle = 2.0
    aperture = 1.0
    focus_distance = 5.0
    main_camera.init_camera(aperture, focus_distance)

    # Mats
    mat_ground = rtm.Lambertian(hex_to_normalized_rgba("#25292c"))
    mat_red_sphere = rtm.Lambertian(rtu.Color(0.6, 0, 0))
    mat_green_sphere = rtm.Lambertian(hex_to_normalized_rgba("#024526"))
    # Texture
    mat_tex_concrete = rtm.TextureColor(rtt.ImageTexture("textures/concrete.jpg"))    
    mat_tex_wood = rtm.TextureColor(rtt.ImageTexture("textures/wood.jpg"))    
    
    # Lights
    light = rtl.Diffuse_light(rtu.Color(0.05, 0.05, 0.05))
    sunLight = rtl.Diffuse_light(rtu.Color(0.4, 0.4, 0.4))
    
    
    world = rts.Scene()
    # Sun
    world.add_object(rto.Sphere(rtu.Vec3( 0, -19, 6), 8, sunLight))
    
    # Table
    world.add_object(rto.Quad(rtu.Vec3(-5,-5, 0), rtu.Vec3(10, 0, 0), rtu.Vec3(0, 10, 0), mat_tex_concrete))
    # Wall
    world.add_object(rto.Quad(rtu.Vec3(-5, 5, 0), rtu.Vec3(10, 0, 0.0), rtu.Vec3(0, 0, 10), mat_tex_concrete))
    # Block light
    y = -13
    world.add_object(rto.Quad(rtu.Vec3(-10, y, 0), rtu.Vec3(10, 0, 0.0), rtu.Vec3(0, 0, 10), mat_tex_concrete)) #left
    world.add_object(rto.Quad(rtu.Vec3(1, y, 0), rtu.Vec3(10, 0, 0.0), rtu.Vec3(0, 0, 10), mat_tex_concrete)) #right
    
    # shpere 
    world.add_object(rto.Sphere(rtu.Vec3(   0,1,0.9),  0.9, mat_red_sphere))
    world.add_object(rto.Sphere(rtu.Vec3(   2,3,1.4),  1.4, mat_green_sphere))
    
    intg = rti.Integrator(bSkyBG=False)

    renderer = rtren.Renderer(main_camera, intg, world)
    renderer.render()
    renderer.write_img2png('final1_test.png')
    
    # Post image processing
    pte.add_grain("final1_test.png", "final1_with_grain.png", intensity=0.01)    

def renderFinal2():
    def createPetals(world, base_pollen_loc, mat_petal):
        x = base_pollen_loc.e[0]
        if(x>0):
            base_pollen_loc += rtu.Vec3(0.1,0,0)
        elif(x<0):
            base_pollen_loc += rtu.Vec3(-0.1,0,0)
        # base_pollen_loc += (rtu.Vec3(0, base_pollen_loc.e[1], base_pollen_loc.e[2]) - base_pollen_loc)

        world.add_object(rto.Sphere(base_pollen_loc + rtu.Vec3( 0,  0.5, -1),  0.35, mat_petal))
        world.add_object(rto.Sphere(base_pollen_loc + rtu.Vec3( 0.35,  0.2, -1),  0.35, mat_petal))
        world.add_object(rto.Sphere(base_pollen_loc + rtu.Vec3(-0.35,  0.2, -1),  0.35, mat_petal))
        world.add_object(rto.Sphere(base_pollen_loc + rtu.Vec3( 0.3,  -0.2, -1),  0.35, mat_petal))
        world.add_object(rto.Sphere(base_pollen_loc + rtu.Vec3(-0.3,  -0.2, -1),  0.35, mat_petal))

    main_camera = rtc.Camera()
    main_camera.aspect_ratio = 16.0/9.0
    main_camera.img_width = 1920
    main_camera.center = rtu.Vec3(0,0,0)
    main_camera.samples_per_pixel = 100
    main_camera.max_depth = 7
    main_camera.vertical_fov = 25
    main_camera.look_from = rtu.Vec3(0, 0, 10)
    main_camera.look_at = rtu.Vec3(0, 0, 0)
    main_camera.vec_up = rtu.Vec3(0, 1, 0)

    defocus_angle = 2.0
    aperture = 1.5
    focus_distance = 10.0
    main_camera.init_camera(aperture, focus_distance)
    
    mat_ground = rtm.Lambertian(rtu.Color(0.8, 0.8, 0.0))
    mat_mountain = rtm.Lambertian(rtu.Color(0.0, 0.247, 0.0))
    mat_leaf = rtm.Lambertian(rtu.Color(0.0, 0.8, 0.0))
    mat_pollen = rtm.Lambertian(rtu.Color(1.0, 0.8, 0.13))
    mat_petal = rtm.Lambertian(rtu.Color(1.0, 0.3, 0.9))
    mat_water = rtm.Mirror(rtu.Color(0.235, 0.6, 1.0))

    light = rtl.Diffuse_light(rtu.Color(0.8, 0.225, 0.0))

    world = rts.Scene()
    
    # x = -left, +right | y = -down, +up | z = -back, +front
    # sun
    world.add_object(rto.Sphere(rtu.Vec3(   0,  -0.2,-30), 5, light))

    world.add_object(rto.Sphere(rtu.Vec3(   0,-100.5,-1),  100, mat_ground))
    world.add_object(rto.Sphere(rtu.Vec3(   0,-100.53,3),  100, mat_water))

    # mountains
    world.add_object(rto.Quad(rtu.Vec3(16.0, -0.6, -10.0), rtu.Vec3(-8, -7, 0.0), rtu.Vec3(-8, 7, 0.0), mat_mountain))
    world.add_object(rto.Quad(rtu.Vec3(-16.0, -0.6, -10.0), rtu.Vec3(8, -7, 0.0), rtu.Vec3(8, 7, 0.0), mat_mountain))
    
    base_flower_loc = rtu.Vec3(0, -0.4, -0.2)
    world.add_object(rto.Sphere(base_flower_loc,  0.2, mat_leaf))
    world.add_object(rto.Sphere(base_flower_loc + rtu.Vec3( 0,  0.3, 0),  0.15, mat_leaf))
    world.add_object(rto.Sphere(base_flower_loc + rtu.Vec3( 0,  0.6, 0),  0.17, mat_leaf))
    base_pollen_loc = base_flower_loc + rtu.Vec3( 0,  1.1, 0)
    world.add_object(rto.Sphere(base_pollen_loc,  0.4, mat_pollen))
    createPetals(world, base_pollen_loc, mat_petal)


    base_flower_loc2 = base_flower_loc + rtu.Vec3(-1.2,  0, 0)
    world.add_object(rto.Sphere(base_flower_loc2,  0.2, mat_leaf))
    world.add_object(rto.Sphere(base_flower_loc2 + rtu.Vec3( 0,  0.3, 0),  0.15, mat_leaf))
    world.add_object(rto.Sphere(base_flower_loc2 + rtu.Vec3( -0.1,  0.6, 0),  0.17, mat_leaf))
    
    base_pollen_loc2 = base_flower_loc2 + rtu.Vec3( -0.2,  1.1, 0)
    world.add_object(rto.Sphere(base_pollen_loc2,  0.4, mat_pollen))
    createPetals(world, base_pollen_loc2, mat_petal)
    
    base_flower_loc3 = base_flower_loc + rtu.Vec3(1.2,  0, 0)
    world.add_object(rto.Sphere(base_flower_loc3,  0.2, mat_leaf))
    world.add_object(rto.Sphere(base_flower_loc3 + rtu.Vec3( 0,  0.3, 0),  0.15, mat_leaf))
    world.add_object(rto.Sphere(base_flower_loc3 + rtu.Vec3( 0.1,  0.6, 0),  0.17, mat_leaf))

    base_pollen_loc3 = base_flower_loc3 + rtu.Vec3( 0.2,  1.1, 0)
    world.add_object(rto.Sphere(base_pollen_loc3,  0.4, mat_pollen))
    createPetals(world, base_pollen_loc3, mat_petal)
    
    intg = rti.Integrator(bSkyBG=True)

    renderer = rtren.Renderer(main_camera, intg, world)
    renderer.render()
    renderer.write_img2png('final2.png')   

def hex_to_normalized_rgba(hex_color):
   
    hex_color = hex_color.lstrip('#')
    
    r = int(hex_color[0:2], 16) / 255
    g = int(hex_color[2:4], 16) / 255
    b = int(hex_color[4:6], 16) / 255
    
    return rtu.Color(r, g, b)


if __name__ == "__main__":
    renderFinal1()
    # renderFinal2()
