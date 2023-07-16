var paragraphs = document.getElementsByTagName("p");
for (var i = 0; i < paragraphs.length; i++) {
  var text = paragraphs[i].innerHTML;

  var regexQuotes = /“([^”]+)”/g;
  text = text.replace(regexQuotes, '<span class="green-text">"$1"</span>');

  var regexEquals = /\s=\s/g;
  text = text.replace(regexEquals, ' <span class="orange-text">=</span> ');

  paragraphs[i].innerHTML = text;
}
