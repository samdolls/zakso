// progressbar 진행상황
document.addEventListener("DOMContentLoaded", function() {
  // 반복되는 요소들에 대한 NodeList를 가져옵니다.
  let presentElements = document.querySelectorAll('.listBox');

  // NodeList를 배열로 변환하여 반복합니다.
  presentElements.forEach(function(presentElement, index) {
    let totalMoney = parseInt(presentElement.querySelector('.totalMoney1').textContent);
    let currentMoney = parseInt(presentElement.querySelector('.currentMoney1').textContent);
    let progress = (currentMoney / totalMoney) * 100;
    
    // 각 요소에 대한 식별자를 사용하여 업데이트합니다.
    let progressBar = presentElement.querySelector('.bar1');
    progressBar.style.width = progress + '%';
    progressBar.setAttribute('aria-valuenow', progress);

    let currentPercent = presentElement.querySelector('.currentPercent');
    currentPercent.innerText = Math.round(progress);
  });
});