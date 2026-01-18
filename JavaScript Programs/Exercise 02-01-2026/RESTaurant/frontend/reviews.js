document.getElementById("review-image-form").addEventListener('submit', function(e) {
    e.preventDefault();
    
    const formdata = new FormData();
    const pb = document.getElementById("progress-bar");
    formdata.append("image", document.getElementById("image").files[0]);
    pb.classList.remove("d-none")

    var xhr = new XMLHttpRequest();
    xhr.open('POST', "http://127.0.0.1:3000/review/add-review", true);

    xhr.upload.onprogress = function (e) {
        if (e.lengthComputable) {
            const percent = Math.round((e.loaded / e.total) * 100);
            pb.style.width = percent + "%";
            pb.innerHTML = percent + "%";
        }
    };

    xhr.onload = function () {
        pb.style.width = "100%";
        pb.innerHTML = "100%";
    };

    xhr.onerror = function () {
        pb.innerHTML = "Error";
    };


    xhr.send(formdata);
});
