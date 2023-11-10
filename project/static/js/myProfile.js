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

  document.querySelectorAll(".myPostFund").forEach(article => {
    article.style.display = "block";
  });
  document.querySelectorAll(".wishlistFund").forEach(article => {
    article.style.display = "none";
  });

  if (document.querySelector(".myPostFund:empty")) {
    noFundText.style.display = "block";
  } else {
    noFundText.style.display = "none";
  }
  wishText.style.display = "none";
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

  document.querySelectorAll(".wishlistFund").forEach(article => {
    article.style.display = "block";
  });
  document.querySelectorAll(".myPostFund").forEach(article => {
    article.style.display = "none";
  });

  if (document.querySelector(".wishlistFund:empty")) {
    wishText.style.display = "block";
  } else {
    wishText.style.display = "none";
  }
  noFundText.style.display = "none";
}

// 세팅 눌렀을 시
let functionBox = document.querySelector(".functionBoxSection");
functionBox.style.display = "none"; 
function showFunctionBox() {
  let bodyElement = document.body;
  let allElementsExceptFunctionBox = document.querySelectorAll("body > *:not(.functionBoxSection)")
  if(functionBox.style.display === "none") {
    functionBox.style.display = "block";
    allElementsExceptFunctionBox.forEach(element => {
      element.style.filter = 'blur(10px)';
      element.style.backgroundColor = "rgba(49, 49, 49, 0.50)";
    });
    bodyElement.style.backgroundColor = "rgba(49, 49, 49, 0.50)";
    bodyElement.style.backdropFilter = 'blur(10px)';
  }
}
