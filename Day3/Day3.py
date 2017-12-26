import math;

def steps_to_center(input):
    layer = math.floor(math.ceil(math.sqrt(input))/2)+1;
    y_value = layer-1;
    num_lower_right = (2*layer-1)**2;
    length_side = math.sqrt(num_lower_right)-1;
    num_lower_left = num_lower_right - length_side; 
    num_top_left = num_lower_left - length_side;
    num_top_right = num_top_left - length_side;
    
    if input <= num_lower_right and input >= num_lower_left:
        center_num = num_lower_right - y_value;
        x_value = input - center_num;
        result = x_value + y_value;
        print(result);
    
    elif input < num_lower_left and input > num_top_left:
        center_num = num_lower_left - y_value;
        x_value = input - center_num;
        result = x_value + y_value;
        print(result);
        
    elif input < num_top_left and input > num_top_right:
        center_num = num_top_left - y_value;
        x_value = input - center_num;
        result = x_value + y_value;
        print(result);
        
    elif input < num_top_right and input > num_top_right - math.sqrt(input)-1:
        center_num = num_top_right - y_value;
        x_value = input - center_num;
        result = x_value + y_value;
        print(result);
        
        
steps_to_center(289326);