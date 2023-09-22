export default function useInput($element) {
    let textElement = $element

    function getInput() {
        return textElement.val().trim().toLowerCase();
    }

    function resetInput() {
        textElement.val('');
    }

    function validate() {
        return textElement.val().trim() != '';
    }

    function lockInput() {
        textElement.prop('disabled', true);
    }

    function unlockInput() {
        textElement.prop('disabled', false);
    }

    return [getInput, resetInput, validate, lockInput, unlockInput];
}