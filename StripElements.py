# StripElements.py
# 
# Joseph Ni
# v0.35
# 
# Notes: Improved Readability and functionality. 
# Applies one set of editing rules to a directory of sorted html files.
#   1) Need ability to strip specific elements that vary but share a pattern:
#       i.e. <something class = "blahblah" style = "style123">(blah blah blah)</something> 
#            <something class = "blahblah" style = "style456">(blah blah blah)</something> 
#       detect: <something class = "blahblah" and strip the rest of that tag.


import bs4
import os
print('Beginning.\n')


#===USER INPUT=========#
#=Adjust navigation through directory of files. 
#=If your files don't follow a set naming convention, this will require serious modification.
firstNum = 0
lastNum = 20
#======================#
try:
    for num in range(firstNum, lastNum + 1):
        # filename is the naming convention of the files in the directory. change as needed
        filename = 'page' + str(num) + '.html'
        # My files were in the format of page1.html, page2.html, page3.html ...

    #1 Load file : change directory as needed.
        directory = 'testingPages/'

        if (os.path.isfile(directory + '%s' %filename)):
            with open(directory + '%s' %filename, 'rb') as inf: #rb, or read binary, deals with encoding not recognizing bytes
                soup = bs4.BeautifulSoup(inf, features="html.parser")
                print(filename + ' loaded')
        else: 
            print('ERROR: ' + filename + ' was not found. Check your directory!\n')
            answer = input("Would you like to continue? (y/n)")
            if (answer is "y"): 
                continue
            elif (answer is "n"): 
                break
            else:
                print("Answer invalid. Canceling operations.")
                break

    #2 Removing all instances of an HTML tag
        tag = 'script'
        if tag in soup:
            [e.extract() for e in soup.findAll(tag)]
            # change 'script' to desired the html tag type and their contained contents to remove
        else: 
            print('Desired html tag: "' + tag + '" not found in ' + filename + '.')

    #3 Removing all instances of a specific element
        element = '<div class="ui-dialog ui-widget ui-widget-content ui-corner-all ui-front ui-dialog-login ui-draggable" tabindex="-1" role="dialog" aria-describedby="general_dialog_outer_1" aria-labelledby="ui-id-1" style="height: auto; width: 680px; top: 128.5px; left: 151px; display: block; z-index: 101; padding: 0px;"><div class="ui-dialog-titlebar ui-widget-header ui-corner-all ui-helper-clearfix ui-draggable-handle" style="display: none;"><span id="ui-id-1" class="ui-dialog-title">Error calling NCIA service login2</span><button type="button" class="ui-button ui-widget ui-state-default ui-corner-all ui-button-icon-only ui-dialog-titlebar-close" role="button" title="Close" style="display: none;"><span class="ui-button-icon-primary ui-icon ui-icon-closethick"></span><span class="ui-button-text">Close</span></button></div><div id="general_dialog_outer_1" class="ui-dialog-content ui-widget-content" style="width: auto; min-height: 96px; max-height: 703px; height: auto; padding: 0px;"><div id="login_dialog"><div id="login_dialog_top_msg"><img id="login_dialog_close" role="button" alt="Close this dialog" src="services/../ncia_common/images/dialog_close_alt.png"><div id="login_dialog_seagull"><img id="login_norton_seagull" src="services/../ncia_common/images/seagull_black_icon_transparent.png" alt=""></div><img src="product/images/ebook_icon_brown.png" style="height:50px; margin:5px 10px 10px 0; float:left" alt=""><div id="login_top_msg_header">Interactive Ebook Edition of</div><br><div id="login_top_msg_title">Psychological Science, Sixth Edition</div><br><div id="login_top_msg_author"></div></div><div id="login_dialog_inner"><div id="login_dialog_error_msg" role="alert" aria-live="assertive"><b>Error:</b> Error calling NCIA service login2</div><fieldset><div><legend class="login_dialog_step_header">Have you already registered for ebook?</legend><div id="login_dialog_div_2"><input type="radio" name="register_login_choice" id="register_login_choice_login" value="login"> <label for="register_login_choice_login" style="text-decoration: none;"><span><span class="ncia_button_color_background"></span></span>Yes, I want to <b>sign in</b>:</label></div><div id="login_dialog_div_3"><span class="login_dialog_text_input_background"></span><input type="email" autocorrect="off" autocapitalize="off" class="login_dialog_text_input" id="username" placeholder="My e-mail address is…"></div><label for="username" class="login_dialog_hidden">Email</label><div id="login_dialog_div_4"><span class="login_dialog_text_input_background"></span><input type="password" id="password" class="login_dialog_text_input" placeholder="My password is…"><label for="password" class="login_dialog_hidden">Password</label><div id="login_dialog_forgot_password_link"><a style="font-size:.9em; font-weight:normal" id="forgot_password_link">Forgot your password?</a>   </div></div><div id="login_dialog_div_5"><input type="radio" name="register_login_choice" id="register_login_choice_register" value="register" checked=""> <label for="register_login_choice_register"><span><span class="ncia_button_color_background"></span></span>No, I need to <b>register, purchase, or sign up for trial access</b>.</label></div></div></fieldset><button id="login_dialog_button" class="ui-button ui-widget ui-state-default ui-corner-all ui-button-text-only" role="button"><span class="ui-button-text"><img alt="" src="services/../ncia_common/images/login_button_arrow.png" class="login_button_arrow_reverse"> &nbsp; Register, Purchase, or Sign Up for Trial Access</span></button><div id="login_dialog_help_div"><i>Need help? Contact <a tabindex="-1" href="http://books.wwnorton.com/books/support/" target="customer_support">W. W. Norton Customer Support</a></i></div></div></div></div></div>'
        if element in soup:
            for el in soup.findAll(element):
                if el.string :
                    el.string.replace_with(el.string.replace(element, ''))
        else: 
            print('Desired element not found in ' + filename + '.')

    #4 Overwrite old file
        with open(directory + '%s' %filename, "w") as outf:
            outf.write(str(soup))
        print(filename + ' modified and saved.' + '\n')
except Exception as e:
    print(e)
finally:
    print('Completed.\n')