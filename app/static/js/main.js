var modal = document.getElementById("formModal");

var btn = document.getElementById("modalBtn");

var span = document.getElementsByClassName("close")[0];
// opening modal by clicking the button
btn.onclick = function(){
    modal.style.display = "block";
}
// closing modal clicking x 
span.onclick = function() {
    modal.style.display = "none";
  }
// close modal clicking outside of it
window.onclick = function(event) {
    if (event.target == modal) {
      modal.style.display = "none";
    }
}
// close modal with esc key
window.addEventListener("keyup", escapeClose);
function escapeClose(e) {
    if (e.keyCode === 27) {
        modal.style.display = "none";
    }
}
