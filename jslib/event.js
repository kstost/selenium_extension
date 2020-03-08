var targetNode = arguments[0];
var eType = arguments[1];
function triggerKeyEvent(node, eventType, key) {
    var event = document.createEvent('Event');
    event.keyCode = key; // Deprecated, prefer .key instead.
    event.key = key;
    event.initEvent(eventType);
    node.dispatchEvent(event);
}
function triggerMouseEvent(node, eventType) {
    var clickEvent = document.createEvent('MouseEvents');
    clickEvent.initEvent(eventType, true, true);
    node.dispatchEvent(clickEvent);
}
function triggerOtherEvent(node, eventType) {
    var evt = document.createEvent("HTMLEvents");
    evt.initEvent(eventType, false, true);
    node.dispatchEvent(evt);

}
let events = {
    click: triggerMouseEvent,
    mouseover: triggerMouseEvent,
    mousedown: triggerMouseEvent,
    mouseover: triggerMouseEvent,
    mouseout: triggerMouseEvent,
    keydown: triggerKeyEvent,
    keypress: triggerKeyEvent,
    keyup: triggerKeyEvent,
};
let fn = events[eType];
if (!fn) {
    fn = triggerOtherEvent;
}
fn(targetNode, eType);