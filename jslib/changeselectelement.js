if (typeof arguments[1] === 'string') {
    arguments[0].value = arguments[1];
} else {
    arguments[0].selectedIndex = arguments[1];
}
function triggerOtherEvent(node, eventType) {
    var evt = document.createEvent("HTMLEvents");
    evt.initEvent(eventType, false, true);
    node.dispatchEvent(evt);

}
triggerOtherEvent(arguments[0], 'change');