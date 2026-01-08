# Design System Documentation

## Overview

This document describes the restrained, production-ready design system implemented for the Django personal website. The redesign eliminates "vibe-coded" aesthetics in favor of credible, technical presentation appropriate for senior engineers, researchers, and hiring managers.

---

## 1. Django-Compatible Styling Strategy

### Approach

The styling system works entirely within Django's template structure:
- All changes are CSS-only; no template restructuring required
- Existing Django blocks (`{% block content %}`, etc.) remain unchanged
- CSS classes map directly to existing HTML structure
- No JavaScript dependencies; all interactions are CSS-based

### Implementation Pattern

```css
/* Classes apply to existing Django template markup */
.container { /* Used in base.html */ }
.card { /* Used in project templates */ }
.hero { /* Used in home.html */ }
```

**Key Principle:** The CSS assumes the existing HTML structure and enhances it without requiring template changes.

### Template Hierarchy Respect

- `base.html` provides global structure (header, footer, container)
- Child templates extend base and fill `{% block content %}`
- CSS classes work at any template level
- No CSS depends on JavaScript or dynamic content

---

## 2. Visual Design System

### Color Palette

**Neutral Base:**
- `--color-bg: #ffffff` - Primary background
- `--color-surface: #fafafa` - Card/secondary backgrounds
- `--color-border: #e5e5e5` - Borders and dividers
- `--color-border-subtle: #f0f0f0` - Light borders

**Text Hierarchy:**
- `--color-text: #1a1a1a` - Primary text (near-black, not pure black)
- `--color-text-secondary: #666666` - Body/secondary text
- `--color-text-muted: #999999` - Captions, metadata

**Accent (Minimal Use):**
- `--color-accent: #0066cc` - Links and active states only
- `--color-accent-hover: #0052a3` - Link hover state

**Design Decision:** Single accent color (blue) used sparingly. No gradients, no warm tones, no marketing colors.

### Typography

**Font Stack:**
```css
--font-sans: -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Roboto', 
             'Helvetica Neue', Arial, sans-serif;
```

**System fonts only** - no web font loading, faster performance, native feel.

**Type Scale:**
- `h1`: `clamp(1.875rem, 4vw, 2.5rem)` - Responsive, max 40px
- `h2`: `1.5rem` (24px)
- `h3`: `1.125rem` (18px)
- Body: `1rem` (16px)
- Small: `0.875rem` (14px)
- Caption: `0.75rem` (12px)

**Line Heights:**
- Body: `1.6` - Optimal for reading
- Headings: `1.3` - Tighter, for impact

**Letter Spacing:**
- Headings: `-0.02em` to `-0.01em` - Slight tightening
- Uppercase labels: `0.05em` - Improved readability

### Spacing Scale

CSS custom properties provide consistent spacing:
```css
--space-xs: 0.25rem;   /* 4px */
--space-sm: 0.5rem;    /* 8px */
--space-md: 1rem;      /* 16px */
--space-lg: 1.5rem;    /* 24px */
--space-xl: 2rem;      /* 32px */
--space-2xl: 3rem;     /* 48px */
--space-3xl: 4rem;     /* 64px */
```

**Usage:** Applied consistently across margins, padding, gaps.

### Layout Constraints

**Max Widths:**
- Content/reading width: `65ch` (optimal line length)
- Page width: `1200px` (prevents over-wide layouts)

**Container Pattern:**
```css
.container {
  max-width: var(--max-width-page);
  margin: 0 auto;
  padding: 0 var(--space-lg);
}
```

**Responsive:** Padding adjusts on mobile; max-width remains consistent.

---

## 3. Layout Discipline Within Existing Structure

### Content Breathing

**Vertical Rhythm:**
- Sections: `var(--space-3xl)` (64px) spacing
- Cards: `var(--space-xl)` (32px) padding
- Paragraphs: `var(--space-md)` (16px) margin-bottom

**Principle:** Generous whitespace without feeling empty. Content has room to breathe without decorative filler.

### Visual Hierarchy

**Methods:**
1. **Font size and weight** - Clear distinction between heading levels
2. **Color contrast** - Primary text vs. secondary text creates hierarchy
3. **Spacing** - Larger margins above sections signal importance
4. **Border usage** - Minimal borders only where separation is needed

**De-emphasis of Non-Critical Elements:**
- Kickers/labels: `0.75rem`, uppercase, muted color
- Metadata: `--color-text-muted`
- Footer: Light background, muted text, minimal visual weight

### Grid Systems

**Existing Grid Classes:**
- `.cols-2`: Two-column layout (used in about, contact, CV)
- `.cols-3`: Three-column layout (projects index)
- `.values-grid`: Auto-fit grid for value cards (min 280px per item)

**Responsive:** All grids collapse to single column below 768px breakpoint.

---

## 4. Copy Refinement

### Improved Headline Examples

**Before:** "Case studies and proof of work."
**After:** "Projects"

**Rationale:** Direct and clear. "Case studies and proof of work" is explanatory text, not a headline.

**Before:** "What drives my work"
**After:** "Principles"

**Rationale:** Removes vague phrasing. "Principles" is concrete and professional.

### Improved About Paragraph

**Before:** "Graduate with a BSc. in Computer Science & Mathematics and an MSc in Quantum Information Science. I focus on quantitative modelling and software tooling. Interested in energy markets and trading, where disciplined analytics, modelling, and reliable systems uncover signals and manage risk."

**After:** "Software engineer with a background in quantitative modeling and data systems. BSc in Computer Science & Mathematics, MSc in Quantum Information Science. Focus on backend services, analytical tooling, and production systems."

**Rationale:**
- Lead with role/identity, not degree status
- Remove "Aspiring" qualifier
- Remove specific industry interest (too narrow for homepage)
- Focus on technical capabilities, not aspirations

### Copy to Remove or Simplify

**Removed:**
- "Aspiring Data Scientist & Quantitative developer" kicker - too positioning-focused
- "What drives my work" - vague, marketing language
- "Get in touch" - generic CTA language (replaced with "Email")
- "Best for direct inquiries" - unnecessary explanation
- "Curious, analytical, detail-oriented" - redundant adjectives

**Simplified:**
- Section headers reduced from full sentences to single words
- Removed emoji icons entirely
- Removed explanatory sub-headers that state the obvious

---

## 5. Interaction Philosophy

### What Has Hover States

**Links:**
- Text underline on hover
- Color shift from accent to accent-hover
- Fast transition (`0.15s ease`)

**Buttons:**
- Background color inversion (text becomes background, background becomes text)
- Border color change
- No transform/scale effects

**Cards (when linked):**
- Border color darkens on hover
- No lift/transform effects
- Subtle visual feedback only

### What Does NOT Animate

- **Page load:** No fade-in animations
- **Scroll:** No parallax or scroll-triggered animations
- **Cards:** No hover transforms, no shadow increases
- **Headers:** No blur effects, no backdrop filters
- **Icons:** Removed entirely

### Quality Through Restraint

**Design Principles:**
1. Fast, predictable transitions (150ms max)
2. Hover states provide feedback without distraction
3. No animations that draw attention away from content
4. Interactions feel immediate and reliable

**Accessibility:**
- `prefers-reduced-motion` respected - all animations disabled
- Focus states visible with clear outline
- Color contrast meets WCAG AA standards

---

## 6. Anti-Patterns Checklist

### Things That Make Sites Feel AI-Generated

**Avoid:**
- Generic value propositions ("passionate about", "crafting solutions")
- Over-explanation of obvious elements
- Redundant adjectives and qualifiers
- Emoji usage in professional contexts
- Marketing language disguised as technical content

### Things That Make Sites Feel Template-Derived

**Avoid:**
- Gradient backgrounds
- Glassmorphism/blur effects
- Generic "hero" sections with large slogans
- Card hover effects with transforms and shadows
- Warm accent colors (oranges, yellows, purples)
- Multiple accent colors
- Decorative icons (especially emoji)

### Things That Make Sites Feel Overdesigned

**Avoid:**
- Page load animations
- Scroll-triggered animations
- Hover transforms on every element
- Multiple font families
- Complex color palettes
- Decorative backgrounds or patterns
- Unnecessary visual flourishes

### Django-Specific Anti-Patterns

**When Restyling Django Sites:**
1. **Don't** restructure templates to fit CSS - work with existing structure
2. **Don't** add JavaScript just for styling - use CSS-only solutions
3. **Don't** break template inheritance - respect block structure
4. **Don't** create new page types - work within existing views
5. **Don't** add build steps unless necessary - Django's static files work fine

---

## 7. Final Sanity Check

### Evaluation Criteria

**✓ JavaScript Independence**
- Site looks correct with JavaScript disabled
- All interactions are CSS-based
- No JavaScript-dependent styling

**✓ Credibility Assessment (20-30 second scan)**
- Does the design suggest technical competence?
- Is the presentation appropriate for senior engineers?
- Would a researcher trust the content?
- Is there unnecessary decoration?

**✓ Content-First Design**
- Does design get out of the way?
- Is typography readable and appropriate?
- Is hierarchy clear without decoration?
- Can users quickly find information?

**✓ Performance**
- No web fonts loaded (system fonts only)
- Minimal CSS (no large frameworks)
- No JavaScript for styling
- Fast initial render

**✓ Accessibility**
- Focus states visible
- Color contrast adequate
- Reduced motion respected
- Semantic HTML preserved

### Success Metrics

**Positive Indicators:**
- Content is immediately scannable
- No visual elements distract from information
- Typography supports quick reading
- Professional appearance without feeling corporate
- Design feels intentional, not templated

**Red Flags:**
- Requires more than 2-3 seconds to understand purpose
- Decorative elements draw attention
- Copy sounds like marketing material
- Visual style feels generic or trendy
- Interactions feel unnecessary or slow

---

## Implementation Notes

### Files Modified

1. **`personal_site/static/css/app.css`** - Complete redesign
2. **`personal_site/templates/base.html`** - Removed Poppins font import
3. **`personal_site/templates/home.html`** - Updated copy
4. **`personal_site/templates/about.html`** - Updated copy
5. **`personal_site/templates/contact.html`** - Simplified layout and copy
6. **`personal_site/templates/projects/index.html`** - Simplified headline
7. **`personal_site/templates/cv.html`** - Updated copy and removed gradient class

### No Changes Required

- URL routing (`urls.py`)
- Views (`views.py`)
- Models (if any)
- Template inheritance structure
- Static file serving

### Testing Checklist

- [ ] All pages render correctly
- [ ] Navigation works as expected
- [ ] Links have proper hover states
- [ ] Responsive breakpoints work
- [ ] No console errors
- [ ] CSS validates
- [ ] Reduced motion preference respected

---

## Design Philosophy Summary

**Core Principle:** The design should signal technical competence and attention to detail without drawing attention to itself.

**Method:**
1. Remove all decorative elements
2. Use system fonts for performance and familiarity
3. Apply minimal color palette
4. Prioritize typography and spacing
5. Simplify interactions
6. Edit copy to be direct and specific

**Result:** A website that feels designed by someone technical, not marketed by someone else. Credible, restrained, and focused on signal over decoration.

