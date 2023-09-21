import showToast from './Toast.js';
import addScore from './Score.js';
import Timer from './Timer.js';

const timer = new Timer();

$('#submit').on('click', async function(event) {
    event.preventDefault();
    timer.start();
    
    const word = $('#word').val().trim();
    if(word != '' && timer.off == false) {
        const response = await submitGuess(word)
        if(response.status == 200) {
            const result = response.data.result;
            showToast(result);

            if(result == 'ok') {
                addScore(word);
            }
        }
        $('#word').val('');
    }
})

async function submitGuess(word) {
    return axios.get(`http://127.0.0.1:5000/submit_word`, {params: {word: word}});
}

