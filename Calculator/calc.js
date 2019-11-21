var arr = [];
var razr;
var devstvie;
razr = 0;
devstvie = 0;
arr = [0, 0];

function OnClick_0() {
	razr < 1 ? arr[0] = arr[0] * 10 + 0 : arr[1] = arr[1] * 10 + 0;
	razr < 1 ? document.getElementById('strochka').value = arr[0] : document.getElementById('strochka').value = arr[1];
}


function OnClick_1() {
	razr < 1 ? arr[0] = arr[0] * 10 + 1 : arr[1] = arr[1] * 10 + 1;
	razr < 1 ? document.getElementById('strochka').value = arr[0] : document.getElementById('strochka').value = arr[1];
}

function OnClick_2() {
	razr < 1 ? arr[0] = arr[0] * 10 + 2 : arr[1] = arr[1] * 10 + 2;
	razr < 1 ? document.getElementById('strochka').value = arr[0] : document.getElementById('strochka').value = arr[1];
}

function OnClick_3() {
	razr < 1 ? arr[0] = arr[0] * 10 + 3 : arr[1] = arr[1] * 10 + 3;
	razr < 1 ? document.getElementById('strochka').value = arr[0] : document.getElementById('strochka').value = arr[1];
}

function OnClick_4() {
	razr < 1 ? arr[0] = arr[0] * 10 + 4 : arr[1] = arr[1] * 10 + 4;
	razr < 1 ? document.getElementById('strochka').value = arr[0] : document.getElementById('strochka').value = arr[1];
}

function OnClick_5() {
	razr < 1 ? arr[0] = arr[0] * 10 + 5 : arr[1] = arr[1] * 10 + 5;
	razr < 1 ? document.getElementById('strochka').value = arr[0] : document.getElementById('strochka').value = arr[1];
}

function OnClick_6() {
	razr < 1 ? arr[0] = arr[0] * 10 + 6 : arr[1] = arr[1] * 10 + 6;
	razr < 1 ? document.getElementById('strochka').value = arr[0] : document.getElementById('strochka').value = arr[1];
}

function OnClick_7() {
	razr < 1 ? arr[0] = arr[0] * 10 + 7 : arr[1] = arr[1] * 10 + 7;
	razr < 1 ? document.getElementById('strochka').value = arr[0] : document.getElementById('strochka').value = arr[1];
}

function OnClick_8() {
	razr < 1 ? arr[0] = arr[0] * 10 + 8 : arr[1] = arr[1] * 10 + 8;
	razr < 1 ? document.getElementById('strochka').value = arr[0] : document.getElementById('strochka').value = arr[1];
}

function OnClick_9() {
	razr < 1 ? arr[0] = arr[0] * 10 + 9 : arr[1] = arr[1] * 10 + 9;
	razr < 1 ? document.getElementById('strochka').value = arr[0] : document.getElementById('strochka').value = arr[1];
}

function OnClick_C() {
	arr[0] = 0;
	arr[1] = 0;
	razr = 0;
	razr < 1 ? document.getElementById('strochka').value = arr[0] : document.getElementById('strochka').value = arr[1];
}

function OnClick_A() {
	alert("Ну и чего ты ожидал?");
}

function OnClick_B() {
	alert("Да, а вот В будет работать, конечно");
}

function OnClick_plus() {
	devstvie = 1;
	razr = 1;
	arr[1] = 0;
	document.getElementById('strochka').value = arr[1];
}

function OnClick_minus() {
	devstvie = 2;
	razr = 1;
	arr[1] = 0;
	document.getElementById('strochka').value = arr[1];
}


function OnClick_div() {
	devstvie = 3;
	razr = 1;
	arr[1] = 0;
	document.getElementById('strochka').value = arr[1];
}

function OnClick_mult() {
	devstvie = 4;
	razr = 1;
	arr[1] = 0;
	document.getElementById('strochka').value = arr[1];
}

function Schitai_poshalyista_ochen_nada() {
	switch(devstvie){
	case 1:{
		arr[0] = arr[0] + arr[1];
		document.getElementById('strochka').value = arr[0];
		}	
	break;

	case 2:{
		arr[0] = arr[0] - arr[1];
		document.getElementById('strochka').value = arr[0];
		}	
	break;

	case 3:{
		if (arr[1] != 0){
		arr[0] = arr[0] / arr[1];
		document.getElementById('strochka').value = arr[0];
		}
		else
		alert("Ты на что делишь дядя?");
		}	
	break;

	case 4:{
		arr[0] = arr[0] * arr[1];
		document.getElementById('strochka').value = arr[0];
		}	
	break;
}
}




