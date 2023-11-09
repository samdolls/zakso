// chekImg 변경
// function checkImg(element) {
//   if (element.src.endsWith("/static/images/blankCheck.svg")) {
//     element.src = "/static/images/checked.svg";
//   } 
//   else {
//     element.src = "/static/images/blankCheck.svg";
//   }
// }

function checkImg(element) {
  // 모든 이미지 초기화
  const checkImgs = document.querySelectorAll('.checkImg');
  checkImgs.forEach(img => {
    img.src = "/static/images/blankCheck.svg";
  });

  // 현재 이미지 선택
  element.src = "/static/images/checked.svg";
}

// 업로드 된 파일 보기
document.getElementById('imgUpload').addEventListener('change', function (e) {
  const imgField = document.querySelector('.imgUploadField');
  let basicImg = document.querySelector(".uploadImg");
  let basicText = document.querySelector(".uploadImgText");
  basicImg.style.display = "none";
  basicText.style.display = "none";
  // imgField.innerHTML = "";
  imgField.style.flexDirection = 'row';
  imgField.style.gap = '0.75rem';
  imgField.style.overflowX = 'scroll';
  // imgField.style.whiteSpace = 'nowrap';

  const files = e.target.files;
  const fileCount = Math.min(files.length, 10); // 최대 10개까지만 허용
  for (let i = 0; i < fileCount; i++) {
    const file = files[i];
    const reader = new FileReader();
    
    const imgElement = document.createElement('img');
    imgElement.style.width = '10.125rem'; // 이미지의 너비 설정
    imgElement.style.height = '10.125em'; // 이미지의 높이 설정
    imgField.appendChild(imgElement); // 이미지 필드에 이미지 추가

    reader.onload = function (event) {
      imgElement.src = event.target.result;
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











