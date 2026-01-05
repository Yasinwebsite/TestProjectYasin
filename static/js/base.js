const menu = document.querySelector(".menu");
const menuList = document.querySelector(".menu-list");
const menuToggle = document.querySelector(".menu .button");
menuToggle.addEventListener("click", function () {
  menu.classList.toggle("active");
  menuList.classList.toggle("active");
});
