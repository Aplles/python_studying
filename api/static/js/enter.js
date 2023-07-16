const wrapper = document.querySelector(".wrapper");
const mainInfo = document.querySelector(".mainInfo");
const signInBtn = document.querySelector(".enter");
const footer = document.querySelector("footer");

signInBtn.addEventListener("click", () => {
  wrapper.classList.add("active");
  mainInfo.classList.add("noactive");
  footer.classList.add("noactive");
});
