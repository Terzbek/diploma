document.addEventListener("DOMContentLoaded", function () {
    const cityButton = document.getElementById("city-button");
    const cityDropdown = document.getElementById("city-dropdown");
    const cityItems = cityDropdown.querySelectorAll("li");

    cityButton.addEventListener("click", function () {
        const isExpanded = cityDropdown.classList.contains("show");
        cityDropdown.classList.toggle("show");
        cityButton.classList.toggle("active");
        cityButton.setAttribute("aria-expanded", !isExpanded);
    });

    cityItems.forEach(item => {
        item.addEventListener("click", function () {
            cityButton.textContent = item.dataset.city;
            cityItems.forEach(i => i.classList.remove("selected"));
            item.classList.add("selected");
            cityDropdown.classList.remove("show");
            cityButton.classList.remove("active");
            cityButton.setAttribute("aria-expanded", "false");
        });
    });

    document.addEventListener("click", function (event) {
        if (!cityButton.contains(event.target) && !cityDropdown.contains(event.target)) {
            cityDropdown.classList.remove("show");
            cityButton.classList.remove("active");
            cityButton.setAttribute("aria-expanded", "false");
        }
    });
});