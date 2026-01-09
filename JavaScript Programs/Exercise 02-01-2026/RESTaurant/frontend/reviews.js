document.getElementById("review-image-form").addEventListener('submit', function(e) {
    e.preventDefault();
    
    const formdata = new FormData();
    const pb = document.getElementById("progress-bar");
    formdata.append("image", document.getElementById("image").files[0]);
    pb.classList.remove("d-none")
    let fakeProgress = 0;
    let fakeInterval;

    var xhr = new XMLHttpRequest();
    xhr.open('POST', "http://127.0.0.1:3000/review/add-review", true);

    xhr.upload.onprogress = function(e) {
        if (e.lengthComputable) {
            let realPercent = Math.round((e.loaded / e.total) * 70);
            fakeProgress = Math.max(fakeProgress, realPercent);
            pb.style.width = fakeProgress + "%";
            pb.innerHTML = fakeProgress + "%";
        }
    };

    xhr.onloadstart = function () {
        fakeInterval = setInterval(() => {
            if (fakeProgress < 95) {
                fakeProgress++;
                pb.style.width = fakeProgress + "%";
                pb.innerHTML = fakeProgress + "%";
            }
        }, 200);
    };

    xhr.onload = function () {
        clearInterval(fakeInterval);
        pb.style.width = "100%";
        pb.innerHTML = "100%";
    };

    xhr.onerror = function () {
        clearInterval(fakeInterval);
        pb.innerHTML = "Error";
    };

    xhr.send(formdata);
});
