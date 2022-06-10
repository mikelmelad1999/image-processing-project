
#import libraries 


from pickletools import decimalnl_long
from tkinter import *
from tkinter import ttk
from turtle import width
from unicodedata import decimal
from numpy import integer, size
from ttkthemes import ThemedTk
from functions import *


ocv = OpenCV()
root = ThemedTk()
root.geometry("800x700")
root.title("Image Processing project")
style = ttk.Style(root)
style.theme_use('xpnative')




def Make_Label(command, frame):
    for labels in frame.grid_slaves():
        labels.grid_forget()
    ttk.Label(
        frame, 
        image = command).grid(row = 0, column = 0)

def Display(command, frame0, frame1, frame2):
    Make_Label(command[0], frame0)
    if frame1 == None and frame2 == None:
        pass
    elif frame2 == None:
        Make_Label(command[1], frame1)
    else:
        Make_Label(command[1], frame1)
        Make_Label(command[2], frame2)





color_conversion_frame = ttk.LabelFrame(
    root, 
    text = 'Convert' )
color_conversion_frame.grid(
    row = 0, column = 2, 
    padx = 3, pady = 15, 
    columnspan = 1, 
    sticky = W)


default_color_radiobutton = ttk.Radiobutton(
    color_conversion_frame, 
    text = 'Default Color', 
    value = 0, 
    width=30 ,

    command = lambda: Display(
        ocv.DefaultColor(), 
        original_image_frame, None, None))
gray_color_radiobutton = ttk.Radiobutton(
    color_conversion_frame, 
    text = 'Gray Color', 
    value = 1, 
    width= 30 ,
    command = lambda: Display(
        ocv.GrayColor(), 
        original_image_frame, None, None))

default_color_radiobutton.grid(
    row = 0, column = 0, 
    sticky = W)
gray_color_radiobutton.grid(
    row = 1, column = 0, 
    sticky = W)



transformations_frame = ttk.LabelFrame(
    root, 
    text = '')
transformations_frame.grid(
    row = 0, column = 3, 
    rowspan = 7, 
    padx = 7, pady = 7)

original_image_frame = ttk.LabelFrame(
    transformations_frame, 
    text = 'Original Image', 
    width = 320, height = 200)
original_image_frame.grid(
    row = 0, 
    padx = 7, pady = 7, 
    sticky = NSEW)

filter_frame = ttk.LabelFrame(
    transformations_frame, 
    text = 'Filter', 
    width = 320, height = 200)
filter_frame.grid(
    row = 1, 
    padx = 7, pady = 7, 
    sticky = NSEW)

filtered_image_frame = ttk.LabelFrame(
    transformations_frame, 
    text = 'result', 
    width = 320, height = 200)
filtered_image_frame.grid(
    row = 2, 
    padx = 7, pady = 7, 
    sticky = NSEW)



image_load_frame = ttk.LabelFrame(
    root, 
    text = 'Load Image')
image_load_frame.grid(
    row = 0, column = 0, 
    columnspan = 2, 
    padx = 7, pady = 7)


image_location_button = ttk.Button(
    image_load_frame, 
    text = 'Open', 
    width = 40,
    command = lambda: Display(
        ocv.OpenImage(), 
        original_image_frame, None, None))
image_location_button.grid(
    row = 0, 
    column = 1)




point_transformations_frame = ttk.LabelFrame(
    root, 
    text = "Point Transform op's")
point_transformations_frame.grid(
    row = 1, column = 0, 
    padx = 7, pady = 7, 
    columnspan = 3)
    

brightness_adjustment_button = ttk.Button(
    point_transformations_frame, 
    text = 'Brightness Adjustment', 
    width = 70, 
    command = lambda: Display(
        ocv.AdjustBrightness(), 
        original_image_frame, None, None))
contrast_adjustment_button = ttk.Button(
    point_transformations_frame, 
    text = 'Contrast Adjustment', 
    width = 70, 
    command = lambda: Display(
        ocv.AdjustContrast(), 
        original_image_frame, None, None))
histogram_button = ttk.Button(
    point_transformations_frame, 
    text = 'Histogram', 
    width = 70, 
    command = lambda: Display(
        ocv.MakeHistogram(), 
        original_image_frame, 
        filter_frame, None))
histogram_equalization_button = ttk.Button(
    point_transformations_frame, 
    text = 'Histogram Equalization', 
    width = 70, 
    command = lambda: Display(
        ocv.EqualizeHistogram(), 
        original_image_frame, 
        filter_frame, 
        filtered_image_frame))

brightness_adjustment_button.grid(
    row = 0, column = 0, 
    padx = 7, pady = 3)
contrast_adjustment_button.grid(
    row = 1, column = 0, 
    padx = 7, pady = 3)
histogram_button.grid(
    row = 2, column = 0, 
    padx = 7, pady = 3)
histogram_equalization_button.grid(
    row = 3, column = 0, 
    padx = 7, pady = 3)




local_transformations_frame = ttk.LabelFrame(
    root, 
    text = "Local Transform op's")
local_transformations_frame.grid(
    row = 3, column = 0, 
    padx = 7, pady = 7, 
    columnspan = 3)

smoothing_filters_frame = ttk.LabelFrame(
    local_transformations_frame, 
    text = '')
smoothing_filters_frame.grid(
    row = 0, column = 0, 
    padx = 7, pady = 7)

edge_detection_filters_frame = ttk.LabelFrame(
    local_transformations_frame, 
    text = 'Edge Detection Filters')
edge_detection_filters_frame.grid(
    row = 0, column = 1, 
    rowspan = 5, 
    padx = 7, pady = 7)

low_pass_filter_button = ttk.Button(
    smoothing_filters_frame, 
    text = 'Low-Pass Filter', 
    width = 21, 
    command = lambda: Display(
        ocv.LowPassFilter(), 
        filtered_image_frame, None, None))
High_pass_filter_button = ttk.Button(
    smoothing_filters_frame, 
    text = 'High-Pass Filter', 
    width = 21, 
    command = lambda: Display(
        ocv.HighPassFilter(), 
        filtered_image_frame, None, None))
median_filter_button = ttk.Button(
    smoothing_filters_frame, 
    text = 'Median Filtering', 
    width = 21, 
    command = lambda: Display(
        ocv.MedianFilter(), 
        filtered_image_frame, None, None))
averaging_filter_button = ttk.Button(
    smoothing_filters_frame, 
    text = 'Averaging Filtering', 
    width = 21, 
    command = lambda: Display(
        ocv.AveragingFilter(), 
        filtered_image_frame, None, None))

low_pass_filter_button.grid(
    row = 0, column = 0, 
    padx = 7, pady = 3)
High_pass_filter_button.grid(
    row = 1, column = 0, 
    padx = 7, pady = 3)
median_filter_button.grid(
    row = 2, column = 0, 
    padx = 7, pady = 3)
averaging_filter_button.grid(
    row = 3, column = 0, 
    padx = 7, pady = 3)

Gaussian_filter_radioutton = ttk.Radiobutton(
    edge_detection_filters_frame, 
    text = 'Gaussian Filter', 
    value = 2, 
    command = lambda: Display(
        ocv.GaussianFilter(), 
        filtered_image_frame, None, None))
laplacian_filter_radiobutton = ttk.Radiobutton(
    edge_detection_filters_frame, 
    text = 'Laplacian Filter', 
    value = 3, 
    command = lambda: Display(
        ocv.LaplacianFilter(), 
        filtered_image_frame, None, None))
log_filter_radiobutton = ttk.Radiobutton(
    edge_detection_filters_frame, 
    text = 'lap of gau(log)', 
    value = 4, 
    command = lambda: Display(
        ocv.LoGFilter(), 
        filtered_image_frame, None, None))
canny_method_radiobutton = ttk.Radiobutton(
    edge_detection_filters_frame, 
    text = 'Canny Method', 
    value = 5, 
    command = lambda: Display(
        ocv.CannyMethod(), 
        original_image_frame, 
        filtered_image_frame, None))
vertical_sobel_radiobutton = ttk.Radiobutton(
    edge_detection_filters_frame, 
    text = 'Vert.Sobel', 
    value = 6, 
    command = lambda: Display(
        ocv.VerticalSobel(), 
        original_image_frame, 
        filtered_image_frame, None))
horizontal_sobel_radiobutton = ttk.Radiobutton(
    edge_detection_filters_frame, 
    text = 'Horiz.Sobel', 
    value = 7, 
    command = lambda: Display(
        ocv.HorizontalSobel(), 
        original_image_frame, 
        filtered_image_frame, None))
vertical_perwitt_radiobutton = ttk.Radiobutton(
    edge_detection_filters_frame, 
    text = 'Vert.Perwitt', 
    value = 8, 
    command = lambda: Display(
        ocv.VerticalPerwitt(), 
        original_image_frame, 
        filtered_image_frame, None))
horizontal_perwitt_radiobutton = ttk.Radiobutton(
    edge_detection_filters_frame, 
    text = 'Horiz.Perwitt', 
    value = 9, 
    command = lambda: Display(
        ocv.HorizontalPerwitt(), 
        original_image_frame, 
        filtered_image_frame, None))

Gaussian_filter_radioutton.grid(
    row = 0, column = 1, 
    sticky = W)
laplacian_filter_radiobutton.grid(
    row = 0, column = 0, 
    sticky = W)
log_filter_radiobutton.grid(
    row = 1, column = 2, 
    sticky = W)
canny_method_radiobutton.grid(
    row = 1, column = 3, 
    sticky = W)
vertical_sobel_radiobutton.grid(
    row = 0, column = 2, 
    sticky = W)
horizontal_sobel_radiobutton.grid(
    row = 0, column = 3, 
    sticky = W)
vertical_perwitt_radiobutton.grid(
    row = 1, column = 0, 
    sticky = W)
horizontal_perwitt_radiobutton.grid(
    row = 1, column = 1, 
    sticky = W)



global_transformations_frame = ttk.LabelFrame(
    root, 
    text = "Global Transforma op's")
global_transformations_frame.grid(
    row = 5, column = 0, 
    padx = 7, pady = 7)

line_detection_button = ttk.Button(
    global_transformations_frame, 
    text = 'Line Detection Using Hough Transform', 
    width = 40, 
    command = lambda: Display(
        ocv.LineDetection(), 
        original_image_frame, 
        filtered_image_frame, None))
circle_detection_button = ttk.Button(
    global_transformations_frame, 
    text = 'Circle Detection Using Hough Transform', 
    width = 40, 
    command = lambda: Display(
        ocv.CircleDetection(), 
        original_image_frame, 
        filtered_image_frame, None))

line_detection_button.grid(
    row = 0, column = 0, 
    padx = 7, pady = 3)
circle_detection_button.grid(
    row = 1, column = 0, 
    padx = 7, pady = 3)




morphological_operations_frame = ttk.LabelFrame(
    root, 
    text = "Morphological Op's")
morphological_operations_frame.grid(
    row = 5, column = 1, 
    padx = 7, pady = 7, 
    columnspan = 2)

kernel_type_frame = ttk.LabelFrame(
    morphological_operations_frame, 
    text = 'Choose Kernel Type')
kernel_type_frame.grid(
    row = 0, column = 3, 
    padx = 7, pady = 7, 
    rowspan = 3)


dilation_button = ttk.Button(
    morphological_operations_frame, 
    text = 'Dilation', 
    width= 30, 
    command = lambda: Display(
        ocv.Dilation(), 
        filtered_image_frame, None, None))
erosion_button = ttk.Button(
    morphological_operations_frame, 
    text = 'Erosion', 
    width = 30, 
    command = lambda: Display(
        ocv.Erosion(), 
        filtered_image_frame, None, None))
close_button = ttk.Button(
    morphological_operations_frame, 
    text = 'Close', 
    width = 30, 
    command = lambda: Display(
        ocv.Close(), 
        filtered_image_frame, None, None))
open_button = ttk.Button(
    morphological_operations_frame, 
    text = 'Open', 
    width = 30, 
    command = lambda: Display(
        ocv.Open(), 
        filtered_image_frame, None, None))

dilation_button.grid(
    row = 0, column = 0, 
    sticky = W)
erosion_button.grid(
    row = 1, column = 0, 
    sticky = W)
close_button.grid(
    row = 2, column = 0, 
    sticky = W)
open_button.grid(
    row = 3, column = 0, 
    sticky = W)



save_button = ttk.Button(
    root, 
    text = 'Save result Image', 
    width = 21, 
    command = ocv.Save)
exit_button = ttk.Button(
    root, 
    text = 'Exit', 
    width = 17, 
    command =lambda: ocv.Exit(root))

save_button.grid(
    row = 6, column = 0, 
    columnspan = 2, 
    pady = 7)
exit_button.grid(
    row = 6, column = 1, 
    columnspan = 2, 
    pady = 7)


root.mainloop()