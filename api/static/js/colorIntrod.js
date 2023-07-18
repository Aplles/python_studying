var preElements = document.getElementsByTagName("pre");
var pElements = document.getElementsByTagName("p");

// Преобразование HTMLCollection в массив
preElements = Array.from(preElements);
pElements = Array.from(pElements);


var paragraphs = preElements.concat(pElements);
for (var i = 0; i < paragraphs.length; i++) {
    var text = paragraphs[i].innerHTML;


    var regexQuotes = /"([^"]+)"/g;
    text = text.replace(regexQuotes, '<span class="green-text">"$1"</span>');

    var regexEquals = /\s=\s/g;
    text = text.replace(regexEquals, ' <span class="orange-text">=</span> ');

    var regexWords = /\b(abs|all|any|ascii|bin|bool|breakpoint|bytearray|bytes|callable|chr|classmethod|compile|complex|delattr|dict|dir|divmod|enumerate|eval|exec|filter|float|format|frozenset|getattr|globals|hasattr|hash|help|hex|id|input|int|isinstance|issubclass|iter|len|list|locals|map|max|memoryview|min|next|object|oct|open|ord|pow|print|property|range|repr|reversed|round|set|setattr|slice|sorted|staticmethod|str|sum|super|tuple|type|vars|zip)\b/g;
    text = text.replace(regexWords, '<span class="purple-text">$&</span>');

    var regexWordsPurple = /\b(self)\b/g;
    text = text.replace(regexWordsPurple, '<span class="purple-additional-text">$&</span>');

    var func = /def\s+(_*\w+)\s*(?=\()/g;
    text = text.replace(func, '<span class="yellow-text">$&</span>');


    var regexNumbers = /\b\d+\b/g;
    text = text.replace(regexNumbers, '<span class="blue-text">$&</span>');

    paragraphs[i].innerHTML = text;

    var regexWordsOrange = /\b(class)(?![^<]*>|[^<>]*<\/)/g;
    text = text.replace(regexWordsOrange, '<span class="orange-text">$&</span>');

    var regexWordsOrangePython = /\b(False|None|True|and|as|assert|async|await|break|continue|def|del|elif|else|except|finally|for|from|global|if|import|in|is|lambda|nonlocal|not|or|pass|raise|return|try|while|with|yield)\b/g;
    text = text.replace(regexWordsOrangePython, '<span class="orange-text">$&</span>');

    paragraphs[i].innerHTML = text;
}
