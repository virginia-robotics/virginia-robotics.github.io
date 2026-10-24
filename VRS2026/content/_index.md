---
# Home-page content for VRS 2026. All event-specific copy lives here; the `vrs`
# theme only provides layout/structure. Edit freely — Markdown/HTML is allowed
# in the About paragraphs.
title: "Virginia Robotics Symposium 2026"

# Hero headline (the date / host / location beneath it come from hugo.toml params)
heroTitle: "Virginia Robotics Symposium"

# About section — one entry per paragraph
about:
  - "The Virginia Robotics Symposium (VRS) brings together robotics researchers from across the Commonwealth for a one-day event of research talks, poster presentations, and social activities — building connections and disseminating ideas across institutions."
  # - "With support from our sponsors, we also plan to feature industry presentations, showcasing robotics innovation from companies across the region."

# Registration card (shows note + cta when registerURL is set, else `pending`)
registration:
  note: "Attendance is free."
  cta: "Click here to register!"
  pending: "Registration will open soon."

# Poster card (shows note + cta when posterURL is set, else `pending`; HTML allowed
# in `pending`). `closed` replaces both while postersPage is false in hugo.toml.
poster:
  closed: "Thank you to everyone who presented a poster at VRS 2026!"
  note: "Students are encouraged to present research posters."
  cta: "Click here to sign up for a poster presentation!"
  pending: 'Posters are at capacity. Check out our posters <a href="/posters/" class="font-semibold text-accent hover:underline">here</a>.'

# Sponsors call-to-action (the linked "Click here" goes to the sponsorMenu PDF)
sponsorsCta: "Interested in sponsoring and showcasing your products?"

# Program section
programIntro: "VRS is a one-day event with keynote talks, a panel, poster presentations, and social activities."
speakersHeading: "Keynote Speakers"
speakersPending: "Speakers to be announced."

# Schedule section
schedulePending: "Detailed schedule coming soon."

# Live Q&A banner (shown above the schedule). Rendered only while the visitor's
# local date is between `start` and `end` (inclusive, YYYY-MM-DD); builds made
# after `end` omit it entirely. Remove `url` to disable.
slido:
  url: "https://app.sli.do/event/dotApbGykjyvp7rgraubPp"
  start: "2026-10-23"
  end: "2026-10-23"
  heading: "Have a question for a speaker or the panel?"
  text: "Submit and upvote questions live on Slido throughout the day."
  cta: "Ask a question on Slido"

# Venue section — one entry per paragraph
venueIntro:
  - "The 2026 symposium will be hosted at the Virginia Tech Graduate Life Center (GLC) Multipurpose Room at 155 Otey St NW, Blacksburg, VA 24061."
  - 'Parking is not provided by the symposium and participants are responsible for their own parking. We recommend <a href="https://parking.vt.edu/parking/parkmobile.html" target="_blank" rel="noopener" class="font-semibold text-accent hover:underline">ParkMobile</a> for parking. Additionally, the Kent Square and North End parking garages, shown below, are both a short walk from the GLC.'
venuePending: "Venue details to be announced."
# Parking maps shown next to the venue map. `embed` is a keyless Google Maps
# embed URL (https://maps.google.com/maps?q=<place>&output=embed); `link` is
# what the "Open in Google Maps" caption points to.
parking:
  - name: "Kent Square Parking Garage"
    embed: "https://maps.google.com/maps?q=Kent+Square+Parking+Garage,+Blacksburg,+VA&z=16&output=embed"
    link: "https://share.google/UWcXDID20umNeILz9"
  - name: "North End Parking Garage"
    embed: "https://maps.google.com/maps?q=North+End+Parking+Garage,+Blacksburg,+VA&z=16&output=embed"
    link: "https://share.google/NMaOrrtNJb1JKJQh2"

# Contact section
contactIntro: "For more information, please reach out to the organizers below."
---
