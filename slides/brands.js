// ABOUTME: Shared brand profiles for public keynote-style decks on the blog.
// ABOUTME: Keeps deck tokens and typography consistent across slide bundles.

window.KEYNOTE_BRANDS = {
  forgeworks: {
    label: "AI Forge",
    tokens: {
      "brand-ink": "#231a14",
      "brand-ink-soft": "#4f4035",
      "brand-paper": "#f8f2e8",
      "brand-paper-deep": "#efe3d4",
      "brand-accent": "#d36e37",
      "brand-accent-strong": "#b85724",
      "brand-sage": "#8b9a74",
      "brand-slate": "#6b5a4d",
      "brand-line": "rgba(35, 26, 20, 0.12)",
      "brand-glow": "rgba(211, 110, 55, 0.28)"
    },
    fonts: {
      display: "\"Fraunces\", \"Iowan Old Style\", serif",
      body: "\"Space Grotesk\", \"Avenir Next\", sans-serif"
    },
    fontLabel: "Display: Fraunces. Body: Space Grotesk.",
    mediaPromptPrefix: "warm parchment editorial presentation, ember accents, thoughtful systems diagrams, confident whitespace",
    defaultDeckType: "narrative"
  }
};

window.KEYNOTE_DEFAULT_ENTITY = "forgeworks";
