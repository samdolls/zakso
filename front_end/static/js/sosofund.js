let cnt = 0;

function input_append() {
  cnt++;
  const app = document.getElementById("append");

  // Create a container div for each set of input boxes
  const rewardContainer = document.createElement("div");

  // Append 펀딩 금액 input box
  const fundingInput = document.createElement("input");
  fundingInput.type = "text";
  fundingInput.placeholder = "펀딩 금액";
  fundingInput.name = "funding_" + cnt; // Add a unique name for each input
  rewardContainer.appendChild(fundingInput);

  // Append 리워드 이름 input box
  const rewardNameInput = document.createElement("input");
  rewardNameInput.type = "text";
  rewardNameInput.placeholder = "리워드 이름";
  rewardNameInput.name = "rewardName_" + cnt; // Add a unique name for each input
  rewardContainer.appendChild(rewardNameInput);

  // Append the container to the main div
  app.appendChild(rewardContainer);
}

function input_result(ff) {
  let str = "";
  for (let i = 1; i <= cnt; i++) {
    const fundingValue = ff["funding_" + i].value;
    const rewardNameValue = ff["rewardName_" + i].value;
    str += `펀딩 금액: ${fundingValue}, 리워드 이름: ${rewardNameValue} | `;
  }
  alert(str);
}


         