"use strict";

var num = 5;
// The platforms
var platforms = [];

function createplat(){
  console.log("génération de la map");
  for (var i = 0; i < map_1.length; i++) {
    for (var j = 0; j < map_1[i].length; j++) {
      if (map_1[i][j] != 0){
        platforms.push(
          {
            x: j*16,
            y: i*16
          }
        );
      }

    }


  }
}




function renderplat(){
    ctx.fillStyle = "#45597E";
    for (var i = 0; i < platforms.length; i++) {
      ctx.fillRect(platforms[i].x, platforms[i].y, 16, 16);
    }
}
