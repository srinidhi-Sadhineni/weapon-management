const API_URL = "";

async function loadEquipment() {
    const equipmentList = document.getElementById("equipment-list");
    const total = document.getElementById("total");

    try {
        const response = await fetch("/api/weapons");

        if (!response.ok) {
            throw new Error("Failed to load equipment");
        }

        const data = await response.json();

        total.textContent = data.length;

        if (data.length === 0) {
            equipmentList.textContent = "No equipment records found.";
            return;
        }

        equipmentList.innerHTML = "";

        data.forEach(item => {
            const card = document.createElement("div");
            card.className = "card";

            const name = document.createElement("h3");
            name.textContent = item.equipment_name;

            const category = document.createElement("p");
            category.textContent = "Category: " + item.category_name;

            const quantity = document.createElement("p");
            quantity.textContent = "Quantity: " + item.quantity;

            const status = document.createElement("p");
            status.textContent = "Status: " + item.status;

            card.append(name, category, quantity, status);
            equipmentList.appendChild(card);
        });

    } catch (error) {
        total.textContent = "Unavailable";
        equipmentList.textContent =
            "Unable to connect to backend. Please check the API server.";
        console.error(error);
    }
}

loadEquipment();