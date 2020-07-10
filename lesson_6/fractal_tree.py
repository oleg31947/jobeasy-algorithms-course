# 1) Create a function draw_branches, which should draw to branches of a tree from one point.
# The function should have the following parameters:
# -the beginning where you start drawing
# -angle of the branches
# - length of the branches
#
# 2) Make draw_branches recursive:
# -- verify the length of the branches, do not draw branches shorter than 10
# - make the function call itself two times and draw branches from the endpoint of the previous branch. The angle of
# the branches should be the same and the length of the branches should decrease by 0.75.


import simple_draw as sd


def draw_branches(start_point, angle, length):
    current_point = start_point
    left_angle = angle - 30
    right_angle = angle + 30
    branch_path_left = sd.get_vector(start_point=current_point, angle=left_angle, length=length, width=2)
    branch_path_right = sd.get_vector(start_point=current_point, angle=right_angle, length=length, width=2)
    sd.line(start_point=current_point, end_point=branch_path_left.end_point, width=2)
    sd.line(start_point=current_point, end_point=branch_path_right.end_point, width=2)
    if length > 2:
        draw_branches(start_point=branch_path_left.end_point, angle=left_angle, length=length * 0.75)
        draw_branches(start_point=branch_path_right.end_point, angle=right_angle, length=length * 0.75)


root_point = sd.get_point(300, 30)
draw_branches(start_point=root_point, angle=90, length=100)
