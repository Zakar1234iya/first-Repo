//var likes = 3;

function increaseLikes(likesNum) {
    //likes++;
    let label = document.getElementById(likesNum);
    //alert(label.innerText)
    var likes = parseInt(label.innerText);
    likes++
    label.innerText = likes;
}