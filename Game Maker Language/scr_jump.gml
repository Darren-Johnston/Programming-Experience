//Must initialize gravSpeed and jump and doubleJump
jumpConst = argument0
gravConst = argument1
stopJump =  argument2
extraGrav = argument3
doubleOn = argument4
doubleConst = argument5
var const = 25, var isTrue = false


if (!jump){
    gravSpeed = 0
    for (i = 0; i < const; i++){
        if (!place_free(x, y-i)){
            isTrue = true
            break
        }
    }
    
    if (!isTrue){
        if (place_free(x,y-1)){
            if (keyboard_check_pressed(vk_space)){
                gravSpeed = -jumpConst
                jump = true
            }
        }
    }
    
    if (place_free(x,y+1)){//gravSpeed
        jump = true
    }
    else if (!place_free(x,y)){
        while (!place_free(x,y)){
            y -= 1
        }
    }
}

else if (jump){
    
    if (doubleOn){
        if (doubleJump){
            if (keyboard_check_pressed(vk_space)){
                if (place_free(x,y-doubleConst)){
                    gravSpeed = -doubleConst
                    doubleJump = false
                }
            }
        }
    }
    
    if (stopJump){
        if (sign(gravSpeed + extraGrav < 0)){
            if (keyboard_check_released(vk_space)){
                 gravSpeed += extraGrav
            }
        }
    }
    
    
    if (!place_free(x,y+gravSpeed)){ //gravSpeed
        if (sign(gravSpeed) <= 0){
            gravSpeed = 0
        }
        
        else if (sign(gravSpeed > 0)){
            gravSpeed = 0
            while (place_free(x,y+1)){
                y += 1
            }
            jump = false
            doubleJump = true
        }
    }
    else if (place_free(x,y+gravSpeed)){
        gravSpeed += gravConst
    }
}

y += gravSpeed
