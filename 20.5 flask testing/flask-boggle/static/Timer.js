export default class Timer {
    constructor() {
        this.timerId = null;
        this.timeLeft = 60;
        this.off = true;
        this.decrementTime = this.decrementTime.bind(this);
    }

    start() {
        if(this.timerId != null)
            return
        this.off = false;
        this.timerId = setInterval(() => {
            this.decrementTime();
        }, 1000);
        $('#timer').addClass('spin')
    }

    decrementTime() {
        this.timeLeft -= 1;
        $('#timer').html(this.timeLeft);
        if(this.timeLeft == 0) {
            $('#timer').removeClass('spin')
            this.off = true;
            this.clearTimer();
        }
    }

    clearTimer() {
        if(this.timerId != null) {
            clearTimeout(this.timerId);
        }
    }
}