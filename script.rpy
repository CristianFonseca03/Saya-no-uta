define c = Character(None, kind=nvl, what_prefix="{cps=20}\"", what_suffix="\"")
define f = Character(None, kind=nvl, what_prefix="{cps=20}\"", what_suffix="\"")
define k = Character(None, kind=nvl, what_prefix="{cps=20}\"", what_suffix="\"")
define o = Character(None, kind=nvl, what_prefix="{cps=20}\"", what_suffix="\"")
define y = Character(None, kind=nvl, what_prefix="{cps=20}\"", what_suffix="\"")
define narrator = Character(None, kind=nvl, what_prefix="{cps=20}")
define gui.nvl_text_ypos = 70
define gui.nvl_text_xpos= 0.17
define gui.nvl_height= 0
define gui.nvl_spacing= 80
define gui.nvl_text_width= 700
define config.window_hide_transition = Dissolve(.5)
define config.window_show_transition = Dissolve(.5)

label start:
    call ch1_main
    call ch1_2_main
