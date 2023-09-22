export default function useButton($element, initialText) {
    const $button = $element;
    let text = initialText;
    render();

    function setText(newText) {
        text = newText;
        render();
    }

    function getText() {
        return text;
    }

    function render() {
        $button.text(text);
    }

    return [setText, getText];
}