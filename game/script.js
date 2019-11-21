var cvs = document.getElementById("canvas");
var ctx = cvs.getContext("2d");
var kamni = [];

var x,y,color;
var temp;

var score = 0;
var bg = new Image();
bg.src="bg.jpg";

var select = 0;

var time = 600;

var game = 0;

var score_audio = new Audio();
score_audio.src = "score.mp3"

for(var i = 0; i < 10; i++){
		kamni[i] = [];	
}	

for(var i = 0; i < 10; i++){
	for(var j = 0; j < 10; j++){
		kamni[i][j] = {
			x : 0,
			y : 0,
			color :0,
			bord : 0,
			idtimer : 0,
			timean : 0,
			
			
			//ONUME1 : function()
			//{
			//	this.x = this.x +4;
			//},
			
			//ONUME2 : function()
			//{
			//	this.y = this.y +4;
			//},
			
			//ONUME3 : function()
			//{
			//	this.x = this.x -4;
			//},
			
			//ONUME4 : function()
			//{
			//	this.y = this.y -4;
			//},
			
			//ONUME5 : function()
			//{
			//	this.x = this.x +2;
			//	this.y = this.y +2;
			//},
			
			
			 ONUME : function()
			 {
				 
				 var e = this;
				 
				 e.timean = 28;
				 e.color = Math.round(Math.random()*6);

				 e.idtimer = setInterval(function()
						{
							if ((e.timean > 0) && (e.bord > 0))
							{
								e.timean--;
								e.bord--;
							}	
							else
							{
							clearInterval(e.idtimer);
							e.bord = 30;
							//e.color = Math.round(Math.random()*6);

							}
						}, 20)
	
				 
			 
				 
			 	// this.x = this.x -2;
			    // this.y = this.y -2;
				
				//var e = this;
				
				//setTimeout(e.ONUME1, 10);

			 	//setTimeout(e.ONUME2, 20);
				//this.ONUME2();
				//this.ONUME3();
				//this.ONUME4();
				//this.ONUME5();

			 	//setTimeout(function(){
			 	//this.y = this.y +4;
			 	//}, 6);

			 	//setTimeout(function(){
			 	//this.x = this.x -4;
			 	//}, 8);

			 	//setTimeout(function(){
			 	//this.y = this.y -4;
			 	//}, 10);

				//setTimeout(function(){
			 	//this.x = this.x +2;
			 	//this.y = this.y +2;
			 	//}, 3500);

			}
		};
	}
}

// for(var i = 0; i < 10; i++){
// 	for(var j = 0; j < 10; j++){
// 		kamni.push({
// 		x : j*22,
// 		y : i*22,
// 		color : Math.round(Math.random()*6)
// 	});
// 	}	
// }

// for(var i = 0; i < 10; i++){
// 	for(var j = 0; j < 10; j++){
// 		document.write(kamni[i][j].x + "<br>");
// 	}
// }

for(var i = 0; i < 10; i++){
	for(var j = 0; j < 10; j++){
		kamni[i][j].y = 60 + i*33;
		kamni[i][j].x = 10 + j*33;
		kamni[i][j].color = Math.round(Math.random()*6);
		kamni[i][j].bord = 30;
	}
}

document.write("<br>");
document.write("<br>");
document.write("<br>");

function CheckColor(){
	for(var i = 0; i < 10; i++){
	for(var j = 0; j < 10; j++){
		if (kamni[i][j].color == 50){
		kamni[i][j].color = Math.round(Math.random()*6);}
		else{}
	}
}
}

// for(var i = 0; i < 10; i++){
// 	for(var j = 0; j < 10; j++){
// 		document.write(kamni[i][j].color + "\t");
// 	}
// 	document.write("<br>");
// }

																			// var devstvie = 0;

																			// if(window.DeviceOrientationEvent){ 
																			// 		window.addEventListener("deviceorientation", Aclr, false); 
																			// 	}
																			// 	else{ 
																			// 		console.log("DeviceMotionEvent is not supported"); 
																			// 	} 

																			// function Aclr(event){ 
																			// 	if (Math.round(event.gamma) > 15){ 
																			// 	//up 
																			// 	devstvie = 1;
																			// 	//	(select == 0) ? select = 9 : select--;
																			// 	} 
																			// 	if (Math.round(event.gamma) < -15){ 
																			// 	//down 
																			// 		devstvie = 2;
																			// 	//	(select == 9) ? select = 0 : select++;
																			// 	} 
																			// 	if (Math.round(event.beta) > 15){ 
																			// 	//right 
																			// 	//switchRight();
																			// 	devstvie = 3;
																			// 	} 
																			// 	if (Math.round(event.beta) < -15){ 
																			// 	//left 
																			// 	devstvie = 4;
																			// 	//switchLeft();
																			// 	} 
																			// } 

															var initialPoint;
															var finalPoint;

															document.addEventListener('touchstart', function(event) {
																event.preventDefault();
																event.stopPropagation();
																initialPoint =event.changedTouches[0];
																}, false);

															document.addEventListener('touchend', function(event) {
																		event.preventDefault();
																		event.stopPropagation();
																		finalPoint=event.changedTouches[0];
																		var xAbs = Math.abs(initialPoint.pageX - finalPoint.pageX);
																		var yAbs = Math.abs(initialPoint.pageY - finalPoint.pageY);
															if (xAbs > 10 || yAbs > 10) 
															{
																if (xAbs > yAbs) 
																{
																	if (finalPoint.pageX < initialPoint.pageX)
																	{
																		/*СВАЙП ВЛЕВО*/
																		Start();
																		switchLeft();
																	}
																	else{
																		/*СВАЙП ВПРАВО*/
																		Start();
																		switchRight();
																	}
																}
																else
																{
																		if (finalPoint.pageY < initialPoint.pageY)
																		{
																			/*СВАЙП ВВЕРХ*/
																			Start();
																			Up();
																		}
																		else
																		{
																			/*СВАЙП ВНИЗ*/
																			Start();
																			Down();
																		}
																}
															}
															else{}
															}, false);


// var startPoint={};
// var nowPoint;
// var ldelay;

// document.addEventListener('touchstart', function(event) {
// 	event.preventDefault();
// 	event.stopPropagation();
// 	startPoint.x=event.changedTouches[0].pageX;
// 	startPoint.y=event.changedTouches[0].pageY;
// 	ldelay=new Date(); 
// 	}, false);
// /*Ловим движение пальцем*/


// document.addEventListener('touchend', function(event) {
// var pdelay=new Date(); 
// nowPoint=event.changedTouches[0];
// var xAbs = Math.abs(startPoint.x - nowPoint.pageX);
// var yAbs = Math.abs(startPoint.y - nowPoint.pageY);
// if ((xAbs > 20 || yAbs > 20) && (pdelay.getTime()-ldelay.getTime())<200) {
// if (xAbs > yAbs) {
// if (nowPoint.pageX < startPoint.x){switchLeft();/*СВАЙП ВЛЕВО*/}
// else{switchRight();/*СВАЙП ВПРАВО*/}
// }
// else {
// if (nowPoint.pageY < startPoint.y){Up();/*СВАЙП ВВЕРХ*/}
// else{Down();/*СВАЙП ВНИЗ*/}
// }
// }
// }, false);

// var touchstartX = 0;
// var touchstartY = 0;
// var touchendX = 0;
// var touchendY = 0;

// cvs.addEventListener('touchstart', function(event) {
// touchstartX = event.pageX;
// touchstartY = event.pageY;
// }, false);

// cvs.addEventListener('touchend', function(event) {
// touchendX = event.pageX;
// touchendY = event.pageY;
// SwipePlease();
// }, false); 

// function SwipePlease() {
// if (touchendX < touchstartX) {
// //left!
// switchLeft();
// }
// if (touchendX > touchstartX) {
// //alert(swiped + 'right!');
// switchRight();
// }
// if (touchendY < touchstartY) {
// //alert(swiped + 'down!');
// Down();
// }
// if (touchendY > touchstartY) {
// //alert(swiped + 'left!');
// Up();
// }
// }

 document.onkeydown = function(e) {
 	    switch (e.keyCode) {
         case 37:
             //left
             switchLeft();
             break;
         case 38:
         	//up
             Up();
             break;
         case 39:
             //right
            switchRight();
             break;
         case 40:
         	//down
             Down();
             break;
     }
 }

function switchRight(){
//	CheckColor();
	temp = kamni[select][9].color;
	for(var i = 9; i > 0; i--){
		kamni[select][i].color = kamni[select][i-1].color;
	}
	kamni[select][0].color = temp;
	checkScoreInPit();
}

function switchLeft(){
//	CheckColor();
	temp = kamni[select][0].color;
	for(var i = 0; i < 9; i++){
		kamni[select][i].color = kamni[select][i+1].color;
	}
	kamni[select][9].color = temp;
	checkScoreInPit();
}

function Up(){
//	CheckColor();
	(select == 0) ? select = 9 : select--;
}

function Down(){
//	CheckColor();
	(select == 9) ? select = 0 : select++;
}




function checkScoreInPit(){
		switch (select) {
//-------------------------------------------------------------------------------------------------------------
//-------------------------------------------------------------------------------------------------------------
//-------------------------------------------------------------------------------------------------------------
//-------------------------------------------------------------------------------------------------------------
			case 0: {
				for(var i = 0; i < 10; i++)
				{
					//----------------------Если 5 в ряд --------------------------
					if 	((kamni[select][i].color == kamni[select+1][i].color) && 
						(kamni[select][i].color == kamni[select+2][i].color) && 
						(kamni[select][i].color == kamni[select+3][i].color) && 
						(kamni[select][i].color == kamni[select+4][i].color))
					{
						score_audio.play();
						score = score +5;

						kamni[select][i].ONUME();
						kamni[select+1][i].ONUME();
						kamni[select+2][i].ONUME();
						kamni[select+3][i].ONUME();
						kamni[select+4][i].ONUME();
					}
					else{}
					//--------------------Если 4 в ряд-----------------------
					if 	((kamni[select][i].color == kamni[select+1][i].color) && 
						(kamni[select][i].color == kamni[select+2][i].color) && 
						(kamni[select][i].color == kamni[select+3][i].color))
					{
						score_audio.play();
						score = score +4;
						
						kamni[select][i].ONUME();
						kamni[select+1][i].ONUME();
						kamni[select+2][i].ONUME();
						kamni[select+3][i].ONUME();

					}
					else{}
					//-------------------Если 3 в ряд ---------------
					if 	((kamni[select][i].color == kamni[select+1][i].color) && 
						(kamni[select][i].color == kamni[select+2][i].color))
					{
						score_audio.play();
						score = score +3;
						
						kamni[select][i].ONUME();
						kamni[select+1][i].ONUME();
						kamni[select+2][i].ONUME();

					}
					else{}

				}
			}
			break;
//-------------------------------------------------------------------------------------------------------------
//-------------------------------------------------------------------------------------------------------------
//-------------------------------------------------------------------------------------------------------------
//-------------------------------------------------------------------------------------------------------------
			case 1: {
				for(var i = 0; i < 10; i++){
//-------------------------------------------------------------------------------------------------------------
					// 5 ///////////////////////////////////////////
					if 	((kamni[select][i].color == kamni[select-1][i].color) && 
						(kamni[select][i].color == kamni[select+1][i].color) && 
						(kamni[select][i].color == kamni[select+2][i].color) && 
						(kamni[select][i].color == kamni[select+3][i].color))
					{
						score_audio.play();
						score = score +5;
						kamni[select-1][i].ONUME();
						kamni[select][i].ONUME();
						kamni[select+1][i].ONUME();
						kamni[select+2][i].ONUME();
						kamni[select+3][i].ONUME();
					}
					else{}
					//5 ///////////////////////////////////////////
					if 	((kamni[select][i].color == kamni[select+1][i].color) && 
						(kamni[select][i].color == kamni[select+2][i].color) && 
						(kamni[select][i].color == kamni[select+3][i].color) && 
						(kamni[select][i].color == kamni[select+4][i].color))
					{
						score_audio.play();
						score = score +5;
						kamni[select][i].ONUME();
						kamni[select+1][i].ONUME();
						kamni[select+2][i].ONUME();
						kamni[select+3][i].ONUME();
						kamni[select+4][i].ONUME();
					}
					else{}
//----------------------------------------------------------------------------------------------------------------
					//4 ////////////////////////////////////////////////////////
					if 	((kamni[select][i].color == kamni[select-1][i].color) && 
						(kamni[select][i].color == kamni[select+1][i].color) && 
						(kamni[select][i].color == kamni[select+2][i].color))
					{
						score_audio.play();
						score = score +4;
						kamni[select-1][i].ONUME();
						kamni[select][i].ONUME();
						kamni[select+1][i].ONUME();
						kamni[select+2][i].ONUME();
					}
					else{}
					//4 ///////////////////////////////////////////
					if 	((kamni[select][i].color == kamni[select+1][i].color) && 
						(kamni[select][i].color == kamni[select+2][i].color) && 
						(kamni[select][i].color == kamni[select+3][i].color))
					{
						score_audio.play();
						score = score +4;
						kamni[select][i].ONUME();
						kamni[select+1][i].ONUME();
						kamni[select+2][i].ONUME();
						kamni[select+3][i].ONUME();
					}
					else{}
//-------------------------------------------------------------------------------------------------------------
					//3 /////////////////////////////////////////////
					if 	((kamni[select][i].color == kamni[select-1][i].color) && 
						(kamni[select][i].color == kamni[select+1][i].color))
					{
						score_audio.play();
						score = score +3;
						kamni[select-1][i].ONUME();
						kamni[select][i].ONUME();
						kamni[select+1][i].ONUME();
					}
					else{}
					//3 ///////////////////////////////////////////
					if 	((kamni[select][i].color == kamni[select+1][i].color) && 
						(kamni[select][i].color == kamni[select+2][i].color))
					{
						score_audio.play();
						score = score +3;
						kamni[select][i].ONUME();
						kamni[select+1][i].ONUME();
						kamni[select+2][i].ONUME();
					}
					else{}

				}
			}
			break;
//-------------------------------------------------------------------------------------------------------------
//-------------------------------------------------------------------------------------------------------------
//-------------------------------------------------------------------------------------------------------------
//-------------------------------------------------------------------------------------------------------------
			case 2: {
				for(var i = 0; i < 10; i++){
//-------------------------------------------------------------------------------------------------------------
					// 5 ///////////////////////////////////////////
					if 	((kamni[select][i].color == kamni[select-1][i].color) && 
						(kamni[select][i].color == kamni[select+1][i].color) && 
						(kamni[select][i].color == kamni[select+2][i].color) && 
						(kamni[select][i].color == kamni[select+3][i].color))
					{
						score_audio.play();
						score = score +5;
						kamni[select-1][i].ONUME();
						kamni[select][i].ONUME();
						kamni[select+1][i].ONUME();
						kamni[select+2][i].ONUME();
						kamni[select+3][i].ONUME();
					}
					else{}
					//5 ///////////////////////////////////////////
					if 	((kamni[select][i].color == kamni[select+1][i].color) && 
						(kamni[select][i].color == kamni[select+2][i].color) && 
						(kamni[select][i].color == kamni[select+3][i].color) && 
						(kamni[select][i].color == kamni[select+4][i].color))
					{
						score_audio.play();
						score = score +5;
						kamni[select][i].ONUME();
						kamni[select+1][i].ONUME();
						kamni[select+2][i].ONUME();
						kamni[select+3][i].ONUME();
						kamni[select+4][i].ONUME();
					}
					else{}
					//5 ///////////////////////////////////////////////////
					if 	((kamni[select][i].color == kamni[select-2][i].color) && 
						(kamni[select][i].color == kamni[select-1][i].color) && 
						(kamni[select][i].color == kamni[select+1][i].color) && 
						(kamni[select][i].color == kamni[select+2][i].color))
					{
						score_audio.play();
						score = score +5;
						kamni[select][i].ONUME();
						kamni[select-2][i].ONUME();
						kamni[select-1][i].ONUME();
						kamni[select+1][i].ONUME();
						kamni[select+2][i].ONUME();
					}
					else{}
//-------------------------------------------------------------------------------------------------------------
					//4 ///////////////////////////////////////////////////
					if 	((kamni[select][i].color == kamni[select-1][i].color) && 
						(kamni[select][i].color == kamni[select+1][i].color) && 
						(kamni[select][i].color == kamni[select+2][i].color))
					{
						score_audio.play();
						score = score +4;
						kamni[select-1][i].ONUME();
						kamni[select][i].ONUME();
						kamni[select+1][i].ONUME();
						kamni[select+2][i].ONUME();
					}
					else{}
					//4 ///////////////////////////////////////////
					if 	((kamni[select][i].color == kamni[select+1][i].color) && 
						(kamni[select][i].color == kamni[select+2][i].color) && 
						(kamni[select][i].color == kamni[select+3][i].color))
					{
						score_audio.play();
						score = score +4;
						kamni[select][i].ONUME();
						kamni[select+1][i].ONUME();
						kamni[select+2][i].ONUME();
						kamni[select+3][i].ONUME();
					}
					else{}
					//4 ///////////////////////////////////////////////////
					if 	((kamni[select][i].color == kamni[select-2][i].color) && 
						(kamni[select][i].color == kamni[select-1][i].color) && 
						(kamni[select][i].color == kamni[select+1][i].color))
					{
						score_audio.play();
						score = score +4;
						kamni[select][i].ONUME();
						kamni[select-2][i].ONUME();
						kamni[select-1][i].ONUME();
						kamni[select+1][i].ONUME();
					}
					else{}
//-------------------------------------------------------------------------------------------------------------
					//3 ///////////////////////////////////////////////////
					if 	((kamni[select][i].color == kamni[select-1][i].color) && 
						(kamni[select][i].color == kamni[select+1][i].color))
					{
						score_audio.play();
						score = score +3;
						kamni[select-1][i].ONUME();
						kamni[select][i].ONUME();
						kamni[select+1][i].ONUME();
					}
					else{}
					//3 ///////////////////////////////////////////
					if 	((kamni[select][i].color == kamni[select+1][i].color) && 
						(kamni[select][i].color == kamni[select+2][i].color))
					{
						score_audio.play();
						score = score +3;
						kamni[select][i].ONUME();
						kamni[select+1][i].ONUME();
						kamni[select+2][i].ONUME();
					}
					else{}
					//3 ///////////////////////////////////////////////////
					if 	((kamni[select][i].color == kamni[select-2][i].color) && 
						(kamni[select][i].color == kamni[select-1][i].color))
					{
						score_audio.play();
						score = score +3;
						kamni[select][i].ONUME();
						kamni[select-2][i].ONUME();
						kamni[select-1][i].ONUME();
					}
					else{}
				}
		}
		break;
//-------------------------------------------------------------------------------------------------------------	
//-------------------------------------------------------------------------------------------------------------
//-------------------------------------------------------------------------------------------------------------
//-------------------------------------------------------------------------------------------------------------
			case 3: {
				for(var i = 0; i < 10; i++){
//-------------------------------------------------------------------------------------------------------------
					// 5 ///////////////////////////////////////////
					if 	((kamni[select][i].color == kamni[select-1][i].color) && 
						(kamni[select][i].color == kamni[select+1][i].color) && 
						(kamni[select][i].color == kamni[select+2][i].color) && 
						(kamni[select][i].color == kamni[select+3][i].color))
					{
						score_audio.play();
						score = score +5;
						kamni[select-1][i].ONUME();
						kamni[select][i].ONUME();
						kamni[select+1][i].ONUME();
						kamni[select+2][i].ONUME();
						kamni[select+3][i].ONUME();
					}
					else{}
					//5 ///////////////////////////////////////////
					if 	((kamni[select][i].color == kamni[select+1][i].color) && 
						(kamni[select][i].color == kamni[select+2][i].color) && 
						(kamni[select][i].color == kamni[select+3][i].color) && 
						(kamni[select][i].color == kamni[select+4][i].color))
					{
						score_audio.play();
						score = score +5;
						kamni[select][i].ONUME();
						kamni[select+1][i].ONUME();
						kamni[select+2][i].ONUME();
						kamni[select+3][i].ONUME();
						kamni[select+4][i].ONUME();
					}
					else{}
					//5 ///////////////////////////////////////////////////
					if 	((kamni[select][i].color == kamni[select-2][i].color) && 
						(kamni[select][i].color == kamni[select-1][i].color) && 
						(kamni[select][i].color == kamni[select+1][i].color) && 
						(kamni[select][i].color == kamni[select+2][i].color))
					{
						score_audio.play();
						score = score +5;
						kamni[select][i].ONUME();
						kamni[select-2][i].ONUME();
						kamni[select-1][i].ONUME();
						kamni[select+1][i].ONUME();
						kamni[select+2][i].ONUME();
					}
					else{}
					//5 //////////////////////////////////////////////////
					if 	((kamni[select][i].color == kamni[select-3][i].color) && 
						(kamni[select][i].color == kamni[select-2][i].color) && 
						(kamni[select][i].color == kamni[select-1][i].color) && 
						(kamni[select][i].color == kamni[select+1][i].color))
					{
						score_audio.play();
						score = score +5;
						kamni[select][i].ONUME();
						kamni[select-3][i].ONUME();
						kamni[select-2][i].ONUME();
						kamni[select-1][i].ONUME();
						kamni[select+1][i].ONUME();
					}
					else{}
//-------------------------------------------------------------------------------------------------------------
					// 4 ///////////////////////////////////////////
					if 	((kamni[select][i].color == kamni[select-1][i].color) && 
						(kamni[select][i].color == kamni[select+1][i].color) && 
						(kamni[select][i].color == kamni[select+2][i].color))
					{
						score_audio.play();
						score = score +4
						kamni[select-1][i].ONUME();
						kamni[select][i].ONUME();
						kamni[select+1][i].ONUME();
						kamni[select+2][i].ONUME();
					}
					else{}
					//4 ///////////////////////////////////////////
					if 	((kamni[select][i].color == kamni[select+1][i].color) && 
						(kamni[select][i].color == kamni[select+2][i].color) && 
						(kamni[select][i].color == kamni[select+3][i].color))
					{
						score_audio.play();
						score = score +4;
						kamni[select][i].ONUME();
						kamni[select+1][i].ONUME();
						kamni[select+2][i].ONUME();
						kamni[select+3][i].ONUME();
					}
					else{}
					//4 ///////////////////////////////////////////////////
					if 	((kamni[select][i].color == kamni[select-2][i].color) && 
						(kamni[select][i].color == kamni[select-1][i].color) && 
						(kamni[select][i].color == kamni[select+1][i].color))
					{
						score_audio.play();
						score = score +4;
						kamni[select][i].ONUME();
						kamni[select-2][i].ONUME();
						kamni[select-1][i].ONUME();
						kamni[select+1][i].ONUME();
					}
					else{}
					//4 //////////////////////////////////////////////////
					if 	((kamni[select][i].color == kamni[select-3][i].color) && 
						(kamni[select][i].color == kamni[select-2][i].color) && 
						(kamni[select][i].color == kamni[select-1][i].color))
					{
						score_audio.play();
						score = score +4;
						kamni[select][i].ONUME();
						kamni[select-3][i].ONUME();
						kamni[select-2][i].ONUME();
						kamni[select-1][i].ONUME();
					}
					else{}
//-------------------------------------------------------------------------------------------------------------
					// 3 ///////////////////////////////////////////
					if 	((kamni[select][i].color == kamni[select-1][i].color) && 
						(kamni[select][i].color == kamni[select+1][i].color))
					{
						score_audio.play();
						score = score +3;
						kamni[select-1][i].ONUME();
						kamni[select][i].ONUME();
						kamni[select+1][i].ONUME();
					}
					else{}
					//3 ///////////////////////////////////////////
					if 	((kamni[select][i].color == kamni[select+1][i].color) && 
						(kamni[select][i].color == kamni[select+2][i].color))
					{
						score_audio.play();
						score = score +3;
						kamni[select][i].ONUME();
						kamni[select+1][i].ONUME();
						kamni[select+2][i].ONUME();
					}
					else{}
					//3 ///////////////////////////////////////////////////
					if 	((kamni[select][i].color == kamni[select-2][i].color) && 
						(kamni[select][i].color == kamni[select-1][i].color))
					{
						score_audio.play();
						score = score +3;
						kamni[select][i].ONUME();
						kamni[select-2][i].ONUME();
						kamni[select-1][i].ONUME();
					}
					else{}
				}
			}
			break;	

//-------------------------------------------------------------------------------------------------------------
//-------------------------------------------------------------------------------------------------------------
//-------------------------------------------------------------------------------------------------------------
//-------------------------------------------------------------------------------------------------------------
			case 4: {
				for(var i = 0; i < 10; i++){
					// 5 ///////////////////////////////////////////
					if 	((kamni[select][i].color == kamni[select-1][i].color) && 
						(kamni[select][i].color == kamni[select+1][i].color) && 
						(kamni[select][i].color == kamni[select+2][i].color) && 
						(kamni[select][i].color == kamni[select+3][i].color))
					{
						score_audio.play();
						score = score +5;
						kamni[select-1][i].ONUME();
						kamni[select][i].ONUME();
						kamni[select+1][i].ONUME();
						kamni[select+2][i].ONUME();
						kamni[select+3][i].ONUME();
					}
					else{}
					//5 ///////////////////////////////////////////
					if 	((kamni[select][i].color == kamni[select+1][i].color) && 
						(kamni[select][i].color == kamni[select+2][i].color) && 
						(kamni[select][i].color == kamni[select+3][i].color) && 
						(kamni[select][i].color == kamni[select+4][i].color))
					{
						score_audio.play();
						score = score +5;
						kamni[select][i].ONUME();
						kamni[select+1][i].ONUME();
						kamni[select+2][i].ONUME();
						kamni[select+3][i].ONUME();
						kamni[select+4][i].ONUME();
					}
					else{}
					//5 ///////////////////////////////////////////////////
					if 	((kamni[select][i].color == kamni[select-2][i].color) && 
						(kamni[select][i].color == kamni[select-1][i].color) && 
						(kamni[select][i].color == kamni[select+1][i].color) && 
						(kamni[select][i].color == kamni[select+2][i].color))
					{
						score_audio.play();
						score = score +5;
						kamni[select][i].ONUME();
						kamni[select-2][i].ONUME();
						kamni[select-1][i].ONUME();
						kamni[select+1][i].ONUME();
						kamni[select+2][i].ONUME();
					}
					else{}
					//5 //////////////////////////////////////////////////
					if 	((kamni[select][i].color == kamni[select-3][i].color) && 
						(kamni[select][i].color == kamni[select-2][i].color) && 
						(kamni[select][i].color == kamni[select-1][i].color) && 
						(kamni[select][i].color == kamni[select+1][i].color))
					{
						score_audio.play();
						score = score +5;
						kamni[select][i].ONUME();
						kamni[select-3][i].ONUME();
						kamni[select-2][i].ONUME();
						kamni[select-1][i].ONUME();
						kamni[select+1][i].ONUME();
					}
					else{}
					//5 //////////////////////////////////////////////////
					if 	((kamni[select][i].color == kamni[select-4][i].color) && 
						(kamni[select][i].color == kamni[select-3][i].color) && 
						(kamni[select][i].color == kamni[select-2][i].color) && 
						(kamni[select][i].color == kamni[select-1][i].color))
					{
						score_audio.play();
						score = score +5;
						kamni[select][i].ONUME();
						kamni[select-4][i].ONUME();
						kamni[select-3][i].ONUME();
						kamni[select-2][i].ONUME();
						kamni[select-1][i].ONUME();
					}
					else{}
//-------------------------------------------------------------------------------------------------------------
					//4 ////////////////////////////////////////////////////
					if 	((kamni[select][i].color == kamni[select-1][i].color) && 
						(kamni[select][i].color == kamni[select+1][i].color) && 
						(kamni[select][i].color == kamni[select+2][i].color))
					{
						score_audio.play();
						score = score +4;
						kamni[select-1][i].ONUME();
						kamni[select][i].ONUME();
						kamni[select+1][i].ONUME();
						kamni[select+2][i].ONUME();
					}
					else{}
					//4 ///////////////////////////////////////////
					if 	((kamni[select][i].color == kamni[select+1][i].color) && 
						(kamni[select][i].color == kamni[select+2][i].color) && 
						(kamni[select][i].color == kamni[select+3][i].color))
					{
						score_audio.play();
						score = score +4;
						kamni[select][i].ONUME();
						kamni[select+1][i].ONUME();
						kamni[select+2][i].ONUME();
						kamni[select+3][i].ONUME();
					}
					else{}
					//4 ///////////////////////////////////////////////////
					if 	((kamni[select][i].color == kamni[select-2][i].color) && 
						(kamni[select][i].color == kamni[select-1][i].color) && 
						(kamni[select][i].color == kamni[select+1][i].color))
					{
						score_audio.play();
						score = score +4;
						kamni[select][i].ONUME();
						kamni[select-2][i].ONUME();
						kamni[select-1][i].ONUME();
						kamni[select+1][i].ONUME();
					}
					else{}
					//4 //////////////////////////////////////////////////
					if 	((kamni[select][i].color == kamni[select-3][i].color) && 
						(kamni[select][i].color == kamni[select-2][i].color) && 
						(kamni[select][i].color == kamni[select-1][i].color))
					{
						score_audio.play();
						score = score +4;
						kamni[select][i].ONUME();
						kamni[select-3][i].ONUME();
						kamni[select-2][i].ONUME();
						kamni[select-1][i].ONUME();
					}
					else{}
//-------------------------------------------------------------------------------------------------------------
					//3 /////////////////////////////////////////////////////
					if 	((kamni[select][i].color == kamni[select-1][i].color) && 
						(kamni[select][i].color == kamni[select+1][i].color))
					{
						score_audio.play();
						score = score +3;
						kamni[select-1][i].ONUME();
						kamni[select][i].ONUME();
						kamni[select+1][i].ONUME();
					}
					else{}
					//3 ///////////////////////////////////////////
					if 	((kamni[select][i].color == kamni[select+1][i].color) && 
						(kamni[select][i].color == kamni[select+2][i].color))
					{
						score_audio.play();
						score = score +3;
						kamni[select][i].ONUME();
						kamni[select+1][i].ONUME();
						kamni[select+2][i].ONUME();
					}
					else{}
					//3 ///////////////////////////////////////////////////
					if 	((kamni[select][i].color == kamni[select-2][i].color) && 
						(kamni[select][i].color == kamni[select-1][i].color))
					{
						score_audio.play();
						score = score +3;
						kamni[select][i].ONUME();
						kamni[select-2][i].ONUME();
						kamni[select-1][i].ONUME();
					}
					else{}
				}
			}
			break;
//-------------------------------------------------------------------------------------------------------------
//-------------------------------------------------------------------------------------------------------------
//-------------------------------------------------------------------------------------------------------------
//-------------------------------------------------------------------------------------------------------------
			case 5: {
				for(var i = 0; i < 10; i++){
					// 5 ///////////////////////////////////////////
					if 	((kamni[select][i].color == kamni[select-1][i].color) && 
						(kamni[select][i].color == kamni[select+1][i].color) && 
						(kamni[select][i].color == kamni[select+2][i].color) && 
						(kamni[select][i].color == kamni[select+3][i].color))
					{
						score_audio.play();
						score = score +5;
						kamni[select-1][i].ONUME();
						kamni[select][i].ONUME();
						kamni[select+1][i].ONUME();
						kamni[select+2][i].ONUME();
						kamni[select+3][i].ONUME();
					}
					else{}
					//5 ///////////////////////////////////////////
					if 	((kamni[select][i].color == kamni[select+1][i].color) && 
						(kamni[select][i].color == kamni[select+2][i].color) && 
						(kamni[select][i].color == kamni[select+3][i].color) && 
						(kamni[select][i].color == kamni[select+4][i].color))
					{
						score_audio.play();
						score = score +5;
						kamni[select][i].ONUME();
						kamni[select+1][i].ONUME();
						kamni[select+2][i].ONUME();
						kamni[select+3][i].ONUME();
						kamni[select+4][i].ONUME();
					}
					else{}
					//5 ///////////////////////////////////////////////////
					if 	((kamni[select][i].color == kamni[select-2][i].color) && 
						(kamni[select][i].color == kamni[select-1][i].color) && 
						(kamni[select][i].color == kamni[select+1][i].color) && 
						(kamni[select][i].color == kamni[select+2][i].color))
					{
						score_audio.play();
						score = score +5;
						kamni[select][i].ONUME();
						kamni[select-2][i].ONUME();
						kamni[select-1][i].ONUME();
						kamni[select+1][i].ONUME();
						kamni[select+2][i].ONUME();
					}
					else{}
					//5 //////////////////////////////////////////////////
					if 	((kamni[select][i].color == kamni[select-3][i].color) && 
						(kamni[select][i].color == kamni[select-2][i].color) && 
						(kamni[select][i].color == kamni[select-1][i].color) && 
						(kamni[select][i].color == kamni[select+1][i].color))
					{
						score_audio.play();
						score = score +5;
						kamni[select][i].ONUME();
						kamni[select-3][i].ONUME();
						kamni[select-2][i].ONUME();
						kamni[select-1][i].ONUME();
						kamni[select+1][i].ONUME();
					}
					else{}
					//5 //////////////////////////////////////////////////
					if 	((kamni[select][i].color == kamni[select-4][i].color) && 
						(kamni[select][i].color == kamni[select-3][i].color) && 
						(kamni[select][i].color == kamni[select-2][i].color) && 
						(kamni[select][i].color == kamni[select-1][i].color))
					{
						score_audio.play();
						score = score +5;
						kamni[select][i].ONUME();
						kamni[select-4][i].ONUME();
						kamni[select-3][i].ONUME();
						kamni[select-2][i].ONUME();
						kamni[select-1][i].ONUME();
					}
					else{}
//-------------------------------------------------------------------------------------------------------------
					//4 ////////////////////////////////////////////////////
					if 	((kamni[select][i].color == kamni[select-1][i].color) && 
						(kamni[select][i].color == kamni[select+1][i].color) && 
						(kamni[select][i].color == kamni[select+2][i].color))
					{
						score_audio.play();
						score = score +4;
						kamni[select-1][i].ONUME();
						kamni[select][i].ONUME();
						kamni[select+1][i].ONUME();
						kamni[select+2][i].ONUME();
					}
					else{}
					//4 ///////////////////////////////////////////
					if 	((kamni[select][i].color == kamni[select+1][i].color) && 
						(kamni[select][i].color == kamni[select+2][i].color) && 
						(kamni[select][i].color == kamni[select+3][i].color))
					{
						score_audio.play();
						score = score +4;
						kamni[select][i].ONUME();
						kamni[select+1][i].ONUME();
						kamni[select+2][i].ONUME();
						kamni[select+3][i].ONUME();
					}
					else{}
					//4 ///////////////////////////////////////////////////
					if 	((kamni[select][i].color == kamni[select-2][i].color) && 
						(kamni[select][i].color == kamni[select-1][i].color) && 
						(kamni[select][i].color == kamni[select+1][i].color))
					{
						score_audio.play();
						score = score +4;
						kamni[select][i].ONUME();
						kamni[select-2][i].ONUME();
						kamni[select-1][i].ONUME();
						kamni[select+1][i].ONUME();
					}
					else{}
					//4 //////////////////////////////////////////////////
					if 	((kamni[select][i].color == kamni[select-3][i].color) && 
						(kamni[select][i].color == kamni[select-2][i].color) && 
						(kamni[select][i].color == kamni[select-1][i].color))
					{
						score_audio.play();
						score = score +4;
						kamni[select][i].ONUME();
						kamni[select-3][i].ONUME();
						kamni[select-2][i].ONUME();
						kamni[select-1][i].ONUME();
					}
					else{}
//-------------------------------------------------------------------------------------------------------------
					//3 /////////////////////////////////////////////////////
					if 	((kamni[select][i].color == kamni[select-1][i].color) && 
						(kamni[select][i].color == kamni[select+1][i].color))
					{
						score_audio.play();
						score = score +3;
						kamni[select-1][i].ONUME();
						kamni[select][i].ONUME();
						kamni[select+1][i].ONUME();
					}
					else{}
					//3 ///////////////////////////////////////////
					if 	((kamni[select][i].color == kamni[select+1][i].color) && 
						(kamni[select][i].color == kamni[select+2][i].color))
					{
						score_audio.play();
						score = score +3;
						kamni[select][i].ONUME();
						kamni[select+1][i].ONUME();
						kamni[select+2][i].ONUME();
					}
					else{}
					//3 ///////////////////////////////////////////////////
					if 	((kamni[select][i].color == kamni[select-2][i].color) && 
						(kamni[select][i].color == kamni[select-1][i].color))
					{
						score_audio.play();
						score = score +3;
						kamni[select][i].ONUME();
						kamni[select-2][i].ONUME();
						kamni[select-1][i].ONUME();
					}
					else{}
				}
			}
			break;
//-------------------------------------------------------------------------------------------------------------
//-------------------------------------------------------------------------------------------------------------
//-------------------------------------------------------------------------------------------------------------
//-------------------------------------------------------------------------------------------------------------
			case 6: {
				for(var i = 0; i < 10; i++){
					// 5 ///////////////////////////////////////////
					if 	((kamni[select][i].color == kamni[select-1][i].color) && 
						(kamni[select][i].color == kamni[select+1][i].color) && 
						(kamni[select][i].color == kamni[select+2][i].color) && 
						(kamni[select][i].color == kamni[select+3][i].color))
					{
						score_audio.play();
						score = score +5;
						kamni[select-1][i].ONUME();
						kamni[select][i].ONUME();
						kamni[select+1][i].ONUME();
						kamni[select+2][i].ONUME();
						kamni[select+3][i].ONUME();
					}
					else{}
					//5 ///////////////////////////////////////////////////
					if 	((kamni[select][i].color == kamni[select-2][i].color) && 
						(kamni[select][i].color == kamni[select-1][i].color) && 
						(kamni[select][i].color == kamni[select+1][i].color) && 
						(kamni[select][i].color == kamni[select+2][i].color))
					{
						score_audio.play();
						score = score +5;
						kamni[select][i].ONUME();
						kamni[select-2][i].ONUME();
						kamni[select-1][i].ONUME();
						kamni[select+1][i].ONUME();
						kamni[select+2][i].ONUME();
					}
					else{}
					//5 //////////////////////////////////////////////////
					if 	((kamni[select][i].color == kamni[select-3][i].color) && 
						(kamni[select][i].color == kamni[select-2][i].color) && 
						(kamni[select][i].color == kamni[select-1][i].color) && 
						(kamni[select][i].color == kamni[select+1][i].color))
					{
						score_audio.play();
						score = score +5;
						kamni[select][i].ONUME();
						kamni[select-3][i].ONUME();
						kamni[select-2][i].ONUME();
						kamni[select-1][i].ONUME();
						kamni[select+1][i].ONUME();
					}
					else{}
					//5 //////////////////////////////////////////////////
					if 	((kamni[select][i].color == kamni[select-4][i].color) && 
						(kamni[select][i].color == kamni[select-3][i].color) && 
						(kamni[select][i].color == kamni[select-2][i].color) && 
						(kamni[select][i].color == kamni[select-1][i].color))
					{
						score_audio.play();
						score = score +5;
						kamni[select][i].ONUME();
						kamni[select-4][i].ONUME();
						kamni[select-3][i].ONUME();
						kamni[select-2][i].ONUME();
						kamni[select-1][i].ONUME();
					}
					else{}
//-------------------------------------------------------------------------------------------------------------
					//4 ////////////////////////////////////////////////////
					if 	((kamni[select][i].color == kamni[select-1][i].color) && 
						(kamni[select][i].color == kamni[select+1][i].color) && 
						(kamni[select][i].color == kamni[select+2][i].color))
					{
						score_audio.play();
						score = score +4;
						kamni[select-1][i].ONUME();
						kamni[select][i].ONUME();
						kamni[select+1][i].ONUME();
						kamni[select+2][i].ONUME();
					}
					else{}
					//4 ///////////////////////////////////////////
					if 	((kamni[select][i].color == kamni[select+1][i].color) && 
						(kamni[select][i].color == kamni[select+2][i].color) && 
						(kamni[select][i].color == kamni[select+3][i].color))
					{
						score_audio.play();
						score = score +4;
						kamni[select][i].ONUME();
						kamni[select+1][i].ONUME();
						kamni[select+2][i].ONUME();
						kamni[select+3][i].ONUME();
					}
					else{}
					//4 ///////////////////////////////////////////////////
					if 	((kamni[select][i].color == kamni[select-2][i].color) && 
						(kamni[select][i].color == kamni[select-1][i].color) && 
						(kamni[select][i].color == kamni[select+1][i].color))
					{
						score_audio.play();
						score = score +4;
						kamni[select][i].ONUME();
						kamni[select-2][i].ONUME();
						kamni[select-1][i].ONUME();
						kamni[select+1][i].ONUME();
					}
					else{}
					//4 //////////////////////////////////////////////////
					if 	((kamni[select][i].color == kamni[select-3][i].color) && 
						(kamni[select][i].color == kamni[select-2][i].color) && 
						(kamni[select][i].color == kamni[select-1][i].color))
					{
						score_audio.play();
						score = score +4;
						kamni[select][i].ONUME();
						kamni[select-3][i].ONUME();
						kamni[select-2][i].ONUME();
						kamni[select-1][i].ONUME();
					}
					else{}
//-------------------------------------------------------------------------------------------------------------
					//3 /////////////////////////////////////////////////////
					if 	((kamni[select][i].color == kamni[select-1][i].color) && 
						(kamni[select][i].color == kamni[select+1][i].color))
					{
						score_audio.play();
						score = score +3;
						kamni[select-1][i].ONUME();
						kamni[select][i].ONUME();
						kamni[select+1][i].ONUME();
					}
					else{}
					//3 ///////////////////////////////////////////
					if 	((kamni[select][i].color == kamni[select+1][i].color) && 
						(kamni[select][i].color == kamni[select+2][i].color))
					{
						score_audio.play();
						score = score +3;
						kamni[select][i].ONUME();
						kamni[select+1][i].ONUME();
						kamni[select+2][i].ONUME();
					}
					else{}
					//3 ///////////////////////////////////////////////////
					if 	((kamni[select][i].color == kamni[select-2][i].color) && 
						(kamni[select][i].color == kamni[select-1][i].color))
					{
						score_audio.play();
						score = score +3;
						kamni[select][i].ONUME();
						kamni[select-2][i].ONUME();
						kamni[select-1][i].ONUME();
					}
					else{}
				}
			}
			break;
			//-------------------------------------------------------------------------------------------------------------
//-------------------------------------------------------------------------------------------------------------
//-------------------------------------------------------------------------------------------------------------
//-------------------------------------------------------------------------------------------------------------
			case 7: {
				for(var i = 0; i < 10; i++){
					//5 ///////////////////////////////////////////////////
					if 	((kamni[select][i].color == kamni[select-2][i].color) && 
						(kamni[select][i].color == kamni[select-1][i].color) && 
						(kamni[select][i].color == kamni[select+1][i].color) && 
						(kamni[select][i].color == kamni[select+2][i].color))
					{
						score_audio.play();
						score = score +5;
						kamni[select][i].ONUME();
						kamni[select-2][i].ONUME();
						kamni[select-1][i].ONUME();
						kamni[select+1][i].ONUME();
						kamni[select+2][i].ONUME();
					}
					else{}
					//5 //////////////////////////////////////////////////
					if 	((kamni[select][i].color == kamni[select-3][i].color) && 
						(kamni[select][i].color == kamni[select-2][i].color) && 
						(kamni[select][i].color == kamni[select-1][i].color) && 
						(kamni[select][i].color == kamni[select+1][i].color))
					{
						score_audio.play();
						score = score +5;
						kamni[select][i].ONUME();
						kamni[select-3][i].ONUME();
						kamni[select-2][i].ONUME();
						kamni[select-1][i].ONUME();
						kamni[select+1][i].ONUME();
					}
					else{}
					//5 //////////////////////////////////////////////////
					if 	((kamni[select][i].color == kamni[select-4][i].color) && 
						(kamni[select][i].color == kamni[select-3][i].color) && 
						(kamni[select][i].color == kamni[select-2][i].color) && 
						(kamni[select][i].color == kamni[select-1][i].color))
					{
						score_audio.play();
						score = score +5;
						kamni[select][i].ONUME();
						kamni[select-4][i].ONUME();
						kamni[select-3][i].ONUME();
						kamni[select-2][i].ONUME();
						kamni[select-1][i].ONUME();
					}
					else{}
//-------------------------------------------------------------------------------------------------------------
					//4 ////////////////////////////////////////////////////
					if 	((kamni[select][i].color == kamni[select-1][i].color) && 
						(kamni[select][i].color == kamni[select+1][i].color) && 
						(kamni[select][i].color == kamni[select+2][i].color))
					{
						score_audio.play();
						score = score +4;
						kamni[select-1][i].ONUME();
						kamni[select][i].ONUME();
						kamni[select+1][i].ONUME();
						kamni[select+2][i].ONUME();
					}
					else{}
					//4 ///////////////////////////////////////////////////
					if 	((kamni[select][i].color == kamni[select-2][i].color) && 
						(kamni[select][i].color == kamni[select-1][i].color) && 
						(kamni[select][i].color == kamni[select+1][i].color))
					{
						score_audio.play();
						score = score +4;
						kamni[select][i].ONUME();
						kamni[select-2][i].ONUME();
						kamni[select-1][i].ONUME();
						kamni[select+1][i].ONUME();
					}
					else{}
					//4 //////////////////////////////////////////////////
					if 	((kamni[select][i].color == kamni[select-3][i].color) && 
						(kamni[select][i].color == kamni[select-2][i].color) && 
						(kamni[select][i].color == kamni[select-1][i].color))
					{
						score_audio.play();
						score = score +4;
						kamni[select][i].ONUME();
						kamni[select-3][i].ONUME();
						kamni[select-2][i].ONUME();
						kamni[select-1][i].ONUME();
					}
					else{}
//-------------------------------------------------------------------------------------------------------------
					//3 /////////////////////////////////////////////////////
					if 	((kamni[select][i].color == kamni[select-1][i].color) && 
						(kamni[select][i].color == kamni[select+1][i].color))
					{
						score_audio.play();
						score = score +3;
						kamni[select-1][i].ONUME();
						kamni[select][i].ONUME();
						kamni[select+1][i].ONUME();
					}
					else{}
					//3 ///////////////////////////////////////////
					if 	((kamni[select][i].color == kamni[select+1][i].color) && 
						(kamni[select][i].color == kamni[select+2][i].color))
					{
						score_audio.play();
						score = score +3;
						kamni[select][i].ONUME();
						kamni[select+1][i].ONUME();
						kamni[select+2][i].ONUME();
					}
					else{}
					//3 ///////////////////////////////////////////////////
					if 	((kamni[select][i].color == kamni[select-2][i].color) && 
						(kamni[select][i].color == kamni[select-1][i].color))
					{
						score_audio.play();
						score = score +3;
						kamni[select][i].ONUME();
						kamni[select-2][i].ONUME();
						kamni[select-1][i].ONUME();
					}
					else{}
				}
			}
			break;
			//-------------------------------------------------------------------------------------------------------------
//-------------------------------------------------------------------------------------------------------------
//-------------------------------------------------------------------------------------------------------------
//-------------------------------------------------------------------------------------------------------------
			case 8: {
				for(var i = 0; i < 10; i++){
					//5 //////////////////////////////////////////////////
					if 	((kamni[select][i].color == kamni[select-3][i].color) && 
						(kamni[select][i].color == kamni[select-2][i].color) && 
						(kamni[select][i].color == kamni[select-1][i].color) && 
						(kamni[select][i].color == kamni[select+1][i].color))
					{
						score_audio.play();
						score = score +5;
						kamni[select][i].ONUME();
						kamni[select-3][i].ONUME();
						kamni[select-2][i].ONUME();
						kamni[select-1][i].ONUME();
						kamni[select+1][i].ONUME();
					}
					else{}
					//5 //////////////////////////////////////////////////
					if 	((kamni[select][i].color == kamni[select-4][i].color) && 
						(kamni[select][i].color == kamni[select-3][i].color) && 
						(kamni[select][i].color == kamni[select-2][i].color) && 
						(kamni[select][i].color == kamni[select-1][i].color))
					{
						score_audio.play();
						score = score +5;
						kamni[select][i].ONUME();
						kamni[select-4][i].ONUME();
						kamni[select-3][i].ONUME();
						kamni[select-2][i].ONUME();
						kamni[select-1][i].ONUME();
					}
					else{}
//-------------------------------------------------------------------------------------------------------------
					//4 ///////////////////////////////////////////////////
					if 	((kamni[select][i].color == kamni[select-2][i].color) && 
						(kamni[select][i].color == kamni[select-1][i].color) && 
						(kamni[select][i].color == kamni[select+1][i].color))
					{
						score_audio.play();
						score = score +4;
						kamni[select][i].ONUME();
						kamni[select-2][i].ONUME();
						kamni[select-1][i].ONUME();
						kamni[select+1][i].ONUME();
					}
					else{}
					//4 //////////////////////////////////////////////////
					if 	((kamni[select][i].color == kamni[select-3][i].color) && 
						(kamni[select][i].color == kamni[select-2][i].color) && 
						(kamni[select][i].color == kamni[select-1][i].color))
					{
						score_audio.play();
						score = score +4;
						kamni[select][i].ONUME();
						kamni[select-3][i].ONUME();
						kamni[select-2][i].ONUME();
						kamni[select-1][i].ONUME();
					}
					else{}
//-------------------------------------------------------------------------------------------------------------
					//3 /////////////////////////////////////////////////////
					if 	((kamni[select][i].color == kamni[select-1][i].color) && 
						(kamni[select][i].color == kamni[select+1][i].color))
					{
						score_audio.play();
						score = score +3;
						kamni[select-1][i].ONUME();
						kamni[select][i].ONUME();
						kamni[select+1][i].ONUME();
					}
					else{}
					//3 ///////////////////////////////////////////////////
					if 	((kamni[select][i].color == kamni[select-2][i].color) && 
						(kamni[select][i].color == kamni[select-1][i].color))
					{
						score_audio.play();
						score = score +3;
						kamni[select][i].ONUME();
						kamni[select-2][i].ONUME();
						kamni[select-1][i].ONUME();
					}
					else{}
				}
			}
			break;
			//-------------------------------------------------------------------------------------------------------------
//-------------------------------------------------------------------------------------------------------------
//-------------------------------------------------------------------------------------------------------------
//-------------------------------------------------------------------------------------------------------------
			case 9: {
				for(var i = 0; i < 10; i++){
					//5 //////////////////////////////////////////////////
					if 	((kamni[select][i].color == kamni[select-4][i].color) && 
						(kamni[select][i].color == kamni[select-3][i].color) && 
						(kamni[select][i].color == kamni[select-2][i].color) && 
						(kamni[select][i].color == kamni[select-1][i].color))
					{
						score_audio.play();
						score = score +5;
						kamni[select][i].ONUME();
						kamni[select-4][i].ONUME();
						kamni[select-3][i].ONUME();
						kamni[select-2][i].ONUME();
						kamni[select-1][i].ONUME();
					}
					else{}
//-------------------------------------------------------------------------------------------------------------
					//4 //////////////////////////////////////////////////
					if 	((kamni[select][i].color == kamni[select-3][i].color) && 
						(kamni[select][i].color == kamni[select-2][i].color) && 
						(kamni[select][i].color == kamni[select-1][i].color))
					{
						score_audio.play();
						score = score +4;
						kamni[select][i].ONUME();
						kamni[select-3][i].ONUME();
						kamni[select-2][i].ONUME();
						kamni[select-1][i].ONUME();
					}
					else{}
//-------------------------------------------------------------------------------------------------------------
					//3 ///////////////////////////////////////////////////
					if 	((kamni[select][i].color == kamni[select-2][i].color) && 
						(kamni[select][i].color == kamni[select-1][i].color))
					{
						score_audio.play();
						score = score +3;
						kamni[select][i].ONUME();
						kamni[select-2][i].ONUME();
						kamni[select-1][i].ONUME();
					}
					else{}
				}
			}
			break;
		}
	}

function print(){
	ctx.drawImage(bg, 0, 0);
	for(var i = 0; i < 10; i++){
		for(var j = 0; j < 10; j++){
		switch(kamni[i][j].color){
				case 0:{
					ctx.fillStyle ="#f00";
					ctx.fillRect(kamni[i][j].x, kamni[i][j].y, kamni[i][j].bord, kamni[i][j].bord);
				}
				break;

				case 1:{
					ctx.fillStyle ="#f0d";
					ctx.fillRect(kamni[i][j].x, kamni[i][j].y, kamni[i][j].bord, kamni[i][j].bord);
				}
				break;

				case 2:{
					ctx.fillStyle ="#30f";
					ctx.fillRect(kamni[i][j].x, kamni[i][j].y, kamni[i][j].bord, kamni[i][j].bord);
				}
				break;
				
				case 3:{
					ctx.fillStyle ="#0fe";
					ctx.fillRect(kamni[i][j].x, kamni[i][j].y, kamni[i][j].bord, kamni[i][j].bord);
				}
				break;

				case 4:{
					ctx.fillStyle ="#00ff26";
					ctx.fillRect(kamni[i][j].x, kamni[i][j].y, kamni[i][j].bord, kamni[i][j].bord);
				}
				break;

				case 5:{
					ctx.fillStyle ="#d0ff00";
					ctx.fillRect(kamni[i][j].x, kamni[i][j].y, kamni[i][j].bord, kamni[i][j].bord);
				}
				break;

				case 6:{
					ctx.fillStyle ="#fb0";
					ctx.fillRect(kamni[i][j].x, kamni[i][j].y, kamni[i][j].bord, kamni[i][j].bord);
				}
				break;
			}
		}
	}

	 //kamni[5][5].ONUME();

	ctx.fillStyle = "#000";
	ctx.font = "28px Verdana";
	ctx.fillText("Счет: " + score, cvs.width/2, cvs.height - 50);

	ctx.strokeStyle = "white";
	ctx.lineWidth=4;
	ctx.strokeRect(kamni[select][0].x - 1, kamni[select][0].y - 1, 330, 30);

	ctx.fillStyle = "#000";
	ctx.font = "28px Verdana";
	ctx.fillText("Время: " + time/10, cvs.width/2, cvs.height - 130);

	setTimeout(function() {
   		ANIME = requestAnimationFrame(print);
		}, 70);
}

bg.onload = print;

	setInterval(function(){
		CheckColor();
	}, 800);

function Start(){
	if (game == 0) {
																					// 	startAccel = setInterval(function(){ 
																					// 		switch(devstvie){ 
																					// // if(window.DeviceOrientationEvent){ 
																					// // 		window.addEventListener("deviceorientation", Aclr, false); 
																					// // 	}
																					// // 	else{ 
																					// // 		console.log("DeviceMotionEvent is not supported"); 
																					// // 	} 

																					// // function Aclr(event){ 
																					// // 	if (Math.round(event.gamma) > 15){ 
																					// // 	//up 
																					// // 	devstvie = 1;
																					// // 	//	(select == 0) ? select = 9 : select--;
																					// // 	} 
																					// // 	if (Math.round(event.gamma) < -15){ 
																					// // 	//down 
																					// // 		devstvie = 2;
																					// // 	//	(select == 9) ? select = 0 : select++;
																					// // 	} 
																					// // 	if (Math.round(event.beta) > 15){ 
																					// // 	//right 
																					// // 	//switchRight();
																					// // 	devstvie = 3;
																					// // 	} 
																					// // 	if (Math.round(event.beta) < -15){ 
																					// // 	//left 
																					// // 	devstvie = 4;
																					// // 	//switchLeft();
																					// // 	} 
																					// // } 
																					// 			case 4: Up(); break;
																					// 			case 3: Down(); break;
																					// 			case 1: switchRight(); break; 
																					// 			case 2: switchLeft(); break; 
																					// 			} 
																					// 		}, 500);
		location.reload;
		game = 1;
		timer = setInterval(function() {
   			if (time == 0) {
   				clearInterval(timer);
   				// clearInterval(startAccel);
   					alert("Время вышло, ваш счет: " + score);
   					game = 0;
   					time = 600;
   					score = 0;
   					// ctx.fillStyle = "#000";
					// ctx.font = "18px Verdana";
					// ctx.fillText("Время вышло, ваш счет: " + score, cvs.width - 400, 200);
   				}
   			else{
   				time--;
   			}
		}, 100);
	}
	else
	{}
}

