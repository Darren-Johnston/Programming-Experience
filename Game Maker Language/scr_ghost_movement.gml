//spr_right = 0
//spr_down = 1
//spr_left = 2
//spr_up = 3

//part_particles_create(global.redline, x + 16, y + 16 , global.pacline, 1)
var spe = 4, org = 4, nSpe = -4;

if (go){

//If you hit a wall, then turn in the best direction
    if place_meeting(x + hspeed, y, obj_wall){
        if obj_pacman.y > y{
            if place_free(x, y + spe){
                hspeed = 0
                vspeed = spe
                image_n = 1
            }
            else{
                hspeed = 0
                vspeed = -spe
                image_n = 3
            }
        }
        else{
            if place_free(x, y - spe){
                hspeed = 0
                vspeed = -spe 
                image_n = 3
            }
            else{
                hspeed = 0
                vspeed = spe 
                image_n = 1
                }
        }
    }
    
    if place_meeting(x, y + vspeed, obj_wall){
        if obj_pacman.x > x{
            if place_free(x + spe, y){
                vspeed = 0
                hspeed = spe 
                image_n = 0
                }
             else{
                vspeed = 0
                hspeed = -spe
                image_n = 2
                }
        }
        else{
            if place_free(x - spe, y){
                vspeed = 0
                hspeed = -spe
                image_n = 2
            }
            else{
                vspeed = 0
                hspeed = spe 
                image_n = 0
            }
        }
    }
    
// Check if pacman is on the same y and then run after him
if (!global.ghostScare) and (!obj_pacman.death){

   if (obj_pacman.y == y){
       if obj_pacman.x < x{
          if place_free(x-spe, y){
             vspeed = 0
              hspeed = -spe
              image_n = 2
            }
        }
        else{
            if place_free(x+spe, y){
                vspeed = 0
                hspeed = spe
                image_n = 0
            }
        }
    }
    
// Check if pacman is on the same x and if so then run after him
    if (obj_pacman.x == x){
       if obj_pacman.y < y{
          if place_free(x, y - spe){
             hspeed = 0
              vspeed = -spe
              image_n = 3
            }
        }
        else{
            if place_free(x, y + spe){
                hspeed = 0
                vspeed = spe 
                image_n = 1
            }
        }
        
    }
}

if (global.ghostScare and speedReverse){
vspeed *= -1
hspeed *= -1
speedReverse = false
}

if (!global.ghostScare and !speedReverse){
vspeed *= -1
hspeed *= -1
speedReverse = true
}

}