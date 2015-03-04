var str = argument0 // String to turn into array
var splitter = argument1; // Character to split at
var array, length = string_length(str),
count = 0, index = 0, arrayIndex = 0;

for (i = 0; i <= length; i++){
    if (string_char_at(str, i) == splitter){
        array[arrayIndex] = string_copy(str, index, count-1);
        array[arrayIndex] = array[arrayIndex] + " ";
        arrayIndex += 1;
        index = i+1;  
        count = 0;
    }
    count += 1;
}

return array;
