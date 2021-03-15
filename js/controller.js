"use strict";

let keys = {
    right: false,
    left: false,
    up: false,
    };


function keydown(e) {
  let gauche = 37;
  let droite = 39;
  let haut = 38;

  if(e.keyCode == gauche) {
    keys.left = true;
  }

  if(e.keyCode == haut) {
    if(player.jump == false) {
      player.y_v = -10;
    }
  }

  if(e.keyCode == droite) {
    keys.right = true;
  }
}

    // This function is called when the pressed key is released
function keyup(e) {
  console.log(e.keyCode);
  let gauche = 37;
  let droite = 39;
  let haut = 38;

  if(e.keyCode == gauche) {
    keys.left = false;
  }

  if(e.keyCode == haut) {
    if(player.y_v < -2) {
      player.y_v = -3;
    }
  }

  if(e.keyCode == droite) {
    keys.right = false;
  }

}
