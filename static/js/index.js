

var doctoSend = document.querySelector('.textdiv .input');
var btn = document.querySelector('.textdiv .btn');
var docReceived = document.querySelector('.textdiv2 .input');
docReceived.disabled = true;

doctoSend.hasPointerCapture


btn.addEventListener('click', () => {
    // console.debug(doctoSend.value);
    docReceived.value = doctoSend.value;
    docReceived.disabled = false;
    btn.textContent = 'SUMMARIZED';
})
console.debug(xx);








