"""

  1. Detect new user come in
  2. Detect new user left
  3. post to chat
  4. take screen photo
  5. save screen photo to directory
  6. stich it all into mosaic image ( side mission )

"""

import time
import calendar
import re
import os

import module_mouse_coordinate_capture
import module_mouse_click
import module_screen_take_photo
import module_screen_read_photo
import module_screen_crop_and_save_photo
import module_keyboard_type


print("----- WELCOME-----")

print("First, please click on icon of 'Chat' Tab title header")
x_chat_title, y_chat_title = module_mouse_coordinate_capture.capture_coordinate()
print("  detected, ", x_chat_title, y_chat_title)

print("Second, please click on Chat Box")
x_chat_box, y_chat_box = module_mouse_coordinate_capture.capture_coordinate()
print("  detected, ", x_chat_box, y_chat_box)

print("Please click on icon of 'People (..)' Tab title header")
x_people_title, y_people_title = module_mouse_coordinate_capture.capture_coordinate()
print("  detected, ", x_people_title, y_people_title)

print("Please click on second line of guest list, where the guest's icon will be at")
x_guest_name, y_guest_name = module_mouse_coordinate_capture.capture_coordinate()
print("  detected, ", x_guest_name, y_guest_name)

print("Please click on Top Left Of guest's Headshot Photo on Screen")
x_top_left_headshot, y_top_left_headshot = module_mouse_coordinate_capture.capture_coordinate()
print("  detected, ", x_top_left_headshot, y_top_left_headshot)

print("Please click on Bottom Right Of guest's Headshot Photo on Screen")
x_bottom_right_headshot, y_bottom_right_headshot = module_mouse_coordinate_capture.capture_coordinate()
print("  detected, ", x_bottom_right_headshot, y_bottom_right_headshot)




print("----- CONFIGURATION COMPLETED -----")

time.sleep(3);

print("----- TAKING PHOTOS -----")

# Loop:
#  1. Capture Screen Shot, Parse Human Count
#  2. If !1 people, Click on Chat Tab
#  2.               Parse Name
#  2.               Print "Taking Picture in 3.."
#  2.               Print "Smile"
#  2.               Save file captured in step (1), cropped with top-left and bottom_right in config-gathering, and save as {guest-name}.png
#  2.               Print "Done, Thank you 'name', Please leave!"
#  2.               Click on People Tab
#  2. ElIf 1 people, Pass
#  2. Sleep 3 second

while True:

    module_mouse_click.click(x_people_title, y_people_title, True)

    # Sub Step A:
    scout_file_name = "photos/scouting.png"
    module_screen_take_photo.save_screen_shot(scout_file_name)
    text_guest_count = module_screen_read_photo.ocr_core(scout_file_name, x_people_title, y_people_title)

    count_human = 1;
    count_human_str_search = re.search(' \(([0-9]+)\)', text_guest_count)
    if count_human:
        count_human = int(count_human_str_search.group(1))

    print(count_human)
    # Sub Step B
    if count_human == 2:
        text_guest_name = module_screen_read_photo.ocr_core(scout_file_name, x_guest_name, y_guest_name).strip()
        print('Handling : ', text_guest_name)

        module_mouse_click.click(x_chat_title, y_chat_title, True)
        time.sleep(1)

        # Sub Step C, D
        module_keyboard_type.type_string('Taking picture in:  3, 2...')
        module_keyboard_type.enter()
        time.sleep(3)
        module_keyboard_type.type_string('Smile!')
        module_keyboard_type.enter()
        module_keyboard_type.enter()
        time.sleep(1)

        # Sub Step E: Save this image
        guest_file_name = './photos/{}__{}.png'.format(text_guest_name, str(calendar.timegm(time.gmtime())));
        module_screen_crop_and_save_photo.crop_and_save(scout_file_name, guest_file_name, x_top_left_headshot, y_top_left_headshot, x_bottom_right_headshot, y_bottom_right_headshot);


        # Sub Step F: Kick them out
        module_keyboard_type.type_string('Thank you {}, You can leave now!'.format(text_guest_name))
        module_keyboard_type.enter()
        module_keyboard_type.enter()

        time.sleep(5)

        # Sub Step G: Click on People Tab
        module_mouse_click.click(x_people_title, y_people_title, True)


    elif count_human > 2:
        print("TOO MANY PEOPLE")

    time.sleep(3)
