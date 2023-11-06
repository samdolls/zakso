// // 슬라이드 만들기
// // 슬라이드 너비(전체 크기)
// const slide = document.querySelector(".bannerBox");
// let slideWidth = slide.clientWidth;
// // 슬라이드 전체를 선택해 값을 변경해주기 위해 슬라이드 전체 선택하기
// let slideItems = document.querySelectorAll(".slideItem");
// // 현재 슬라이드 위치가 슬라이드 개수를 넘어가지 않게 하기 위한 변수
// const maxSlide = slideItems.length;
// // 현재 슬라이드
// let currentSlide = 1;
// // 페이지네이션
// const pagination = document.querySelector(".dotList");
// const paginationItems = document.querySelectorAll(".dotList span");
// // 무한 슬라이드 생성
// const startSlide = slideItems[0];
// const endSlide = slideItems[slideItems.length - 1];
// const startElem = document.createElement("div");
// const endElem = document.createElement("div");
// endSlide.classList.forEach((c) => endElem.classList.add(c));
// endElem.innerHTML = endSlide.innerHTML;
// startSlide.classList.forEach((c) => startElem.classList.add(c));
// startElem.innerHTML = startSlide.innerHTML;
// // 각 복제한 엘리먼트 추가하기
// slideItems[0].before(endElem);
// slideItems[slideItems.length - 1].after(startElem);
// // 이동시키기
// let offset = slideWidth + currentSlide;
// slideItems.forEach((i) => {
//   i.setAttribute("style", `left: ${-offset}px`);
// });




// 찜하기
function toggleImg(element) {
  if(element.src.endsWith("blankHeart.svg")) {
    element.src = "/front_end/static/images/fillHeart.svg";
  }
  else {
    element.src = "/front_end/static/images/blankHeart.svg";
  }
}