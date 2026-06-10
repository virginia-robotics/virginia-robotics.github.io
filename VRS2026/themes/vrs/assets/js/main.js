// Mobile menu toggle
const toggle = document.getElementById("nav-toggle");
const mobile = document.getElementById("nav-mobile");
if (toggle && mobile) {
  toggle.addEventListener("click", () => {
    const open = mobile.classList.toggle("hidden") === false;
    toggle.setAttribute("aria-expanded", String(open));
  });
  // Close the menu after tapping a link
  mobile.querySelectorAll("a").forEach((a) =>
    a.addEventListener("click", () => {
      mobile.classList.add("hidden");
      toggle.setAttribute("aria-expanded", "false");
    })
  );
}
