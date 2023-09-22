export default function useScoreBox($element) {
    const widget = $element;
    let score = 0;

    function setScore(newScore) {
        score = newScore;
        render();
    }

    function getScore() {
        return score;
    }

    function render() {
        widget.text(score);
    }

    return [setScore, getScore];
}