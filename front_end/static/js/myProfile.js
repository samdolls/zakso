// 버튼 선택시
function showMyFund() {
  let myPostFundButton = document.querySelector(".myPostFund");
  let wishlistFundButton = document.querySelector(".wishlistFund");
  let noFundText = document.querySelector(".noFundTextBox");
  let wishText = document.querySelector(".noWishTextBox");
  wishlistFundButton.style.border = "1px solid #D6D6D6";
  wishlistFundButton.style.color = "#1F1F1F";
  myPostFundButton.style.border = "1px solid #F33D69";
  myPostFundButton.style.color = "#F33D69";
  wishText.style.display = "none";

  document.querySelectorAll(".blankHeart").forEach(fillHeart => {
    let article = fillHeart.closest("article");
    let listBox = article.querySelector(".listBox");

    article.style.display = fillHeart.classList.contains("blankHeart") ? "block" : "none";
    listBox.style.display = fillHeart.classList.contains("blankHeart") ? "flex" : "none";

    if(article.style.display === "none") {
      noFundText.style.display = "block"
    }
    else {
      noFundText.style.display = "none";
    }
  });
}
function showWishFund() {
  let myPostFundButton = document.querySelector(".myPostFund");
  let wishlistFundButton = document.querySelector(".wishlistFund");
  let wishText = document.querySelector(".noWishTextBox");
  let noFundText = document.querySelector(".noFundTextBox");
  myPostFundButton.style.border = "1px solid #D6D6D6";
  myPostFundButton.style.color = "#1F1F1F";
  wishlistFundButton.style.border = "1px solid #F33D69";
  wishlistFundButton.style.color = "#F33D69";
  noFundText.style.display = "none";

  document.querySelectorAll(".blankHeart").forEach(fillHeart => {
    let article = fillHeart.closest("article");
    let listBox = article.querySelector(".listBox");
    article.style.display = fillHeart.src.endsWith("fillHeart.svg") ? "block" : "none";
    listBox.style.display = fillHeart.src.endsWith("fillHeart.svg") ? "flex" : "none";
    if(article.style.display === "none") {
      wishText.style.display = "block";
    }
    else {
      wishText.style.display = "none";
    }
  });
}

// 세팅 눌렀을 시 
function showFunctionBox() {
  let bodyElement = document.body;
  let functionBox = document.querySelector(".functionBoxSection");
  if(functionBox.style.display === "none") {
    functionBox.style.display = "flex";
    bodyElement.background = "rgba(49, 49, 49, 0.50)";
    bodyElement.style.backdropFilter = 'blur(10px)';
  }
}
