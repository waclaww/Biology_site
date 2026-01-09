let testArr = [];let arrLength = 0;let rightAnswers = 0;let currentQuestion = 0;let userAnswers = [];let wrongAnswers = 0;const wrongAnswersLimit = 100;var dateNow = new Date();
var timeLimitInMinutes = 15;var countDownDate = new Date(dateNow.getTime() + timeLimitInMinutes*60000);var rulesToLearn = "";let isuser = document.getElementById("getUserName").innerHTML;
function setArr(){
    let str = `${document.getElementsByClassName("rightArray")[0].innerHTML}`;
    document.getElementsByClassName("rightArray")[0].innerHTML = "";
    let preArr = str.split("|");
    arrLength = preArr.length;
    for(let i = 0; i<arrLength; i++){
        testArr[i] = preArr[i].split("#");
        userAnswers[i] = [-1, -2];
    }
}setArr();
function setQuestionNums(){
    let el = document.getElementsByClassName("testQuestionsNums")[0];
    let preDiv = "";
    let preClass = "";
    for(let i=1; i<arrLength; i++){
        preClass = "testQuestionNum";

        if(userAnswers[i-1][0] == -1){
            preClass += " unansweredQuestion";
        }
        else{
            if(userAnswers[i-1][0] == userAnswers[i-1][1]){
                preClass += " rightQuestion";
            }
            else{
                preClass += " wrongQuestion";
            }
        }

        if(i-1 == currentQuestion){
            preClass += " currentQuestion";
            
        }
        preDiv += `<input type="button" id="testQuestionNum" class="${preClass}" value="${i}">`;
    }
    el.innerHTML = preDiv;
}

function setButtons(){
    let el = document.getElementsByClassName("testAnswersContainer")[0];
    let preDiv = "";
    let sub = 0;
    for(let i=0; i<4; i++){
        if(testArr[currentQuestion][3+i] != "none"){
            preDiv += `<input type="button" class="answerButton" id="answerButton" value="${(i+1)-sub}. ${testArr[currentQuestion][3+i]}">`;
        }
        else{
            sub += 1;
        }
    }
    el.innerHTML = preDiv;
}
function setButtonAfterAnswer(){
    let el = document.getElementsByClassName("testAnswersContainer")[0];
    let preDiv = "";
    let sub = 0;
    let preClass = "";
    for(let i=0; i<4; i++){
        if(testArr[currentQuestion][3+i] != "none"){
            preClass = "";
            if(i+1 == testArr[currentQuestion][7]){
                preClass += "answerButtonRight";
            }
            else{
                preClass += "answerButtonWrong";
            }
            if(userAnswers[currentQuestion][0] == i+1){
                preClass += " answerButtonPicked";
            }
            preDiv += `<input type="button" class="${preClass}" value="${(i+1)-sub}. ${testArr[currentQuestion][3+i]}">`;
        }
        else{
            sub += 1;
        }
    }
    el.innerHTML = preDiv;
}
function setImageContainer(){
    if(testArr[currentQuestion][2] == "none"){
        document.getElementsByClassName("testImageContainer")[0].innerHTML = `<div class="testQuestionContainer">${testArr[currentQuestion][1]}</div>`;
    }
    else{
        document.getElementsByClassName("testImageContainer")[0].innerHTML = `<a href="${testArr[currentQuestion][2]}" target="_blank"><img src="${testArr[currentQuestion][2]}" alt="testImage" class="testImage"></a><div class="testQuestionContainer">${testArr[currentQuestion][1]}</div>`;
    }
}
function checkUnanswered(){
    let unanswered = -1;
    for(let i=0; i<arrLength; i++){
        if(userAnswers[i][0] == -1 && unanswered == -1){
            unanswered = i;
        }
    }
    return unanswered;
}

function endScreen(n){
    // n == 0 - Win
    // n == 1 - Lose because of wrong answers limit
    // n = 2 - Lose because of time
    if(isuser == "True"){
        check_username();
    }
    // setStatistics();
    if(n == 0){
        document.getElementsByClassName("testImageContainer")[0].innerHTML = `<div class="testQuestionContainerWin">Тест пройден</div><div class="testQuestionContainer">Результат прохождения теста сохранен в ваш профиль.</div>`;
        document.getElementsByClassName("testAnswersContainer")[0].innerHTML = `<input type="button" class="answerButton" id="againButton" value="Заново">`;
    }
    else if(n == 1){
        document.getElementsByClassName("testImageContainer")[0].innerHTML = `<div class="testQuestionContainerLose">Тест не сдан!</div><div class="testQuestionContainer">Вы провалили тест, совершив ${wrongAnswersLimit} ошибки!</div>`;
        document.getElementsByClassName("testAnswersContainer")[0].innerHTML = `<input type="button" class="answerButton" id="againButton" value="Заново">`;
    }
    else if(n == 2){
        document.getElementsByClassName("testImageContainer")[0].innerHTML = `<div class="testQuestionContainerLose">Тест не сдан!</div><div class="testQuestionContainer">Время вышло!</div>`;
        document.getElementsByClassName("testAnswersContainer")[0].innerHTML = `<input type="button" class="answerButton" id="againButton" value="Заново">`;
    }
    if(rulesToLearn != ""){
        document.getElementsByClassName("testQuestionContainer")[0].innerHTML = document.getElementsByClassName("testQuestionContainer")[0].innerHTML + `<br><br>Вам следует подучить следующие пункты ПДД:<br><br>${rulesToLearn}`;
    }
    setQuestionNums();
    document.getElementsByClassName("testTime")[0].value = `00:00`;
}

document.addEventListener('click',(e) =>
    {
        let elementID = e.target.id;
        if(elementID == "answerButton"){
            let answerClicked = e.target.value.split(". ")[1];
            let answerRight = testArr[currentQuestion][parseInt(testArr[currentQuestion][7])+2];
            if(answerClicked == answerRight){
                rightAnswers += 1;
                userAnswers[currentQuestion] = [parseInt(e.target.value.split(". ")[0]), parseInt(testArr[currentQuestion][7])];
                currentQuestion = checkUnanswered();
                setQuestionNums();
                setButtons();
                setImageContainer();
            }
            else{
                wrongAnswers += 1;
                userAnswers[currentQuestion] = [parseInt(e.target.value.split(". ")[0]), parseInt(testArr[currentQuestion][7])];

                if(testArr[currentQuestion][9] != "Вопрос не имеет ссылок на пункты ПДД"){
                    rulesToLearn += ` ${testArr[currentQuestion][9]}`;
                }
                
                currentQuestion = checkUnanswered();
                setQuestionNums();
                setButtons();
                setImageContainer();
            }
            if(currentQuestion >= arrLength-1 && wrongAnswers < wrongAnswersLimit){
                currentQuestion = -1;
                endScreen(0);
            }
            else if(wrongAnswers >= wrongAnswersLimit){
                currentQuestion = -1;
                endScreen(1);
            }
        }
        else if(elementID == "againButton"){
            dateNow = new Date();
            countDownDate = new Date(dateNow.getTime() + timeLimitInMinutes*60000);
            currentQuestion = 0;
            userAnswers = [];
            rulesToLearn = "";
            wrongAnswers = 0;
            rightAnswers = 0;
            for(let i=0; i<arrLength; i++){
                userAnswers[i] = [-1, -2];
            }
            setQuestionNums();
            setButtons();
            setImageContainer();
            startCountdown();
        }
        else if(elementID == "testQuestionNum" && currentQuestion != -1 && e.target.value != `${currentQuestion+1}`){
            if(userAnswers[parseInt(e.target.value)-1][0] == -1){
                currentQuestion = parseInt(e.target.value)-1;
                setQuestionNums();
                setButtons();
                setImageContainer();
            }
            else{
                // Uncomment code below to return "Look already answered" feature

                // currentQuestion = parseInt(e.target.value)-1;
                // setQuestionNums();
                // setImageContainer();
                // setButtonAfterAnswer();
            }
        }
    }
);

function getTwoDigitNum(n){
    if(n < 10){
        return `0${n}`;
    }
    else{
        return n;
    }
}

async function request(url, data, csrftoken) {
    const response = await fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
            'X-CSRFToken': csrftoken,
        },
        body: JSON.stringify(data),
    })
    const result = await response.text()
    return result
}

async function check_username() {
    const url = window.location.href
    const data = `${document.getElementById("testId").innerHTML}#${rightAnswers}#${wrongAnswers}#${arrLength-1}`
    const csrftoken = document.getElementById("csrf").innerHTML
    const result = await request(url, data, csrftoken)
    console.log(result)
}

function startCountdown(){
    var x = setInterval(function() {
    if(currentQuestion != -1){
        var now = new Date().getTime();
        var distance = countDownDate - now;
        var minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
        var seconds = Math.floor((distance % (1000 * 60)) / 1000);

        document.getElementsByClassName("testTime")[0].value = `${getTwoDigitNum(minutes)}:${getTwoDigitNum(seconds)}`;
        if (distance < 0) {
            clearInterval(x);
            document.getElementsByClassName("testTime")[0].value = `00:00`;
            currentQuestion = -1;
            endScreen(2);
        }
    }
}, 1000);
}

setQuestionNums();
setButtons();
setImageContainer();
startCountdown();