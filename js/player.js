"use strict";

var gravity = 0.2;
var friction = 0.4;

var player = {
    x: 50,
    y: 50,
    x_v: 0,
    y_v: 0,
    jump : true,
    height: 34,
    width: 20
    };

function renderplayer(){
    // ctx.fillRect(0, 0, ctx.canvas.height, ctx.canvas.width);
    ctx.fillStyle = "#F08080";
    ctx.fillRect(player.x, player.y, player.width, player.height);
    }

function move() {
  if(player.jump == false) {
      player.x_v *= friction;
  }
  else {
      // If the player is in the air then apply the effect of gravity
      player.y_v += gravity;
  }

  player.jump = true;

  // Déplacements latéraux
  if(keys.left) {
      player.x_v = -2.5;
      if (colx()== true) {
        player.x += player.x_v;
      }
  }

  if(keys.right) {
      player.x_v = 2.5;
      if (colx()== true) {
        player.x += player.x_v;
      }
  }



  if (coly()==true) {
    player.y += player.y_v;
  }
  else {
    player.y_v = 0;
  }

}

function coly() {
  for (var i = 0; i < platforms.length; i++) {
    if (platforms[i].x < player.x+player.width && player.x+player.width < platforms[i].x+16 || platforms[i].x< player.x && player.x < platforms[i].x+16) {
      if (platforms[i].y < player.y+player.height+player.y_v && player.y+player.height+player.y_v < platforms[i].y+16) {
        return false;
      }
    }
  }
  return true;
}

function colx() {
  for (var i = 0; i < platforms.length; i++) {
    if (platforms[i].y < player.y+player.height-1 && player.y+player.height-1 < platforms[i].y+16
      || platforms[i].y<= player.y && player.y <= platforms[i].y+16
      ||platforms[i].y < player.y+(player.height/2)-1 && player.y+(player.height/2)-1 < platforms[i].y+16) {

      if (platforms[i].x < player.x+player.width+player.x_v-1 && player.x+player.width+player.x_v-1 < platforms[i].x+16
        || platforms[i].x < player.x+player.x_v && player.x+player.x_v < platforms[i].x+16) {

        return false;
      }
    }
  }
  return true;
}
