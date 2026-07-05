---
type: Jurisdiction
title: "Schuylkill County, PA"
classification: county
fips: "42107"
state: "PA"
demographics:
  population: 143558
  population_under_18: 28557
  population_18_64: 84775
  population_65_plus: 30226
  median_household_income: 68313
  poverty_rate: 12.75
  homeownership_rate: 76.09
  unemployment_rate: 5.63
  median_home_value: 153000
  gini_index: 0.43
  vacancy_rate: 13.83
  race_white: 125928
  race_black: 4118
  race_asian: 697
  race_native: 104
  hispanic: 11184
  bachelors_plus: 28107
districts:
  - to: "us/states/pa/districts/09"
    rel: in-district
    area_weight: 0.9993
  - to: "us/states/pa/districts/senate/29"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/pa/districts/house/107"
    rel: in-district
    area_weight: 0.3195
  - to: "us/states/pa/districts/house/124"
    rel: in-district
    area_weight: 0.309
  - to: "us/states/pa/districts/house/123"
    rel: in-district
    area_weight: 0.2372
  - to: "us/states/pa/districts/house/116"
    rel: in-district
    area_weight: 0.1342
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, pa]
timestamp: "2026-07-03"
---

# Schuylkill County, PA

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 143558 |
| Under 18 | 28557 |
| 18–64 | 84775 |
| 65+ | 30226 |
| Median household income | 68313 |
| Poverty rate | 12.75 |
| Homeownership rate | 76.09 |
| Unemployment rate | 5.63 |
| Median home value | 153000 |
| Gini index | 0.43 |
| Vacancy rate | 13.83 |
| White | 125928 |
| Black | 4118 |
| Asian | 697 |
| Native | 104 |
| Hispanic/Latino | 11184 |
| Bachelor's or higher | 28107 |

## Districts

- [PA-09](/us/states/pa/districts/09.md) — 100% (congressional)
- [PA Senate District 29](/us/states/pa/districts/senate/29.md) — 100% (state senate)
- [PA House District 107](/us/states/pa/districts/house/107.md) — 32% (state house)
- [PA House District 124](/us/states/pa/districts/house/124.md) — 31% (state house)
- [PA House District 123](/us/states/pa/districts/house/123.md) — 24% (state house)
- [PA House District 116](/us/states/pa/districts/house/116.md) — 13% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
