export default function Timer(initialTime, $element, additionalFunction = null) {
    let initial = initialTime;
    let timer = $element;
    let time = initialTime;
    let timerId = null;
    render()

    function start() {
        if(timerId == null && time > 0) {
            timerId = setInterval( () => {
                setTime(--time)
            }, 1000)
        }
    }

    function stop() {
        if(timerId != null) {
            clearInterval(timerId);
            timerId = null;
        }
    }

    function reset() {
        if(timerId != null) {
            stop();
            setTime(initial);
            start();
        } else {
            setTime(initial);
        }
    }

    function setTime(newTime) {
        time = newTime;
        render();
        
        if(time == 0) {
            stop();
            if(additionalFunction != null)
                additionalFunction();
        }
    }

    function isRunning() {
        return timerId != null && time > 0
    }

    function isZero() {
        return time == 0;
    }

    function render() {
        timer.text(time)
    }

    return [start, stop, reset, isRunning, isZero];
}