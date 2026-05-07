/*MESSAGING: START*/
function uniqueIdSync(fullName, phone, email, password) {
  const raw = `${fullName}|${phone}|${email}|${password}`;
  let hash = 0;
  for (let i = 0; i < raw.length; i++) {
    const chr = raw.charCodeAt(i);
    hash = (hash << 5) - hash + chr;
    hash |= 0; // force into 32-bit int
  }
  return "USR_" + Math.abs(hash).toString(36);
}
const loggedInUser = { name: "John Doe", avatar: "https://randomuser.me/api/portraits/men/75.jpg", USER_UNIQUE_ID:uniqueIdSync("John Doe").toLowerCase()};
const eid = (id) => document.getElementById(id);
function makeDraggable(childElement, parentElementOverride = null) {
  const parentElement = parentElementOverride || childElement.parentElement;
  let isDragging = false;
  let offsetX = 0, offsetY = 0;

  function startDrag(e) {
    e.preventDefault();
    isDragging = true;
    parentElement.style.cursor = "grabbing";

    const clientX = e.touches ? e.touches[0].clientX : e.clientX;
    const clientY = e.touches ? e.touches[0].clientY : e.clientY;

    offsetX = clientX - parentElement.offsetLeft;
    offsetY = clientY - parentElement.offsetTop;

    document.addEventListener("mousemove", dragMove);
    document.addEventListener("mouseup", endDrag);
    document.addEventListener("touchmove", dragMove, { passive: false });
    document.addEventListener("touchend", endDrag);
  }

  function dragMove(e) {
    if (!isDragging) return;

    const clientX = e.touches ? e.touches[0].clientX : e.clientX;
    const clientY = e.touches ? e.touches[0].clientY : e.clientY;

    parentElement.style.left = (clientX - offsetX) + "px";
    parentElement.style.top = (clientY - offsetY) + "px";
  }

  function endDrag() {
    isDragging = false;
    parentElement.style.cursor = "grab";

    document.removeEventListener("mousemove", dragMove);
    document.removeEventListener("mouseup", endDrag);
    document.removeEventListener("touchmove", dragMove);
    document.removeEventListener("touchend", endDrag);
  }

  childElement.addEventListener("mousedown", startDrag);
  childElement.addEventListener("touchstart", startDrag, { passive: false });
}
export function chatMegaMachine(){

const MessageChatBox = eid('MessageChatBox'),
      ChatImageShare = eid('ChatImageShare'),
      ShareImage = eid('ShareImage'),
      sendMessage = eid("sendMessage"),
      chatInput = eid("chatInput"),
      chatBody = document.querySelector(".chat-body");
makeDraggable(eid('Your_messages_header'));
const MessagesScreenDynamicSizingPos = ()=>{
let window_width = window.innerWidth,
    MessagesScreen_w = window_width*0.75,
    MessagesScreen_x_off = Math.round((window_width-MessagesScreen_w)/2);
MessagesScreen.style.width = `${MessagesScreen_w}px`;
MessagesScreen.style.left = `${MessagesScreen_x_off}px`;
const messageBoxTwins = eid('messageBoxTwins');
let messageBoxTwins_width = messageBoxTwins.clientWidth-20;
const pikins = Array.from(MessagesScreen.children),
      twins_boxes = Array.from(pikins[1].children),
      firstElementChild_ = twins_boxes[0],
      lastElementChild_ = twins_boxes[2];
let firstElementChild_cw = Math.round(messageBoxTwins_width*0.30),
    lastElementChild_cw = Math.round(messageBoxTwins_width*0.60);
firstElementChild_.style.width = `${firstElementChild_cw}px`;
lastElementChild_.style.width = `${lastElementChild_cw}px`;
}
MessagesScreenDynamicSizingPos();
window.addEventListener('resize',()=>{
MessagesScreenDynamicSizingPos();
})
ChatImageShare.addEventListener('click', (e)=>{
ShareImage.click();
})
var fake_src = '',
    image_name = '';
const img_name = (img_src)=>{
let slashe = '';
slashe = img_src.includes('\\')?'\\':'/';
let fake_src_split = img_src.split(slashe),
    fake_src_split_len = fake_src_split.length;
return fake_src_split[fake_src_split_len-1];
}
var image_shared = [];
ShareImage.addEventListener('change',()=>{
image_shared = ShareImage.files;
const url = URL.createObjectURL(image_shared[0])
fake_src = url;
image_name = img_name(ShareImage.value);
chatInput.value = image_name;
})
// pass the variable name as string
// Send message
sendMessage.addEventListener("click", (e) => {
var wrong_image_name = false,
    clean_records = true;
let text = chatInput.value.trim();
const msg = document.createElement("div");
msg.style.cssText = `
overflow-wrap: break-word;
max-width:20vw;
background: rgba(212, 175, 55, 1);
box-shadow: 0 4px 12px rgba(34, 139, 34, 0.35); /* forest limegreen tint */
color:#000;
font-weight:600;
`;
if (!text) return;
if(fake_src.trim().length>0){
if(text==image_name){
var MessageChatBox_x = Math.round(0.4*MessageChatBox.scrollWidth),
    MessageChatBox_y = Math.round(0.4*MessageChatBox.scrollHeight);
text = `<img src="${fake_src}" alt="${image_name}" style="width:${MessageChatBox_x}px;height:${MessageChatBox_y}px;border-radius:10px;">`;
msg.innerHTML = text;
msg.style.background = "transparent";
fake_src='';
}else{
alert("can't send this image, check image name");
wrong_image_name = true;
clean_records = false;
}
}else{
if(text.includes('http:') || text.includes('https:')){
msg.innerHTML = `<a href="${text}">${text}</a>`;
msg.style.background = "transparent";
}else{
if(!wrong_image_name){
msg.innerHTML = `<span>${text}</span>`;
}
}
}
if(clean_records){
msg.className = "message-sent";
chatBody.appendChild(msg);
chatInput.value = "";
chatBody.scrollTop = chatBody.scrollHeight;

let msg_date = new Date().toLocaleString();
const chat_dic = { 
                  'ImageSharedData':{
                    'image_shared':image_shared,
                    'image_name':image_name
                  },
                  'loggedInUser':loggedInUser,
                  'msg_text':text,
                  'msg_date':msg_date
                  };
}
});

// Enter key to send
chatInput.addEventListener("keydown", (e) => {
if (e.key === "Enter") {
  sendMessage.click();
}
});
//***********************************************
};
/*MESSAGING: END*/