var timeoutID;

function PageMovement() {
  timeoutID = window.setTimeout(page_replace, 400);
}

function PageMovement2() {
  timeoutID = window.setTimeout(page_replace2, 400);
}

function page_replace() {
  location.replace("sentencesCheck.py");
}
function page_replace2() {
  location.replace("sentences.py");
}
