"use strict";
const form = document.querySelector("#enquiry-form");
const result = document.querySelector("#enquiry-result");
const status = document.querySelector("#result-status");
const output = document.querySelector("#enquiry-text");
function clearResult() {
  result.hidden = true;
}
form.addEventListener("input", clearResult);
form.addEventListener("change", clearResult);
document.querySelectorAll("[data-size]").forEach((link) =>
  link.addEventListener("click", () => {
    document.querySelector("#quantity").value = link.dataset.size;
    clearResult();
  }),
);
form.addEventListener("submit", (event) => {
  event.preventDefault();
  const data = new FormData(form);
  const value = (key) => String(data.get(key) || "").trim();
  for (const id of ["name", "area"]) {
    const field = document.getElementById(id);
    field.setCustomValidity(value(id) ? "" : "Please enter this detail.");
    if (!field.reportValidity()) {
      field.addEventListener("input", () => field.setCustomValidity(""), {
        once: true,
      });
      return;
    }
  }
  output.value = `Asmo Fresh Milk delivery enquiry\n\nName: ${value("name")}\nMobile: ${value("phone")}\nLocality: ${value("area")}\nBottle size: ${value("quantity")}\nDelivery preference: ${value("schedule")}\n\nPlease confirm pricing and availability for my locality.`;
  document.querySelector("#email-enquiry").href =
    `mailto:aaashokreddy@gmail.com?subject=${encodeURIComponent("Asmo Fresh Milk delivery enquiry")}&body=${encodeURIComponent(output.value)}`;
  status.textContent =
    "Your enquiry is ready. Choose how you’d like to send it:";
  result.hidden = false;
  document.querySelector("#email-enquiry").focus({ preventScroll: true });
  result.scrollIntoView({
    block: "nearest",
    behavior: matchMedia("(prefers-reduced-motion: reduce)").matches
      ? "instant"
      : "smooth",
  });
});
document.querySelector("#copy-enquiry").addEventListener("click", async () => {
  try {
    await navigator.clipboard.writeText(output.value);
    status.textContent =
      "Copied. Paste your enquiry into an email to aaashokreddy@gmail.com.";
  } catch {
    output.focus();
    output.select();
    status.textContent =
      "Select and copy the enquiry below, then email it to aaashokreddy@gmail.com.";
  }
});
if ("IntersectionObserver" in window) {
  const floating = document.querySelector(".mobile-enquire");
  const visible = new Set();
  const observer = new IntersectionObserver((entries) => {
    entries.forEach((entry) =>
      entry.isIntersecting
        ? visible.add(entry.target.id)
        : visible.delete(entry.target.id),
    );
    floating.classList.toggle("is-hidden", visible.size > 0);
  });
  observer.observe(document.querySelector("#home"));
  observer.observe(document.querySelector("#order"));
  if (!matchMedia("(prefers-reduced-motion: reduce)").matches) {
    const reveal = new IntersectionObserver(
      (entries) => {
        entries.forEach((entry) => {
          if (!entry.isIntersecting) return;
          if (entry.target.animate)
            entry.target.animate(
              [
                { opacity: 0.45, transform: "translateY(18px)" },
                { opacity: 1, transform: "translateY(0)" },
              ],
              { duration: 600, easing: "ease-out" },
            );
          reveal.unobserve(entry.target);
        });
      },
      { threshold: 0.1 },
    );
    document
      .querySelectorAll(
        ".section-heading,.product,.story-copy,.delivery-copy,.faq-layout,.order-copy",
      )
      .forEach((element) => reveal.observe(element));
  }
}

document.querySelector("#prepare-enquiry").disabled = false;
