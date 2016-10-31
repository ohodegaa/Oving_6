-----------  PLAB OVING 6  -----------

- Simen Husoy
- Mari Fredriksen
- Ole Haakon Oedegaard


Skapnr.: 41
Kode til skap: 020


Oversikt:

format: *modulename.py* (*classname*)
            *function1*
            *function2*
            ***

Sensobs:
    camera (Camera):
        __init__(img_width=128, img_height=96, img_rot=0)
        get_value
        update
        reset
        sensor_get_value

    irproximity_sensor (IRProximitySensor):
        __init__()
        setup
        get_value
        update
        reset
        sensor_get_value
    reflectance_sensors (ReflectanceSensors):
        __init__(self, auto_calibrate=False, min_reading=100, max_reading=1000)
        setup
        calibrate
        get_sensor_reading
        recharge_capacitors
        reset
        get_value
        update
        compute_value
        normalize
    ultrasonic (Ultrasonic):
        __init__()
        setup
        get_value
        update
        reset
        sensor_get_value
        send_activation_pulse
        compute_distance


Utilities:
    imager2 (Imager):
        __init__(self,fid=False,image=False,width=100,height=100,background='black',mode='RGB')
        init_image
        load_image
        dump_image
        get_image
        set_image
        display
        get_image_dims
        copy_image_dims
        get_color_rgb
        resize
        scale
        get_pixel
        set_pixel
        combine_pixels
        map_image
        map_image2
        map_color_wta
        gen_grayscale
        scale_colors
        paste
        concat_vert
        concat_horiz
        morph
        morph4
        morphroll
        tunnel
        mortun

    zumo_button (ZumoButton):
        __init__()
        wait_for_press

Motobs:
    motors (Motors):
        __init__()
        setup
        forward
        backward
        left
        right
        stop
        set_value
        set_left_speed
        set_right_speed
        set_left_dir
        set_right_dir
        persist