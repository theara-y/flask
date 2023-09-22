export default function useApi() {
    const URL = 'http://127.0.0.1:5000/';

    async function submitWord(word) {
        const response = await axios.get(URL + 'submit_word', {params: {word: word}});
        if(response.status == 200)
            return response.data.result;
        return response.status;
    }

    async function submitBestScore(bestScore) {
        const response = await axios.get(URL + 'submit_best_score', {params: {best_score: bestScore}});
        if(response.status == 200)
            return response.data.result;
        return response.status
    }

    return [submitWord, submitBestScore];
}
