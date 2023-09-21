class Toast {
    constructor() {
        this.timerId = null;
        this.show = this.show.bind(this)
        this.newTimer = this.newTimer.bind(this)
    }

    show(message) {
        $('#toast').html(message).addClass('show-toast')
        this.timerId = this.newTimer(3000)
    }

    newTimer(waitTime) {
        this.clearTimer();
        return setTimeout(function() {
            $('#toast').removeClass('show-toast')
        }, waitTime)
    }

    clearTimer() {
        if(this.timerId != null) {
            clearTimeout(this.timerId)
        }
    }
}

const toast = new Toast()
export default toast.show