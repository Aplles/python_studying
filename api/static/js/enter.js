const wrapper = document.querySelector(".wrapper");
const mainInfo = document.querySelector(".mainInfo");
const signInBtn = document.querySelector(".enter");
const footer = document.querySelector("footer");
const header = document.querySelector("header");

signInBtn.addEventListener("click", () => {
    wrapper.classList.add("active");
    mainInfo.classList.add("noactive");
    header.classList.add("activet");
    footer.classList.add("noactive");
});
