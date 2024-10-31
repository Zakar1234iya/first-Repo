console.log("page loaded...");

function mouseOver(){
    var x = document.getElementById("myVideo"); 
    x.muted = "true";
    x.play();
    
}
function mouseOut(){
    var x = document.getElementById("myVideo"); 
    x.muted = "false";
    x.pause();
    
}