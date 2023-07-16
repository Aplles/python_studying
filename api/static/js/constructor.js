//блок с текстом
function createBlock() {
  const divBlock = document.createElement("div");
  divBlock.classList.add("divBlock");
  const title = document.createElement("p");
  title.innerHTML = "БЛОК С ТЕКСТОМ - TextBlock_TEXT";

  // Создаем новый блок p
  const P = document.createElement("P");
  divBlock.appendChild(P);
  P.classList.add("block");
  // Создаем input для ввода текста
  var input = document.createElement("input");
  input.type = "text";
  input.classList.add("inputBtn");
  input.name = "TextBlock_TEXT_позиция_text";

  var deleteButton = document.createElement("button");
  deleteButton.innerHTML = "Удалить";
  deleteButton.classList.add("dltBtn");
  deleteButton.onclick = function () {
    divBlock.remove();
    title.remove();
  };

  divBlock.appendChild(input);

  // Добавляем новый блок в контейнер
  const container = document.getElementById("blocks-container");
  container.appendChild(title);
  container.appendChild(divBlock);
  divBlock.appendChild(deleteButton);
}

//блок с текстом
function createBlock_H1() {
  // const container = document.getElementById("blocks-container");

  const divBlock = document.createElement("div");
  divBlock.classList.add("divBlock");
  // Создаем новый блок h1
  const H1 = document.createElement("h1");
  H1.classList.add("block");
  divBlock.appendChild(H1);
  const title = document.createElement("p");
  title.innerHTML = "БЛОК С ЗАГОЛОВКОМ - TextBlock_HEADERTEXT";

  // Создаем input для ввода текста
  var input = document.createElement("input");
  input.type = "text";
  input.classList.add("inputBtn");
  input.name = "TextBlock_HEADERTEXT_текст_text";
  var deleteButton = document.createElement("button");
  deleteButton.innerHTML = "Удалить";
  deleteButton.classList.add("dltBtn");
  deleteButton.onclick = function () {
    divBlock.remove();
    title.remove();
  };

  divBlock.appendChild(input);
  // Добавляем новый блок в контейнер
  const container = document.getElementById("blocks-container");
  container.appendChild(title);
  container.appendChild(divBlock);
  divBlock.appendChild(deleteButton);
}

//добавление блока текст_линия
function createBlock_TextBlock_Line() {
  // blockCount++; // Увеличиваем значение нарастающего числа id

  const divBlock = document.createElement("div");
  divBlock.classList.add("divBlock");
  // Создаем новый блок div
  const block = document.createElement("div");

  block.classList.add("designation"); // Добавляем класс "designation"
  block.classList.add("block");
  divBlock.appendChild(block);
  // Создаем элемент p и добавляем текст
  const P = document.createElement("p");
  const title = document.createElement("p");
  title.innerHTML = "БЛОК ТЕКСТ ЛИНИЯ - TextBlock_QUOTETEXT";

  // Создаем SVG элемент
  const svg = document.createElementNS("http://www.w3.org/2000/svg", "svg");
  svg.setAttribute("width", "10");
  svg.setAttribute("height", "81");
  svg.setAttribute("viewBox", "0 0 4 81");
  svg.setAttribute("fill", "none");

  // Создаем path элемент
  const path = document.createElementNS("http://www.w3.org/2000/svg", "path");
  path.setAttribute("d", "M2 2L2 79");
  path.setAttribute("stroke", "white");
  path.setAttribute("stroke-width", "4");
  path.setAttribute("stroke-linecap", "round");
  // Добавляем svg и p в блок
  block.appendChild(svg);
  svg.appendChild(path);
  block.appendChild(P);
  // Создаем input для ввода текста
  var input = document.createElement("input");
  input.type = "text";
  input.classList.add("inputBtn");
  input.name = "TextBlock_QUOTETEXT_код_text";
  var deleteButton = document.createElement("button");
  deleteButton.innerHTML = "Удалить";
  deleteButton.classList.add("dltBtn");
  deleteButton.onclick = function () {
    divBlock.remove();
    title.remove();
  };

  divBlock.appendChild(input);

  // Добавляем новый блок в контейнер
  const container = document.getElementById("blocks-container");
  container.appendChild(title);
  container.appendChild(divBlock);
  divBlock.appendChild(deleteButton);
}

//добавление блока с кодом
function createBlock_TextBlock_CODE() {
  // blockCount++; // Увеличиваем значение нарастающего числа id
  const divBlock = document.createElement("div");
  divBlock.classList.add("divBlock");

  // Создаем новый блок p
  const P = document.createElement("P");
  divBlock.appendChild(P);
  P.classList.add("block");

  const title = document.createElement("p");
  title.innerHTML = "БЛОК С КОДОМ - TextBlock_CODE";

  // Создаем новый блок div
  const block = document.createElement("div");
  block.classList.add("example_designation"); // Добавляем класс "designation"
  block.classList.add("block");
  divBlock.appendChild(block);
  block.appendChild(P);
  // Создаем input для ввода текста
  var input = document.createElement("input");
  input.type = "text";
  input.classList.add("inputBtn");
  input.name = "TextBlock_CODE_код_text";
  var deleteButton = document.createElement("button");
  deleteButton.innerHTML = "Удалить";
  deleteButton.classList.add("dltBtn");
  deleteButton.onclick = function () {
    divBlock.remove();
    title.remove();
  };

  divBlock.appendChild(input);
  // Добавляем новый блок в контейнер
  const container = document.getElementById("blocks-container");
  container.appendChild(title);
  container.appendChild(divBlock);
  divBlock.appendChild(deleteButton);
}

//добавление блока с картинкой
function createBlock_ImageBlock() {
  // Создаем новый блок section
  const section = document.createElement("section");
  section.classList.add("codeExample"); // Добавляем класс "codeExample"
  section.classList.add("divBlock");

  const title = document.createElement("p");
  title.innerHTML = "БЛОК С КАРТИНКОЙ - ImageBlock";

  // Создаем элемент img
  var imagePreview = document.createElement("img");
  var imageInput = document.createElement("input");
  imageInput.type = "file";
  imageInput.name = "ImageBlock_позиция_image";
  imageInput.classList.add("inputBtn");

  imageInput.addEventListener("change", function (event) {
    var file = event.target.files[0];
    var reader = new FileReader();

    reader.onload = function (e) {
      imagePreview.src = e.target.result;
    };

    reader.readAsDataURL(file);
  });

  var deleteButton = document.createElement("button");
  deleteButton.innerHTML = "Удалить";
  deleteButton.classList.add("dltBtn");
  deleteButton.onclick = function () {
    // При клике на кнопку удаляем блок
    deleteButton.remove();
    title.remove();
    section.remove();
  };

  // Добавляем элемент img в блок section

  section.appendChild(imageInput);
  section.appendChild(imagePreview);
  // Добавляем новый блок в контейнер
  const container = document.getElementById("blocks-container");
  container.appendChild(title);
  container.appendChild(section);
  container.appendChild(deleteButton);
}

function createBlock_link() {
  const divBlock = document.createElement("div");
  divBlock.classList.add("divBlock");

  // const title = document.createElement("p");
  // title.innerHTML = "БЛОК С ССЫЛКОЙ - LinkBlock";

  // Создаем новый блок nav_lesson
  const lessons_designation = document.createElement("div");
  lessons_designation.classList.add("lessons_designation");
  divBlock.appendChild(lessons_designation);
  var navLesson_btn = document.createElement("button");
  navLesson_btn.innerHTML = "Добавить";
  navLesson_btn.classList.add("dltBtn");
  divBlock.appendChild(navLesson_btn);

  function create_navLesson() {
    const nav_lesson = document.createElement("div");
    nav_lesson.classList.add("nav_lesson");
    lessons_designation.appendChild(nav_lesson);

    const img = document.createElement("img");
    img.src = "./assets/2basics.svg";
    nav_lesson.appendChild(img);

    const P = document.createElement("p");
    nav_lesson.appendChild(P);

    // Создаем input для ввода текста
    var input = document.createElement("input");
    input.type = "text";
    input.classList.add("inputBtn");
    input.name = "LinkBlock_позиция_text";

    var deleteButton = document.createElement("button");
    deleteButton.innerHTML = "Удалить";
    deleteButton.classList.add("dltBtn");
    deleteButton.onclick = function () {
      divBlock.remove();
      title.remove();
    };

    nav_lesson.appendChild(input);
    lessons_designation.appendChild(deleteButton);
  }
  // Добавляем новый блок в контейнер
  const container = document.getElementById("blocks-container");

  // container.appendChild(title);
  container.appendChild(divBlock);
  navLesson_btn.onclick = create_navLesson;
}

//добавление hr
function createBlock_hrBlock() {
  const divBlock = document.createElement("div");
  divBlock.classList.add("divBlock");
  // Создаем новый блок hr
  const hr = document.createElement("hr");

  const title = document.createElement("p");
  title.innerHTML = "БЛОК hr";
  // Создаем input для ввода текста
  var input = document.createElement("input");
  input.type = "text";
  input.value = "hr1";
  input.classList.add("inputBtn");
  input.classList.add("hrInput");
  input.name = "DividerBlock_позиция_hr";
  input.style.visibility = "hidden";
  // Создаем кнопку "удалить"
  var deleteButton = document.createElement("button");
  deleteButton.innerHTML = "Удалить";
  deleteButton.classList.add("dltBtn");
  deleteButton.onclick = function () {
    // При клике на кнопку удаляем блок
    divBlock.remove();
    deleteButton.remove();
    title.remove();
  };
  // Добавляем новый блок в контейнер

  const container = document.getElementById("blocks-container");
  container.appendChild(title);
  container.appendChild(divBlock);
  divBlock.appendChild(hr);
  divBlock.appendChild(input);
  hr.appendChild(deleteButton);
}

function createBlock_ExplanationDesignation() {
  const explanationDesignation = document.createElement("div");
  explanationDesignation.classList.add("explanation_designation");
  explanationDesignation.classList.add("divBlock");

  const title = document.createElement("p");
  title.innerHTML = "БЛОК С ИКОНКОЙ И ТЕКСТОМ - CalloutBlock";

  var input = document.createElement("input");
  input.type = "text";
  input.name = "CalloutBlock_позиция_text";
  input.classList.add("inputBtn");

  var imageInput = document.createElement("input");
  imageInput.type = "file";
  imageInput.name = "CalloutBlock_позиция_image";
  imageInput.classList.add("inputBtn");

  const img = document.createElement("img");
  const p = document.createElement("p");

  imageInput.addEventListener("change", function (event) {
    var file = event.target.files[0];
    var reader = new FileReader();

    reader.onload = function (e) {
      img.src = e.target.result;
    };

    reader.readAsDataURL(file);
  });

  var deleteButton = document.createElement("button");
  deleteButton.classList.add("dltBtn");
  deleteButton.innerHTML = "Удалить";
  deleteButton.onclick = function () {
    deleteButton.remove();
    explanationDesignation.remove();
    title.remove();
  };
  explanationDesignation.appendChild(img);
  // explanationDesignation.appendChild(svg);
  explanationDesignation.appendChild(p);

  explanationDesignation.appendChild(imageInput);
  explanationDesignation.appendChild(input);

  const container = document.getElementById("blocks-container");
  container.appendChild(title);
  container.appendChild(explanationDesignation);
  explanationDesignation.appendChild(deleteButton);
}

function hideBtn() {
  var buttons = document.getElementsByClassName("dltBtn");

  for (var i = 0; i < buttons.length; i++) {
    buttons[i].style.display = "none";
  }
}

function saveInputs() {
  var main = document.querySelector("main");
  var inputs = main.querySelectorAll("input");
  var count = 1;

  inputs.forEach(function (input) {
    var name = input.name.split("_");
    var type = name[0];
    var newName = name.join("_");

    // Получить родительский элемент divBlock
    var parentDivBlock = input.closest(".divBlock");

    // Получить id родительского элемента divBlock
    var divBlockId = parentDivBlock.getAttribute("id");

    // Заменить _позиция в имени newName
    newName = newName.replace("_позиция", "_" + divBlockId);

    if (type === "TextBlock_TEXT_" && input.name.includes("_позиция_text")) {
      newName = "TextBlock_TEXT_" + divBlockId + "_text";
    } else if (type === "TextBlock" && input.name.includes("_код_text")) {
      newName = "TextBlock_CODE_" + divBlockId + "_text";
    } else if (
      type === "CalloutBlock" &&
      input.name.includes("_позиция_text")
    ) {
      newName = "CalloutBlock_" + divBlockId + "_text";
    } else if (
      type === "CalloutBlock" &&
      input.name.includes("_позиция_image")
    ) {
      newName = "CalloutBlock_" + divBlockId + "_image";
    } else if (type === "TextBlock" && input.name.includes("_текст_text")) {
      newName = "TextBlock_HEADERTEXT_" + divBlockId + "_text";
    } else if (type === "LinkBlock" && input.name.includes("_позиция_text")) {
      newName = "LinkBlock_" + divBlockId + "_text";
    } else if (type === "ImageBlock" && input.name.includes("_позиция_image")) {
      newName = "ImageBlock_" + divBlockId + "_image";
    } else if (type === "TextBlock" && input.name.includes("_код_text")) {
      newName = "TextBlock_QUOTETEXT_" + divBlockId + "_text";
    } else if (type === "DividerBlock" && input.name.includes("_позиция_hr")) {
      newName = "DividerBlock_" + divBlockId;
    }

    input.name = newName;
  });
}
//id
function assignIDs() {
  var blocks = document.getElementsByClassName("divBlock");
  var input = document.getElementsByClassName("inputBtn");

  for (var i = 0; i < blocks.length; i++) {
    blocks[i].id = i + 1;
  }
  saveInputs();
  hideBtn();
}
