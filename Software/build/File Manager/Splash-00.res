tcl86t.dll      tk86t.dll       tk              __splash              �  �  �   �   Xtk\ttk\cursors.tcl tk\tk.tcl tk\ttk\ttk.tcl tk\ttk\utils.tcl tk\ttk\fonts.tcl tk\license.terms tk86t.dll tcl86t.dll tk\text.tcl VCRUNTIME140.dll proc _ipc_server {channel clientaddr clientport} {
set client_name [format <%s:%d> $clientaddr $clientport]
chan configure $channel \
-buffering none \
-encoding utf-8 \
-eofchar \x04 \
-translation cr
chan event $channel readable [list _ipc_caller $channel $client_name]
}
proc _ipc_caller {channel client_name} {
chan gets $channel cmd
if {[chan eof $channel]} {
chan close $channel
exit
} elseif {![chan blocked $channel]} {
if {[string match "update_text*" $cmd]} {
global status_text
set first [expr {[string first "(" $cmd] + 1}]
set last [expr {[string last ")" $cmd] - 1}]
set status_text [string range $cmd $first $last]
}
}
}
set server_socket [socket -server _ipc_server -myaddr localhost 0]
set server_port [fconfigure $server_socket -sockname]
set env(_PYIBoot_SPLASH) [lindex $server_port 2]
image create photo splash_image
splash_image put $_image_data
unset _image_data
proc canvas_text_update {canvas tag _var - -} {
upvar $_var var
$canvas itemconfigure $tag -text $var
}
package require Tk
set image_width [image width splash_image]
set image_height [image height splash_image]
set display_width [winfo screenwidth .]
set display_height [winfo screenheight .]
set x_position [expr {int(0.5*($display_width - $image_width))}]
set y_position [expr {int(0.5*($display_height - $image_height))}]
frame .root
canvas .root.canvas \
-width $image_width \
-height $image_height \
-borderwidth 0 \
-highlightthickness 0
.root.canvas create image \
[expr {$image_width / 2}] \
[expr {$image_height / 2}] \
-image splash_image
wm attributes . -transparentcolor magenta
.root.canvas configure -background magenta
pack .root
grid .root.canvas -column 0 -row 0 -columnspan 1 -rowspan 2
wm overrideredirect . 1
wm geometry . +${x_position}+${y_position}
wm attributes . -topmost 1
raise .�PNG

   IHDR   @   @   �iq�  �IDATx��KlE��ήI�8NҼ�J�@�@ĩ=p�$�����{�rG-z�B%��ġ)pN���&��/�Fi�&uv�����4�Sg�;K�'�;�����7��!""""b�"~D��t{e�W���+��e!���YY��l�[3��֜����G�i;�/�{^?Ekΰ��8�U�� �M�xѫ��~4�By���4�ȀfW��D4���*Pnz�?��u��B��P����c�/�x�D���]o<��8��+����C 2 �@�q^�Y�w�cw��u߱m��5�D��C�ګ��~�Ԧ�fe�t*\Èr@�+�l"�]�h]����`#pV�8�Ĳ0[S�63�Bc��m�B�[W�$�.���-��&f��r��_~õ��Bn�upW�1z�p��*��q�R����xw��7�	*��.�����Ze�b	Xdh��2!�$O�"���,�iI'�&/�����Z~	�����m�mS��s�� ��"�%}%��H+�����M������{B�aO�J`9��mܞ±w�PD;�R��7\�@;��f�bX�7�!0{����sv�F|���*ef���E���|����� hIY���� �5''�m#y�Мh�fm1��́��D`i��J����� �G�:�m����6��͝k�����! �Em���
m��7���^�F��.���.�A�����hk��P��>�x�Vi`�L����E�֡����ٚ� ��x��\��hU��*p���GKB�70��뵒�&~��蛛tկ�2��S���-s��}D��Usܾ2�U��7j��Ago�3�����;	��ͷ[� ����X7 9����5��tu�3�=�B5J��89qd'1B�E``P�=�D����q�D>��ʯKs�� �q���{��E1�f��!�j�LgP�$F"IGg��$SVOU����u��D)�T���-d�X��U] �8���"2K�+@�{���  �H�d��훎���L��d������zч�b�� ���q�H$��6 �3_E�N���Y�E�-R��lkUg�\���38�ў�V�Ώ�����L��4#��Y�U �	���>9'��|�d�.���x��B%������DDDDD�g�����nrq�    IEND�B`��PNG

   IHDR   @   @   �iq�  �IDATx��KlE��ήI�8NҼ�J�@�@ĩ=p�$�����{�rG-z�B%��ġ)pN���&��/�Fi�&uv�����4�Sg�;K�'�;�����7��!""""b�"~D��t{e�W���+��e!���YY��l�[3��֜����G�i;�/�{^?Ekΰ��8�U�� �M�xѫ��~4�By���4�ȀfW��D4���*Pnz�?��u��B��P����c�/�x�D���]o<��8��+����C 2 �@�q^�Y�w�cw��u߱m��5�D��C�ګ��~�Ԧ�fe�t*\Èr@�+�l"�]�h]����`#pV�8�Ĳ0[S�63�Bc��m�B�[W�$�.���-��&f��r��_~õ��Bn�upW�1z�p��*��q�R����xw��7�	*��.�����Ze�b	Xdh��2!�$O�"���,�iI'�&/�����Z~	�����m�mS��s�� ��"�%}%��H+�����M������{B�aO�J`9��mܞ±w�PD;�R��7\�@;��f�bX�7�!0{����sv�F|���*ef���E���|����� hIY���� �5''�m#y�Мh�fm1��́��D`i��J����� �G�:�m����6��͝k�����! �Em���
m��7���^�F��.���.�A�����hk��P��>�x�Vi`�L����E�֡����ٚ� ��x��\��hU��*p���GKB�70��뵒�&~��蛛tկ�2��S���-s��}D��Usܾ2�U��7j��Ago�3�����;	��ͷ[� ����X7 9����5��tu�3�=�B5J��89qd'1B�E``P�=�D����q�D>��ʯKs�� �q���{��E1�f��!�j�LgP�$F"IGg��$SVOU����u��D)�T���-d�X��U] �8���"2K�+@�{���  �H�d��훎���L��d������zч�b�� ���q�H$��6 �3_E�N���Y�E�-R��lkUg�\���38�ў�V�Ώ�����L��4#��Y�U �	���>9'��|�d�.���x��B%������DDDDD�g�����nrq�    IEND�B`�