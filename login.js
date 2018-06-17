var inputList = document.querySelectorAll("input");
// TO ADD COLOR CHANGE TO LABEL
for(var i = 0;i<inputList.length;i++){
	inputList[i].addEventListener("focus",function(){
		document.getElementById(this.name).style.color = "rgb(0,39,41)";
	});
	inputList[i].addEventListener("focusout",function(){
		document.getElementById(this.name).style.color = "rgb(153,157,176)";
	});
}
document.querySelector("select").addEventListener("focus",function(){
	document.getElementById(this.name).style.color = "rgb(0,39,41)";
});
document.querySelector("select").addEventListener("focusout",function(){
	document.getElementById(this.name).style.color = "rgb(153,157,176)";
});