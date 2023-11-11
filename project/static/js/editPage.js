// chekImg 변경
// function checkImg(element) {
//   if (element.src.endsWith("/static/images/blankCheck.svg")) {
//     element.src = "/static/images/checked.svg";
//   } 
//   else {
//     element.src = "/static/images/blankCheck.svg";
//   }
// }

function checkImg(radioId) {
  const radio = document.getElementById(radioId);
  // 모든 이미지 초기화
  const checkImgs = document.querySelectorAll('.checkImg');
  checkImgs.forEach(img => {
    img.src = "/static/images/blankCheck.svg";
  });
  radio.checked = !radio.checked;
  // 현재 이미지 선택
  const img = document.querySelector(`#${radioId} + .checkImg`);
  img.src = "/static/images/checked.svg";
}

// 업로드 된 파일 보기
document.getElementById('imgUpload').addEventListener('change', function (e) {
  var previewContainer = document.querySelector('.imgUploadField');
  previewContainer.innerHTML = '';

  var files = e.target.files;

  for (var i = 0; i < files.length; i++) {
    var file = files[i];
    var reader = new FileReader();

    reader.onload = function (e) {
      var img = document.createElement('img');
      img.src = e.target.result;
      img.alt = 'upload';
      img.className = 'uploadImg';
      img.style='width:100%; height:100%;'
      previewContainer.appendChild(img);
    };

    reader.readAsDataURL(file);
  }
});

// 파일 초기화하기
function resetFile() {
  const imgElements = document.querySelectorAll('.imgUploadField img');
  let basicImg = document.querySelector(".uploadImg");
  let basicText = document.querySelector(".uploadImgText");

  if (imgElements.length > 0) {
    for(let i=0; i<imgElements.length-1;i++) {
      imgElements.forEach(img => {
        img.remove();
      });
    }
    basicImg.style.display = "inline";
    basicText.style.display = "block";
  }
}