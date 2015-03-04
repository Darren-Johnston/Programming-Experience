str = argument0; // total string to be displayed
color = argument1; // color of text
count = argument2; // current placeholder in text
spe = argument3; // integer determining text speed
var length = string_length(str);

draw_set_color(color);
var newString = string_copy(str, 0, count);
draw_text(x, y, newString);

if (count < length){
    if (count + spe < length){
        for (i = 0; i < spe; i++){
            count = scr_inc(count);
        }
    }
    else{
        for (i = 0; i < length; i++){
            count = scr_inc(count);
        }
    }
}
return count;
