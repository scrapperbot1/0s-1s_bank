document.addEventListener("DOMContentLoaded", () => {
document.body.classList.add("loaded");
});
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
const displayer = (screen_ele_arg, y_offset = eid('Header').scrollHeight) => {
  screen_ele_arg.style.display = 'flex';
  screen_ele_arg.style.position = 'absolute';
  screen_ele_arg.style.top = `0`;
  screen_ele_arg.style.transition = 'top 0.3s linear';

  // wait until next frame to apply new position
  requestAnimationFrame(() => {
    screen_ele_arg.style.top = `${y_offset}px`;
  });
};
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
    // small helper
    const eid = (id) => document.getElementById(id);
    const wL = (custom_href)=>{
      window.location.href=custom_href;
    }
    const Header=eid('Header');
    var Header_scrollHeight=Header.scrollHeight;
    // ensure we start at top when page loads / reloads
    document.addEventListener("DOMContentLoaded", () => { window.scrollTo(0,0); });
    window.onload = function(){ window.scrollTo({ top:0, left:0, behavior:'smooth' }); };

    /* ====== Navigation (loads pages) ====== */
    try {
      const Real_Estate = eid('Real_Estate');
      const Building_Construction = eid('Building_Construction');
      const Property_Rentals = eid('Property_Rentals');

      if(Real_Estate) Real_Estate.addEventListener('click', ()=> { window.location.href='RealEstateSectionRecs/RealEstateSection.html'; });
      if(Building_Construction) Building_Construction.addEventListener('click', ()=> { window.location.href='Building_And_Construction_Recs/BnChtml.html'; });
      if(Property_Rentals) Property_Rentals.addEventListener('click', ()=> { window.location.href='PropetiesRentalsSectionRecs/PR_html.html'; });
    } catch(e){
      console.warn('Navigation bindings failed:', e);
    }

    /* ====== User details / forms handling ====== */
    const INNER_WIDTH = window.innerWidth;
    const INNER_HEIGHT = window.innerHeight;
    const Sign_in = eid('Sign_in');
    const Sign_up = eid('Sign_up');
    const LoginSignUp = eid('LoginSignUp'); // link in login pane to open sign up
    const Sign_UpLogin = eid('Sign_UpLogin'); // link in signup pane to open login
    const form_container_login = eid('form_container_login');
    const form_container_signup = eid('form_container_signup');
    const form_container_reset_password_id = eid('form_container_reset_password_id');
    const ResetPasswordLogin = eid('ResetPasswordLogin');
    const Forgotten_password_Reset = eid('Forgotten_password_Reset');
    var form_container_login_scrollWidth=form_container_login.scrollWidth;
    var form_container_signup_scrollWidth=form_container_signup.scrollWidth;
    var form_container_reset_password_id_scrollWidth=form_container_reset_password_id.scrollWidth;

/*DATABASE ENTERIES ARRIVAL JS CODE: START*/
const userLoginFlagger = (loginLogic)=>{
const mascomUserInfo = eid('MASCOM_USER_INFO'),
      profilePicContainer2   = eid('User_profile_pic'),
      userNameNotiMesgField_id=eid('userNameNotiMesgField_id');
if (!loginLogic) {
  Sign_in.style.display = 'block';
  Sign_up.style.display = 'block';
  userNameNotiMesgField_id.style.display='none';
  profilePicContainer2.style.display='none';
}
}
userLoginFlagger(true);
/*DATABASE ENTERIES ARRIVAL JS CODE: END*/

const leftPosition=()=>{
var INNER_WIDTH_DYNAMIC = window.innerWidth;
var form_container_login_scrollWidth_dyna=form_container_login.scrollWidth;
var form_container_signup_scrollWidth_dyna=form_container_signup.scrollWidth;
var form_container_reset_password_id_scrollWidth_dyna=form_container_reset_password_id.scrollWidth;
var fnlinw=Math.round((INNER_WIDTH_DYNAMIC-form_container_login_scrollWidth_dyna)/2)  //fnlinw;
var fnsunw=Math.round((INNER_WIDTH_DYNAMIC-form_container_signup_scrollWidth_dyna)/2)  //fnsunw;
var fnrpnw=Math.round((INNER_WIDTH_DYNAMIC-form_container_reset_password_id_scrollWidth_dyna)/2)  //fnrpnw;
form_container_login.style.left=`${fnlinw}px`;
form_container_signup.style.left=`${fnsunw}px`;
form_container_reset_password_id.style.left=`${fnrpnw}px`;
}
const topPosition=()=>{
var INNER_HEIGHT_DYNAMIC = window.innerHeight;
var form_container_login_scrollHeight_dyna=form_container_login.scrollHeight;
var form_container_signup_scrollHeight_dyna=form_container_signup.scrollHeight;
var form_container_reset_password_id_scrollHeight_dyna=form_container_reset_password_id.scrollHeight;
var fnlinh=Math.round((INNER_HEIGHT_DYNAMIC-form_container_login_scrollHeight_dyna)/2)  //fnlinh;
var fnsunh=Math.round((INNER_HEIGHT_DYNAMIC-form_container_signup_scrollHeight_dyna)/2)  //fnsunh;
var fnrpnh=Math.round((INNER_HEIGHT_DYNAMIC-form_container_reset_password_id_scrollHeight_dyna)/2)  //fnrpnh;
form_container_login.style.top=`${fnlinh}px`;
form_container_signup.style.top=`${fnsunh}px`;
form_container_reset_password_id.style.top=`${fnrpnh}px`;
}

    /*USER DETAILS JS CODE: START*/
    const signinClickEventHandler=()=>{
    form_container_login.style.top=`${0}px`;
    form_container_login.style.transition='top 1s linear';
    form_container_login.style.display='block';
    var form_container_loginHeight=form_container_login.scrollHeight;
    var form_container_SignUpwidth=form_container_signup.scrollWidth;
    var form_container_reset_password_idWidth=form_container_reset_password_id.scrollWidth;
    if(form_container_reset_password_idWidth>0){
    form_container_reset_password_id.style.transition='top 1s linear';
    form_container_reset_password_id.style.display='none';
    }
    if(form_container_SignUpwidth>0){
    form_container_signup.style.transition='top 1s linear';
    form_container_signup.style.display='none';
    }
    var auto_marginTopLogin=Math.round((INNER_HEIGHT-form_container_loginHeight)/2);
    form_container_login.style.top=`${auto_marginTopLogin}px`;
    }
    Sign_in.addEventListener('click',()=>{
    signinClickEventHandler();
    leftPosition();
    topPosition();
    })

/*USER LOGIN DATA COLLECTION JS CODE: START*/
const UserInputDataBtn_Login=eid('UserInputDataBtn_Login');
UserInputDataBtn_Login.addEventListener('click',()=>{
const emailLogin = eid('emailLogin');
const password_login = eid('password_login');
const remember = eid('remember');
let emailLogin_value=emailLogin.value;
let password_login_value=password_login.value;
let remember_value=remember.value;
let UserLoginDetails={
                      'emailLogin':emailLogin_value,
                      'password_login':password_login_value,
                      'remember':remember_value,
                      };
})
/*USER LOGIN DATA COLLECTION JS CODE: END*/
    const signUpEventHandler=()=>{
    form_container_signup.style.top=`${0}px`;
    form_container_signup.style.transition='top 1s linear';
    form_container_signup.style.display='block';
    var form_container_signupHeight=form_container_signup.scrollHeight;
    var form_container_Loginpwidth=form_container_login.scrollWidth;
    var form_container_reset_password_idWidth=form_container_reset_password_id.scrollWidth;
    if(form_container_reset_password_idWidth>0){
    form_container_reset_password_id.style.transition='top 1s linear';
    form_container_reset_password_id.style.display='none';
    }
    if(form_container_Loginpwidth>0){
    form_container_login.style.transition='top 1s linear';
    form_container_login.style.display='none';
    }
    var auto_marginTopSignUp=Math.round((INNER_HEIGHT-form_container_signupHeight)/2);
    form_container_signup.style.top=`${auto_marginTopSignUp}px`;
    }
    Sign_up.addEventListener('click',()=>{
    signUpEventHandler();
    leftPosition();
    topPosition();
    })

/*USER REGISTERATION DATA COLLECTION JS CODE: START*/
const UserInputDataBtn_SignUp=eid('UserInputDataBtn_SignUp');
UserInputDataBtn_SignUp.addEventListener('click',()=>{
const fullname = eid('fullname');
const tel = eid('tel');
const emailSignUp = eid('emailSignUp');
const PasswordSignUp = eid('PasswordSignUp');
const Input_Male = document.getElementsByClassName('Input_Male')[0];
const Input_Female = document.getElementsByClassName('Input_Female')[0];
let fullname_value=fullname.value;
let tel_value=tel.value;
let emailSignUp_value=emailSignUp.value;
let PasswordSignUp_value=PasswordSignUp.value;
let Input_Male_value=Input_Male.value;
let Input_Female_value=Input_Female.value;
let UserSignupDetails={
                      'fullname':fullname_value,
                      'tel':tel_value,
                      'emailSignUp':emailSignUp_value,
                      'PasswordSignUp':PasswordSignUp_value,
                      'Input_Male':Input_Male_value,
                      'Input_Female':Input_Female_value
                      };
})
/*USER REGISTERATION DATA COLLECTION JS CODE: END*/

    LoginSignUp.addEventListener('click',()=>{
    signUpEventHandler();
    leftPosition();
    topPosition();
    })

    Sign_UpLogin.addEventListener('click',()=>{
    signinClickEventHandler();
    leftPosition();
    topPosition();
    })
    ResetPasswordLogin.addEventListener('click',()=>{
    form_container_reset_password_id.style.display='none';
    signinClickEventHandler();
    leftPosition();
    topPosition();
    })
    Forgotten_password_Reset.addEventListener('click',()=>{
    form_container_reset_password_id.style.top=`${0}px`;
    form_container_login.style.display='none';
    form_container_reset_password_id.style.transition='top 1s linear';
    form_container_reset_password_id.style.display='block';
    var form_container_reset_password_id_height=form_container_reset_password_id.scrollHeight;
    var auto_marginTopSignUp=Math.round((INNER_HEIGHT-form_container_reset_password_id_height)/2);
    form_container_reset_password_id.style.top=`${auto_marginTopSignUp}px`;
    leftPosition();
    topPosition();
    });

/*USER LOGIN DATA COLLECTION JS CODE: START*/
const UserInputDataBtn_ResetPassword=eid('UserInputDataBtn_ResetPassword');
UserInputDataBtn_ResetPassword.addEventListener('click',()=>{
const Input_ResetPassword = document.getElementsByClassName('emailLogin')[0];
const Input_ConfirmResetPassword = document.getElementsByClassName('password_login')[0];
let Input_ResetPassword_value=Input_ResetPassword.value;
let Input_ConfirmResetPassword_value=Input_ConfirmResetPassword.value;
let UserPasswordResetDetails={
                      'Input_ResetPassword':Input_ResetPassword_value,
                      'Input_ConfirmResetPassword':Input_ConfirmResetPassword_value
                      };
let PasswordLengthMet=true;
let oldPassword='ThisMyOldPassword';
if(oldPassword==Input_ResetPassword_value || oldPassword==Input_ConfirmResetPassword_value){
PasswordLengthMet=false;
alert("Please the new password shouldn't match the old one");
}
if(Input_ConfirmResetPassword!=Input_ResetPassword_value){
PasswordLengthMet=false;
alert("Passwords do not match");
}
if(PasswordLengthMet){
alert('password reset!');
}
})
/*USER LOGIN DATA COLLECTION JS CODE: END*/
window.addEventListener("resize", ()=>{
leftPosition();
topPosition();
});

window.addEventListener("DOMContentLoaded", ()=>{
form_container_login.style.transition='top 1s linear';
form_container_signup.style.transition='top 1s linear';
form_container_reset_password_id.style.transition='top 1s linear';
leftPosition();
topPosition();
});
/*USER DETAILS JS CODE: END*/

/* USER PROFILE PIC MACHINERY: START */
const changeProfilePicBtn   = eid('ChangeProfilePic'),
      profilePicInput       = eid('ProfilePicChange'),
      profilePicImg         = eid('user_profile_pic_img'),
      profilePicContainer   = eid('User_profile_pic'),
      projectorParent       = eid('u_pic_projector_parent'),
      projector             = eid('u_pic_projector');

changeProfilePicBtn.addEventListener('click', triggerFileInput);
profilePicInput.addEventListener('change', handleFileChange);
profilePicContainer.addEventListener('click', openProjector);

function triggerFileInput() {
  profilePicInput.click();
}

function handleFileChange() {
  const file = profilePicInput.files[0];
  if (!file) return;

  const url = URL.createObjectURL(file);
  profilePicImg.src = url;

  const previewImg = eid('User_profile_pic_img_chage');
  if (previewImg) previewImg.src = url;
}

function openProjector() {
  const headerHeight = Header.scrollHeight;
  projectorParent.style.display = 'flex';
  projectorParent.style.top = `${headerHeight}px`;
  projectorParent.style.transition = 'top 1s linear';

  const projectorImg = projector.querySelector('img') || document.createElement('img');
  projectorImg.id = 'User_profile_pic_img_chage';
  projectorImg.src = profilePicImg.src;
  projectorImg.style.cssText = `
    width: 70%;
    height: auto;
    border-radius: 10px;
    position: relative;
  `;
  if (!projector.contains(projectorImg)) projector.appendChild(projectorImg);
}

function updateProjectorPosition() {
  const headerHeight = Header.scrollHeight;
  projectorParent.style.transition = 'top 1s linear';
  projectorParent.style.top = `${headerHeight}px`;
}

['load', 'resize'].forEach(evt =>
  window.addEventListener(evt, updateProjectorPosition)
);
/* USER PROFILE PIC MACHINERY: END */


/*NEW ADVERT CREATION JS CODE: START*/
const Advertise=eid('Advertise');
Advertise.addEventListener('click',()=>{
window.location.href='http://localhost/LandingPageRecs/new_item.html';
});
/*NEW ADVERT CREATION JS CODE: END*/
    /* ====== Moving news ticker ====== */
(function(){
  const NewsInMotion = eid('NewsInMotion');
  const MovingNewsItem1 = eid('MovingNewsItem1');
let paused = false,
    today_time = new Date().toLocaleString();
const News_In_Motion_Trends = [
`<span class="post-number">${1}</span>.<img src="http://localhost/LandingPageRecs/user_photos/IMG20250628114159.jpg"> New arrivals! Contact me before they run out of stock<small> 🕰️ ${today_time}</small> <span style="color:red;">|</span> `,
`<span class="post-number">${2}</span>.<img src="http://localhost/LandingPageRecs/user_photos/IMG20250628114159.jpg"> New ring light for sale at Sakumonor<small> 🕰️ ${today_time}</small> <span style="color:red;">|</span> `,
`<span class="post-number">${3}</span>.<img src="http://localhost/LandingPageRecs/user_photos/IMG20250628114159.jpg"> Single room self-contained for rent at Pokuase<small> 🕰️ ${today_time}</small> <span style="color:red;">|</span> `,
`<span class="post-number">${4}</span>.<img src="http://localhost/LandingPageRecs/user_photos/IMG20250628114159.jpg"> 2024 Kia for sale<small> 🕰️ ${today_time}</small> <span style="color:red;">|</span> `,
`<span class="post-number">${5}</span>.<img src="http://localhost/LandingPageRecs/user_photos/IMG20250628114159.jpg"> iphone 15 pro max, GHS 13,000. Negotiable<small> 🕰️ ${today_time}</small> <span style="color:red;">|</span> `,
`<span class="post-number">${6}</span>.<img src="http://localhost/LandingPageRecs/user_photos/IMG20250628114159.jpg"> Masons needed urgently for immediate employment<small> 🕰️ ${today_time}</small> <span style="color:red;">|</span> `,
`<span class="post-number">${7}</span>.<img src="http://localhost/LandingPageRecs/user_photos/IMG20250628114159.jpg"> A storage facility at Trantra Hills for rent, 3years advance.<small> 🕰️ ${today_time}</small> <span style="color:red;">|</span> `,
`<span class="post-number">${8}</span>.<img src="http://localhost/LandingPageRecs/user_photos/IMG20250628114159.jpg"> 20 buckets of deluxy paint for sale. Offwhite color.<small> 🕰️ ${today_time}</small>`];
MovingNewsItem1.innerHTML = News_In_Motion_Trends.map((trend, trend_dex)=>

`<a href="#" data-postid='${trend_dex}'>${trend.replaceAll('\n','')}</a> `

).join('')

MovingNewsItem1.addEventListener('mouseover', ()=> paused = true);
MovingNewsItem1.addEventListener('mouseout', ()=> paused = false);

let start = null;
let speed = 80; // pixels per second
let x = window.innerWidth;
function animate(time) {
let MovingNewsItem1_width = MovingNewsItem1.scrollWidth,
    win_width = window.innerWidth,
    total_x_offset = MovingNewsItem1_width;
let news_timeFrameEnd = Math.round(win_width/speed);
total_x_offset = win_width+MovingNewsItem1_width;
  if (!start) start = time;
  const elapsed = (time - start) / 1000;
  if (!paused) {
    x -= Math.round(speed * (1/60));
    if (x < -(total_x_offset)) x = win_width;
    MovingNewsItem1.style.transform = `translateX(${x}px)`;
  }
  requestAnimationFrame(animate);
}

requestAnimationFrame(animate);

})();
MovingNewsItem1.addEventListener('click',(item_event)=>{
const item_event_target = item_event.target,
      item_event_targetTagName = item_event_target.tagName.toLowerCase();
if(item_event_targetTagName == 'a'){
let PostID = item_event_target.dataset.postid;
localStorage.setItem('MASCOM_LeftSideBar_a_element_clicked',PostID);
window.location.href = 'http://localhost/LandingPageRecs/listing.html';
}
})
const NotificationsIcon = eid('NotificationsIcon'),
      NotificationsScreen = eid('NotificationsScreen'),
      MessagesScreen = eid('MessagesScreen'),
      MessagesIcon = eid('MessagesIcon');

NotificationsIcon.addEventListener('click', () => {
  displayer(NotificationsScreen);
});

MessagesIcon.addEventListener('click', () => {
  displayer(MessagesScreen);
});

const notiMsgScreenGuy = (div_element, screen_ele) => {

  div_element.addEventListener('mouseover', () => {
    displayer(screen_ele);
  });
};

// pass the variable name as string
notiMsgScreenGuy(NotificationsIcon, NotificationsScreen);
notiMsgScreenGuy(MessagesIcon, MessagesScreen);


    const closeChatNotifi = eid("closeChatNotifi"),
          sendMessage = eid("sendMessage"),
          chatInput = eid("chatInput"),
          chatBody = document.querySelector(".chat-body");
    // Close button
    closeChatNotifi.addEventListener("click", () => {
      NotificationsScreen.style.display = "none";
    });
    closeChatMsg.addEventListener("click", () => {
      MessagesScreen.style.display = "none";
    });
/*USER SEARCH SUGGESTION BOX JS CODE:START*/
const data = [
  "3-Bedroom Apartment at East Legon with Pool",
  "2-Bedroom House for Rent at Spintex Road",
  "Mason for hire in Kumasi - 5 years experience",
  "Carpenter available in Accra - Affordable rates",
  "Spacious Shop for Rent at Spintex Road",
  "Land for Sale at Dodowa with Titled Documents",
  "Cleaner for hire - Daily & Weekly services",
  "Executive Office Space for Rent in Osu",
  "Painter for hire in Takoradi - Interior & Exterior",
  "Fully Furnished 1-Bedroom Apartment at Airport City"
];

const SearchField = document.getElementById("SearchField");
const suggestions = document.getElementById("suggestions");

let activeIndex = -1; // for keyboard navigation
let debounceTimer;

// Escape regex special chars in query
const escapeRegex = str => str.replace(/[.*+?^${}()|[\]\\]/g, "\\$&");

const renderSuggestions = query => {
  suggestions.innerHTML = "";
  activeIndex = -1;

  if (!query) {
    suggestions.style.display = "none";
    SearchField.setAttribute("aria-expanded", "false");
    return;
  }

  const matches = data.filter(item => 
    item.toLowerCase().includes(query.toLowerCase())
  );

  if (matches.length === 0) {
    suggestions.innerHTML = `<div class="no-results">No results found</div>`;
    suggestions.style.display = "block";
    SearchField.setAttribute("aria-expanded", "true");
    return;
  }

  const regex = new RegExp(`(${escapeRegex(query)})`, "gi");

  matches.slice(0, 8).forEach((match, index) => {
    const div = document.createElement("div");
    div.className = "suggestion";
    div.setAttribute("role", "option");
    div.innerHTML = match.replace(regex, "<strong>$1</strong>");
    
    div.onclick = () => {
      SearchField.value = match;
      suggestions.style.display = "none";
      SearchField.setAttribute("aria-expanded", "false");
    };

    suggestions.appendChild(div);
  });

  suggestions.style.display = "block";
  SearchField.setAttribute("aria-expanded", "true");
};

const debounce = (func, delay) => {
  return (...args) => {
    clearTimeout(debounceTimer);
    debounceTimer = setTimeout(() => func(...args), delay);
  };
};

SearchField.addEventListener("input", debounce(e => {
  renderSuggestions(e.target.value.trim());
}, 200));

SearchField.addEventListener("keydown", e => {
  const items = suggestions.querySelectorAll(".suggestion");
  if (!items.length) return;

  if (e.key === "ArrowDown") {
    e.preventDefault();
    activeIndex = (activeIndex + 1) % items.length;
  } else if (e.key === "ArrowUp") {
    e.preventDefault();
    activeIndex = (activeIndex - 1 + items.length) % items.length;
  } else if (e.key === "Enter") {
    e.preventDefault();
    if (activeIndex >= 0) {
      items[activeIndex].click();
    }
  } else if (e.key === "Escape") {
    suggestions.style.display = "none";
    SearchField.setAttribute("aria-expanded", "false");
  }

  items.forEach((item, i) => {
    item.classList.toggle("active", i === activeIndex);
  });
});
searchBtn.addEventListener('click', () => {
let SearchField_value=SearchField.value,
    locationPicked=LocationsDivTriggerClick.textContent;
if (locationPicked.toLowerCase().includes('all ghana')) {
  locationPicked = 'All Ghana';
}

let exporter= {'searchInput_value':searchInput_value,'locationPicked':locationPicked};
});
/*USER SEARCH SUGGESTION BOX JS CODE:START*/
/* ====== Populate region select (for convenience) ====== */
(function populateRegionsFromSelect(){
  // your large location select exists already — no duplicate population needed here.
  // If you wanted to dynamically add regions instead of the long HTML list, do it here.
})();

/* ====== Small helpers (images clickable demo) ====== */
(function imagesClickable(){
  const imgs = document.querySelectorAll('#UserPostImages img');
  imgs.forEach(img=>{
    img.addEventListener('click', ()=> {
      // Example behavior — go to a details page (replace with real link)
      // window.location.href = 'listing-details.html';
      img.style.transform = 'scale(1.02)';
      setTimeout(()=> img.style.transform = '', 250);
    });
  });
})();

/*ITEMS LOCATIONS SEARCH JS CODE: END*/
/*CATEGORY ADVERTS DISPLAY: START*/
    // ------- Sample data (client-side demo) -------
    const properties = [
      // Lands
      {id:1,category:'lands',postedAt: '2025-09-18T08:30:00Z',title:'Premium Land — Oyarifa',region:'Greater Accra',price:25000,unit:'GHS',img:'http://localhost/LandingPageRecs/user_photos/seaFront/IMG-20250531-WA0009.jpg',desc:'A fenced 0.5 acre close to the main road. Perfect for development.'},
      {id:2,category:'lands',postedAt: '2025-08-22T14:00:00Z',title:'Riverside Plot — Ada',region:'Greater Accra',price:18000,unit:'GHS',img:'http://localhost/LandingPageRecs/user_photos/seaFront/IMG-20250531-WA0010.jpg',desc:'Mature land facing the river — scenic and private.'},
      // Apartments
      {id:3,category:'apartments',postedAt: '2025-09-25T09:15:00Z',title:'2BR Apartment — Cantonments',region:'Greater Accra',price:380000,unit:'GHS',img:'http://localhost/LandingPageRecs/user_photos/seaFront/WhatsApp%20Image%202025-07-12%20at%2013.04.48_8eb9ed99.jpg',desc:'Spacious 2-bedroom apartment with parking and pool access.'},
      {id:4,category:'apartments',postedAt: '2025-09-10T12:00:00Z',title:'3BR Family Home — Kumasi',region:'Ashanti',price:280000,unit:'GHS',img:'http://localhost/LandingPageRecs/user_photos/seaFront/IMG-20250531-WA0013.jpg',desc:'Modern family apartment close to schools and markets.'},
      // Projects
      {id:5,category:'projects',postedAt: '2025-07-01T10:00:00Z',title:'Rising Heights — Accra Project',region:'Greater Accra',price:1500000,unit:'GHS',img:'http://localhost/LandingPageRecs/user_photos/seaFront/WhatsApp%20Image%202025-07-12%20at%2013.04.50_190aaaee.jpg',desc:'A mixed-use development currently under construction. Expected completion: Q4 2026.'},
      {id:6,category:'projects',postedAt: '2025-06-15T16:45:00Z',title:'limegreen Villas — Eco Project',region:'Eastern',price:900000,unit:'GHS',img:'http://localhost/LandingPageRecs/user_photos/seaFront/WhatsApp%20Image%202025-07-12%20at%2013.04.48_90980c95.jpg',desc:'Sustainable housing project with solar integration.'}
    ];

    // DOM refs
    const listingsEl = document.getElementById('listings');
    const sortSelect = document.getElementById('sortSelect');
    const Your_Saves_ele= eid('Your_Saves');

    // render listings
    function renderListings(properties_arg2=properties,filters={}){
      let out = [...properties_arg2];
      // category
      if(filters.category && filters.category!=='all') out = out.filter(p=>p.category===filters.category);
      // region
      if(filters.region) out = out.filter(p=>p.region===filters.region);
      // search
      if(filters.q) out = out.filter(p=> (p.title+" "+p.region+" "+p.desc).toLowerCase().includes(filters.q.toLowerCase()));
      // sort
      if(filters.sort==='priceAsc') out.sort((a,b)=>a.price-b.price);
      else if(filters.sort==='priceDesc') out.sort((a,b)=>b.price-a.price);
      else out.sort((a,b)=>b.id-b.id); // keep order

      listingsEl.innerHTML = out.map((p, p_index)=>`<div class="card" data-postid="${p_index+1}">
        <img class="thumb" src='${p.img}'>
        <div style="margin-top:10px;display:flex;flex-direction:column;">
          <div class="title">${p.title}</div><small style="color:#777;"> 👁️: 25k</small>
          <div class="category-date">
            <div style="display:flex;gap:8px;margin-top:10px">
            <small class="post-sub-category" style="color:#777;">sub 🏷️: ${p.category}</small>
            <small class="post-date" style="color:#777;">📅 Posted: Sept 24, 2025</small>
           </div>
          <div class="region-date">
            <small class="meta-price" style="color:#777;">📍 Location: ${p.region}</small>
            <div class="price">Price: ${p.unit} ${formatNumber(p.price)}</div>
          </div>
          </div>
        </div>
        <div class="performance-actions">
          <button class="btn secondary"  id="actionBtnSave${p_index+1}" data-id="${p_index+1}">save</button>
          <button class="btn secondary" id="actionBtnLikes${p_index+1}" data-id="${p_index+1}">👍:2k</button>
          <button class="btn secondary" id="actionBtnChat${p_index+1}" data-id="${p_index+1}">chat</button>
        </div>
      </div>`).join('')
    }

    function formatNumber(n){return n.toLocaleString('en-US')}

    renderListings();
/*ADS SORTING JS CODE: START*/
function sortProperties(list, sortBy) {
  const arr = [...list];
  const getTime = (p) => {
    const candidates = [p.postedAt, p.date, p.createdAt];
    for (const c of candidates) {
      if (!c) continue;
      const t = Date.parse(c);
      if (!isNaN(t)) return t;
    }
    return typeof p.id === 'number' ? p.id : 0;
  };

  switch (sortBy) {
    case 'new':
      arr.sort((a, b) => getTime(b) - getTime(a));
      break;

    case 'priceAsc':
      arr.sort((a, b) => a.price - b.price);
      break;

    case 'priceDesc':
      arr.sort((a, b) => b.price - a.price);
      break;

    default:
      console.warn('Unknown sort option:', sortBy);
  }

  return arr;
}

document.addEventListener('DOMContentLoaded', () => {
  renderListings(sortProperties(properties, 'new'));
  sortSelect.addEventListener('change', function () {
    const sorted = sortProperties(properties, this.value);
    renderListings(sorted);
  });
});

/*ADS SORTING JS CODE: END*/
    listingsEl.addEventListener('click',e=>{
    let e_target_className = e.target.parentElement.className;
    if(e_target_className){
      e_target_className = e_target_className.trim().toLowerCase();
      if(e_target_className == 'card'){
        window.location.href = 'http://localhost/LandingPageRecs/listing.html';
      }
    }
    });
/*CATEGORY ADVERTS DISPLAY: END*/
//***********************************************
/*MESSAGING: START*/
import {chatMegaMachine} from './reusable_js_codes.js';
chatMegaMachine();
/*MESSAGING: END*/
//***********************************************
/*CATEGORY ADVERTS DISPLAY ACTIONS CODE: START*/
function parseCount(str) {
  let num = parseFloat(str);
  let suffix = str.replace(/[0-9\.\s]/g, '').toUpperCase();
  switch (suffix) {
    case 'K': return num * 1e3;
    case 'M': return num * 1e6;
    case 'B': return num * 1e9;
    default: return num;
  }
}

function formatCount(num) {
  if (num >= 1e9) return (num / 1e9).toFixed(1).replace(/\.0$/, '') + 'B';
  if (num >= 1e6) return (num / 1e6).toFixed(1).replace(/\.0$/, '') + 'M';
  if (num >= 1e3) return (num / 1e3).toFixed(1).replace(/\.0$/, '') + 'k';
  return num.toString();
}

function updateCount(str, delta = 1) {
  let value = parseCount(str);
  value += delta;
  if (value < 0) value = 0;
  return formatCount(value);
}

var likes_action_array = [],
    saves_action_array = [];
listingsEl.addEventListener('click',(event)=>{
const target_clicked = event.target,
      target_clicked_parent = target_clicked.parentElement,
      ancestor = target_clicked_parent.parentElement,
      target_clicked_parent_offsetTop = listingsEl.offsetTop,
      ancestor_y_offset = ancestor.offsetTop,
      target_clicked_className = target_clicked.id.trim().toLowerCase();
if(target_clicked_className.includes('actionbtnsave')){
let SaveDate = new Date().toLocaleString(),
    ancestor_postid = ancestor.dataset.postid,
    actionBtnSave_d_id = target_clicked.dataset.id.trim().toLowerCase(),
    Your_Saves_Cont = eid('Your_Saves_Cont'),
    Your_Saves_number = Number(Your_Saves_ele.textContent.trim()),
    Your_Saves_Cont_child = document.createElement('a');
saves_action_array.push(actionBtnSave_d_id);
saves_action_array = saves_action_array.slice(0,2);
if(actionBtnSave_d_id != 'set'){
let saveDate = new Date().toLocaleString(),
    postTitle = ancestor.querySelector('.title');
target_clicked.dataset.id = 'set';
target_clicked.style.background = 'limegreen';
Your_Saves_number+=1;
Your_Saves_Cont_child.innerHTML = `<span class="saved-number">${Your_Saves_number}</span>. ${postTitle.textContent}  <button>del</button><br><small>${saveDate}</small><br><br>`;
Your_Saves_Cont_child.dataset.postid = `${ancestor_postid}`;
Your_Saves_Cont_child.href = '#';
Your_Saves_Cont.appendChild(Your_Saves_Cont_child);
target_clicked.dataset.p_id = `${ancestor_postid}`;

/*A new post has been added to favourite: sever data collection goes here*/

}
if(actionBtnSave_d_id == 'set'){
target_clicked.dataset.id = saves_action_array[0];
target_clicked.style.background = 'var(--accent)';
Your_Saves_number-=1;
let childToRemove = eid(target_clicked.dataset.p_id);
if (childToRemove) {
    Your_Saves_Cont.removeChild(childToRemove);
   
    /*A new post added to favourite has been remove: server data collection here*/

    const Your_Saves_Cont_children = Your_Saves_Cont.querySelectorAll('a');
    Your_Saves_Cont_children.forEach((a_node, index) => {
    let humanIndex = index + 1;
    let span = a_node.querySelector('.saved-number');
    if (span) {
        span.textContent = humanIndex;
        }
    });
}

}
Your_Saves_ele.textContent = `${Your_Saves_number}`;
}
if(target_clicked_className.includes('actionbtnlikes')){
let actionBtnLikes_textContent = target_clicked.textContent.trim().split(':')[1],
    actionBtnLikes_d_id = target_clicked.dataset.id.trim().toLowerCase(),
    actionBtnLikes_textContent_num = actionBtnLikes_textContent;
likes_action_array.push(actionBtnLikes_d_id);
likes_action_array = likes_action_array.slice(0,2);
if(actionBtnLikes_d_id != 'set'){
let likeDate = new Date().toLocaleString();
target_clicked.dataset.id = 'set';
target_clicked.style.background = 'limegreen';
actionBtnLikes_textContent_num=updateCount(actionBtnLikes_textContent,1);

/*Loggin user liked a post: server data collection goes here*/

}
if(actionBtnLikes_d_id == 'set'){
target_clicked.dataset.id = likes_action_array[0];
target_clicked.style.background = 'var(--accent)';

/*Loggin user unliked a post: server data collection goes here*/

actionBtnLikes_textContent_num=updateCount(actionBtnLikes_textContent,-1);
}
target_clicked.textContent = `👍:${actionBtnLikes_textContent_num}`;
}

if(target_clicked_className.includes('actionbtnchat')){
displayer(MessagesScreen,ancestor_y_offset);
}
})

/*LEFT SIDE BAR JS CODE HERE: START*/
const Your_Posts_Cont = eid('Your_Posts_Cont'),
      Your_Saves_Cont = eid('Your_Saves_Cont'),
      Your_Posts = eid('Your_Posts'),
      Your_Saves = eid('Your_Saves');
const today = new Date().toLocaleString();
const Your_Posts_Cont_posts = [
`<span class="post-number">${1}</span>. New arrivals! Contact me before they run out of stock  <button>del</button><br><small>${today}</small><br><br>`,
`<span class="post-number">${2}</span>. New ring light for sale at Sakumonor  <button>del</button><br><small>${today}</small><br><br>`,
`<span class="post-number">${3}</span>. Single room self-contained for rent at Pokuase  <button>del</button><br><small>${today}</small><br><br>`,
`<span class="post-number">${4}</span>. 2024 Kia for sale  <button>del</button><br><small>${today}</small><br><br>`,
`<span class="post-number">${5}</span>. iphone 15 pro max, GHS 13,000. Negotiable <button>del</button><br><small>${today}</small><br><br>`,
`<span class="post-number">${6}</span>. Masons needed urgently for immediate employment  <button>del</button><br><small>${today}</small><br><br>`,
`<span class="post-number">${7}</span>. A storage facility at Trantra Hills for rent, 3years advance.  <button>del</button><br><small>${today}</small><br><br>`,
`<span class="post-number">${8}</span>. 20 buckets of deluxy paint for sale. Offwhite color.  <button>del</button><br><small>${today}</small><br><br>`];

const Your_Saves_Cont_posts = [
`<span class="saved-number">${1}</span>. 20 acres of registered and fenced land at Obeyeyei  <button>del</button><br><small>${today}</small><br><br>`,
`<span class="saved-number">${2}</span>. Brand new Toyota Hilux for sale, 2022 model - Achimota New Station.  <button>del</button><br><small>${today}</small><br><br>`,
`<span class="saved-number">${3}</span>. Chamber and Hall self-contained for two years advance rent.  <button>del</button><br><small>${today}</small><br><br>`,
`<span class="saved-number">${4}</span>. I am selling all my room stuff, I am traveling to USA.  <button>del</button><br><small>${today}</small><br><br>`,
`<span class="saved-number">${5}</span>. HP coire i7 laptop going for sales - James Town  <button>del</button><br><small>${today}</small><br><br>`,
`<span class="saved-number">${6}</span>. Royal okada motor for sale at a cool GHS 8500, Nungua.  <button>del</button><br><small>${today}</small><br><br>`,
`<span class="saved-number">${7}</span>. A short let 3-Bedroom aparemtn for thre months rent at Fijai, Kasoa  <button>del</button><br><small>${today}</small><br><br>`,
`<span class="saved-number">${8}</span>. Scafolds for hire at Achiaman.  <button>del</button><br><small>${today}</small><br><br>`
                              ];
Your_Posts_Cont_posts.forEach((posts, post_index)=>{
  const post_title_ele = document.createElement('a'),
  unique_post_id = uniqueIdSync(posts);
  post_title_ele.dataset.postid = `${unique_post_id}`;
  post_title_ele.href = '#';
  post_title_ele.innerHTML = posts.trim();
  Your_Posts_Cont.appendChild(post_title_ele);
})
Your_Saves_Cont_posts.forEach((saves, save_index) => {
  const post_save_title_ele = document.createElement('a'),
        unique_save_id = uniqueIdSync(saves);
  post_save_title_ele.dataset.postid = `${unique_save_id}`;
  post_save_title_ele.href = '#';
  post_save_title_ele.innerHTML = saves.trim(); 
  
  Your_Saves_Cont.appendChild(post_save_title_ele);
});
Your_Posts.textContent = Your_Posts_Cont_posts.length;
Your_Saves.textContent = Your_Saves_Cont_posts.length;
/*LEFT SIDE BAR JS CODE HERE: END*/

const LeftSideBar = eid('LeftSideBar');
LeftSideBar.addEventListener('mouseover',(mo_event)=>{
const mo_event_target = mo_event.target,
      mo_event_targetTagName = mo_event_target.tagName.toLowerCase();
if(mo_event_targetTagName=='a'){
const mouseOver = ()=>{
const button = mo_event_target.querySelector('button');
button.style.display = 'block';
button.style.transition = 'all 0.5s ease';
}
requestAnimationFrame(mouseOver);
}
})

LeftSideBar.addEventListener('click', (LeftSideBar_event)=>{
const LeftSideBar_event_target = LeftSideBar_event.target,
      potentialButtonParent = LeftSideBar_event_target.parentElement,
      potentialButtonParent_parent = potentialButtonParent.parentElement,
      Your_Posts_Cont_ele = potentialButtonParent_parent.id,
      potentialButtonParent_id = potentialButtonParent.dataset.postid,
      elementTagName = LeftSideBar_event_target.tagName.toLowerCase();
if(elementTagName == 'a'){
localStorage.setItem('MASCOM_LeftSideBar_a_element_clicked',potentialButtonParent_id);
window.location.href = 'http://localhost/LandingPageRecs/listing.html';
}
if(elementTagName == 'button'){
if(Your_Posts_Cont_ele == 'Your_Saves_Cont'){
let childToRemove = document.querySelector(`[data-postid="${potentialButtonParent_id}"]`);
if (childToRemove) {
    let span_found = false;
    Your_Saves_Cont.removeChild(childToRemove);

    /*A post added to favourite has been remove: server data collection here*/

    const Your_Saves_Cont_children = Your_Saves_Cont.querySelectorAll('a'),
          Your_Saves_Cont_children_len = Your_Saves_Cont_children.length;
    if(Your_Saves_Cont_children_len>0){
    Your_Saves_Cont_children.forEach((a_node, index) => {
    let humanIndex = index + 1;
    let span = a_node.querySelector('.saved-number');
    if (span) {
        span.textContent = humanIndex;
        span_found = true;
        }
    });
    }else{
      span_found = true;
    }
let Your_Saves_number1 = Number(Your_Saves_ele.textContent.trim());
if(span_found && Your_Saves_number1>0){
Your_Saves_ele.textContent = `${Your_Saves_number1-1}`;
const button_linked = document.querySelector(`[data-p_id = '${potentialButtonParent_id}']`);
if(button_linked){
button_linked.style.background = 'var(--accent)';
button_linked.dataset.id = '0';
}
}
}
}
if(Your_Posts_Cont_ele == 'Your_Posts_Cont'){
const Your_Posts = eid('Your_Posts'),
      Your_Posts_count = Number(Your_Posts.textContent.trim());
const thePost = document.querySelector(`[data-postid = '${potentialButtonParent.dataset.postid}']`);
if(thePost){
potentialButtonParent_parent.removeChild(thePost);

/*Loggin user has deleted a post: server data collection here*/

Your_Posts.textContent = Your_Posts_count-1;
    const Your_Saves_Cont_children = potentialButtonParent_parent.querySelectorAll('a');
    Your_Saves_Cont_children.forEach((a_node, index) => {
    let humanIndex = index + 1;
    let span = a_node.querySelector('.post-number');
    if (span){
        span.textContent = humanIndex;
        }
    });
}
}
}
})
/*CATEGORY ADVERTS DISPLAY ACTIONS CODE: END*/
const LocationsDivTriggerClick = eid('LocationsDivTriggerClick');
const tems_locations_container_id = eid('tems_locations_container_id');

window.addEventListener('click', (event) => {
  let tElement = event.target;

  let clickedInsideTrigger = LocationsDivTriggerClick.contains(tElement);
  let clickedInsideContainer = tems_locations_container_id.contains(tElement);
  let clickedInsideContainer2=u_pic_projector_parent.contains(tElement);
  let clickedInsideContainer3 = profilePicContainer.contains(tElement);
  if(!clickedInsideContainer2 && !clickedInsideContainer3){
    u_pic_projector_parent.style.display = 'none'
  }
  if (!clickedInsideTrigger && !clickedInsideContainer) {
    tems_locations_container_id.style.display = 'none';
  }
});

LocationsDivTriggerClick.addEventListener('click', () => {
  tems_locations_container_id.style.top = '0';
  var INNER_HEIGHT_D = window.innerHeight;
  tems_locations_container_id.style.display = 'flex';
  var tems_locations_container_id_clientHeight=tems_locations_container_id.offsetHeight;
  var mrgTop=Math.round((INNER_HEIGHT_D-tems_locations_container_id_clientHeight)/2);
  tems_locations_container_id.style.transition = 'top 1s linear';
  setTimeout(() => {
    tems_locations_container_id.style.top = `${mrgTop}px`;
  }, 50);
});
tems_locations_container_id.addEventListener('click', (event) => {
  const clickedElement = event.target;
  if (clickedElement !== tems_locations_container_id && tems_locations_container_id.contains(clickedElement)) {
    if (clickedElement.childNodes.length === 1) {
      
      const clickedText = clickedElement.textContent.trim();
      LocationsDivTriggerClick.innerHTML = clickedText;
      tems_locations_container_id.style.display = 'none';
    }
  }
});

/*ITEMS LOCATIONS SEARCH JS CODE: END*/

    /* ====== End of script ====== */
/*FOOTER SOCIAL MEDIA HANDLE LINKS CODE: START*/
    const Facebook_mascom_socials=eid('Facebook_mascom_socials');
    const LinkedIn_mascom_socials=eid('LinkedIn_mascom_socials');
    const YouTube_mascom_socials=eid('YouTube_mascom_socials');
    const tiktok_mascom_socials=eid('tiktok_mascom_socials');
    const Instagram_mascom_socials=eid('Instagram_mascom_socials');
    Facebook_mascom_socials.addEventListener('click',()=>{
      wL('https://bit.ly/46ygGpJ');
    })
    LinkedIn_mascom_socials.addEventListener('click',()=>{
      wL('#');
    })
    YouTube_mascom_socials.addEventListener('click',()=>{
      wL('https://bit.ly/4mnRcBd');
    })
    tiktok_mascom_socials.addEventListener('click',()=>{
      wL('https://bit.ly/4pBPTSb');
    })
    Instagram_mascom_socials.addEventListener('click',()=>{
      wL('https://bit.ly/3VIESkl');
    })
    /*FOOTER SOCIAL MEDIA HANDLE LINKS CODE: END*/