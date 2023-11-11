function copyUrl() {
    var currentUrl = window.location.href;

    var tempInput = document.createElement("input");
    tempInput.value = currentUrl;
    document.body.appendChild(tempInput);
    tempInput.select();
    document.execCommand("copy");
    document.body.removeChild(tempInput);

    alert('링크가 복사되었습니다: ' + currentUrl);
}
