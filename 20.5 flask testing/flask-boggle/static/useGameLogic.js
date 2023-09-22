export default function useGameLogic() {
    let words = []

    function validateWord(word, response) {
        if(isAlreadyUsed(word)) {
            return [0, `Already used ${word}!`];
        }
        if(response == 'ok') {
            words.push(word);
            return [getPointValue(word), response]
        }
        return [0, response];
    }

    function getPointValue(word) {
        return word.length;
    }

    function isAlreadyUsed(word) {
        return words.includes(word)
    }

    return [validateWord]
}