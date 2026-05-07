document.addEventListener("DOMContentLoaded", () => {
document.body.classList.add("loaded");
});
const eid = (id) => document.getElementById(id);
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

const wL = (custom_href)=>{
window.location.href=custom_href;
};

const mascom_logo=document.getElementsByClassName('logo')[0];
mascom_logo.addEventListener('click',()=>{
window.location.href='http://localhost/LandingPageRecs/MASCOM.html';
})

/*NEW ADVERT CREATION JS CODE: START*/
const Advertise=eid('Advertise');
Advertise.addEventListener('click',()=>{
window.location.href='http://localhost/LandingPageRecs/new_item.html';
})

/*DATABASE ENTERIES ARRIVAL JS CODE: START*/
const userLoginFlagger = (loginLogic)=>{
const loginBtn = eid('loginBtn'),
      profilePicContainer2   = eid('User_profile_pic');
if (!loginLogic) {
  loginBtn.style.display = 'block';
  profilePicContainer2.style.display = 'none';
}
}
userLoginFlagger(true);
/*DATABASE ENTERIES ARRIVAL JS CODE: END*/

/*NEW ADVERT CREATION JS CODE: END*/
/*ITEMS LOCATIONS SEARCH JS CODE: START*/
const LocationsDivTriggerClick = eid('LocationsDivTriggerClick');
const tems_locations_container_id = eid('tems_locations_container_id');

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

// ====== Locations Search ======
window.addEventListener("click", (event) => {
  if (
    !LocationsDivTriggerClick.contains(event.target) &&
    !tems_locations_container_id.contains(event.target)
  ) {
    tems_locations_container_id.style.display = "none";
  }
});

LocationsDivTriggerClick.addEventListener("click", () => {
  tems_locations_container_id.style.display = "flex";
  tems_locations_container_id.style.top = "0";
  const mrgTop = Math.round((window.innerHeight - tems_locations_container_id.offsetHeight) / 2);
  tems_locations_container_id.style.transition = "top 1s linear";
  setTimeout(() => (tems_locations_container_id.style.top = `${mrgTop}px`), 50);
});

tems_locations_container_id.addEventListener("click", (event) => {
  const clickedElement = event.target;
  if (clickedElement !== tems_locations_container_id && clickedElement.children.length === 0) {
    LocationsDivTriggerClick.textContent = clickedElement.textContent.trim();
    tems_locations_container_id.style.display = "none";
  }
});

/*ITEMS LOCATIONS SEARCH JS CODE: END*/
/*CATEGORY ADVERTS DISPLAY: START*/
    // ------- Sample data (client-side demo) -------
    const professions = [
      // Lands
      {id:1,category:'Architect',postedAt: '2025-09-18T08:30:00Z',name:'Alice Asafu-Adjaye',region:'Accra, Greater Accra Region',price:1200,unit:'GHS',img:'http://localhost/LandingPageRecs/Building_And_Construction_Recs/photos/Alice_Asafu_Adjaye.jpeg',desc:'Founded her own practice “Mustard”; moved back to Ghana in 2012 after working in the UK.'},
      {id:2,category:'Electricians',postedAt: '2025-08-22T14:00:00Z',name:'Ing. Isaac Ofosu Appiah',region:'Greater Accra',price:1000,unit:'GHS',img:'http://localhost/LandingPageRecs/Building_And_Construction_Recs/photos/Ing_Isaac_Ofosu_Appiah.jpeg',desc:'CEO of GENEC ELECTRIX LTD, awarded “Most Promising Electrical Contractor” in 2023 by the Ghana Construction Industry Excellence Awards.'},
      // Apartments
      {id:3,category:'Painters',postedAt: '2025-09-25T09:15:00Z',name:'Amoako Boafo',region:'Greater Accra',price:500,unit:'GHS',img:'http://localhost/LandingPageRecs/Building_And_Construction_Recs/photos/Amoako_Boafo.jpg',desc:'Figurative painting; known for vibrant portraits of Black figures; international reputation.'},
      {id:4,category:'Steel Benders',postedAt: '2025-09-10T12:00:00Z',name:'Nyamedze Kingdom Enterprise',region:'Ashanti',price:300,unit:'GHS',img:'http://localhost/LandingPageRecs/Building_And_Construction_Recs/photos/Nyamedze Kingdom Enterprise.jpg',desc:'Nyamedze Kingdom Enterprise, very known nationally'},
      // Projects
      {id:5,category:'Carpenters',postedAt: '2025-07-01T10:00:00Z',name:'Daniel Mensah (Hello Design Coffin Works)',region:'Greater Accra',price:250,unit:'GHS',img:'http://localhost/LandingPageRecs/Building_And_Construction_Recs/photos/250px-Daniel_Mensah__Hello__2006._Foto_Regula_Tschumi.jpg',desc:'A Ga carpenter, fantasy coffin artist. Trained under Paa Joe.'},
      {id:6,category:'Masons',postedAt: '2025-06-15T16:45:00Z',name:'The Quansah Family',region:'Amasaman',price:200,unit:'GHS',img:'http://localhost/LandingPageRecs/Building_And_Construction_Recs/photos/mason.webp',desc:'Highly skillful with their masonary works and other duties.'}
    ];
    // DOM refs
    const listingsEl = document.getElementById('listings');
    const searchInput = document.getElementById('searchInput');
    const searchBtn = document.getElementById('searchBtn');
    const sortSelect = document.getElementById('sortSelect');

    // render listings
    function renderListings(professions_arg2=professions,filters={}){
      let out = [...professions_arg2];
      // category
      if(filters.category && filters.category!=='all') out = out.filter(p=>p.category===filters.category);
      // region
      if(filters.region) out = out.filter(p=>p.region===filters.region);
      // search
      if(filters.q) out = out.filter(p=> (p.name+" "+p.region+" "+p.desc).toLowerCase().includes(filters.q.toLowerCase()));
      // sort
      if(filters.sort==='priceAsc') out.sort((a,b)=>a.price-b.price);
      else if(filters.sort==='priceDesc') out.sort((a,b)=>b.price-a.price);
      else out.sort((a,b)=>b.id-b.id); // keep order

      listingsEl.innerHTML = out.map((p, p_index)=>`<div class="card" data-postid="${p_index+1}">
        <img class="thumb" src='${p.img}'>
        <div style="margin-top:10px;display:flex;flex-direction:column;">
          <div class="title">${p.name}</div><small style="color:#777;"> 👁️: 25k</small>
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
  renderListings(sortProperties(professions, 'new'));
  sortSelect.addEventListener('change', function () {
    const sorted = sortProperties(professions, this.value);
    renderListings(sorted);
  });
});

/*ADS SORTING JS CODE: END*/

    // click handlers
    document.getElementById('categoryChips').addEventListener('click',e=>{
      if(e.target.classList.contains('chip-cat-loader')) renderListings(professions,{category:e.target.dataset.cat})
    });


    // request trigger actions
    document.getElementById('hero_card_2_id').addEventListener('click',e=>{
      const CATEGORY = ['find masons','find carpenters','find steel benders','find electricians','find painters', 'find architects'],
            cate_target = e.target.textContent.trim().toLowerCase();
      if(CATEGORY.includes(cate_target)){
      window.location.href = 'http://localhost/LandingPageRecs/request.html';
      localStorage.setItem('RefererCategory', `buildingandconstruction_${cate_target}`);
      }
    });

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
/*CATEGORY ADVERTS DISPLAY ACTIONS CODE: START*/
//***********************************************
    const closeChatMsg = eid('closeChatMsg'),
          sendMessage = eid("sendMessage"),
          MessagesScreen = eid('MessagesScreen'),
          chatInput = eid("chatInput"),
          chatBody = document.querySelector(".chat-body");
    closeChatMsg.addEventListener("click", () => {
      MessagesScreen.style.display = "none";
    });

/*MESSAGING: START*/
import {chatMegaMachine} from './reusable_js_codes.js';
chatMegaMachine();
/*MESSAGING: END*/
//***********************************************
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
    actionBtnSave_d_id = target_clicked.dataset.id.trim().toLowerCase();
saves_action_array.push(actionBtnSave_d_id);
saves_action_array = saves_action_array.slice(0,2);
if(actionBtnSave_d_id != 'set'){
let saveDate = new Date().toLocaleString(),
    postTitle = ancestor.querySelector('.title');
target_clicked.dataset.id = 'set';
target_clicked.style.background = 'limegreen';
}
if(actionBtnSave_d_id == 'set'){
target_clicked.dataset.id = saves_action_array[0];
target_clicked.style.background = 'var(--accent)';

}
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
}
if(actionBtnLikes_d_id == 'set'){
target_clicked.dataset.id = likes_action_array[0];
target_clicked.style.background = 'var(--accent)';
actionBtnLikes_textContent_num=updateCount(actionBtnLikes_textContent,-1);
}
target_clicked.textContent = `👍:${actionBtnLikes_textContent_num}`;
}

if(target_clicked_className.includes('actionbtnchat')){
displayer(MessagesScreen,ancestor_y_offset);
}
})
/*CATEGORY ADVERTS DISPLAY ACTIONS CODE: END*/
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
    searchInput.setAttribute("aria-expanded", "false");
    return;
  }

  const matches = data.filter(item => 
    item.toLowerCase().includes(query.toLowerCase())
  );

  if (matches.length === 0) {
    suggestions.innerHTML = `<div class="no-results">No results found</div>`;
    suggestions.style.display = "block";
    searchInput.setAttribute("aria-expanded", "true");
    return;
  }

  const regex = new RegExp(`(${escapeRegex(query)})`, "gi");

  matches.slice(0, 8).forEach((match, index) => {
    const div = document.createElement("div");
    div.className = "suggestion";
    div.setAttribute("role", "option");
    div.innerHTML = match.replace(regex, "<strong>$1</strong>");
    
    div.onclick = () => {
      searchInput.value = match;
      suggestions.style.display = "none";
      searchInput.setAttribute("aria-expanded", "false");
    };

    suggestions.appendChild(div);
  });

  suggestions.style.display = "block";
  searchInput.setAttribute("aria-expanded", "true");
};

const debounce = (func, delay) => {
  return (...args) => {
    clearTimeout(debounceTimer);
    debounceTimer = setTimeout(() => func(...args), delay);
  };
};

searchInput.addEventListener("input", debounce(e => {
  renderSuggestions(e.target.value.trim());
}, 200));

searchInput.addEventListener("keydown", e => {
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
    searchInput.setAttribute("aria-expanded", "false");
  }

  items.forEach((item, i) => {
    item.classList.toggle("active", i === activeIndex);
  });
});
var category_selected = 'all';
const categoryChips_marker = eid('categoryChips_marker');
categoryChips_marker.addEventListener('click', (clicked_ele)=>{
let clicked_ele_clicked = clicked_ele.target,
    clicked_ele_clicked_array = Array.from(categoryChips_marker.children),
    clicked_ele_clicked_array_len = Array.from(clicked_ele_clicked.children).length,
    chd_textContent1 = clicked_ele_clicked.textContent.toLowerCase();
if(clicked_ele_clicked_array_len == 0){
clicked_ele_clicked_array.forEach(chd => {
let chd_textContent = chd.textContent.toLowerCase();
if(chd_textContent!=chd_textContent1){
chd.style.backgroundColor = 'var(--accent)';
}
}) 
}

if(categoryChips_marker.contains(clicked_ele_clicked) && clicked_ele_clicked_array_len == 0){
clicked_ele_clicked.style.background = 'limegreen';
category_selected = chd_textContent1;
}
})

searchBtn.addEventListener('click', () => {
let searchInput_value=searchInput.value,
    locationPicked=LocationsDivTriggerClick.textContent;
if (locationPicked.toLowerCase().includes('all ghana')) {
  locationPicked = 'All Ghana';
}

let exporter= {'searchInput_value':searchInput_value,'locationPicked':locationPicked,'category_selected':category_selected};
});
/*USER SEARCH SUGGESTION BOX JS CODE:END*/
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
    /*FOOTER SOCIAL MEDIA HANDLE LINKS CODE: START*/