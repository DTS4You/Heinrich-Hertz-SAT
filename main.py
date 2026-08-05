######################################################
### Main-Program                                   ###
### Projekt : Heinrich-Hertz-SAT                   ###
### Version : 1.06                                 ###
### Datum   : 05.08.2026                           ###
######################################################
from machine import Pin, Timer      # type: ignore
from libs.module_init import Global_Module as MyModule
import time                         # type: ignore

#------------------------------------------------------------------------------
# 01 -> Next OBP              -> 4.12                         -> 15
# 02 -> Fraunhofer OBP        -> 4.11                         -> 14
# 03 -> GeReLEO Smart         -> 4.07                         -> 10
# 04 -> Flex INET             -> 4.03 , 4.05                  ->  6 ,  8
# 05 -> Flex OMUX             -> 4.02 , 4.06                  ->  5 ,  9
# 06 -> 300W FPM              -> 4.01 , 4.04                  ->  4 ,  7
# 07 -> 250W FPM              -> 4.08 , 4.09                  -> 11 , 12
# 08 -> PLIU                  -> 4.10                         -> 13
# 09 -> H2KAR Reflektor       -> 6.05                         -> 28
# 10 -> HEMPT                 -> 5.08                         -> 23
# 11 -> Reaktionsräder        -> 5.06 , 6.06                  -> 21 , 29
# 12 -> Batterie              -> 7.02 , 7.03                  -> 33 , 34
# 13 -> Apogäums-Triebwerk    -> 7.01                         -> 32
# 14 -> Tank (Xe)             -> 5.04 , 6.03                  -> 19 , 26
# 15 -> Tank (MMH/MON)        -> 5.01 , 5/02 , 6.01 , 6.02    -> 16 , 17 , 24 , 25
# 16 -> Sternsensor           -> 1.01 , 2.01                  ->  1 ,  2
# 17 -> Tank (He)             -> 5.03 , 6.04                  -> 18 , 27
# 18 -> SADM                  -> 3.01                         ->  3
# 19 -> 10 N Triebwerke       -> 5.07 , 6.07                  -> 22 , 30
# 20 -> HET                   -> 6.08                         -> 31
#------------------------------------------------------------------------------
pix_array_01 = [15]
pix_array_02 = [15]
pix_array_03 = [10]
pix_array_04 = [ 6, 8]
pix_array_05 = [ 5, 9]
pix_array_06 = [ 4, 7]
pix_array_07 = [11,12]
pix_array_08 = [13]
pix_array_09 = [28]
pix_array_10 = [23]
pix_array_11 = [21,29]
pix_array_12 = [33,34]
pix_array_13 = [32]
pix_array_14 = [19,26]
pix_array_15 = [16,17,24,25]
pix_array_16 = [1, 2]
pix_array_17 = [18,27]
pix_array_18 = [ 3]
pix_array_19 = [22,30]
pix_array_20 = [31]
#------------------------------------------------------------------------------

obj_offset = 0          # Offset bei Zählung ab 1 = -1

def blink_func():
    MyWS2812.do_blink()


# ------------------------------------------------------------------------------
# --- Main Function                                                          ---
# ------------------------------------------------------------------------------
def main():

    print("=== Start Main ===")
    
    blink_couter = 0
    
    MyWS2812.do_all_def()	# Alle Leds auf Default-Wert
       
    while MySerial.sercon_read_flag():

        if blink_couter > 50:
            blink_couter = 0
            blink_func()
        
        MySerial.sercon_read_line()
        if MySerial.get_ready_flag():       # Zeichenkette empfangen
            print(MySerial.get_string())
            MyDecode.decode_input(str(MySerial.get_string()))
            #MyDecode.decode_printout()
            if MyDecode.get_valid_flag() == True:
                #print("Valid Command")
                if MyDecode.get_cmd_1() == "do":
                    #print("do")
                    if MyDecode.get_cmd_2() == "all":
                        #print("all")
                        if MyDecode.get_value_1() == 0:
                            #print("off")
                            MyWS2812.do_all_off()
                        if MyDecode.get_value_1() == 1:
                            #print("on")
                            MyWS2812.do_all_on()
                        if MyDecode.get_value_1() == 2:
                            #print("def")
                            MyWS2812.do_all_def()
                    if MyDecode.get_cmd_2() == "obj":
                        #print("obj")
                        #print(MyDecode.get_value_1())
                        #print(segment_map[MyDecode.get_value_1()])
                        MyWS2812.do_all_off()
                        if MyDecode.get_value_1() == 1:
                            for i in pix_array_01:
                                MyWS2812.set_led_obj(i + obj_offset, MyDecode.get_value_2())
                        if MyDecode.get_value_1() == 2:
                            for i in pix_array_02:
                                MyWS2812.set_led_obj(i + obj_offset, MyDecode.get_value_2())
                        if MyDecode.get_value_1() == 3:
                            for i in pix_array_03:
                                MyWS2812.set_led_obj(i + obj_offset, MyDecode.get_value_2())
                        if MyDecode.get_value_1() == 4:
                            for i in pix_array_04:
                                MyWS2812.set_led_obj(i + obj_offset, MyDecode.get_value_2())
                        if MyDecode.get_value_1() == 5:
                            for i in pix_array_05:
                                MyWS2812.set_led_obj(i + obj_offset, MyDecode.get_value_2())
                        if MyDecode.get_value_1() == 6:
                            for i in pix_array_06:
                                MyWS2812.set_led_obj(i + obj_offset, MyDecode.get_value_2())
                        if MyDecode.get_value_1() == 7:
                            for i in pix_array_07:
                                MyWS2812.set_led_obj(i + obj_offset, MyDecode.get_value_2())
                        if MyDecode.get_value_1() == 8:
                            for i in pix_array_08:
                                MyWS2812.set_led_obj(i + obj_offset, MyDecode.get_value_2())
                        if MyDecode.get_value_1() == 9:
                            for i in pix_array_09:
                                MyWS2812.set_led_obj(i + obj_offset, MyDecode.get_value_2())
                        if MyDecode.get_value_1() == 10:
                            for i in pix_array_10:
                                MyWS2812.set_led_obj(i + obj_offset, MyDecode.get_value_2())
                        if MyDecode.get_value_1() == 11:
                            for i in pix_array_11:
                                MyWS2812.set_led_obj(i + obj_offset, MyDecode.get_value_2())
                        if MyDecode.get_value_1() == 12:
                            for i in pix_array_12:
                                MyWS2812.set_led_obj(i + obj_offset, MyDecode.get_value_2())
                        if MyDecode.get_value_1() == 13:
                            for i in pix_array_13:
                                MyWS2812.set_led_obj(i + obj_offset, MyDecode.get_value_2())
                        if MyDecode.get_value_1() == 14:
                            for i in pix_array_14:
                                MyWS2812.set_led_obj(i + obj_offset, MyDecode.get_value_2())
                        if MyDecode.get_value_1() == 15:
                            for i in pix_array_15:
                                MyWS2812.set_led_obj(i + obj_offset, MyDecode.get_value_2())
                        if MyDecode.get_value_1() == 16:
                            for i in pix_array_16:
                                MyWS2812.set_led_obj(i + obj_offset, MyDecode.get_value_2())
                        if MyDecode.get_value_1() == 17:
                            for i in pix_array_17:
                                MyWS2812.set_led_obj(i + obj_offset, MyDecode.get_value_2())
                        if MyDecode.get_value_1() == 18:
                            for i in pix_array_18:
                                MyWS2812.set_led_obj(i + obj_offset, MyDecode.get_value_2())
                        if MyDecode.get_value_1() == 19:
                            for i in pix_array_19:
                                MyWS2812.set_led_obj(i + obj_offset, MyDecode.get_value_2())
                        if MyDecode.get_value_1() == 20:
                            for i in pix_array_20:
                                MyWS2812.set_led_obj(i + obj_offset, MyDecode.get_value_2())
                        #=======================================================================

                if MyDecode.get_cmd_1() == "test":
                    #print("Test")
                    if MyDecode.get_cmd_2() == "led":
                        #print("LED")
                        MyWS2812.test_led(MyDecode.get_value_1(), MyDecode.get_value_2())
                

        blink_couter = blink_couter + 1
        # Loop-Delay !!!
        time.sleep(0.01)        # 10ms
        


    print("=== End of Main ===")

# ==============================================================================
# ==============================================================================
    
# ###############################################################################
# ### Main                                                                    ###
# ###############################################################################


if __name__ == "__main__":

    if MyModule.inc_ws2812:
        #print("WS2812 -> Load-Module")
        import libs.module_ws2812_v2 as MyWS2812         # Modul WS2812  -> WS2812-Ansteuerung
        #print("WS2812 -> Setup")
        MyWS2812.setup_ws2812()
        ### Test ###
        #print("WS2812 -> Run self test")
        MyWS2812.self_test()
        #print("WS2812 -> Blink Test")
        #MyWS2812.do_blink_test()
        #print("WS2812 -> Dot-Test")
        #MyWS2812.do_dot_test()

    if MyModule.inc_decoder:
        #print("Decode -> Load-Module")
        import libs.module_decode as MyDecode
        #print("Decode -> Setup")
        MyDecode.decode_setup()
        ### Test ###
        #print("Decode -> Test")
        #MyDecode.decode_input("Test")

    if MyModule.inc_serial:
        #print("Serial-COM -> Load-Module")
        import libs.module_serial as MySerial
        #print("Serial-Con -> Setup")
        MySerial.sercon_setup()
        ### Test ###
        #print("Serial-Con -> Test")
        #MySerial.sercon_write_out("Start Test")

    main()      # Start Main $$$

# Normal sollte das Programm hier nie ankommen !
print("___End of Programm___ !!!")

# ##############################################################################
