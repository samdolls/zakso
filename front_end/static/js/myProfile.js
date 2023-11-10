// 버튼 선택시
function showMyFund() {
  let myPostFundButton = document.querySelector(".myPostFund");
  let wishlistFundButton = document.querySelector(".wishlistFund");
  let noFundText = document.querySelector(".noFundTextBox");
  wishlistFundButton.style.border = "1px solid #D6D6D6";
  wishlistFundButton.style.color = "#1F1F1F";
  myPostFundButton.style.border = "1px solid #F33D69";
  myPostFundButton.style.color = "#F33D69";

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
  myPostFundButton.style.border = "1px solid #D6D6D6";
  myPostFundButton.style.color = "#1F1F1F";
  wishlistFundButton.style.border = "1px solid #F33D69";
  wishlistFundButton.style.color = "#F33D69";

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

