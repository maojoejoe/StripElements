# StripElements.py
# 
# Joseph Ni
# v0.3
# 
# Notes:
# Basic functionality implemented. Strips tags and specific lines of code. 
#   1) Need better exception handling.
#   2) Need ability to strip specific elements that vary but share a pattern:
#       i.e. <something class = "blahblah" style = "style123">(blah blah blah)</something> 
#            <something class = "blahblah" style = "style456">(blah blah blah)</something> 
#       detect: <something class = "blahblah" and strip the rest of that tag.
#   3) Need friendlier directory navigation modding

import bs4

try:
#=Adjust navigation through directory of files. 
# If your files don't follow a set naming convention, 
# this will require serious modification
    for num in range(288,291):
        # pageNum is the naming convention of the files in the directory. change as needed
        # I was stripping overlays from 291 html pages from an online textbook 
        pageNum = 'page' + str(num) + '.html'
        print("Stripping " + pageNum)

#=Load file : change directory as needed.
        with open("Offline TextBook Element Stripper/rawPages/%s" %pageNum, 'r', encoding='utf-8') as inf:
            #store in soup
            soup = bs4.BeautifulSoup(inf, features="html.parser")

#=Removing all instances of an HTML tag
            [e.extract() for e in soup.findAll('script')]
            # change 'script' to desired the html tag type + their contained contents to remove

#=Removing all instances of a specific element
        for element in soup.findAll('<div class="ui-dialog ui-widget ui-widget-content ui-corner-all ui-front ui-dialog-login ui-draggable" tabindex="-1" role="dialog" aria-describedby="general_dialog_outer_1" aria-labelledby="ui-id-1" style="height: auto; width: 680px; top: 128.5px; left: 151px; display: block; z-index: 101; padding: 0px;"><div class="ui-dialog-titlebar ui-widget-header ui-corner-all ui-helper-clearfix ui-draggable-handle" style="display: none;"><span id="ui-id-1" class="ui-dialog-title">Error calling NCIA service login2</span><button type="button" class="ui-button ui-widget ui-state-default ui-corner-all ui-button-icon-only ui-dialog-titlebar-close" role="button" title="Close" style="display: none;"><span class="ui-button-icon-primary ui-icon ui-icon-closethick"></span><span class="ui-button-text">Close</span></button></div><div id="general_dialog_outer_1" class="ui-dialog-content ui-widget-content" style="width: auto; min-height: 96px; max-height: 703px; height: auto; padding: 0px;"><div id="login_dialog"><div id="login_dialog_top_msg"><img id="login_dialog_close" role="button" alt="Close this dialog" src="services/../ncia_common/images/dialog_close_alt.png"><div id="login_dialog_seagull"><img id="login_norton_seagull" src="services/../ncia_common/images/seagull_black_icon_transparent.png" alt=""></div><img src="product/images/ebook_icon_brown.png" style="height:50px; margin:5px 10px 10px 0; float:left" alt=""><div id="login_top_msg_header">Interactive Ebook Edition of</div><br><div id="login_top_msg_title">Psychological Science, Sixth Edition</div><br><div id="login_top_msg_author"></div></div><div id="login_dialog_inner"><div id="login_dialog_error_msg" role="alert" aria-live="assertive"><b>Error:</b> Error calling NCIA service login2</div><fieldset><div><legend class="login_dialog_step_header">Have you already registered for ebook?</legend><div id="login_dialog_div_2"><input type="radio" name="register_login_choice" id="register_login_choice_login" value="login"> <label for="register_login_choice_login" style="text-decoration: none;"><span><span class="ncia_button_color_background"></span></span>Yes, I want to <b>sign in</b>:</label></div><div id="login_dialog_div_3"><span class="login_dialog_text_input_background"></span><input type="email" autocorrect="off" autocapitalize="off" class="login_dialog_text_input" id="username" placeholder="My e-mail address is…"></div><label for="username" class="login_dialog_hidden">Email</label><div id="login_dialog_div_4"><span class="login_dialog_text_input_background"></span><input type="password" id="password" class="login_dialog_text_input" placeholder="My password is…"><label for="password" class="login_dialog_hidden">Password</label><div id="login_dialog_forgot_password_link"><a style="font-size:.9em; font-weight:normal" id="forgot_password_link">Forgot your password?</a>   </div></div><div id="login_dialog_div_5"><input type="radio" name="register_login_choice" id="register_login_choice_register" value="register" checked=""> <label for="register_login_choice_register"><span><span class="ncia_button_color_background"></span></span>No, I need to <b>register, purchase, or sign up for trial access</b>.</label></div></div></fieldset><button id="login_dialog_button" class="ui-button ui-widget ui-state-default ui-corner-all ui-button-text-only" role="button"><span class="ui-button-text"><img alt="" src="services/../ncia_common/images/login_button_arrow.png" class="login_button_arrow_reverse"> &nbsp; Register, Purchase, or Sign Up for Trial Access</span></button><div id="login_dialog_help_div"><i>Need help? Contact <a tabindex="-1" href="http://books.wwnorton.com/books/support/" target="customer_support">W. W. Norton Customer Support</a></i></div></div></div></div></div>'):
            if element.string :
                element.string.replace_with(i.string.replace('<div class="ui-dialog ui-widget ui-widget-content ui-corner-all ui-front ui-dialog-login ui-draggable" tabindex="-1" role="dialog" aria-describedby="general_dialog_outer_1" aria-labelledby="ui-id-1" style="height: auto; width: 680px; top: 128.5px; left: 151px; display: block; z-index: 101; padding: 0px;"><div class="ui-dialog-titlebar ui-widget-header ui-corner-all ui-helper-clearfix ui-draggable-handle" style="display: none;"><span id="ui-id-1" class="ui-dialog-title">Error calling NCIA service login2</span><button type="button" class="ui-button ui-widget ui-state-default ui-corner-all ui-button-icon-only ui-dialog-titlebar-close" role="button" title="Close" style="display: none;"><span class="ui-button-icon-primary ui-icon ui-icon-closethick"></span><span class="ui-button-text">Close</span></button></div><div id="general_dialog_outer_1" class="ui-dialog-content ui-widget-content" style="width: auto; min-height: 96px; max-height: 703px; height: auto; padding: 0px;"><div id="login_dialog"><div id="login_dialog_top_msg"><img id="login_dialog_close" role="button" alt="Close this dialog" src="services/../ncia_common/images/dialog_close_alt.png"><div id="login_dialog_seagull"><img id="login_norton_seagull" src="services/../ncia_common/images/seagull_black_icon_transparent.png" alt=""></div><img src="product/images/ebook_icon_brown.png" style="height:50px; margin:5px 10px 10px 0; float:left" alt=""><div id="login_top_msg_header">Interactive Ebook Edition of</div><br><div id="login_top_msg_title">Psychological Science, Sixth Edition</div><br><div id="login_top_msg_author"></div></div><div id="login_dialog_inner"><div id="login_dialog_error_msg" role="alert" aria-live="assertive"><b>Error:</b> Error calling NCIA service login2</div><fieldset><div><legend class="login_dialog_step_header">Have you already registered for ebook?</legend><div id="login_dialog_div_2"><input type="radio" name="register_login_choice" id="register_login_choice_login" value="login"> <label for="register_login_choice_login" style="text-decoration: none;"><span><span class="ncia_button_color_background"></span></span>Yes, I want to <b>sign in</b>:</label></div><div id="login_dialog_div_3"><span class="login_dialog_text_input_background"></span><input type="email" autocorrect="off" autocapitalize="off" class="login_dialog_text_input" id="username" placeholder="My e-mail address is…"></div><label for="username" class="login_dialog_hidden">Email</label><div id="login_dialog_div_4"><span class="login_dialog_text_input_background"></span><input type="password" id="password" class="login_dialog_text_input" placeholder="My password is…"><label for="password" class="login_dialog_hidden">Password</label><div id="login_dialog_forgot_password_link"><a style="font-size:.9em; font-weight:normal" id="forgot_password_link">Forgot your password?</a>   </div></div><div id="login_dialog_div_5"><input type="radio" name="register_login_choice" id="register_login_choice_register" value="register" checked=""> <label for="register_login_choice_register"><span><span class="ncia_button_color_background"></span></span>No, I need to <b>register, purchase, or sign up for trial access</b>.</label></div></div></fieldset><button id="login_dialog_button" class="ui-button ui-widget ui-state-default ui-corner-all ui-button-text-only" role="button"><span class="ui-button-text"><img alt="" src="services/../ncia_common/images/login_button_arrow.png" class="login_button_arrow_reverse"> &nbsp; Register, Purchase, or Sign Up for Trial Access</span></button><div id="login_dialog_help_div"><i>Need help? Contact <a tabindex="-1" href="http://books.wwnorton.com/books/support/" target="customer_support">W. W. Norton Customer Support</a></i></div></div></div></div></div>', ''))

#=Overwrite old file
        with open("Offline TextBook Element Stripper/rawPages/%s" %pageNum, "w") as outf:
            outf.write(str(soup))

#As long as the desired elements are stripped, continue. 
except Exception:
    pass     


