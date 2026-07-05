---
type: Jurisdiction
title: "Christian County, IL"
classification: county
fips: "17021"
state: "IL"
demographics:
  population: 33538
  population_under_18: 6482
  population_18_64: 20259
  population_65_plus: 6797
  median_household_income: 62611
  poverty_rate: 10.19
  homeownership_rate: 75.2
  unemployment_rate: 4.57
  median_home_value: 115500
  gini_index: 0.4435
  vacancy_rate: 10.52
  race_white: 30883
  race_black: 734
  race_asian: 247
  race_native: 21
  hispanic: 1112
  bachelors_plus: 5432
districts:
  - to: "us/states/il/districts/15"
    rel: in-district
    area_weight: 0.9987
  - to: "us/states/il/districts/senate/54"
    rel: in-district
    area_weight: 0.6844
  - to: "us/states/il/districts/senate/48"
    rel: in-district
    area_weight: 0.3156
  - to: "us/states/il/districts/house/107"
    rel: in-district
    area_weight: 0.4942
  - to: "us/states/il/districts/house/95"
    rel: in-district
    area_weight: 0.1959
  - to: "us/states/il/districts/house/108"
    rel: in-district
    area_weight: 0.1902
  - to: "us/states/il/districts/house/96"
    rel: in-district
    area_weight: 0.1197
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, il]
timestamp: "2026-07-03"
---

# Christian County, IL

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 33538 |
| Under 18 | 6482 |
| 18–64 | 20259 |
| 65+ | 6797 |
| Median household income | 62611 |
| Poverty rate | 10.19 |
| Homeownership rate | 75.2 |
| Unemployment rate | 4.57 |
| Median home value | 115500 |
| Gini index | 0.4435 |
| Vacancy rate | 10.52 |
| White | 30883 |
| Black | 734 |
| Asian | 247 |
| Native | 21 |
| Hispanic/Latino | 1112 |
| Bachelor's or higher | 5432 |

## Districts

- [IL-15](/us/states/il/districts/15.md) — 100% (congressional)
- [IL Senate District 54](/us/states/il/districts/senate/54.md) — 68% (state senate)
- [IL Senate District 48](/us/states/il/districts/senate/48.md) — 32% (state senate)
- [IL House District 107](/us/states/il/districts/house/107.md) — 49% (state house)
- [IL House District 95](/us/states/il/districts/house/95.md) — 20% (state house)
- [IL House District 108](/us/states/il/districts/house/108.md) — 19% (state house)
- [IL House District 96](/us/states/il/districts/house/96.md) — 12% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
