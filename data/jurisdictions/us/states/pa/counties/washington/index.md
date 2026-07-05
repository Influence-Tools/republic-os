---
type: Jurisdiction
title: "Washington County, PA"
classification: county
fips: "42125"
state: "PA"
demographics:
  population: 210042
  population_under_18: 41070
  population_18_64: 122805
  population_65_plus: 46167
  median_household_income: 78958
  poverty_rate: 9.61
  homeownership_rate: 76.1
  unemployment_rate: 4.78
  median_home_value: 228500
  gini_index: 0.4539
  vacancy_rate: 9.62
  race_white: 189198
  race_black: 6683
  race_asian: 2711
  race_native: 178
  hispanic: 4335
  bachelors_plus: 69127
districts:
  - to: "us/states/pa/districts/14"
    rel: in-district
    area_weight: 0.9993
  - to: "us/states/pa/districts/senate/46"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/pa/districts/house/48"
    rel: in-district
    area_weight: 0.3615
  - to: "us/states/pa/districts/house/15"
    rel: in-district
    area_weight: 0.3377
  - to: "us/states/pa/districts/house/50"
    rel: in-district
    area_weight: 0.1415
  - to: "us/states/pa/districts/house/46"
    rel: in-district
    area_weight: 0.1088
  - to: "us/states/pa/districts/house/39"
    rel: in-district
    area_weight: 0.0275
  - to: "us/states/pa/districts/house/40"
    rel: in-district
    area_weight: 0.0229
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, pa]
timestamp: "2026-07-03"
---

# Washington County, PA

County jurisdiction — 2 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 210042 |
| Under 18 | 41070 |
| 18–64 | 122805 |
| 65+ | 46167 |
| Median household income | 78958 |
| Poverty rate | 9.61 |
| Homeownership rate | 76.1 |
| Unemployment rate | 4.78 |
| Median home value | 228500 |
| Gini index | 0.4539 |
| Vacancy rate | 9.62 |
| White | 189198 |
| Black | 6683 |
| Asian | 2711 |
| Native | 178 |
| Hispanic/Latino | 4335 |
| Bachelor's or higher | 69127 |

## Districts

- [PA-14](/us/states/pa/districts/14.md) — 100% (congressional)
- [PA Senate District 46](/us/states/pa/districts/senate/46.md) — 100% (state senate)
- [PA House District 48](/us/states/pa/districts/house/48.md) — 36% (state house)
- [PA House District 15](/us/states/pa/districts/house/15.md) — 34% (state house)
- [PA House District 50](/us/states/pa/districts/house/50.md) — 14% (state house)
- [PA House District 46](/us/states/pa/districts/house/46.md) — 11% (state house)
- [PA House District 39](/us/states/pa/districts/house/39.md) — 3% (state house)
- [PA House District 40](/us/states/pa/districts/house/40.md) — 2% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
