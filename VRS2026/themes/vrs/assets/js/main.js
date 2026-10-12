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

// Poster search (/posters/): filter rows by title, presenter, or PI.
// Every whitespace-separated term must appear somewhere in the row.
const search = document.getElementById("poster-search");
const rows = Array.from(document.querySelectorAll(".poster-row"));
if (search && rows.length) {
  const empty = document.getElementById("poster-empty");
  const count = document.getElementById("poster-count");
  const apply = () => {
    const terms = search.value.toLowerCase().split(/\s+/).filter(Boolean);
    let shown = 0;
    rows.forEach((row) => {
      const hay = row.dataset.search;
      const hit = terms.every((t) => hay.includes(t));
      row.classList.toggle("hidden", !hit);
      if (hit) shown++;
    });
    if (empty) empty.classList.toggle("hidden", shown > 0);
    if (count) count.textContent = terms.length ? `Showing ${shown} of ${rows.length} posters` : `${rows.length} posters`;
  };
  search.addEventListener("input", apply);
  apply();
}
