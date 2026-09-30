const API_BASE = "http://127.0.0.1:8000";

/*
|--------------------------------------------------------------------------
| County and town data
|--------------------------------------------------------------------------
*/

const towns = {
  Nairobi: [
    "Kilimani",
    "Westlands",
    "Kasarani",
    "Embakasi"
  ],
  Kiambu: [
    "Ruiru",
    "Thika",
    "Kiambu Town",
    "Limuru"
  ],
  Mombasa: [
    "Nyali",
    "Bamburi",
    "Likoni",
    "Mtwapa"
  ],
  Nakuru: [
    "Nakuru Town",
    "Naivasha",
    "Gilgil"
  ],
  "Uasin Gishu": [
    "Eldoret",
    "Turbo",
    "Kesses"
  ],
  Kajiado: [
    "Kitengela",
    "Ngong",
    "Kajiado Town"
  ]
};

/*
|--------------------------------------------------------------------------
| Search elements
|--------------------------------------------------------------------------
*/

const county = document.getElementById("county");
const town = document.getElementById("town");
const searchForm = document.getElementById("searchForm");
const searchMessage = document.getElementById("searchMessage");

/*
|--------------------------------------------------------------------------
| County → Town dropdown
|--------------------------------------------------------------------------
*/

county?.addEventListener("change", () => {
  if (!town) return;

  town.innerHTML = '<option value="">All towns</option>';

  const selectedCounty = county.value;
  const list = towns[selectedCounty] || [];

  town.disabled = !selectedCounty;

  list.forEach(name => {
    const option = document.createElement("option");
    option.value = name;
    option.textContent = name;
    town.appendChild(option);
  });
});

/*
|--------------------------------------------------------------------------
| Purpose buttons
|--------------------------------------------------------------------------
*/

document.querySelectorAll(".purpose-btn").forEach(button => {
  button.addEventListener("click", () => {
    document
      .querySelectorAll(".purpose-btn")
      .forEach(btn => btn.classList.remove("active"));

    button.classList.add("active");
  });
});

/*
|--------------------------------------------------------------------------
| Load properties
|--------------------------------------------------------------------------
*/

async function loadProperties(filters = {}) {
  const params = new URLSearchParams();

  Object.entries(filters).forEach(([key, value]) => {
    if (value !== undefined && value !== null && value !== "") {
      params.set(key, value);
    }
  });

  const queryString = params.toString();
  const endpoint = queryString
    ? `${API_BASE}/api/properties?${queryString}`
    : `${API_BASE}/api/properties`;

  try {
    const response = await fetch(endpoint, {
      method: "GET",
      headers: {
        "Accept": "application/json"
      }
    });

    let data;

    try {
      data = await response.json();
    } catch {
      throw new Error("The server returned an invalid response.");
    }

    if (!response.ok) {
      const message = Array.isArray(data.detail)
        ? data.detail.map(error => error.msg).join(", ")
        : data.detail || "Could not load properties.";

      throw new Error(message);
    }

    const properties = Array.isArray(data)
      ? data
      : data.properties || [];

    renderProperties(properties);

    return properties;
  } catch (error) {
    console.error("Load properties error:", error);

    const grid = document.getElementById("propertyGrid");

    if (grid) {
      grid.innerHTML = `
        <div class="empty-state">
          <p>Unable to load properties at the moment.</p>
          <button class="green-btn" type="button" onclick="loadProperties()">
            Try again
          </button>
        </div>
      `;
    }

    throw error;
  }
}

/*
|--------------------------------------------------------------------------
| Render properties
|--------------------------------------------------------------------------
*/

function renderProperties(properties) {
  const grid = document.getElementById("propertyGrid");

  if (!grid) return;

  if (!Array.isArray(properties) || properties.length === 0) {
    grid.innerHTML = `
      <div class="empty-state">
        <p>No matching properties found.</p>
        <button
          class="green-btn"
          type="button"
          onclick="openPostModal()"
        >
          Post a property
        </button>
      </div>
    `;
    return;
  }

  grid.innerHTML = properties
    .map(property => {
      const title = escapeHtml(property.title || "Untitled property");
      const propertyTown = escapeHtml(property.town || "");
      const propertyCounty = escapeHtml(property.county || "");
      const propertyType = escapeHtml(property.property_type || "");
      const purpose = escapeHtml(property.purpose || "");
      const description = escapeHtml(property.description || "");

      const price = Number(property.price || 0).toLocaleString();

      const imageHtml = property.image_url
        ? `
          <img
            class="property-image"
            src="${escapeHtml(property.image_url)}"
            alt="${title}"
            loading="lazy"
          >
        `
        : "";

      return `
        <article class="property-card">
          ${imageHtml}

          <div class="property-card-body">
            <h3>${title}</h3>

            <p class="property-location">
              ${propertyTown}${propertyTown && propertyCounty ? ", " : ""}${propertyCounty}
            </p>

            <strong class="property-price">
              KES ${price}
            </strong>

            <small class="property-type">
              ${propertyType}
            </small>

            <small class="property-purpose">
              ${purpose === "rent" ? "For rent" : "Land for sale"}
            </small>

            ${
              description
                ? `<p class="property-description">${description}</p>`
                : ""
            }
          </div>
        </article>
      `;
    })
    .join("");
}

/*
|--------------------------------------------------------------------------
| Search form
|--------------------------------------------------------------------------
*/

searchForm?.addEventListener("submit", async event => {
  event.preventDefault();

  const purpose =
    document.querySelector(".purpose-btn.active")?.dataset.purpose || "";

  const filters = {
    county: county?.value || "",
    town: town?.value || "",
    type: document.getElementById("type")?.value || "",
    purpose
  };

  if (searchMessage) {
    searchMessage.textContent = "Searching...";
  }

  try {
    const properties = await loadProperties(filters);

    if (searchMessage) {
      searchMessage.textContent =
        `${properties.length} ${properties.length === 1 ? "property" : "properties"} found.`;
    }
  } catch (error) {
    if (searchMessage) {
      searchMessage.textContent =
        "Unable to search properties. Please try again.";
    }
  }
});

/*
|--------------------------------------------------------------------------
| Post-property modal
|--------------------------------------------------------------------------
*/

function openPostModal() {
  const modal = document.getElementById("modal");

  if (!modal) return;

  modal.classList.add("open");
  document.body.style.overflow = "hidden";
}

function closePostModal() {
  const modal = document.getElementById("modal");

  if (!modal) return;

  modal.classList.remove("open");
  document.body.style.overflow = "";
}

/*
|--------------------------------------------------------------------------
| FAQ modal
|--------------------------------------------------------------------------
*/

function openFaqModal() {
  const modal = document.getElementById("faqModal");

  if (!modal) return;

  modal.classList.add("open");
  document.body.style.overflow = "hidden";
}

function closeFaqModal() {
  const modal = document.getElementById("faqModal");

  if (!modal) return;

  modal.classList.remove("open");
  document.body.style.overflow = "";
}

/*
|--------------------------------------------------------------------------
| Submit property listing
|--------------------------------------------------------------------------
*/

async function submitListing(event) {
  event.preventDefault();

  const form = event.target;

  if (!form) {
    alert("Listing form could not be found.");
    return;
  }

  const data = new FormData(form);
  const token = localStorage.getItem("nyumbalink_token");

  if (!token) {
    alert("Please sign in as a landlord before posting a property.");
    window.location.href = "landlord-login.html";
    return;
  }

  const title = data.get("title")?.trim();
  const propertyType = data.get("property_type")?.trim();
  const purpose = data.get("purpose")?.trim();
  const countyValue = data.get("county")?.trim();
  const townValue = data.get("town")?.trim();
  const priceValue = Number(data.get("price"));
  const description = data.get("description")?.trim() || null;
  const imageUrl = data.get("image_url")?.trim() || null;

  /*
  |--------------------------------------------------------------------------
  | Client-side validation
  |--------------------------------------------------------------------------
  */

  if (!title || !propertyType || !purpose || !countyValue || !townValue) {
    alert("Please complete all required property fields.");
    return;
  }

  if (!["rent", "land"].includes(purpose)) {
    alert("Purpose must be either Rent or Buy land.");
    return;
  }

  if (!Number.isFinite(priceValue) || priceValue <= 0) {
    alert("Please enter a valid price greater than zero.");
    return;
  }

  const submitButton = form.querySelector('button[type="submit"]');
  const originalButtonText = submitButton
    ? submitButton.textContent
    : "Publish property";

  try {
    if (submitButton) {
      submitButton.disabled = true;
      submitButton.textContent = "Publishing...";
    }

    const payload = {
      title,
      property_type: propertyType,
      purpose,
      county: countyValue,
      town: townValue,
      price: priceValue,
      description,
      image_url: imageUrl
    };

    console.log("Submitting property:", payload);

    const response = await fetch(`${API_BASE}/api/properties`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": `Bearer ${token}`
      },
      body: JSON.stringify(payload)
    });

    let result;

    try {
      result = await response.json();
    } catch {
      throw new Error(
        `The server returned an invalid response. HTTP status: ${response.status}`
      );
    }

    if (!response.ok) {
      if (response.status === 401) {
        localStorage.removeItem("nyumbalink_token");
        localStorage.removeItem("nyumbalink_user");

        throw new Error(
          "Your session has expired. Please sign in again."
        );
      }

      const errorMessage = Array.isArray(result.detail)
        ? result.detail.map(error => error.msg).join(", ")
        : result.detail || "Could not create listing.";

      throw new Error(errorMessage);
    }

    alert("Property published successfully.");

    form.reset();
    closePostModal();

    await loadProperties();
  } catch (error) {
    console.error("Submit listing error:", error);
    alert(error.message || "Could not create listing.");
  } finally {
    if (submitButton) {
      submitButton.disabled = false;
      submitButton.textContent = originalButtonText;
    }
  }
}

/*
|--------------------------------------------------------------------------
| Browse and area filters
|--------------------------------------------------------------------------
*/

function showAll() {
  document
    .querySelector(".latest")
    ?.scrollIntoView({ behavior: "smooth" });

  loadProperties().catch(error => {
    console.error("Could not load all properties:", error);
  });
}

function filterArea(area) {
  document
    .querySelector(".latest")
    ?.scrollIntoView({ behavior: "smooth" });

  loadProperties({ town: area }).catch(error => {
    console.error("Could not filter by area:", error);
  });
}

/*
|--------------------------------------------------------------------------
| HTML escaping
|--------------------------------------------------------------------------
*/

function escapeHtml(value = "") {
  return String(value)
    .replaceAll("&", "&amp;")
    .replaceAll("<", "&lt;")
    .replaceAll(">", "&gt;")
    .replaceAll('"', "&quot;")
    .replaceAll("'", "&#039;");
}

/*
|--------------------------------------------------------------------------
| Modal interactions
|--------------------------------------------------------------------------
*/

document.getElementById("modal")?.addEventListener("click", event => {
  if (event.target.id === "modal") {
    closePostModal();
  }
});

document.getElementById("faqModal")?.addEventListener("click", event => {
  if (event.target.id === "faqModal") {
    closeFaqModal();
  }
});

document.addEventListener("keydown", event => {
  if (event.key === "Escape") {
    closePostModal();
    closeFaqModal();
  }
});

/*
|--------------------------------------------------------------------------
| Initial property loading
|--------------------------------------------------------------------------
*/

window.addEventListener("DOMContentLoaded", () => {
  loadProperties().catch(error => {
    console.error("Initial property loading failed:", error);
  });
});