import RT_utility as rtu
import RT_camera as rtc
import RT_renderer as rtren
import RT_material as rtm
import RT_scene as rts
import RT_object as rto
import RT_integrator as rti
import RT_light as rtl
import RT_texture as rtt

def renderPhong():
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

    defocus_angle =0.0
    focus_distance = 10.0
    main_camera.init_camera(defocus_angle, focus_distance)
    # add objects to the scene

    tex_checker_bw = rtt.CheckerTexture(0.32, rtu.Color(.2, .2, .2), rtu.Color(.9, .9, .9))
    mat_tex_checker_bw = rtm.TextureColor(tex_checker_bw)

    mat_phong1 = rtm.Phong(rtu.Color(.2, .2, .2),1,1,   0.08)
    mat_phong2 = rtm.Phong(rtu.Color(.2, .2, .2),1,1,   8.00)
    mat_phong3 = rtm.Phong(rtu.Color(.2, .2, .2),1,1, 300.00)

    world = rts.Scene()
    world.add_object(rto.Sphere(rtu.Vec3(   0,-100.5,-1),  100, mat_tex_checker_bw))
    world.add_object(rto.Sphere(rtu.Vec3(-1.0,   0.0,-1),  0.5, mat_phong1))    # left
    world.add_object(rto.Sphere(rtu.Vec3(   0,   0.0,-1),  0.5, mat_phong2))    # center
    world.add_object(rto.Sphere(rtu.Vec3( 1.0,   0.0,-1),  0.5, mat_phong3))    # right

    dlight = rtl.Diffuse_light(rtu.Color(0.9, 0.9, 0.9))
    world.add_object(rto.Sphere(rtu.Vec3(   0, 1.0, 0.0), 0.05, dlight))
    # world.add_object(rto.Quad(rtu.Vec3(-0.5,1.5,-0.5), rtu.Vec3(0,0,-7.5), rtu.Vec3(3,0,-0.5), dlight))

    intg = rti.Integrator()

    renderer = rtren.Renderer(main_camera, intg, world)
    renderer.render()
    renderer.write_img2png('week08_brdf_Phong.png')    

def renderBlinn():
    main_camera = rtc.Camera()
    main_camera.aspect_ratio = 16.0/9.0
    main_camera.img_width = 480
    main_camera.center = rtu.Vec3(0,0,0)
    main_camera.samples_per_pixel = 30
    main_camera.max_depth = 5
    main_camera.vertical_fov = 60
    main_camera.look_from = rtu.Vec3(-2, 2, 1)
    main_camera.look_at = rtu.Vec3(0, 0, -1)
    main_camera.vec_up = rtu.Vec3(0, 1, 0)

    defocus_angle =0.0
    focus_distance = 10.0
    main_camera.init_camera(defocus_angle, focus_distance)
    # add objects to the scene

    tex_checker_bw = rtt.CheckerTexture(0.32, rtu.Color(.2, .2, .2), rtu.Color(.9, .9, .9))

    mat_tex_checker_bw = rtm.TextureColor(tex_checker_bw)

    mat_blinn1 = rtm.Blinn(rtu.Color(.2, .2, .2),1,1,   0.08)
    mat_blinn2 = rtm.Blinn(rtu.Color(.2, .2, .2),1,1,   8.00)
    mat_blinn3 = rtm.Blinn(rtu.Color(.2, .2, .2),1,1, 300.00)


    world = rts.Scene()
    world.add_object(rto.Sphere(rtu.Vec3(   0,-100.5,-1),  100, mat_tex_checker_bw))
    world.add_object(rto.Sphere(rtu.Vec3(-1.0,   0.0,-1),  0.5, mat_blinn1))    # left
    world.add_object(rto.Sphere(rtu.Vec3(   0,   0.0,-1),  0.5, mat_blinn2))    # center
    world.add_object(rto.Sphere(rtu.Vec3( 1.0,   0.0,-1),  0.5, mat_blinn3))    # right

    dlight = rtl.Diffuse_light(rtu.Color(0.9, 0.9, 0.9))
    world.add_object(rto.Sphere(rtu.Vec3(   0, 1.0, 0.0), 0.05, dlight))
    # world.add_object(rto.Quad(rtu.Vec3(-0.5,1.5,-0.5), rtu.Vec3(0,0,-7.5), rtu.Vec3(3,0,-0.5), dlight))

    intg = rti.Integrator()

    renderer = rtren.Renderer(main_camera, intg, world)
    renderer.render()
    renderer.write_img2png('week08_brdf_Blinn.png')    

def renderCook():
    main_camera = rtc.Camera()
    main_camera.aspect_ratio = 16.0/9.0
    main_camera.img_width = 480
    main_camera.center = rtu.Vec3(0,0,0)
    main_camera.samples_per_pixel = 10
    main_camera.max_depth = 5
    main_camera.vertical_fov = 60
    main_camera.look_from = rtu.Vec3(-2, 2, 1)
    main_camera.look_at = rtu.Vec3(0, 0, -1)
    main_camera.vec_up = rtu.Vec3(0, 1, 0)

    defocus_angle =0.0
    focus_distance = 10.0
    main_camera.init_camera(defocus_angle, focus_distance)
    # add objects to the scene

    tex_checker_bw = rtt.CheckerTexture(0.32, rtu.Color(.2, .2, .2), rtu.Color(.9, .9, .9))

    mat_tex_checker_bw = rtm.TextureColor(tex_checker_bw)

    mat_blinn1 = rtm.CookTorrance(rtu.Color(.2, .2, .2),1,1,   0.08)
    mat_blinn2 = rtm.CookTorrance(rtu.Color(.2, .2, .2),1,1,   8.00)
    mat_blinn3 = rtm.CookTorrance(rtu.Color(.2, .2, .2),1,1, 300.00)


    world = rts.Scene()
    world.add_object(rto.Sphere(rtu.Vec3(   0,-100.5,-1),  100, mat_tex_checker_bw))
    world.add_object(rto.Sphere(rtu.Vec3(-1.0,   0.0,-1),  0.5, mat_blinn1))    # left
    world.add_object(rto.Sphere(rtu.Vec3(   0,   0.0,-1),  0.5, mat_blinn2))    # center
    world.add_object(rto.Sphere(rtu.Vec3( 1.0,   0.0,-1),  0.5, mat_blinn3))    # right

    dlight = rtl.Diffuse_light(rtu.Color(0.9, 0.9, 0.9))
    world.add_object(rto.Sphere(rtu.Vec3(   0, 1.0, 0.0), 0.05, dlight))
    # world.add_object(rto.Quad(rtu.Vec3(-0.5,1.5,-0.5), rtu.Vec3(0,0,-7.5), rtu.Vec3(3,0,-0.5), dlight))

    intg = rti.Integrator()

    renderer = rtren.Renderer(main_camera, intg, world)
    renderer.render()
    renderer.write_img2png('week08_brdf_Cook.png') 

if __name__ == "__main__":
    # renderPhong()
    # renderBlinn()
    renderCook()


