class Score {
    constructor() {
        this.score = 0;
        this.addScore = this.addScore.bind(this);
    }

    addScore(word) {
        this.score += word.length;
        $('#score-display').html(this.score);
    }
}

const scoreDisplay = new Score()
export default scoreDisplay.addScore