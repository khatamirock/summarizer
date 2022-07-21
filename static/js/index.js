
var slider = document.getElementById("slder");
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



    var data = JSON.stringify({
        "doc": doctoSend.value,
        "ratio": slider.value

    });


    var xhr = new XMLHttpRequest();
    xhr.withCredentials = true;

    xhr.addEventListener("readystatechange", function () {
        if (this.readyState === 4) {
            console.log(this.responseText);
            dat = JSON.parse(this.responseText);
            docReceived.value = dat['Summery'];
        }
    });

    xhr.open("POST", "/sumry");
    xhr.setRequestHeader("content-type", "application/json");
    xhr.setRequestHeader("cache-control", "no-cache");

    xhr.send(data);


})
console.debug(xx);






