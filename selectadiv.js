   
 function untoggle() {
	window.selectedid = 'none';
}
  
  function toggle(tovalue) {
	if (window.selectedid == 'none') {
		window.selectedid = tovalue;
		console.log('SET')
		document.getElementById(tovalue).style.background = 'black';
	} else {
		window.selectedid = 'none';
		console.log('RESET')
		document.getElementById(tovalue).style.background = '#3b55cc';
	}
}
function plot(event) {
	document.getElementById(window.selectedid).style.left = event.clientX - 10+'px'
	document.getElementById(window.selectedid).style.top = event.clientY - 10+'px'
	console.log('Moved to x='+event.clientX+' y='+event.clientY+' id='+window.selectedid)
}

document.body.addEventListener('mousemove', e => {
plot(e);
})