"use strict";

var gravity = 0.4;
var friction = 0.2;

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
    ctx.fillRect(0, 0, ctx.canvas.height, ctx.canvas.width);
    ctx.fillStyle = "#F08080";
    ctx.fillRect(player.x, player.y, player.width, player.height);
    }

function move() {
  if(player.jump == false) {
      player.x_v *= friction;
  } else {
      // If the player is in the air then apply the effect of gravity
      player.y_v += gravity;

  }
  player.jump = true;
  // If the left key is pressed increase the relevant horizontal velocity
  if(keys.left) {
      player.x_v = -2.5;
  }
  if(keys.right) {
      player.x_v = 2.5;
  }
  // Updating the y and x coordinates of the player
  if (coly() == true) {
    player.y += player.y_v;
  }
  if (colx() == true){

  }
  player.x += player.x_v;

  // A simple code that checks for collions with the platform
  let o = -1;
  for (var i = 0; i < platforms.length; i++) {
    if(platforms[i].x < player.x && player.x < platforms[i].x + 16 &&
    platforms[i].y < player.y && player.y < platforms[i].y + 16){
        o = i;
    }
  }


  if (o > -1){
      player.jump = false;
      player.y = platforms[o].y;
  }

}

function coly() {
  for (var i = 0; i < platforms.length; i++) {
    // if (player.x + player.x_v == platforms[i].x && player.y+player.y_v == platforms[i].y && player.x + player.width + player.x_v == platforms[i].x && player.y+player.height+player.y_v == platforms[i].y){
    //   console.log("collisions");
    // }
    // if (player.x == platforms[i].x) {
    //   console.log("collisions");
    // }
    if (player.y+player.height+player.y_v  == platforms[i].y) {
      if (player.x < platforms[i].x+16 && player.x > platforms[i].x) {
        return false;
      }


      // console.log("collide");
    }
  }
  return true;
}

function colx() {

}
