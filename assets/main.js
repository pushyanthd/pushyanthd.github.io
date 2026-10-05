"use strict";
document.getElementById("year").textContent = new Date().getFullYear();
if ("IntersectionObserver" in window) {
  const links = Array.from(document.querySelectorAll("nav a"));
  const observer = new IntersectionObserver((entries) => {
    for (const entry of entries) {
      if (entry.isIntersecting) {
        for (const link of links) {
          if (link.hash === "#" + entry.target.id) link.setAttribute("aria-current", "location");
          else link.removeAttribute("aria-current");
        }
      }
    }
  }, { rootMargin: "-20% 0px -60% 0px" });
  for (const link of links) {
    const section = document.querySelector(link.hash);
    if (section) observer.observe(section);
  }
}
