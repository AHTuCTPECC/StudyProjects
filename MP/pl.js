var video;
var duration;
var range;
var volum4ik

window.onload = function(){
	video = document.getElementById('video');
	duration = document.getElementById('range');
	duration.value = 0;
	duration.min = 0;
	duration.max = video.duration;
	volum4ik = document.getElementById('volum4ik');
	timeshow = document.getElementById('timeshow')
} 

function PlayPouse(){
	   if (video.paused) {
            video.play();
            document.getElementById('PP').value = "||";
            range = setInterval(PolziTvar, 1000/66);
        	} 
        else {
            video.pause();
            document.getElementById('PP').value = "►";  
            clearInterval(range);
       	 	}

}

function StopThis(){
	video.currentTime = 0;
	video.pause();
	document.getElementById('PP').value = "►";
}

function FullPlease(){ 
	video.webkitRequestFullscreen();
} 

function PolziTvar () {
	duration.value = video.currentTime;
}

function stopAnime(){
	clearInterval(range);
	if (video.paused) {

	}
	else{
		PlayPouse();
	}
}

function playAgain () {
	video.currentTime = duration.value;
	PlayPouse();
}

function MinusYshi(){
	video.volume = volum4ik.value/100;
}

function timetable(){
	document.getElementById("timeshow").innerHTML= (Math.ceil(video.currentTime/60)-1) + ":" + Math.ceil(video.currentTime - (((Math.ceil(video.currentTime/60)-1)*60))) + "/" + (Math.round(video.duration/60)-1) + ":" + (Math.round(video.duration - (((Math.round(video.duration/60)-1)*60)))+1) ;
}

function SpeedNormal(){
	video.play();
    video.playbackRate = 1;
}

function SpeedUp(){
	video.play();
    video.playbackRate = 2;
}

function SpeedDown(){
	video.play();
    video.playbackRate = 0.5;
}
