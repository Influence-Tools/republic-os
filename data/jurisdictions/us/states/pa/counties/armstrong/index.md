---
type: Jurisdiction
title: "Armstrong County, PA"
classification: county
fips: "42005"
state: "PA"
demographics:
  population: 64622
  population_under_18: 12227
  population_18_64: 36874
  population_65_plus: 15521
  median_household_income: 65008
  poverty_rate: 11.79
  homeownership_rate: 78.82
  unemployment_rate: 4.33
  median_home_value: 157300
  gini_index: 0.4293
  vacancy_rate: 12.74
  race_white: 61501
  race_black: 608
  race_asian: 228
  race_native: 12
  hispanic: 605
  bachelors_plus: 12329
districts:
  - to: "us/states/pa/districts/15"
    rel: in-district
    area_weight: 0.9986
  - to: "us/states/pa/districts/senate/41"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/pa/districts/house/63"
    rel: in-district
    area_weight: 0.6387
  - to: "us/states/pa/districts/house/60"
    rel: in-district
    area_weight: 0.3611
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, pa]
timestamp: "2026-07-03"
---

# Armstrong County, PA

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 64622 |
| Under 18 | 12227 |
| 18–64 | 36874 |
| 65+ | 15521 |
| Median household income | 65008 |
| Poverty rate | 11.79 |
| Homeownership rate | 78.82 |
| Unemployment rate | 4.33 |
| Median home value | 157300 |
| Gini index | 0.4293 |
| Vacancy rate | 12.74 |
| White | 61501 |
| Black | 608 |
| Asian | 228 |
| Native | 12 |
| Hispanic/Latino | 605 |
| Bachelor's or higher | 12329 |

## Districts

- [PA-15](/us/states/pa/districts/15.md) — 100% (congressional)
- [PA Senate District 41](/us/states/pa/districts/senate/41.md) — 100% (state senate)
- [PA House District 63](/us/states/pa/districts/house/63.md) — 64% (state house)
- [PA House District 60](/us/states/pa/districts/house/60.md) — 36% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
