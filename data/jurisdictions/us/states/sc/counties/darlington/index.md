---
type: Jurisdiction
title: "Darlington County, SC"
classification: county
fips: "45031"
state: "SC"
demographics:
  population: 62558
  population_under_18: 13894
  population_18_64: 36240
  population_65_plus: 12424
  median_household_income: 48581
  poverty_rate: 21.09
  homeownership_rate: 70.91
  unemployment_rate: 6.65
  median_home_value: 158200
  gini_index: 0.5234
  vacancy_rate: 14.12
  race_white: 33788
  race_black: 25447
  race_asian: 364
  race_native: 184
  hispanic: 1552
  bachelors_plus: 12052
districts:
  - to: "us/states/sc/districts/07"
    rel: in-district
    area_weight: 0.9981
  - to: "us/states/sc/districts/senate/29"
    rel: in-district
    area_weight: 0.9751
  - to: "us/states/sc/districts/senate/30"
    rel: in-district
    area_weight: 0.0247
  - to: "us/states/sc/districts/house/62"
    rel: in-district
    area_weight: 0.4302
  - to: "us/states/sc/districts/house/54"
    rel: in-district
    area_weight: 0.237
  - to: "us/states/sc/districts/house/65"
    rel: in-district
    area_weight: 0.1994
  - to: "us/states/sc/districts/house/53"
    rel: in-district
    area_weight: 0.1332
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, sc]
timestamp: "2026-07-03"
---

# Darlington County, SC

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 62558 |
| Under 18 | 13894 |
| 18–64 | 36240 |
| 65+ | 12424 |
| Median household income | 48581 |
| Poverty rate | 21.09 |
| Homeownership rate | 70.91 |
| Unemployment rate | 6.65 |
| Median home value | 158200 |
| Gini index | 0.5234 |
| Vacancy rate | 14.12 |
| White | 33788 |
| Black | 25447 |
| Asian | 364 |
| Native | 184 |
| Hispanic/Latino | 1552 |
| Bachelor's or higher | 12052 |

## Districts

- [SC-07](/us/states/sc/districts/07.md) — 100% (congressional)
- [SC Senate District 29](/us/states/sc/districts/senate/29.md) — 98% (state senate)
- [SC Senate District 30](/us/states/sc/districts/senate/30.md) — 2% (state senate)
- [SC House District 62](/us/states/sc/districts/house/62.md) — 43% (state house)
- [SC House District 54](/us/states/sc/districts/house/54.md) — 24% (state house)
- [SC House District 65](/us/states/sc/districts/house/65.md) — 20% (state house)
- [SC House District 53](/us/states/sc/districts/house/53.md) — 13% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
