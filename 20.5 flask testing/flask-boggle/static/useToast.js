export default function useToast() {
    let message = null;
    let timerId = null;

    function setMessage(newMessage) {
        message = newMessage;
        render();
    }

    function startTimer() {
        timerId = setTimeout( () => {
            hide();
        }, 3000);
    }

    function show() {
        $('.toast').addClass('show-toast');
        startTimer();
    }

    function hide() {
        $('.toast').removeClass('show-toast');
        timerId = null;
    }

    function render() {
        $('.toast').text(message)

        if(timerId != null) {
            clearTimeout(timerId);
            hide()
            setTimeout(show, 300);
        } else {
            show();
        }
    }

    return [setMessage]
}