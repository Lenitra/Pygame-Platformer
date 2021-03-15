"use strict";

var gravity = 0.6;
var friction = 0.2;

var player = {
    x: 200,
    y: 200,
    x_v: 0,
    y_v: 0,
    jump : true,
    height: 34,
    width: 20
    };

function renderplayer(){
    ctx.fillRect(0, 0, ctx.canvas.height, ctx.canvas.width);
    ctx.fillStyle = "#F08080";
    ctx.fillRect((player.x)-player.width, (player.y)-player.height, player.width, player.height);
    }
