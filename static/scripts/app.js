const articles = document.querySelectorAll(".articles article");

let index = 0;

function showArticle(index) {
  // hide all the articles
  articles.forEach((article) => (article.style.display = "none"));

  articles[index].style.display = "block";
}

showArticle(index);

function handleKeyPress(event) {
  if (event.keyCode === 37) {
    index--;
    index;
    if (index < 0) {
      index = articles.length - 1;
    }

    showArticle(index);
  }

  if (event.keyCode === 39) {
    index++;

    if (index >= articles.length) {
      index = 0;
    }

    showArticle(index);
  }
}

document.addEventListener("keydown", handleKeyPress);

setInterval(() => {
  index++;

  if (index >= articles.length) {
    index = 0;
  }

  showArticle(index);
}, 4000);
