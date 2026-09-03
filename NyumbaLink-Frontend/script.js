const towns = {
  Nairobi: ["Kilimani", "Westlands", "Kasarani", "Embakasi"],
  Kiambu: ["Ruiru", "Thika", "Kiambu Town", "Limuru"],
  Mombasa: ["Nyali", "Bamburi", "Likoni", "Mtwapa"],
  Nakuru: ["Nakuru Town", "Naivasha", "Gilgil"],
  "Uasin Gishu": ["Eldoret", "Turbo", "Kesses"],
  Kajiado: ["Kitengela", "Ngong", "Kajiado Town"]
};

const county = document.getElementById("county");
const town = document.getElementById("town");
const searchForm = document.getElementById("searchForm");
const searchMessage = document.getElementById("searchMessage");

county.addEventListener("change", () => {
  town.innerHTML = '<option value="">All towns</option>';
  const list = towns[county.value] || [];
  town.disabled = !county.value;
  list.forEach(name => {
    const option = document.createElement("option");
    option.textContent = name;
    option.value = name;
    town.appendChild(option);
  });
});

document.querySelectorAll(".purpose-btn").forEach(btn => {
  btn.addEventListener("click", () => {
    document.querySelectorAll(".purpose-btn").forEach(b => b.classList.remove("active"));
    btn.classList.add("active");
  });
});

searchForm.addEventListener("submit", (event) => {
  event.preventDefault();
  const purpose = document.querySelector(".purpose-btn.active").dataset.purpose;
  const countyValue = county.value || "all counties";
  const townValue = town.value || "all towns";
  const typeValue = document.getElementById("type").value || "any property type";
  searchMessage.textContent = `Searching ${purpose === "rent" ? "rental homes" : "land"} in ${townValue}, ${countyValue} — ${typeValue}.`;
});

function openPostModal() {
  document.getElementById("modal").classList.add("open");
  document.body.style.overflow = "hidden";
}
function closePostModal() {
  document.getElementById("modal").classList.remove("open");
  document.body.style.overflow = "";
}

function openFaqModal() {
  document.getElementById("faqModal").classList.add("open");
  document.body.style.overflow = "hidden";
}

function closeFaqModal() {
  document.getElementById("faqModal").classList.remove("open");
  document.body.style.overflow = "";
}
function submitListing(event) {
  event.preventDefault();
  closePostModal();
  alert("Listing details saved. Connect this form to your backend to publish the property.");
}
function showAll() {
  document.querySelector(".latest").scrollIntoView({ behavior: "smooth" });
}

document.getElementById("modal").addEventListener("click", e => {
  if (e.target.id === "modal") closePostModal();
});
document.getElementById("faqModal").addEventListener("click", e => {
  if (e.target.id === "faqModal") closeFaqModal();
});
document.addEventListener("keydown", e => {
  if (e.key === "Escape") {
    closePostModal();
    closeFaqModal();
  }
});


function filterArea(area) {
  showAll();
  const message = document.getElementById("searchMessage");
  if (message) message.textContent = `Showing properties around ${area}.`;
}
