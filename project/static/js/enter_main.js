function checkOnlyOne(element) {
  
  const checkboxes 
      = document.getElementsByName("choice");
  
  checkboxes.forEach((cb) => {
    cb.checked = false;
  })
  
  element.checked = true;
}