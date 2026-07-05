---
type: Jurisdiction
title: "St. Clair County, AL"
classification: county
fips: "01115"
state: "AL"
demographics:
  population: 94166
  population_under_18: 22993
  population_18_64: 29622
  population_65_plus: 41551
  median_household_income: 77463
  poverty_rate: 11.35
  homeownership_rate: 82.61
  unemployment_rate: 4.56
  median_home_value: 226300
  gini_index: 0.3923
  vacancy_rate: 10.55
  race_white: 78776
  race_black: 9575
  race_asian: 537
  race_native: 337
  hispanic: 2805
  bachelors_plus: 18784
districts:
  - to: "us/states/al/districts/03"
    rel: in-district
    area_weight: 0.9982
  - to: "us/states/al/districts/senate/11"
    rel: in-district
    area_weight: 0.5767
  - to: "us/states/al/districts/senate/17"
    rel: in-district
    area_weight: 0.4231
  - to: "us/states/al/districts/house/30"
    rel: in-district
    area_weight: 0.4563
  - to: "us/states/al/districts/house/50"
    rel: in-district
    area_weight: 0.376
  - to: "us/states/al/districts/house/36"
    rel: in-district
    area_weight: 0.1375
  - to: "us/states/al/districts/house/45"
    rel: in-district
    area_weight: 0.0299
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, al]
timestamp: "2026-07-03"
---

# St. Clair County, AL

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 94166 |
| Under 18 | 22993 |
| 18–64 | 29622 |
| 65+ | 41551 |
| Median household income | 77463 |
| Poverty rate | 11.35 |
| Homeownership rate | 82.61 |
| Unemployment rate | 4.56 |
| Median home value | 226300 |
| Gini index | 0.3923 |
| Vacancy rate | 10.55 |
| White | 78776 |
| Black | 9575 |
| Asian | 537 |
| Native | 337 |
| Hispanic/Latino | 2805 |
| Bachelor's or higher | 18784 |

## Districts

- [AL-03](/us/states/al/districts/03.md) — 100% (congressional)
- [AL Senate District 11](/us/states/al/districts/senate/11.md) — 58% (state senate)
- [AL Senate District 17](/us/states/al/districts/senate/17.md) — 42% (state senate)
- [AL House District 30](/us/states/al/districts/house/30.md) — 46% (state house)
- [AL House District 50](/us/states/al/districts/house/50.md) — 38% (state house)
- [AL House District 36](/us/states/al/districts/house/36.md) — 14% (state house)
- [AL House District 45](/us/states/al/districts/house/45.md) — 3% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
