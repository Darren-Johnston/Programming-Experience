array = argument0;
maxLetters = argument1;
var letPerLine = maxLetters;

var totalString = "", numLetters = 0;

for (i = 0; i < array_length_1d(array); i++){
    numLetters = string_length(array[i]);
    if (numLetters > maxLetters){
        totalString = totalString + "#" + array[i];
        maxLetters = letPerLine;
    }
    else{
        totalString += array[i];
        maxLetters -= numLetters;
    }
}

return totalString;