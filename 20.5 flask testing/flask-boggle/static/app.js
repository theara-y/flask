import useInput from './useInput.js';
import useApi from './useApi.js';
import useToast from './useToast.js';
import useScoreBox from './useScore.js';
import useGameLogic from './useGameLogic.js';
import useTimer from './useTimer.js';
import useButton from './useButton.js';

const [getInput, resetInput, inputIsValid, lock, unlock] = useInput($('#textbox'));
const [submitWord, submitScore] = useApi();
const [showToast] = useToast();
const [setScore, getScore] = useScoreBox($('#current-score'));
const [setBest, getBest] = useScoreBox($('#best-score'));
const [validateWord] = useGameLogic();
const [startTimer, stopTimer, resetTimer, isRunning, isZero] = useTimer(180, $('#timer'), whenTimeIsOver);
const [setButton, getButton] = useButton($('#new-game-btn'), 'Start Game')

lock();

$('#submit-btn').on('click', async function(event) {
    event.preventDefault();
    const word = getInput();
    if(inputIsValid()) {
        const response = await submitWord(word)
        const [points, message] = validateWord(word, response)
        
        showToast(message);
        setScore(getScore() + points);
    }
    resetInput();
})

$('#new-game-btn').on('click', async function(event) {
    if(getButton() == 'Start Game') {
        setButton('New Game');
        unlock();
        startTimer();
    } else if(getButton() == 'Restart' || getButton() == 'New Game') {
        stopTimer()
        location.reload()
    }
});

$(document).ready(async function() {
    const bestScore = await submitScore(0);
    setBest(bestScore);
});

async function whenTimeIsOver() {
    lock();
    const bestScore = await submitScore(getScore());
    setBest(bestScore);
    setButton('Restart');
}
