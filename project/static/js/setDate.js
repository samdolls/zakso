// 년,월,일 dropbox
let today = new Date();
let todayYear = today.getFullYear();
let index = 0;
let startYear = todayYear - 10;
let endYear = todayYear + 10;

for(let i = startYear; i<=endYear; i++) {
  document.getElementById("setYear").options[index] = new Option(i, i);
  document.getElementById("setYear").value = todayYear;
  index++;
}
index = 0;

let todayMonth = today.getMonth()+1;
let startMonth = 1;
let endMonth = 12;
for(startMonth; startMonth<=endMonth; startMonth++) {
  document.getElementById("setMonth").options[index] = new Option(startMonth, startMonth);
  document.getElementById("setMonth").value = todayMonth;
  index++;
}
index = 0;

let todayDay = today.getDate();
function updateDays() {
  let selectedMonth = parseInt(document.getElementById("setMonth").value);
  let startDay = 1;
  let endDay = new Date(todayYear, selectedMonth, 0).getDate();
  
  for (let i = 0; i < setDay.options.length; i++) {
    setDay.options[i].style.display = "none";
  }
  for(startDay; startDay<=endDay; startDay++) {
    document.getElementById("setDay").options[index] = new Option(startDay, startDay);
    index++;
  }
}
updateDays();
document.getElementById("setMonth").addEventListener("change", updateDays);
document.getElementById("setDay").value = todayDay;

// 이미지 클릭 시 드랍다운 보이기
// function showDropdown() {
//   let option = document.getElementById("setYear").options;
//   if(option.style.display === "none") {
//     option.style.dispaly = "block";
//   }
//   else {
//     option.style.display = "none";
//   }
// }